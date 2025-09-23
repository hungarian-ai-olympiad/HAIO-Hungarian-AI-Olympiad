"""judge_api.py

# Set your API key and base URL at the top of this file
### Hint descriptions are automatically loaded from Hugging Face

Usage:
    from judge_api import guess
    
    guesses = guess([[1, 2, 3]], options=["cat", "dog", "house"])
"""

from typing import List, Optional
from datasets import load_dataset

from openai import OpenAI
from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Configuration - UPDATE THESE VALUES
# ---------------------------------------------------------------------------
API_KEY = "sk-or-v1-put-your-openrouter-api-key-here"  # Put your OpenRouter API key here
BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "google/gemini-2.5-flash-lite-preview-06-17"

_client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# ---------------------------------------------------------------------------
# Load hint descriptions from Hugging Face dataset
# ---------------------------------------------------------------------------
try:
    print("Loading hint descriptions from Hugging Face...")
    ds = load_dataset("IOAI-official/ioai2025-onsite-concepts-hint-descriptions", split="train")
    _HINT_DICT = {row["ID"]: row["Description"].replace("\n", ", ") for row in ds}
    print(f"Loaded {len(_HINT_DICT)} hint descriptions")
except Exception as e:
    print(f"Warning: Could not load hint descriptions from Hugging Face: {e}")
    print("Falling back to empty dictionary")
    _HINT_DICT = {}

_ORDINALS = ["first", "second", "third", "fourth"]


class GuessResponse(BaseModel):
    answer: List[str] = Field(description="List of guessed keywords")

def guess(clues: List[List[int]], options: Optional[List[str]] = None, N: int = 10) -> List[str]:
    """Generate guesses for a Concepts game based on clues.
    
    Args:
        clues: List of clues, where each clue is a list of hint indices
        options: List of possible answer options (optional)
        N: Number of guesses to generate (default: 10)
        
    Returns:
        List of guesses
    """
    # Build clue string
    clue_str = ""
    for i, clue in enumerate(clues):
        clue_str += f"{_ORDINALS[i]} clue:\n"
        for hint_idx in clue:
            desc = _HINT_DICT.get(hint_idx, f"[hint {hint_idx}]")
            clue_str += f" - {desc}\n"
        clue_str += "\n"

    # Create prompt
    option_str = "\n".join(options) if options else ""
    prompt = f"""You are playing a Concepts game. A player has a secret keyword and has provided you with the following clue:
{clue_str}

{'The secret keyword is guaranteed among the following options:' if options else ''}
{option_str}

Now, provide exactly {N} guesses of the secret keyword."""

    # Make API call
    response = _client.beta.chat.completions.parse(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant playing a Concepts guessing game."},
            {"role": "user", "content": prompt}
        ],
        response_format=GuessResponse,
        temperature=0,
        max_tokens=1500
    )
    
    return response.choices[0].message.parsed.answer


__all__ = ["guess"]

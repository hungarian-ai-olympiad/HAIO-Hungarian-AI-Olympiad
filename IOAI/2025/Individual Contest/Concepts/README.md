# IOAI 2025 Concepts Task

This folder contains resources for the Concepts task (day 1, task 3) in IOAI 2025.

## File Descriptions

- [`Concepts.ipynb`](Concepts.ipynb): The baseline notebook, including the problem statement.
- [`Concepts_Solution.ipynb`](Concepts_Solution.ipynb): The official intended solution notebook from the ISC and HSC.
- [`judge_api.py`](judge_api.py): This scripts simulates the judge api accessible to contestants during the competition. You need an openrouter token to run use this script.
- [`metrics.py`](metrics.py): The evaluation script.
- [`llm_proxy_tutorial.ipynb`](llm_proxy_tutorial.ipynb): During the competition the contestants were allowed to access LLMs for this problem only using a custom proxy and custom api keys. This was the tutorial notebook for using the custom LLM proxy. We are keeping this tutorial notebook here to inform you that you are allowed and encouraged to use LLMs to assist in solving this problem, with limitations outlined in the tutorial notebook.

## Usage

To run this task, you need an openrouter token to run the evaluation API. Go to https://openrouter.ai/ to create an API key, and insert it in [`judge_api.py`](judge_api.py). The solution notebook also uses LLM APIs, which the contestants had access to through an [official proxy](llm_proxy_tutorial.ipynb) using official IOAI tokens. You will be able to run the [solution](Concepts_Solution.ipynb) with any OpenAI API base url and corresponding token of your choice.

First, run [`Concepts.ipynb`](Concepts.ipynb) or [`Concepts_Solution.ipynb`](Concepts_Solution.ipynb). This will generate an `out` folder containing `clues_a.jsonl`, `clues_b.jsonl`, and potentially other files. The two `jsonl` files are the answers that will be evaluated.

After running a solution, run `metrics.py` to evaluate your answers. It will log your scores on both the validation and testing set as well as generate a `score.json` file under `out`.

## On-Site Limitations

During the competition, the participants were allocated $10 worth of credits for using the LLM proxy and $12,500$ total judge api calls (as well as rate limitations). The contestants submitted a notebook that was ran on inference machines, which generated `jsonl` files that were evaluated on separate evaluation machines. The inference machines did not have access to the judge api and the evaluation machines accessed it through a secret url. This means the contestants were not able access the judge api during inference or evaluation. The API was solely meant to assist in the training process and as a way to validate their solutions locally before submission. It should not be involved during inference. Furthermore, the API was a black box to the contestants and they did not know how it was implemented.

It is also worth noting that the current implementation of the [judge api script](judge_api.py) might be affected by randomness in the response of the LLM. This may result in some small oscillations in scoring. The implementation of the API server used for the competition is much more robust and ensures fairness and reproducibility.

There was also a total upload file size limit of `1GB` from the contestants' local computers to the inference machines. The inference machines also did not have access to any huggingface models other than the ones listed above.

You should keep these limitations in mind while solving this problem.

## Credits

This problem was provided by **[Alham Fikri Aji](https://afaji.github.io/)** - [Linkedin](https://www.linkedin.com/in/afaji/)

### HSC contributors

- [Jett Chen](https://jettchen.me/) - [Linkedin](https://www.linkedin.com/in/jettchen/)
- [Sijun Li](https://github.com/Silicon23)
- [Shao Duan](https://github.com/shaoxiongduan)

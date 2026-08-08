# HAIO — Olimpiai felkészülés / Olympiad Preparation

<a href="#hu">🇭🇺 Magyar</a> · <a href="#en">🇬🇧 English</a>

A nemzetközi diákolimpiákra (IOAI, IAIO) készülő haladó tananyag. Minden notebook magyarul és angolul is elérhető.

---

<a id="hu"></a>

## 🇭🇺 Magyar

Az IOAI és IAIO versenyszabályzatában szereplő témakörök szerint rendezve.

### Felügyelt Tanulás

| Téma | Leírás | Megnyitás |
|---|---|---|
| **Random Forest** | Döntési fák ensemble módszere bagging-gel; OOB hiba, feature importance és gyakorlati hiperparaméter-hangolás. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-dT1kFHZO24u4VRNOV0usNtA8RHvlvt-?usp=sharing) |
| **Gradient Boosting (XGBoost, CatBoost, LightGBM)** | Boosting alapok és modern implementációk; tanulási ráta, fa-mélység, regularizáció és Kaggle-szintű alkalmazás. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1BcvYnFzhQbn2YIHjBRcxa5N09JJOCgjZ?usp=sharing) |

### Felügyelet Nélküli Tanulás

| Téma | Leírás | Megnyitás |
|---|---|---|
| **Főkomponens-analízis (PCA)** | Lineáris dimenziócsökkentés sajátérték-felbontással; varianciaarány, vizualizáció és zajcsökkentés. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1oNKakZPngo20NaBwXfb_g8Ii4nhpaQLH?usp=sharing) |
| **Hierarchikus Klaszterezés** | Agglomeratív klaszterezés dendrogrammal; összekapcsolási módszerek és a klaszterszám leolvasása. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1wiK1mgez792f6-478-AgXnL23NYMf8Ub?usp=sharing) |
| **t-SNE, UMAP és további dimenziócsökkentő módszerek** | Nemlineáris dimenziócsökkentés: t-SNE perplexitás, UMAP topológia-megőrzés, klaszterek 2D vizualizációja. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/11ciyZDZg6soq3_vhEpeUhPVitgqxacwN?usp=sharing) |
| **DBSCAN Klaszterezés** | Sűrűségalapú klaszterezés: tetszőleges alakú klaszterek és zajpontok az eps és min_samples paraméterekkel. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ZoCkRPMYO4ZlxwB8k4QwJrBMgZwDjWKe?usp=sharing) |
| **Pszeudó-címkézés (Pseudo-Labeling)** | Félig felügyelt tanulás: címkézetlen adatok bevonása a modell saját predikcióival, konfidencia-szűréssel. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1c14XBMlpe1R8auLKtmR6Yv4fEkgtq6rb?usp=sharing) |
| **Félig felügyelt módszerek (Contrastive Learning)** | Reprezentáció-tanulás kontrasztos célfüggvénnyel; pozitív és negatív párok, augmentáció, downstream feladatok. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1xOXo4VXsc9uA0WOOY5BZmqQCndYSnDLj?usp=sharing) |

### Deep Learning Alapok

| Téma | Leírás | Megnyitás |
|---|---|---|
| **Momentum módszerek (Adam, AdamW)** | Gradiens-frissítés simítása momentummal; Adam adaptivitása, AdamW és a súly-csökkentés szétválasztása. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1xzaSqyyhIBtHSZRBTymPiecrLGUxQKKv?usp=sharing) |
| **Adaptív tanulási ráták** | Per-paraméter learning rate: AdaGrad, RMSProp, Adam; mikor és miért segítenek a sima SGD-vel szemben. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-Dlk-TcwUGrRdiC-QdwlCnaGRAm09d1s?usp=sharing) |
| **Konvergencia és tanulási ráták** | LR ütemezések (cosine, warmup, step decay), divergencia diagnosztikája és gyakorlati keresési stratégiák. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ReL5TwCD-9IVLEPNh701u1S2NxkrZELE?usp=sharing) |
| **Súly-regularizáció (L1, L2)** | L1/L2 büntetések hatása a súlyokra; ridge vs. lasso és a túltanulás visszaszorítása. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ORxDr_aM9UB_Gc5JG6udZUxFMO0J5ycW?usp=sharing) |
| **Korai leállítás (Early Stopping)** | Validációs hiba monitorozása; mikor érdemes leállítani a tanítást, patience és a legjobb súlyok visszaállítása. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1aKO4gIhDH7dFMS-jrUYiKOwZa042-plG?usp=sharing) |
| **Dropout és Gaussian zaj** | Sztochasztikus regularizáció train és inference közben; dropout valószínűség hangolása és zaj injekció. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1sBlBSwVEJaeimg6Z77V6MST_kxpi0S4T?usp=sharing) |
| **Súlyinicializáció** | Xavier/Glorot és He inicializáció; miért vezet rossz init eltűnő vagy robbanó gradiensekhez. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1CEJG8lWn9KWaYPLLufhBkkonAQmlacOc?usp=sharing) |
| **Batch Normalization** | Aktivációk normalizálása rétegen belül; train/eval különbség, futó statisztikák és alternatívák (LayerNorm). | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1R9rZnFUNYFu5uFv9B5FQpAsO8arn-9ce?usp=sharing) |
| **Autoencoderek és sparse autoencoderek** | Tömörített reprezentáció tanítása rekonstrukciós veszteséggel; sparsity-büntetés és anomáliadetekció. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1koCLiFMOzsb8I6lTos5xOJH7-_fdh_mV?usp=sharing) |

### Computer Vision

| Téma | Leírás | Megnyitás |
|---|---|---|
| **Konvolúciós rétegek alapjai** | Konvolúció működése képeken; kernel, stride, padding és a receptív mező intuíciója. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/18wsiy47KV9RqUEWu4mgUJSLol-yDW50k?usp=sharing) |
| **Pooling technikák (Max, Average)** | Térbeli leskálázás max és average pool-lal; invariancia, információvesztés, modern alternatívák (strided conv). | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1wpq3awgQu1ovRpZAUgC5LFFxgEj1rh-5?usp=sharing) |
| **Képosztályozás alapjai** | End-to-end CNN pipeline egy klasszikus adathalmazon; tanítás, kiértékelés, tévesztési mátrix. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1VbY5UvCRc0Y6Yc71dB-7rHKyixf7FaIv?usp=sharing) |
| **Objektumdetektálás alapjai (YOLO, SSD)** | Egylépéses detektorok: anchor box-ok, confidence és NMS, bounding box regresszió. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1YivEcStxythK0ifS90rWptNGZujvYPDD?usp=sharing) |
| **Képszegmentáció alapjai (U-Net)** | Pixelszintű osztályozás encoder-decoder architektúrával és skip kapcsolatokkal. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1OsAOIMDzEEnSrMjy5Pe24fQ8ehRDL_f5?usp=sharing) |
| **Transfer learning képosztályozásra (ResNet, MobileNet)** | Előtanított backbone finomhangolása saját adathalmazon; rétegfagyasztás és learning rate stratégiák. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ldNE0T2UolxGdSzlavoDB5IppK_5e5FQ?usp=sharing) |
| **Képi adatdúsítási technikák** | Augmentációs receptek (flip, crop, color jitter, mixup, cutmix) és hatásuk a generalizációra. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1NI7P9hHpm-EPCCyfWJeQjxg81ipgrKR7?usp=sharing) |
| **Feature extraction előtanított modellekkel** | Backbone embedding-jeinek kinyerése; klasszikus klasszifikátor a tetejére, mikor éri meg. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zm39jABblfTL6PWIhjnP6V5yTTSdwe0q?usp=sharing) |
| **Bevezetés a GAN-okba** | Generátor és diszkriminátor adversarial játéka; egyszerű képgenerálás és tipikus instabilitások. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1C8OkywWxGIwLv0o_5XTWTVrzNbC0q_pj?usp=sharing) |
| **Bevezetés a self-supervised tanulásba (vision)** | Pretext feladatok és kontrasztos módszerek (SimCLR, MoCo) felirat nélküli képekhez. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1pmQ7VO1H0gEg6HF4rl2WFxruBH_GLcH2?usp=sharing) |
| **Vision Transformerek (ViT) alapjai** | Képek mint patch-szekvenciák; attention képekre, CNN-ekkel való összevetés és gyakorlati tippek. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1oebPtVWgizeh1POfaGDiBp7BjMrdo9ov?usp=sharing) |
| **CLIP és multimodális tanulás** | Kép-szöveg közös embedding tér; zero-shot osztályozás és prompt-alapú használat. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1GdI04EuRRWkDLnGEPctq2Xi_FR2SYwm6?usp=sharing) |
| **Generatív modellek (Stable Diffusion, DALL-E)** | Diffúziós modellek intuíciója; szöveg-kép generálás és gyakorlati prompt-tervezés. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1VeIUa4YGlWLcO_UiswWxszurzcMxcsAk?usp=sharing) |

### Természetes Nyelv Feldolgozás (NLP)

| Téma | Leírás | Megnyitás |
|---|---|---|
| **Szóbeágyazások (Word Embeddings)** | Word2Vec, GloVe és fastText; szavak vektorrá alakítása, analógiák és vizualizáció. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ABEr94vZ0c_zv_LIFheBpCI6E0RmZfEd?usp=sharing) |
| **Transformer alapok** | Self-attention, multi-head attention és pozíció-kódolás; miért váltotta le az RNN-eket NLP-ben. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Y88zeXDskuI0GBrdlmJmmmbcQUS2HLFR?usp=sharing) |
| **Szövegosztályozás** | Klasszikus és transformer-alapú pipeline tokenizálástól a kiértékelésig. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Wc68c52gNlBSp-0GUB4XApfHe0ojKTHE?usp=sharing) |
| **Előtanított NLP modellek bevezető (BERT, GPT)** | Encoder és decoder modellek; mit tanulnak előtanításkor és hogyan használjuk őket downstream feladatokra. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1sqUzyFQWO97qRfcnh5QTxb5MzPl0Gr4P?usp=sharing) |
| **Kérdés-válasz előtanított modellekkel** | Extraktív QA finomhangolás SQuAD-szerű adatokon; span-predikció és kiértékelés. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1u0P_a7Nn3OaW2vRMF052uqwwXJQpybit?usp=sharing) |
| **Bevezetés a nagy nyelvi modellekbe (LLM-ek, GPT-4)** | LLM-ek képességei és korlátai; tokenizálás, kontextusablak és prompting alapok. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/11N-HBzafAKFc8_T8Pn3ULrsGmH5NjUEw?usp=sharing) |
| **Egyszerű chatbotok építése NLP-vel** | Beszélgetés-állapot, retrieval és LLM hívások összekapcsolása minimális chatbottá. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1lRlexWOlU62u_-tFfl-9HtsnkgzfaeB8?usp=sharing) |
| **Modell finomhangolás: módszerek és korlátok (LoRA, Adapters)** | Paraméter-hatékony finomhangolás: LoRA mátrixok, adapterek, mikor melyiket érdemes választani. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1rf0apYjlQlhWbLmObcy3BiOGcDzyq_Z2?usp=sharing) |
| **LLM ágensek alapjai** | Eszközhasználat, tervezés és végrehajtási ciklus; ReAct minta és egyszerű ágens-implementáció. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1DRg_ejGWKFGNGnfZhZKusknhhMHBnijk?usp=sharing) |
| **RLHF (RL from Human Feedback)** | Reward modell tanítása emberi preferenciákból; PPO az LLM finomhangolásához. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qbFZro89RIo-L7vF8rvqi71DkhJUTwib?usp=sharing) |
| **LLM-ek finomhangolása DPO és PPO módszerrel** | Preferencia-alapú finomhangolás: PPO klasszikus RLHF, DPO közvetlen optimalizáció reward modell nélkül. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1KCUyJVMSGf3DuiGGtRfvtG-nkeN45-Cc?usp=sharing) |

### Recommender Systems

| Téma | Leírás | Megnyitás |
|---|---|---|
| **Bevezetés a Recommender Systemekbe** | Recommender System bevezető előadás. | [📁 anyag](https://drive.google.com/file/d/1tWl4Qm6DevtpJjyiw1Ngm7PPq5WFYnXe/view?usp=sharing) |
| **Kollaboratív Szűrés** | Kollaboratív szűrés alapok és alkalmazások. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1vKbgXlhRSU2ciYnLbsQJhrBgfmkPtGps?usp=sharing) |
| **Tartalomalapú Szűrés** | Tartalomalapú szűrés alapok és alkalmazások. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1QlNiAIEHyn1FcHYYTVJAn5xGtH3VOzHt?usp=sharing) |
| **Hibrid Ajánlórendszerek** | Hibrid ajánlórendszerek alapok és alkalmazások. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1JX43jTlxuWmk9z_Jbw4kzLnnC_ee3VoS?usp=sharing) |
| **Mátrix Faktorizáció** | Mátrix faktorizáció alapok és alkalmazások. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1vm580ZMkBXmSQUnQLxPnodIfYBFujDiM?usp=sharing) |
| **Deep Learning az Ajánlórendszerekben** | Deep learning technikák ajánlórendszerekben. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1OHx86fEniGl2uN2kht-ZK-h4cElvjZJH?usp=sharing) |

### Gaussian Mixture Models

| Téma | Leírás | Megnyitás |
|---|---|---|
| **Bevezetés a GMM-ekbe** | Gaussian Mixture Model bevezető előadás. | [📁 anyag](https://drive.google.com/file/d/1DhYlJ0Q4_8Wse0jlSY1wxMlwf5yH3f1-/view?usp=sharing) |
| **Gaussian Mixture Models (GMM)** | Gaussian Mixture Models alapok és alkalmazások. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1dxj_T_CjiIIyDXOxF7vcLNxE_KABIS0Q?usp=sharing) |
| **PCA vizualizációs alkalmazása** | Principal Component Analysis (PCA) algoritmus és alkalmazásai. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1oNKakZPngo20NaBwXfb_g8Ii4nhpaQLH?usp=sharing) |
| **t-SNE magas dimenziós adatok reprezentálására** | t-SNE algoritmus és alkalmazásai magas dimenziós adatok reprezentálására. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/11ciyZDZg6soq3_vhEpeUhPVitgqxacwN?usp=sharing) |

### Reinforcement Learning

| Téma | Leírás | Megnyitás |
|---|---|---|
| **Markov Decision Processes (MDPs)** | Markov döntési folyamatok alapjai. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1FppLPFl9nZgXrMI2XtgeXSf185F0PlHs) |
| **Bellman Equations** | Bellman egyenletek és optimális policy. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1XzBENgQ7j_st3rt6_AQ3RDd1JEWH7M5d) |
| **Exploration vs Exploitation** | Felfedezés és kihasználás egyensúlya. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/15DBXAkw0DXmFdeYmGpJP5wjrQa7VHN8t) |
| **Q-Learning** | Q-learning algoritmus és implementáció. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1GFtgy-lG1X_yDVhyzROuEk1doYU7865J?usp=sharing) |
| **TD-Learning** | Temporal Difference learning módszerek. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/13kTqEXwJ-xiBn-xpTLto-xvOlhMnrwXT) |

### AI Search

| Téma | Leírás | Megnyitás |
|---|---|---|
| **Breadth-First Search (BFS), Depth-First Search (DFS)** | Breadth-First Search (BFS) és Depth-First Search (DFS) algoritmusok alapjai. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qQOoEpsOx83BG0mQ2WBzwaTJKkBjP3D2?usp=sharing) |
| **Uniform Cost Search** | Uniform Cost Search algoritmus. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kIeVNahVNpOH6tZGYtE072cNtel1aGim?usp=sharing) |
| **A* Algorithm and heuristics** | A* algoritmus és heurisztikák. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1USwZh5D912RW0w1BmpNu44DquDsBkjdy?usp=sharing) |
| **Minimax search (game AI)** | Minimax keresés (játék AI). | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_IkCPL3MEH3Zsy6RwCFqCb7ranHtfAwO?usp=sharing) |

### Logical Reasoning

| Téma | Leírás | Megnyitás |
|---|---|---|
| **Logika és ami belőle következik** | Logika és ami belőle következik előadás. | [📁 anyag](https://drive.google.com/file/d/1GgSd_m-9Ja6xcmSJ3ZiMoAiwomCbd0RW/view?usp=sharing) |
| **Konjunktív Normálforma (CNF) és Logikai Összekötők** | Konjunktív normálforma és logikai összekötők. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/10EUPsCUI2V5YeM2blMdw600sv73rqdSc?usp=sharing) |
| **Unifikáció a Következtetésben** | Unifikáció a következtetésben. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1POXUcohFP8rZuCNapKa79M1dQPhsz1CP?usp=sharing) |
| **Kielégíthetőség és SAT Megoldók** | Kielégíthetőség és SAT megoldó algoritmusok. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/108ELcGwKuwIQbo0VHOfCUbKE1SIzZwyA?usp=sharing) |

### Kényszer-Kielégítési Problémák (CSPs)

| Téma | Leírás | Megnyitás |
|---|---|---|
| **Bevezetés a CSP-kbe** | Kényszer-Kielégítési Problémák bevezető előadás. | [📁 anyag](https://drive.google.com/file/d/1lDo8u16Jmvvprk_XrwGL4K4Z6WhuVgyL/view?usp=sharing) |
| **Kényszer-Kielégítési Problémák** | CSP alapok és megoldási technikák. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1PV6RwKYtJSSfPvIfoOmO7aaRgDZkTaPj?usp=sharing) |
| **AC3 Algoritmus** | Arc Consistency Algorithm és alkalmazásai. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1GdmrFvVdTNPYmoLMvE-dYv6xvp1C7_Gr?usp=sharing) |
| **Forward Checking** | Forward Checking technika a CSP-k megoldásában. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1LZvTQYkAC-i2qgxvxiFbI4ax5Pi9Sxzp?usp=sharing) |

### Kernel Methods

| Téma | Leírás | Megnyitás |
|---|---|---|
| **Soft and Hard-margin SVM** | Support Vector Machine alapok: soft és hard margin. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1uo-IvOCOYpvPCTPWXF_hwB13Yzh8_T6k) |
| **Kernel Trick** | A kernel trükk elmélete és alkalmazása. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1N49rHTzSKeAJu4V9T6h27-f0vLohV5u5) |
| **RBF Kernel** | Radial Basis Function kernel és alkalmazásai. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Wfhi1F555tMfLooINtwNYZ8M_ggM786T) |

---

<a id="en"></a>

## 🇬🇧 English

Organised by the topics listed in the IOAI and IAIO syllabi.

### Supervised Learning

| Topic | Description | Open |
|---|---|---|
| **Random Forest** | An ensemble of decision trees built with bagging; OOB error, feature importance and practical hyperparameter tuning. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/19lpqCx9FmMoW--RMoUxZ_YalvDXM1b74?usp=sharing) |
| **Gradient Boosting (XGBoost, CatBoost, LightGBM)** | Boosting fundamentals and modern implementations; learning rate, tree depth, regularisation and Kaggle-level application. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1mA15_WwDHX9b5_t3gyJ37-SMzl-8dlZH?usp=sharing) |

### Unsupervised Learning

| Topic | Description | Open |
|---|---|---|
| **Principal Component Analysis (PCA)** | Linear dimensionality reduction via eigendecomposition; explained variance ratio, visualisation and noise reduction. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1aTubFVZgHp7tAjc1oNQJrbdN_zOE0CD6?usp=sharing) |
| **Hierarchical Clustering** | Agglomerative clustering with dendrograms; linkage methods and reading the cluster count off the tree. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_F8b4VGRuosCNQaZKroSdKyMToAALZU2?usp=sharing) |
| **t-SNE, UMAP and further dimensionality reduction methods** | Non-linear dimensionality reduction: t-SNE perplexity, UMAP topology preservation, 2D visualisation of clusters. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1U6j6sj_0gzNsr7VcCzh8q8KzyAx6V-qo?usp=sharing) |
| **DBSCAN Clustering** | Density-based clustering: arbitrarily shaped clusters and noise points via the eps and min_samples parameters. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1R0f_2avUW3SIB3gdPq0mQnzU8_6VCLH-?usp=sharing) |
| **Pseudo-Labelling** | Semi-supervised learning: bringing unlabelled data in using the model's own predictions, with confidence filtering. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/17y1T_7-FkGgtghyxdad3H5X8_EwOIw4k?usp=sharing) |
| **Semi-supervised methods (Contrastive Learning)** | Representation learning with a contrastive objective; positive and negative pairs, augmentation, downstream tasks. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ewc9gNxv8TCYEQCrC7JNtHxnVqpftItI?usp=sharing) |

### Deep Learning Fundamentals

| Topic | Description | Open |
|---|---|---|
| **Momentum methods (Adam, AdamW)** | Smoothing gradient updates with momentum; Adam's adaptivity, AdamW and decoupled weight decay. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1a-h9ZGr7RaHHwQji17m6tD2UCXxwESjy?usp=sharing) |
| **Adaptive learning rates** | Per-parameter learning rates: AdaGrad, RMSProp, Adam; when and why they help compared with plain SGD. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1o2HnevZ1NrpCHcYAzp4YgXXeGWuWGoHy?usp=sharing) |
| **Convergence and learning rates** | LR schedules (cosine, warmup, step decay), diagnosing divergence and practical search strategies. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1xzye_qAqzbaHkoHaQ7jEbU5-M-Rogsa6?usp=sharing) |
| **Weight regularisation (L1, L2)** | The effect of L1/L2 penalties on the weights; ridge vs. lasso and curbing overfitting. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1SlqQgMzEloyVPEKPCAd1VJpGV_dXYqt7?usp=sharing) |
| **Early Stopping** | Monitoring validation error; when to stop training, patience and restoring the best weights. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/15heIW8ODNScL4BFE_vsLYlf-QHK4SX80?usp=sharing) |
| **Dropout and Gaussian noise** | Stochastic regularisation during training and inference; tuning the dropout probability and injecting noise. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1wrB2BaGAUlvCJKOloLKOhgfSYCkRrKSQ?usp=sharing) |
| **Weight initialisation** | Xavier/Glorot and He initialisation; why a poor init leads to vanishing or exploding gradients. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1pJGcUS1_XBiH20SfuKh0gvqwktuhXcVP?usp=sharing) |
| **Batch Normalization** | Normalising activations within a layer; the train/eval difference, running statistics and alternatives (LayerNorm). | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1FG8jlqOb7WJQzlvkD4rD_jhZ5Upmxt58?usp=sharing) |
| **Autoencoders and sparse autoencoders** | Learning a compressed representation with a reconstruction loss; sparsity penalty and anomaly detection. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1oLioqcgWoghVNIzjTy02SyiN4xv6IcLO?usp=sharing) |

### Computer Vision

| Topic | Description | Open |
|---|---|---|
| **The basics of convolutional layers** | How convolution works on images; kernel, stride, padding and the intuition behind the receptive field. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1KqLcNITGF16cT3J7xIrpKr7lRLUtdJka?usp=sharing) |
| **Pooling techniques (Max, Average)** | Spatial downsampling with max and average pooling; invariance, information loss, modern alternatives (strided conv). | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1l9T1DFfO7O2aZqUo19j1UQ5oeQ0POG3W?usp=sharing) |
| **The basics of image classification** | An end-to-end CNN pipeline on a classic dataset; training, evaluation, confusion matrix. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/11TWbma4P1mhRpGVR6-kDq7EHO8q32nWF?usp=sharing) |
| **The basics of object detection (YOLO, SSD)** | Single-stage detectors: anchor boxes, confidence and NMS, bounding box regression. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1f4coIRuBVqDPHW4e8p_q8tGqHaqKn6-Z?usp=sharing) |
| **The basics of image segmentation (U-Net)** | Pixel-level classification with an encoder-decoder architecture and skip connections. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1JO-QDtCV2E_gdX_8bdIyHMogGVslmIXj?usp=sharing) |
| **Transfer learning for image classification (ResNet, MobileNet)** | Fine-tuning a pre-trained backbone on your own dataset; layer freezing and learning rate strategies. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1tFq0KmgUHvN3iqHXeJZZF10EbifmC8Q_?usp=sharing) |
| **Image augmentation techniques** | Augmentation recipes (flip, crop, color jitter, mixup, cutmix) and their effect on generalisation. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qYiK6hnqoTDJFwnlGkDnNGbwwPDylfaF?usp=sharing) |
| **Feature extraction with pre-trained models** | Extracting embeddings from a backbone; putting a classical classifier on top, and when it is worth it. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WAGk6Ialhv6uLctpjentZR3W0Q-U2yrI?usp=sharing) |
| **Introduction to GANs** | The adversarial game between generator and discriminator; simple image generation and typical instabilities. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yJ4kJrqiUVfiJzHFlojTd0CV2STxyfsh?usp=sharing) |
| **Introduction to self-supervised learning (vision)** | Pretext tasks and contrastive methods (SimCLR, MoCo) for unlabelled images. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1tn42OKmjSdHo6vz-T7htqVYmtFfhxqdc?usp=sharing) |
| **The basics of Vision Transformers (ViT)** | Images as sequences of patches; attention over images, comparison with CNNs and practical tips. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1vpZv7_SjBSxTCq-5OZnzF87YWh1Tc82y?usp=sharing) |
| **CLIP and multimodal learning** | A shared image-text embedding space; zero-shot classification and prompt-based use. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1XtfDbXajfclN7ff02b_XTVh-JPZNHDoJ?usp=sharing) |
| **Generative models (Stable Diffusion, DALL-E)** | The intuition behind diffusion models; text-to-image generation and practical prompt design. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/12OLpMv1tlFFbRXKEG7ydIeB7PuUZLSAa?usp=sharing) |

### Natural Language Processing (NLP)

| Topic | Description | Open |
|---|---|---|
| **Word Embeddings** | Word2Vec, GloVe and fastText; turning words into vectors, analogies and visualisation. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1CfVO4nGTb9tGAgn-AMWGaEwoAKS6KGvJ?usp=sharing) |
| **Transformer basics** | Self-attention, multi-head attention and positional encoding; why it replaced RNNs in NLP. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1IGLjtPCxu1-wmGfJg7lF6yAwFbHcNhxn?usp=sharing) |
| **Text classification** | Classical and transformer-based pipelines from tokenisation to evaluation. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/18RRQKtpUh_CnU07oA-EVNx9huNzghEzM?usp=sharing) |
| **Introduction to pre-trained NLP models (BERT, GPT)** | Encoder and decoder models; what they learn during pre-training and how to use them for downstream tasks. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1L8Y3Hp-ruhMm44acD7Y2Vecv-_mCr-VM?usp=sharing) |
| **Question answering with pre-trained models** | Fine-tuning extractive QA on SQuAD-style data; span prediction and evaluation. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/17oPX5o9wTQaYOuUfg-OLvMHgjMhr75K6?usp=sharing) |
| **Introduction to large language models (LLMs, GPT-4)** | The capabilities and limits of LLMs; tokenisation, the context window and prompting basics. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1p6-vYmKb8JBlJHHiVDIYEaDepwrlFOl6?usp=sharing) |
| **Building simple chatbots with NLP** | Wiring conversation state, retrieval and LLM calls together into a minimal chatbot. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/18nW-300P0I1X3ZkUHuPoa6KE_weh7g_G?usp=sharing) |
| **Model fine-tuning: methods and limits (LoRA, Adapters)** | Parameter-efficient fine-tuning: LoRA matrices, adapters, and which one to choose when. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1aeiiCuD87sKjhbdZFLVnR8aPBgN_OoEB?usp=sharing) |
| **The basics of LLM agents** | Tool use, planning and the execution loop; the ReAct pattern and a simple agent implementation. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1QYDA9L0_Wu9QI8jnxjS5AzvIEXwZkQF3?usp=sharing) |
| **RLHF (RL from Human Feedback)** | Training a reward model from human preferences; PPO for fine-tuning the LLM. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Y5BRKRN-96OCnlNN8Fi21nEuZ-LfLuOV?usp=sharing) |
| **Fine-tuning LLMs with DPO and PPO** | Preference-based fine-tuning: PPO as classic RLHF, DPO as direct optimisation without a reward model. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/107qR7reLIjL2csDdUZ649UvTJl93bPHx?usp=sharing) |

### Recommender Systems

| Topic | Description | Open |
|---|---|---|
| **Introduction to Recommender Systems** | Introductory lecture on recommender systems. | [📁 files](https://drive.google.com/file/d/1tWl4Qm6DevtpJjyiw1Ngm7PPq5WFYnXe/view?usp=sharing) |
| **Collaborative Filtering** | The basics of collaborative filtering and its applications. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/115QmqopBn_AwYLRQg1KACBtVG85E-CfF?usp=sharing) |
| **Content-Based Filtering** | The basics of content-based filtering and its applications. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1sp3lKyerUvhsEyl_hYJX5aN1l1GStRVv?usp=sharing) |
| **Hybrid Recommender Systems** | The basics of hybrid recommender systems and their applications. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1l3IUf1gHQ9JzXvzEf_3tITMHiaKSmybv?usp=sharing) |
| **Matrix Factorisation** | The basics of matrix factorisation and its applications. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kJQ_3Na786F6BIlE8PCQxPddtzA27f57?usp=sharing) |
| **Deep Learning in Recommender Systems** | Deep learning techniques in recommender systems. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1QKbQk5Hngorc26qFF7TlKkEE9_wQ5-U2?usp=sharing) |

### Gaussian Mixture Models

| Topic | Description | Open |
|---|---|---|
| **Introduction to GMMs** | Introductory lecture on Gaussian Mixture Models. | [📁 files](https://drive.google.com/file/d/1DhYlJ0Q4_8Wse0jlSY1wxMlwf5yH3f1-/view?usp=sharing) |
| **Gaussian Mixture Models (GMM)** | The basics of Gaussian Mixture Models and their applications. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1AtSyK_8XqX8BFjdszvvd7EWZ6twRVL5q?usp=sharing) |
| **Using PCA for visualisation** | The Principal Component Analysis (PCA) algorithm and its applications. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1aTubFVZgHp7tAjc1oNQJrbdN_zOE0CD6?usp=sharing) |
| **t-SNE for representing high-dimensional data** | The t-SNE algorithm and its applications for representing high-dimensional data. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1U6j6sj_0gzNsr7VcCzh8q8KzyAx6V-qo?usp=sharing) |

### Reinforcement Learning

| Topic | Description | Open |
|---|---|---|
| **Markov Decision Processes (MDPs)** | The basics of Markov decision processes. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1KCeN8lqvBFjSseNdg6mRwRVR14ZpzjSm?usp=sharing) |
| **Bellman Equations** | Bellman equations and the optimal policy. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/18A8_yJ_tielAHkO4yKgN4juayJqZCMDE?usp=sharing) |
| **Exploration vs Exploitation** | Balancing exploration and exploitation. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1QyHfp46PEj_9HFfI4EA4ToIUvb7Xxu1e?usp=sharing) |
| **Q-Learning** | The Q-learning algorithm and its implementation. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kz7XpoS4THbGx_lXPkBiRU68qGCz-unY?usp=sharing) |
| **TD-Learning** | Temporal difference learning methods. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Q0yRyB4oV_o4YSGGk4-_XHETijE28m_T?usp=sharing) |

### AI Search

| Topic | Description | Open |
|---|---|---|
| **Breadth-First Search (BFS), Depth-First Search (DFS)** | The basics of the Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_h9OpMQlpWX6rDAMZfAkaKdCMA2S_q_4?usp=sharing) |
| **Uniform Cost Search** | The Uniform Cost Search algorithm. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1MZgAnP9V5tAZ7ILGnc05eQTbDYIkDXyF?usp=sharing) |
| **A* Algorithm and heuristics** | The A* algorithm and heuristics. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1N3TwNI6mLPugEEPdnFONgQdfAQrfW1GZ?usp=sharing) |
| **Minimax search (game AI)** | Minimax search (game AI). | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1A3sEZXm5i35Wt1GgVPbYNdJLiG3cZUC3?usp=sharing) |

### Logical Reasoning

| Topic | Description | Open |
|---|---|---|
| **Logic and what follows from it** | The 'Logic and what follows from it' lecture. | [📁 files](https://drive.google.com/file/d/1GgSd_m-9Ja6xcmSJ3ZiMoAiwomCbd0RW/view?usp=sharing) |
| **Conjunctive Normal Form (CNF) and Logical Connectives** | Conjunctive normal form and logical connectives. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-qgaja7m2S5EIrXZIdmpc-qVvx6bT4Je?usp=sharing) |
| **Unification in Inference** | Unification in inference. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_j22TacjAt75l6DG7uYcMnXBdkLsw9sg?usp=sharing) |
| **Satisfiability and SAT Solvers** | Satisfiability and SAT solver algorithms. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1E09_Me_pgPCRhGPpdp4DJcJdbfQIhvDk?usp=sharing) |

### Constraint Satisfaction Problems (CSPs)

| Topic | Description | Open |
|---|---|---|
| **Introduction to CSPs** | Introductory lecture on constraint satisfaction problems. | [📁 files](https://drive.google.com/file/d/1lDo8u16Jmvvprk_XrwGL4K4Z6WhuVgyL/view?usp=sharing) |
| **Constraint Satisfaction Problems** | CSP basics and solution techniques. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1xwoNO__jBAEZqI1R361vzcQkZkkhc5g2?usp=sharing) |
| **AC3 Algorithm** | The Arc Consistency Algorithm and its applications. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1YwJodAqRAaGL8iGmDB8n3BkX40zFFm8H?usp=sharing) |
| **Forward Checking** | The Forward Checking technique for solving CSPs. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zmMC5NVPfp-J0phJ4ZDB-ydM2Mh-BGXW?usp=sharing) |

### Kernel Methods

| Topic | Description | Open |
|---|---|---|
| **Soft and Hard-margin SVM** | Support Vector Machine basics: soft and hard margin. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/18QQgZvnMGcZOxdpIQgRJamlXjs0MwP4t?usp=sharing) |
| **Kernel Trick** | The theory and application of the kernel trick. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1NDznv41Y_ZaMqCpn23JrGEiNKlcTL6-X?usp=sharing) |
| **RBF Kernel** | The Radial Basis Function kernel and its applications. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1rBBz5jytzZdTc-bd7mhhrtSEAkpMOUfZ?usp=sharing) |

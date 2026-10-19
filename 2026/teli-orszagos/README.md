# HAIO 2026 | Téli Országos Válogató / Winter National Qualifier

<a href="#hu">🇭🇺 Magyar</a> · <a href="#en">🇬🇧 English</a>

---

<a id="hu"></a>

## 🇭🇺 Magyar

Helyszín: ELTE Lágymányosi Campus, Budapest · 2026. október 17.

Egyetlen helyszíni forduló, amely az IAIO 2027 nemzetközi mesterséges intelligencia diákolimpiára való bejutásról döntött. Két részből állt: egy háromórás elméleti és egy egyórás gyakorlati, gépi tanulási fordulóból.

### Elméleti rész

Háromórás, papíralapú feladatsor 22 feladattal, feleletválasztós és kifejtős kérdésekkel, összesen 160 pontért. Témakörök: keresés, felügyelt és felügyelet nélküli tanulás, ajánlórendszerek, megerősítéses tanulás, modellek kiértékelése és kernelmódszerek.

| Fájl | Leírás |
|------|--------|
| [`elmeleti/elmeleti-fordulo.pdf`](elmeleti/elmeleti-fordulo.pdf) | Elméleti feladatsor |
| [`elmeleti/elmeleti-fordulo-megoldasok.pdf`](elmeleti/elmeleti-fordulo-megoldasok.pdf) | Megoldókulcs |

### Gyakorlati rész

| Feladat | Kategória | Leírás | Feladat | Colab | Megoldás | Colab |
|---------|-----------|--------|---------|-------|----------|-------|
| Kettős Könyvelés | ML | Rekordpárosítás: a GPS-rekordok és a forgalmi napló bejegyzéseinek egy-egy párosítása blokkokon belül, közös azonosító nélkül | [`feladat`](feladatok/kettos-konyveles.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hungarian-ai-olympiad/HAIO-Hungarian-AI-Olympiad/blob/main/2026/teli-orszagos/feladatok/kettos-konyveles.ipynb) | [`megoldás`](megoldasok/kettos-konyveles-megoldas.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hungarian-ai-olympiad/HAIO-Hungarian-AI-Olympiad/blob/main/2026/teli-orszagos/megoldasok/kettos-konyveles-megoldas.ipynb) |

Az adatok és a teszthalmaz kulcsa (`test_key.csv`) a [`feladatok/adatok/kettos-konyveles/`](feladatok/adatok/kettos-konyveles/) mappában vannak. A megoldás-notebook tíz megoldást épít fel egymás után, mindegyik egy új ötlettel tér el az előzőtől. A pontosságot és a pontszámot a teszthalmazon mértük, a DOCK kiértékelőjének görbéjével:

| # | Megoldás | Teszt pontosság | Pont |
|---:|---|---:|---:|
| 1 | Véletlen párosítás | 0,0068 | 0,00 |
| 2 | Rendezés menetidő szerint | 0,1251 | 8,41 |
| 3 | Két jellemzőpár + magyar módszer | 0,3386 | 25,93 |
| 4 | Lineáris regresszió + magyar módszer | 0,3185 | 24,93 |
| 5 | Gradient boosting, legközelebbi szomszéd | 0,6872 | 49,54 |
| 6 | Gradient boosting + magyar módszer | 0,7445 | 54,94 |
| 7 | Gradient boosting + Mahalanobis | 0,7494 | 55,53 |
| 8 | Gradient boosting + robusztus költség | 0,8213 | 64,34 |
| 9 | Útvonal-memória + robusztus költség | 0,8447 | 70,58 |
| 10 | Párosító osztályozó | 0,8886 | 80,00 |

### Feladat one-pager

- [ML One Pager (Kettős Könyvelés)](../docs/one-pagerek/teli-orszagos/ml-one-pager.pdf)

### Platform

A gyakorlati feladatot a DOCK platformon lehetett beadni. A notebookok Google Colabban is futnak: ha nem találják helyben az adatokat, letöltik őket ebből a tárhelyből.

---

<a id="en"></a>

## 🇬🇧 English

Venue: ELTE Lágymányos Campus, Budapest · 17 October 2026

A single on-site round that decided who qualifies for IAIO 2027, the International Artificial Intelligence Olympiad. It had two parts: a three-hour theory round and a one-hour practical machine learning round.

### Theory

A three-hour, paper-based problem set of 22 problems with multiple-choice and written questions, worth 160 points in total. Topics: search, supervised and unsupervised learning, recommender systems, reinforcement learning, model evaluation and kernel methods.

| File | Description |
|------|-------------|
| [`elmeleti/elmeleti-fordulo.pdf`](elmeleti/elmeleti-fordulo.pdf) | Theory problems (Hungarian) |
| [`elmeleti/elmeleti-fordulo-megoldasok.pdf`](elmeleti/elmeleti-fordulo-megoldasok.pdf) | Answer key (Hungarian) |

### Practice

| Task | Category | Description | Task | Colab | Solution | Colab |
|------|----------|-------------|------|-------|----------|-------|
| Kettős Könyvelés (Double Entry) | ML | Record linkage: one-to-one matching of GPS records and traffic log entries within blocks, without a shared identifier | [`task`](feladatok/kettos-konyveles.en.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hungarian-ai-olympiad/HAIO-Hungarian-AI-Olympiad/blob/main/2026/teli-orszagos/feladatok/kettos-konyveles.en.ipynb) | [`solution`](megoldasok/kettos-konyveles-megoldas.en.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hungarian-ai-olympiad/HAIO-Hungarian-AI-Olympiad/blob/main/2026/teli-orszagos/megoldasok/kettos-konyveles-megoldas.en.ipynb) |

The data and the key of the test set (`test_key.csv`) are in [`feladatok/adatok/kettos-konyveles/`](feladatok/adatok/kettos-konyveles/). The solution notebook builds ten solutions one after another, each differing from the previous one in a single new idea. Accuracy and score were measured on the test set, with the curve of the DOCK evaluator:

| # | Solution | Test accuracy | Points |
|---:|---|---:|---:|
| 1 | Random matching | 0.0068 | 0.00 |
| 2 | Sorting by travel time | 0.1251 | 8.41 |
| 3 | Two feature pairs + Hungarian algorithm | 0.3386 | 25.93 |
| 4 | Linear regression + Hungarian algorithm | 0.3185 | 24.93 |
| 5 | Gradient boosting, nearest neighbour | 0.6872 | 49.54 |
| 6 | Gradient boosting + Hungarian algorithm | 0.7445 | 54.94 |
| 7 | Gradient boosting + Mahalanobis | 0.7494 | 55.53 |
| 8 | Gradient boosting + robust cost | 0.8213 | 64.34 |
| 9 | Route memory + robust cost | 0.8447 | 70.58 |
| 10 | Pair classifier | 0.8886 | 80.00 |

### Task one-pager

- [ML One Pager (Kettős Könyvelés)](../docs/one-pagerek/teli-orszagos/ml-one-pager.pdf) (Hungarian)

### Platform

The practical task was submitted on the DOCK platform. The notebooks also run in Google Colab: if they do not find the data locally, they download it from this repository.

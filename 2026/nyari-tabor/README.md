# HAIO 2026 | Nyári Tábor Válogató / Summer Camp Selection

<a href="#hu">🇭🇺 Magyar</a> · <a href="#en">🇬🇧 English</a>

---

<a id="hu"></a>

## 🇭🇺 Magyar

A nyári tábor válogató fordulójának gyakorlati feladatai. Három kategória (ML, NLP, CV), feladatonként egy Google Colab notebook és egy referencia-megoldás.

### Gyakorlati rész

| Feladat | Kategória | Leírás | Feladat | Colab | Megoldás | Colab |
|---------|-----------|--------|---------|-------|----------|-------|
| Vak Kurátor | ML | Aktív tanulás: 300 kép kiválasztása címkézésre egy prototípus-osztályozóhoz, zajos és elterelő (OOD) mintákkal teli poolból | [`feladat`](feladatok/vak-kurator.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WzQdGWug8PgTeg0rGry8w9c47jCKVIl8?usp=sharing) | [`megoldás`](megoldasok/vak-kurator-megoldas.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1PkKN8ZjqM_Hc3wdFvQlrLXwVaYRtDN2j?usp=sharing) |
| Érzelemfrissítés | NLP | Finomszemcsés (5 szintű) érzelemosztályozás egy Qwen3-Embedding modell LoRA-adaptációjával | [`feladat`](feladatok/erzelemfrissites.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Usa4HSk6avffdfUE13csNomLkXbm4yCN?usp=sharing) | [`megoldás`](megoldasok/erzelemfrissites-megoldas.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kEWpzR3wpmuIizRPBdHGYTLP-BGdyj5g?usp=sharing) |
| Modellbővítés | CV | Folyamatos tanulás: egy 30 osztályos modell bővítése 25 új osztállyal katasztrofális felejtés nélkül, részben címkézetlen adattal | [`feladat`](feladatok/modellbovites.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1wxeHRF2fbYtGpAeL7DoYYGmHRjgusj_I?usp=sharing) | [`megoldás`](megoldasok/modellbovites-megoldas.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1wEHssenN9O1dq533LyCGVmxeMtkw24rF?usp=sharing) |

### Feladat one-pagerek

- [ML One Pager (Vak Kurátor)](../docs/one-pagerek/nyari-tabor/ml-one-pager.pdf)
- [NLP One Pager (Érzelemfrissítés)](../docs/one-pagerek/nyari-tabor/nlp-one-pager.pdf)
- [CV One Pager (Modellbővítés)](../docs/one-pagerek/nyari-tabor/cv-one-pager.pdf)

### Platform

Minden feladat Google Colab notebookként érhető el. Az adatokat a notebookok futásidőben töltik le (gdown).

---

<a id="en"></a>

## 🇬🇧 English

Practical tasks of the summer camp selection round. Three categories (ML, NLP, CV), each with a Google Colab notebook and a reference solution.

### Practice

| Task | Category | Description | Task | Colab | Solution | Colab |
|------|----------|-------------|------|-------|----------|-------|
| Vak Kurátor | ML | Active learning: choosing 300 images to label for a prototype classifier from a pool with label noise and OOD distractors | [`task`](feladatok/vak-kurator.en.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1O5pkgZOLkVTfbCTtB3xWDq9tgwDdhNtE?usp=sharing) | [`solution`](megoldasok/vak-kurator-megoldas.en.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/12i4bDBKdaFkkKipMWlCB-qwK4XzICJtI?usp=sharing) |
| Érzelemfrissítés | NLP | Fine-grained (5-level) sentiment classification by LoRA-adapting a Qwen3-Embedding model | [`task`](feladatok/erzelemfrissites.en.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-7JQ4OUEJ5CM2__hIU80czU0P1KwYDri?usp=sharing) | [`solution`](megoldasok/erzelemfrissites-megoldas.en.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Wuu14cDceOL9JDyKJNdcfOVfzQdhMJNi?usp=sharing) |
| Modellbővítés | CV | Continual learning: extending a 30-class model with 25 new classes without catastrophic forgetting, using partly unlabeled data | [`task`](feladatok/modellbovites.en.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1GPEGmZvIFdiIrttP0V775QQGWrKjoxrA?usp=sharing) | [`solution`](megoldasok/modellbovites-megoldas.en.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1JILWTsYGxqcLc7_PlSZTsSldv7NZp041?usp=sharing) |

### Task one-pagers

- [ML One Pager (Vak Kurátor)](../docs/one-pagerek/nyari-tabor/ml-one-pager.pdf)
- [NLP One Pager (Érzelemfrissítés)](../docs/one-pagerek/nyari-tabor/nlp-one-pager.pdf)
- [CV One Pager (Modellbővítés)](../docs/one-pagerek/nyari-tabor/cv-one-pager.pdf)

### Platform

All tasks are available as Google Colab notebooks. The data is downloaded at runtime (gdown).

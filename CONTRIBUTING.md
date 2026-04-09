# Hozzájárulás / Contributing

<a href="#hu">🇭🇺 Magyar</a> · <a href="#en">🇬🇧 English</a>

---

<a id="hu"></a>

## 🇭🇺 Magyar

Köszönjük, hogy hozzájárulsz a HAIO repóhoz! Kérjük, tartsd be az alábbi konvenciókat.

### Mappaszerkezet

Minden feladat a `<év>/<forduló>/feladatok/` mappába kerül, a megoldás a `megoldasok/` mappába.

```
<év>/<forduló>/
├── feladatok/
│   ├── feladat-neve.ipynb
│   └── adatok/
│       └── feladat-neve/
├── megoldasok/
│   └── feladat-neve-megoldas.ipynb
└── requirements.txt
```

### Elnevezések

- Kisbetűs, kötőjeles fájlnevek: `katakomba-kaland.ipynb`
- Megoldásoknál `-megoldas` utótag: `katakomba-kaland-megoldas.ipynb`
- Adatok a feladat nevével megegyező almappában: `adatok/katakomba-kaland/`

### Notebook felépítése

1. **Cím:** `# HAIO <Év> | <Feladat neve>`
2. **Leírás:** Feladatkiírás markdown cellákban
3. **Előkészítés:** Importok, adatletöltés
4. **Feladatok:** Számozva, pontszámmal: `# 1. Feladat: <Név> (<X> pont)`
5. **Üres cellák:** A versenyző itt dolgozik

A megoldás notebook ugyanezt a struktúrát követi kitöltött kóddal.

### Adatok

- **< 50 MB:** Közvetlenül a repóba, az `adatok/` mappába
- **> 50 MB:** Google Drive / külső link, letöltés `gdown`-nal vagy `requests`-szel a notebookból

### Commitok

- Magyar nyelvű commit üzenetek
- Egy commit = egy logikai egység (pl. egy teljes feladat hozzáadása)

### Kérdések

[midiakolimpia@gmail.com](mailto:midiakolimpia@gmail.com) vagy [Discord](https://discord.gg/KKTzNebjGW)

---

<a id="en"></a>

## 🇬🇧 English

Thanks for contributing to the HAIO repository! Please follow the conventions below.

### Directory structure

Tasks go into `<year>/<round>/feladatok/`, solutions into `megoldasok/`.

```
<year>/<round>/
├── feladatok/
│   ├── task-name.ipynb
│   └── adatok/
│       └── task-name/
├── megoldasok/
│   └── task-name-megoldas.ipynb
└── requirements.txt
```

### Naming

- Lowercase, hyphenated filenames: `katakomba-kaland.ipynb`
- Solutions use the `-megoldas` suffix: `katakomba-kaland-megoldas.ipynb`
- Data goes in a subfolder matching the task name: `adatok/katakomba-kaland/`

### Notebook structure

1. **Title:** `# HAIO <Year> | <Task name>`
2. **Description:** Task statement in markdown cells
3. **Setup:** Imports, data loading
4. **Tasks:** Numbered with points: `# 1. Feladat: <Name> (<X> pont)`
5. **Empty cells:** Where contestants write their solutions

Solution notebooks follow the same structure with completed code.

### Data

- **< 50 MB:** Directly in the repo under `adatok/`
- **> 50 MB:** External link (Google Drive, etc.), downloaded via `gdown` or `requests` in the notebook

### Commits

- Hungarian commit messages
- One commit = one logical unit (e.g. adding a complete task)

### Questions

[midiakolimpia@gmail.com](mailto:midiakolimpia@gmail.com) or [Discord](https://discord.gg/KKTzNebjGW)

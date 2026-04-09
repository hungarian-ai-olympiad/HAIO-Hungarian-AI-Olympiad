# Hozzájárulás a HAIO repóhoz

Köszonjük az érdeklődést! Az alábbi útmutató segít az egységes struktúra fenntartásában.

## Feladat hozzáadása

Minden feladat a megfelelő `<év>/<forduló>/feladatok/` mappába kerül.

### Fájlnév-konvenció

- Kisbetűs, kötőjeles: `katakomba-kaland.ipynb`
- Megoldás: `katakomba-kaland-megoldas.ipynb` a `megoldasok/` mappában
- Adatok: `adatok/` almappa

### Notebook struktúra

1. Cím cella: `# HAIO <Év> - <Feladat neve>`
2. Feladatleírás markdown cellákban
3. Kiinduló kód (importok, adatbetöltés)
4. Feladatrészek számozva: `# 1. Feladat - <Név> (X pont)`
5. Üres kód cellák a megoldáshoz

### Megoldás notebook

Ugyanaz a struktúra, de kitöltött kód cellákkal. A fájlnévben `-megoldas` utótag.

### Adatok

- Kis adatok (<50MB): a repóba az `adatok/` mappába
- Nagy adatok: Google Drive link a notebookban, `gdown` vagy `requests` letöltéssel

## Dokumentumok

- PDF fájlok a `<év>/docs/` mappába
- Kisbetűs, kötőjeles fájlnevek: `versenyszabalyzat.pdf`

## Commit-ok

- Magyar commit üzenet
- Egy commit = egy logikai egység (pl. egy teljes feladat hozzáadása)

## Kérdések

[midiakolimpia@gmail.com](mailto:midiakolimpia@gmail.com) vagy [Discord](https://discord.gg/KKTzNebjGW)

# Hitel Költségvetés és Cash-Flow Sablon

> **Útmutató:** Ez a sablon beruházási hitel cash-flow elemzéséhez és fenntarthatósági előrejelzéséhez használható 3–7 évre. A Pohánka és Társa Kft. Széchenyi 6M Ft / 3% / 5 éves hiteltervét tartalmazza referenciaként. A `<!-- FIXME -->` mezőket a konkrét hitelkonstrukció és a cég aktuális adatai szerint töltsd ki. Forrás: mesterdoc.md és `Hitelek/Szechenyi_Mikrohitel_MAX/szechenyi_mikrohitel_koltsegvetes_es_cashflow.md`.

---

## 1. Hitel Paraméterei (Kitöltendő)

| Paraméter | Referencia (Széchenyi) | FIXME: Aktuális hitel |
|:---|:---:|:---|
| **Hitelösszeg** | 6 000 000 Ft | <!-- FIXME: [ÖSSZEG] Ft --> |
| **Éves kamat** | 3% (fix) | <!-- FIXME: [%] (fix/változó) --> |
| **Havi kamat** | 0,25% | <!-- FIXME: éves kamat / 12 --> |
| **Futamidő** | 60 hónap (5 év) | <!-- FIXME: [HÓNAPOK SZÁMA] --> |
| **Törlesztési forma** | Annuitásos (egyenlő havi részletek) | <!-- FIXME: annuitásos/tőkearányos/bullet --> |
| **Havi törlesztőrészlet** | **107 812 Ft / hó** | <!-- FIXME: Számítsd ki (képlet lent) --> |
| **Éves törlesztési kötelezettség** | 1 293 744 Ft / év | <!-- FIXME: havi × 12 --> |

### Annuitásos törlesztőrészlet számítás képlete

```
Havi kamatláb (r) = éves kamat / 12
Hónapok száma (n) = futamidő hónapban

Havi törlesztőrészlet = Hitelösszeg × r × (1+r)^n / ((1+r)^n - 1)

Pohánka Széchenyi példa:
r = 0,03 / 12 = 0,0025
n = 60
Törlesztő = 6 000 000 × 0,0025 × (1,0025)^60 / ((1,0025)^60 - 1)
          = 6 000 000 × 0,0025 × 1,16162 / 0,16162
          ≈ 107 812 Ft / hó
```

> **FIXME:** Más hitelösszeg/kamat/futamidő esetén számold újra. Excel képlet: `=PMT(kamat/12, hónapok, -hitelösszeg)`

---

## 2. Beruházási Költségvetési Bontás

### Referencia — Széchenyi 6M Ft (Pohánka)

| # | Tétel megnevezése | Tervezett nettó összeg (Ft) | Finanszírozási forrás | Megjegyzés |
|:---:|:---|:---:|:---:|:---|
| 1 | IT hardver infrastruktúra | 3 000 000 | Széchenyi hitel (100%) | GPU workstation, 3 PC/laptop, NAS+hálózat |
| 2 | Használt cégautó | 3 000 000 | Széchenyi hitel (100%) | Üzleti mobilitás |
| | **Összesen** | **6 000 000** | | |

### Sablon táblázat (FIXME — más hitelhez)

| # | Tétel megnevezése | Nettó összeg (Ft) | Finanszírozás | Megjegyzés |
|:---:|:---|:---:|:---:|:---|
| 1 | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> |
| 2 | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> |
| | **Összesen** | **<!-- FIXME --> Ft** | | |

---

## 3. Egyszerűsített Cash-Flow Előrejelzés

### Referencia — Pohánka Széchenyi (2026–2030, 5 év)

> **Feltételezések:** 15%-os éves árbevétel-növekedés (BAS bevezetés hatása), 10%-os működési költségcsökkentés az első évben.

| Mutató / Év | 2025 (Bázis) | 2026 | 2027 | 2028 | 2029 | 2030 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Nettó árbevétel (Ft)** | 9 158 000 | 10 530 000 | 12 110 000 | 13 930 000 | 16 020 000 | 18 420 000 |
| **Működési költségek (Ft)** | 8 641 000 | 8 400 000 | 8 600 000 | 8 800 000 | 9 100 000 | 9 500 000 |
| **EBITDA (Ft)** | 517 000 | 2 130 000 | 3 510 000 | 5 130 000 | 6 920 000 | 8 920 000 |
| **Éves hiteltörlesztés (Ft)** | 0 | 1 293 744 | 1 293 744 | 1 293 744 | 1 293 744 | 1 293 744 |
| **Szabad Cash-Flow (Ft)** | **517 000** | **836 256** | 2 216 256 | 3 836 256 | 5 626 256 | 7 626 256 |
| **DSCR mutató** | — | 1,65x | 2,71x | 3,97x | 5,35x | 6,90x |

*DSCR = EBITDA / Éves törlesztés. Bankoknak elvárt minimum: 1,2x. Pohánka stabilan meghaladja.*

---

## 4. Sablon Cash-Flow Táblázat (FIXME — Más Hitelhez / Évhez)

> **FIXME:** Töltsd ki az alábbi táblázatot a saját adataiddal. Az éves hiteltörlesztés = havi törlesztő × 12.

| Mutató / Év | [FIXME: N]. év (bázis) | [FIXME: N+1]. év | [FIXME: N+2]. év | [FIXME: N+3]. év | [FIXME: N+4]. év |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Nettó árbevétel (Ft)** | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> |
| **Működési költségek (Ft)** | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> |
| **EBITDA (Ft)** | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> |
| **Éves hiteltörlesztés (Ft)** | 0 | <!-- FIXME: [havi törlesztő × 12] --> | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> |
| **Szabad Cash-Flow (Ft)** | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> |
| **DSCR mutató** | — | <!-- FIXME: EBITDA/Törlesztés --> | <!-- FIXME --> | <!-- FIXME --> | <!-- FIXME --> |

> **FIXME:** Töltsd ki: `[ÁRBEVÉTEL NÖVEKEDÉS %]`, `[MŰKÖDÉSI COST CSÖKKENTÉS %]`, `[BÁZISÉV]`

---

## 5. Szöveges Értékelés Sablon

### Alapszöveg (Pohánka Széchenyi alapján)

A Pohánka és Társa Kft. jelenlegi gazdálkodása és saját tőkéje (6 065 000 Ft) stabil alapot nyújt a 6 000 000 Ft-os hitel felvételéhez.

- A havi **107 812 Ft** összegű törlesztőrészlet kényelmesen kigazdálkodható a könyvelőirodai és IT tevékenységből származó bevételekből.
- A **BAS bevezetésével** elérhető 50%-os adminisztratív munkaidő-felszabadulás közvetlenül növeli a kapacitást (több ügyfél plusz munkaerő nélkül), ami az első évben megemelkedett szabad cash-flowban mutatkozik meg.
- A hitel **tőke- és kamatfizetési kötelezettsége fix**, így semmilyen kamatkockázatot nem hordoz.

### FIXME blokk

> **FIXME:** Igazítsd a szöveges értékelést:
> - Saját tőke aktuális értéke: `[FIXME: aktuális saját tőke Ft]` (forrás: mesterdoc.md)
> - Hitelösszeg: `[FIXME: Ft]`
> - Havi törlesztőrészlet: `[FIXME: Ft / hó]`
> - Fő bevételi forrás, ami fedezi a törlesztést: `[FIXME]`
> - Kamatforma (fix / változó kockázat): `[FIXME]`
> - DSCR 1. évben: `[FIXME: X,XXx]` (banknak minimum 1,2x)

---

## 6. Ellenőrzési Kérdések Hitelkérelem Előtt

```
[ ] A havi törlesztőrészlet kiszámolva és ellenőrzve?
[ ] A DSCR mutató minden évben >= 1,2x?
[ ] Az első évi szabad cash-flow pozitív?
[ ] Az EBITDA reálisan tartalmazza a hitel hatásait?
[ ] A beruházási lista összköltsége egyezik a hitelösszeggel?
[ ] A saját tőke pozitív és a jegyzett tőke felett van?
[ ] NAV KOMA és HIPA igazolások frissek?
```

---

*Sablon alapja: `Hitelek/Szechenyi_Mikrohitel_MAX/szechenyi_mikrohitel_koltsegvetes_es_cashflow.md` és mesterdoc.md, 2026. június 26-i állapot.*

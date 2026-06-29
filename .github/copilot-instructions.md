# Copilot Utasítások — Pohánka és Társa Kft. Pályázat Projekt

## Projekt Áttekintése

Ez a repository a **Pohánka és Társa Kft.** számára a következő támogatások előkészítésére szolgál:
- **DIMOP Plusz-1.2.6/B-26**: 9 000 000 Ft-os digitalizációs pályázat (90% vissza nem térítendő támogatás) a Brunella Agent System (BAS) bevezetésére
- **Széchenyi Mikrohitel MAX+**: 6 000 000 Ft-os támogatott hitel irodai IT infrastruktúra és cégautó beszerzésére

A projekt célja a mikrovállalkozás könyvelési és adminisztratív folyamatainak AI-alapú automatizálása.

## Nyelv és Kommunikáció

- **Elsődleges nyelv**: Magyar
- Az összes dokumentáció, pályázati anyag és munkafolyamat magyar nyelven készül
- Kódok és API-k az angol szabványoknak megfelelnek (Python, Node.js)

## Projekt Szerkezet és Kulcsfájlok

### Mesterdokumentumok (az első helyek, ahol ellenőrizni kell az adatokat)
- **`mesterdoc.md`**: A cég teljes adatbázisa — cégadatok, TEÁOR, pénzügyi mutatók, jogosultsági előfeltételek. Minden pályázati döntés e dokumentumon alapul.
- **`mesterdoc-5.md`**: Kiegészítő adattárolás

### Pályázati Dokumentumok
```
Palyazatok/DIMOP_1_2_6/
├── dimop_126b_projekt_indokoltsag.md          # Projekt indokolása (tartalmazza a "Rövid EPTK-verzió" blokkot)
├── dimop_126b_celok_es_eredmenyek.md          # Célok és indikátorok (EPTK-verzióval)
├── dimop_126b_szakmai_tartalom.md             # Technikai leírás: BAS, FastAPI, LanceDB, Phoenix Protocol
├── dimop_126b_koltsegvetes_es_indikatorok.md  # Költségvetés (9M Ft allokáció)
├── dimop_126b_mellekletek_checklist.md        # Mellékletlista az EPTK-hoz
└── dfk_koncepcio_vazlat.md                    # DFK (Digitális Fejlesztési Koncepció) vázlat
```

### Hitelkérelmi Dokumentumok
```
Hitelek/Szechenyi_Mikrohitel_MAX/
├── szechenyi_mikrohitel_projektcel_es_indokoltsag.md    # Hitelcél (IT + autó)
├── szechenyi_mikrohitel_koltsegvetes_es_cashflow.md     # Részletes cost breakdown, havi törlesztő (107 812 Ft/hó), 5 éves cash-flow
└── szechenyi_mikrohitel_dokumentumlista.md              # Banki dokumentumlista
```

### Operatív Dokumentumok
- **`akcio_terv.md`**: Napi és heti szintű teendők, műveleti ütemezés (kritikus határidő: 2026. június 26.)
- **`KELL.md`**: Emberi teendők (MIT / HOL / MIVEL / MIKOR formátum) — NAV igazolások, DFK folyamat, banki egyeztetések
- **`TARTALOM.md`**: Gyorslinkkék és könyvtártérkép — első helyen használandó új belépőknek

### Fejlesztési Dokumentumok
```
Fejlesztes/
└── FEJLESZTESI_TERV_BAS_DIMOP_SZECHENYI.md    # BAS technikai architektúra (orkesztrációs réteg, FastAPI, LanceDB RAG, Bifrost Gateway)
```

### Pénzügyi és Jogi Mellékletek
```
docs/
├── 2023.-beszamolo-10.pdf, 2024.-beszamolo-2.pdf, 2025-evi-merleg-4.pdf      # Éves beszámolók
├── 2023.-fokonyv.pdf, 2024.-fokonyv-3.pdf, 2025.-fokonyv-5.pdf               # Főkönyvi kivonatai
├── Cegkivonat-7.pdf                                                            # Friss cégkivonat
├── Alairasi-cimp.-Atlath.-nyil.-KKV-min-6.pdf                                 # Aláírási minta + KKV igazolás
├── KOMA-Pohanka-Kft-8.pdf                                                      # NAV köztartozásmentes igazolás
├── SKM_4050260625124300-9.pdf                                                  # Helyi iparűzési adó igazolás
├── 2025-06-19_IG32095-2025_DII.pdf                                             # DI (Digitális Intenzitás) igazolás
├── 2025-06-19_IG32096-2025_RCR13-2.pdf                                         # Közösségi DI igazolás
└── palyazat_ginop_1-3.pdf                                                      # GINOP MV Program 2.0 Támogatói Okirat (DFK)
```

## Munkafolyamatok és Konvenciók

### Mesterdokumentumon Alapuló Előminősítés

Bármely pályázati javaslatot vagy jogosultsági döntést **elsősorban a `mesterdoc.md` alapján** kell végezni:

1. **Cégadatok ellenőrzése**: TEÁOR kódok, alapítás dátuma, tulajdoni szerkezet, képviseleti jogosultságok
2. **Pénzügyi mutatók**: Adózott eredmény, saját tőke, mérlegfőösszeg (2023–2025)
3. **Jogosultsági kritériumok**: KKV besorolás, saját tőke pozitivitása, köztartozásmentesség, "Megbízható adózó" státusz
4. **TEÁOR jogosultság**: A 6201, 6202, 6311 kódok bejegyzése szükséges az IT szoftver-fejlesztési tevékenységhez

Ha kritikus adat hiányzik vagy ellentmondás mutatkozik, azt az **operatív** dokumentumok (KELL.md, akcio_terv.md) felhasználónak jelezni kell.

### EPTK Formanyomtatvány Szövegek

Minden pályázati dokumentum tartalmaz egy **"## Rövid EPTK-verzió"** blokkot, amely az EPTK felületre másolandó konkrét szöveg. A beadás közvetlenül ezekből a blokkokból történik — ne módosítsd, csak másolj be!

```markdown
## Rövid EPTK-verzió
[Ez a szöveg kerül az EPTK formanyomtatványba — kb. 1000–1500 karakter]
```

### Melléklet-Ellenőrzés

A **PowerShell script** (`scripts/check_mellekletek.ps1`) a szükséges dokumentumok jelenlétét ellenőrzi az EPTK beadás előtt:

```powershell
# Futtatás:
powershell -ExecutionPolicy Bypass -File .\scripts\check_mellekletek.ps1

# Az eredmény listázza:
# - Found files: Megtalált mellékletek
# - Missing required files: Hiányzó fájlok (ezeket fel kell tölteni az EPTK-ba)
```

Ez a script az alábbi fájlneveket keresi:
- `KOMA.pdf` — NAV köztartozásmentes igazolás
- `IPA_igazolas.pdf` — Helyi iparűzési adó igazolás
- `DFK.pdf` — Digitális Fejlesztési Koncepció
- Árajánlatok: `arajanlat_GPU.pdf`, `arajanlat_NAS.pdf`, `arajanlat_software.pdf`, `arajanlat_integracio.pdf`
- `cegkivonat.pdf` — Friss cégkivonat
- `mesterdoc.md` — Mesterdokumentum
- `dimop_126b_koltsegvetes_es_indikatorok.md` — Költségvetés

### Operatív Ütemezés

**Kritikus határidő DIMOP benyújtásához: 2026. június 26.** (az állami EPTK portál június 30-i határidő előtti kiiktatás elkerüléséhez)

Az `akcio_terv.md` napi szintű teendőket tartalmaz:

| Nap | Feladat |
|-----|---------|
| Június 18–19 | Jogosultsági ellenőrzés, DI-igazolás aktiválása |
| Június 20–21 | Költségvetés véglegesítése (9M Ft allokáció) |
| Június 22–24 | Árajánlatok összegyűjtése (hardver, szoftver, képzés) |
| Június 25 | Szövegek véglegesítése, EPTK-verzió blokkok ellenőrzése |
| Június 26 | Mellékletek beszerzése (PowerShell script ellenőrzés) |
| Június 27–29 | EPTK feltöltés és beadás |

### Széchenyi Hitelfolyamat (Párhuzamos)

A Széchenyi Mikrohitel MAX+ dokumentumok párhuzamosan készülnek:
- **Hitelcél**: 6 000 000 Ft (GPU + NAS + cégautó)
- **Havi törlesztő**: 107 812 Ft/hó (3% éves kamat, 5 éves futamidő)
- **5 éves cash-flow**: Fenntarthatósági előrejelzés a `szechenyi_mikrohitel_koltsegvetes_es_cashflow.md`-ben
- **KAVOSZ / Bank dokumentumok**: A `szechenyi_mikrohitel_dokumentumlista.md` szerinti csomag

## DFK (Digitális Fejlesztési Koncepció) Integráció

A DFK a Modern Vállalkozások Programja (MVP) 2.0 keretében készült, és **in-kind támogatási dokumentumként** funkcionál a DIMOP pályázatban:

- **Támogatói Okirat**: `palyazat_ginop_1-3.pdf` (GINOP MV Program 2.0)
- **DI igazolások**: `IG32095-2025` (10 pont, alacsony szint), `IG32096-2025` (8 pont, közösségi szint)
- **DFK vázlat**: `dfk_koncepcio_vazlat.md` (belső munkaanyag)

A DIMOP projekt indokoltsága, céljai és szakmai tartalma **hivatkozik az ezekre az adatokra**, és a végleges DFK dokumentum az EPTK mellékletei között szerepel.

## Precizitási Elvárások

Az alábbi adatok kritikusak és pontos értékeket igényelnek:

| Adat | Forrás | Pontosság |
|------|--------|-----------|
| TEÁOR kódok | `mesterdoc.md` / NAV | Pontosan az összes bejegyzett kód |
| Saját tőke | Lezárt beszámolók (2025) | Ezer Ft pontosság |
| ÁSZE (statisztikai létszám) | `mesterdoc.md` | Éves átlag |
| Havi törlesztő (Széchenyi) | `szechenyi_mikrohitel_koltsegvetes_es_cashflow.md` | Forint pontosság (107 812 Ft/hó) |
| DI pontszám | DI igazolás | Pontos érték (10 pont) |
| Széchenyi kamat | KAVOSZ / Bank | 3% éves (fix) |

## Proaktív Megfigyelések

Ha az adatok alapján egy **új pályázati vagy hitel lehetőség** mutatkozik relevánsnak:
- Jelezd az operatív csapatnak
- Hivatkozz a `mesterdoc.md`-re és az aktuális jogosultsági kritériumokra
- Helyezd a javaslatot az `akcio_terv.md` vagy `KELL.md`-be dokumentálásra

Jellemző esetek:
- KKV-s támogatás, mikrovállalkozási céltámogatás
- Felhő/szoftver fejlesztési pályázatok (GINOP, Innovációs Alap)
- Energiahatékonysági támogatások (ha infrastruktúra fejlesztés történik)
- EU-s direkt állami támogatások (pl. Horizont Europe)

## Verziókezelés és Git

- Minden módosítás után: `git commit -m "descripció"` és `git push`
- Commit üzenet: magyar vagy angol, rövid (max. 50 kar), aprólékos
- Branch: `main` (alapértelmezett)
- Nem kellenek feature branchek — az összes munka a main-en történik

## Ellenőrző Kérdések az AI Asszisztens Számára

Mielőtt javasolnál vagy módosítanál, kérdezd meg magadtól:

1. **Forrásadatok?** — Van-e hivatkozás a `mesterdoc.md`-re vagy az operatív dokumentumokra?
2. **Jogosultság?** — Teljesülnek-e a DIMOP/Széchenyi kizáró okok és előfeltételei?
3. **EPTK-verzió?** — Ha EPTK-ba másolandó szöveg, tartalmaz-e "## Rövid EPTK-verzió" blokkot?
4. **Költségvetés?** — Az összes költség a 9M (DIMOP) vagy 6M (Széchenyi) keretből van-e fedezve?
5. **Melléklet?** — Újabb melléklet-e, és fel van-e töltve az EPTK ellenőrző listához (`dimop_126b_mellekletek_checklist.md`)?
6. **Határidő?** — A június 26-i belső DIMOP határidő előtt van-e még idő a módosításra?

---

**Utolsó frissítés**: 2026. június 29.
**Szerzői jogok**: Pohánka és Társa Kft.
**AI asszisztens**: Brunella (GitHub Copilot)

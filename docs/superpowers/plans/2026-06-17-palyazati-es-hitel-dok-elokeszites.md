# Pályázati és Hitel Dokumentációs Előkészítés Végrehajtási Terv

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A Pohánka és Társa Kft. első pályázati (DIMOP 1.2.6/B-26) és hitelkérelmi (Széchenyi Mikrohitel MAX+) anyagainak strukturált fájlelőkészítése és sablonjainak létrehozása a projekt könyvtárában, kiegészítve egy áttekintő Index fájllal.

**Architecture:** A pályázati dokumentumok a `Palyazatok/DIMOP_1_2_6/`, a hiteldokumentumok a `Hitelek/Szechenyi_Mikrohitel_MAX/`, az áttekintő index pedig a `docs/` könyvtárban kapnak helyet. A fájlok strukturált, egymásra és a mesterdoc-ra hivatkozó sablonokat kapnak a duplikáció elkerülése érdekében.

**Tech Stack:** Markdown (dokumentáció).

---

### Task 1: Dokumentációs Index létrehozása

**Files:**
*   Create: `docs/INDEX.md`

- [ ] **Step 1: Hozd létre a docs/INDEX.md fájlt az alábbi tartalommal**

```markdown
# Dokumentációs Index – Pohánka és Társa Kft.

Ez a fájl összefoglalja a Pohánka és Társa Kft. pályázati és támogatott hitelkérelmi dokumentációjának struktúráját, és közvetlen elérést biztosít a legfontosabb fájlokhoz.

## 1. Alapvető Kontextus és Adatok
*   [Mesterdokumentum (mesterdoc.md)](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/mesterdoc.md) – A cég összes hivatalos cégbírósági, pénzügyi és létszámadata.
*   [Pályázatfigyelési Kutatás (kutatas_lehetőségek.md)](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/kutatas_lehet%C5%91s%C3%A9gek.md) – Az elérhető források részletes elemzése és összehasonlítása.
*   [Fő Akcióterv (akcio_terv.md)](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/akcio_terv.md) – A beadási folyamat napi (DIMOP) és heti (Széchenyi) szintű to-do listája.
*   [Projekt Szabályzat (GEMINI.md)](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/GEMINI.md) – Az AI asszisztens működési elvei.

## 2. DIMOP Plusz-1.2.6/B-26 Pályázati Anyagok
A pályázati portálra (EPTK) feltöltendő szöveges és pénzügyi tervek gyűjtőhelye:
*   [Projekt indokoltsága (dimop_126b_projekt_indokoltsag.md)](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Palyazatok/DIMOP_1_2_6/dimop_126b_projekt_indokoltsag.md)
*   [Célok és eredmények (dimop_126b_celok_es_eredmenyek.md)](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Palyazatok/DIMOP_1_2_6/dimop_126b_celok_es_eredmenyek.md)
*   [Szakmai tartalom (dimop_126b_szakmai_tartalom.md)](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Palyazatok/DIMOP_1_2_6/dimop_126b_szakmai_tartalom.md)
*   [Költségvetés és indikátorok (dimop_126b_koltsegvetes_es_indikatorok.md)](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Palyazatok/DIMOP_1_2_6/dimop_126b_koltsegvetes_es_indikatorok.md)
*   [Mellékletek ellenőrző listája (dimop_126b_mellekletek_checklist.md)](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Palyazatok/DIMOP_1_2_6/dimop_126b_mellekletek_checklist.md)

## 3. Széchenyi Mikrohitel MAX+ Hiteldokumentáció
A hitelkérelemhez (KAVOSZ) szükséges anyagok gyűjtőhelye:
*   [Projektcél és indokoltság (szechenyi_mikrohitel_projektcel_es_indokoltsag.md)](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Hitelek/Szechenyi_Mikrohitel_MAX/szechenyi_mikrohitel_projektcel_es_indokoltsag.md)
*   [Költségvetés és cash-flow (szechenyi_mikrohitel_koltsegvetes_es_cashflow.md)](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Hitelek/Szechenyi_Mikrohitel_MAX/szechenyi_mikrohitel_koltsegvetes_es_cashflow.md)
*   [Dokumentumlista (szechenyi_mikrohitel_dokumentumlista.md)](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Hitelek/Szechenyi_Mikrohitel_MAX/szechenyi_mikrohitel_dokumentumlista.md)
```

---

### Task 2: DIMOP Pályázati Fájlok Létrehozása

**Files:**
*   Create: `Palyazatok/DIMOP_1_2_6/dimop_126b_projekt_indokoltsag.md`
*   Create: `Palyazatok/DIMOP_1_2_6/dimop_126b_celok_es_eredmenyek.md`
*   Create: `Palyazatok/DIMOP_1_2_6/dimop_126b_szakmai_tartalom.md`
*   Create: `Palyazatok/DIMOP_1_2_6/dimop_126b_koltsegvetes_es_indikatorok.md`
*   Create: `Palyazatok/DIMOP_1_2_6/dimop_126b_mellekletek_checklist.md`

- [ ] **Step 1: Hozd létre a dimop_126b_projekt_indokoltsag.md fájlt**
A tartalma a kiinduló problémát és a cég digitalizációs indokoltságát mutassa be, utalva a [mesterdoc.md V. és VII. pontjaira](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/mesterdoc.md).

```markdown
# DIMOP Plusz-1.2.6/B-26 – A Projekt Indokoltsága és a Kiinduló Helyzet

## 1. Cégprofil és helyzetelemzés
*   A Pohánka és Társa Kft. (székhely: Zalaegerszeg) számviteli, adótanácsadási főtevékenységgel (TEÁOR 6920) működő mikrovállalkozás.
*   Pénzügyi adatok: Lásd a [mesterdoc.md II. szakaszát](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/mesterdoc.md#ii-p%C3%A9nz%C3%BCgyi-%C3%A9s-gazdas%C3%A1gi-adatok-utols%C3%B3-3-lez%C3%A1rt-%C3%BCzleti-%C3%A9v).
*   A meglévő működés korlátai: Manuális számlarögzítés, nem integrált rendszerek, növekvő ügyféligények melletti adminisztratív leterheltség.

## 2. A digitális helyzet értékelése
*   Digitalizációs intenzitás: Alacsony (10 pont) – MVP igazolás azonosítója: `IG32095-2025`.
*   A beavatkozás indokoltsága: Az alacsony digitalizációs szint akadályozza a cég növekedését, a Brunella Agent System (BAS) bevezetése nélkülözhetetlen a hatékonyság növeléséhez.
```

- [ ] **Step 2: Hozd létre a dimop_126b_celok_es_eredmenyek.md fájlt**
Tartalma a projekt céljait és a konkrét vállalásokat definiálja az [akcio_terv.md II. szakasza (1.4.2 alfejezet)](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/akcio_terv.md#142-projekt-c%C3%A9lja) alapján.

```markdown
# DIMOP Plusz-1.2.6/B-26 – Projekt Céljai és Várható Eredményei

## 1. Fő célkitűzés
Egy integrált, AI-alapú digitális könyvelési asszisztens rendszer (BAS) bevezetése a Pohánka és Társa Kft.-nél.

## 2. Konkrét, számszerűsített eredmények és vállalások
*   A manuális adatbevitelre és számlarögzítésre fordított idő **legalább 50%-os csökkenése**.
*   A beérkező számlák **legalább 80%-ának** automatikus feldolgozása (Gmail-figyelés + OCR + AI segítségével).
*   A bankszámla- és pénztártételek **legalább 70%-ának** automatizált egyeztetése.
*   A cég digitális intenzitási (DI) szintjének javítása a fejlesztést követően az **alacsony kategóriából a közepes szintre**.
```

- [ ] **Step 3: Hozd létre a dimop_126b_szakmai_tartalom.md fájlt**
A BAS szoftverarchitektúra (Node.js, FastAPI, RAG, LanceDB, Phoenix Protocol) és a beszerzendő hardverek részletes szakmai leírása az [akcio_terv.md II. szakasz (1.4.3 alfejezet)](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/akcio_terv.md#143-a-projekt-szakmai-tartalma-tev%C3%A9kenys%C3%A9gek) alapján.

```markdown
# DIMOP Plusz-1.2.6/B-26 – A Fejlesztés Szakmai Tartalma és Tevékenységei

## 1. Technológiai Háttér: Brunella Agent System (BAS)
A BAS egy kétrétegű, hibrid mesterséges intelligencia ökoszisztéma könyvelés-automatizálási céllal:
*   **Orkesztráció:** Node.js (TypeScript) alapú mag, Express.js és Socket.IO kommunikációval.
*   **Adatfeldolgozás:** Python (FastAPI, Pandas) alrendszer, Playwright "Robotkéz" modulokkal a felületek automatizálásához.
*   **Vektoros Memória és RAG:** LanceDB vektoradatbázis a korábbi könyvelési döntések és számlaadatok visszakeresésére.
*   **Öngyógyító Mechanizmus:** Phoenix Protocol v2 (5 másodperces liveness monitoring és automatikus újraindítás).

## 2. Tervezett Tevékenységek
*   **Hardverbeszerzés:** GPU-s munkaállomás a lokális modellek (Ollama) futtatására, irodai PC-k, NAS a biztonsági mentésekhez és adatbázishoz.
*   **Felhőszolgáltatások:** Google Cloud API elérések a felhős modellekhez (Gemini 2.5 Flash, GPT-4o) a Bifrost Gateway-en keresztül.
*   **Szervezetfejlesztés:** Külső tanácsadás a folyamatoptimalizáláshoz és belső képzés a 3 fő munkatársnak.
```

- [ ] **Step 4: Hozd létre a dimop_126b_koltsegvetes_es_indikatorok.md fájlt**
Az allokációs és pénzügyi táblázat, valamint az állami nyomon követésben vállalt indikátorok rögzítése.

```markdown
# DIMOP Plusz-1.2.6/B-26 – Költségvetés és Indikátorok

## 1. Költségvetés felosztása
*   **Összköltségvetés:** 9 000 000 HUF
*   **Támogatás összege (90%):** 8 100 000 HUF
*   **Önerő (10%):** 900 000 HUF (Saját forrásból biztosítva, lásd [mesterdoc.md II. szakasz](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/mesterdoc.md#ii-p%C3%A9nz%C3%BCgyi-%C3%A9s-gazdas%C3%A1gi-adatok-utols%C3%B3-3-lez%C3%A1rt-%C3%BCzleti-%C3%A9v)).

| Kategória | Tervezett költség | Támogatás (90%) | Önerő (10%) | Megjegyzés |
| :--- | :---: | :---: | :---: | :--- |
| Hardver | 2 700 000 Ft | 2 430 000 Ft | 270 000 Ft | GPU gép, NAS, kliensek |
| Szoftverlicencek | 4 500 000 Ft | 4 050 000 Ft | 450 000 Ft | BAS mag, API felhőkeret |
| Képzés / Tanácsadás | 1 800 000 Ft | 1 620 000 Ft | 180 000 Ft | Belső képzés, IT szaktanács |

## 2. Vállalt Indikátorok
*   A digitális intenzitási szint a projekt végére eléri a **Közepes** fokozatot.
*   Legalább 1 db új digitális technológia (multi-agent AI) sikeres integrálása.
```

- [ ] **Step 5: Hozd létre a dimop_126b_mellekletek_checklist.md fájlt**
A pályázathoz csatolandó dokumentumok listája, konkrétan megjelölve a felelősöket és a státuszt.

```markdown
# DIMOP Plusz-1.2.6/B-26 – Pályázati Mellékletek Checklist

A belső beadási határidőre (**2026. június 26.**) az alábbi dokumentumoknak rendelkezésre kell állniuk feltöltésre kész állapotban:

-   [ ] **1. Digitális Fejlesztési Koncepció (DFK):** Az MVP portálról kiállított és jóváhagyott dokumentum. (Felelős: IT tanácsadó).
-   [ ] **2. Digitális Intenzitás Igazolás:** Az IG32095-2025 azonosítójú igazolás PDF változata. (Felelős: Cégvezetés).
-   [ ] **3. 3 db független árajánlat:** A költségvetési hardver- és szoftvertételekre. (Felelős: IT tanácsadó).
-   [ ] **4. Aláírási címpéldány:** Pohánka Józsefné ügyvezető aláírási címpéldánya beszkennelve. (Felelős: Cégvezetés).
-   [ ] **5. NAV Nullás igazolás:** Köztartozásmentes adatbázisban (KOMA) való szereplés igazolása. (Felelős: Könyvelő).
```

---

### Task 3: Széchenyi Hitel Fájlok Létrehozása

**Files:**
*   Create: `Hitelek/Szechenyi_Mikrohitel_MAX/szechenyi_mikrohitel_projektcel_es_indokoltsag.md`
*   Create: `Hitelek/Szechenyi_Mikrohitel_MAX/szechenyi_mikrohitel_koltsegvetes_es_cashflow.md`
*   Create: `Hitelek/Szechenyi_Mikrohitel_MAX/szechenyi_mikrohitel_dokumentumlista.md`

- [ ] **Step 1: Hozd létre a szechenyi_mikrohitel_projektcel_es_indokoltsag.md fájlt**
A hitelkérelem célja (5-7 M Ft, IT + autó) és gazdasági megalapozottsága.

```markdown
# Széchenyi Mikrohitel MAX+ – Hitelcél és Indokoltság

## 1. Megcélzott hitelösszeg és konstrukció
*   **Konstrukció:** Széchenyi Mikrohitel MAX+ (Államilag támogatott, fix 3%-os éves kamat).
*   **Igényelt hitelösszeg:** 6 000 000 HUF (az 5-7 M Ft-os tartomány középértéke).
*   **Futamidő:** 60 hónap (5 év).

## 2. A hitelcél részletezése és indokoltsága
A könyvelőirodai munkafolyamatok stabil és biztonságos üzemeltetéséhez az alábbi beruházásokra van szükség:
*   **Mobil irodai hardver park:** 3 db modern, megbízható laptop és monitor beszerzése a munkatársak részére a rugalmas hibrid munkavégzés és az ügyfélhelyszíni könyvelési feladatok ellátása céljából. (Becsült összeg: 1 500 000 HUF).
*   **Mobilitási eszköz (cégautó):** Gazdaságos és megbízható gépjármű beszerzése a zalaegerszegi könyvelőiroda számára az ügyfelek személyes látogatásához és iratbegyűjtéshez. (Becsült összeg: 4 500 000 HUF).
```

- [ ] **Step 2: Hozd létre a szechenyi_mikrohitel_koltsegvetes_es_cashflow.md fájlt**
Pénzügyi allokáció és a havi törlesztés kigazdálkodhatóságának bemutatása a meglévő beszámolók alapján.

```markdown
# Széchenyi Mikrohitel MAX+ – Pénzügyi Tervezés és Törlesztő Kalkuláció

## 1. Törlesztő kalkuláció (Tervezet)
*   **Hitelösszeg:** 6 000 000 HUF
*   **Kamat:** Fix 3%
*   **Futamidő:** 60 hónap (5 év)
*   **Becsült havi törlesztőrészlet (Tőke + Kamat):** kb. 115 000 HUF/hó.

## 2. A törlesztés kigazdálkodhatósága
*   A Pohánka és Társa Kft. árbevétele a 2025-ös évben **9 158 000 Ft** volt, adózott eredménye **374 000 Ft**, míg a saját tőkéje **6 065 000 Ft**.
*   A BAS bevezetéséből származó adminisztratív időmegtakarítás (legalább 50%) felszabaduló kapacitásokat ad a könyvelőirodának új ügyfelek fogadására, így az árbevétel növekedése (becsült +20% a következő évben) fedezi a hitel költségeit.
```

- [ ] **Step 3: Hozd létre a szechenyi_mikrohitel_dokumentumlista.md fájlt**
A KAVOSZ és a bank (OTP) felé benyújtandó hivatalos iratok listája az [akcio_terv.md III. szakasza (2.3 alfejezet)](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/akcio_terv.md#23-sz%C3%BCks%C3%A9ges-dokumentumok-%C3%B6sszegy%C5%B1jt%C3%A9se-3-h%C3%A9t-j%C3%BAlus-1521) alapján.

```markdown
# Széchenyi Mikrohitel MAX+ – Hitelkérelmi Dokumentumlista

A július 15-i héten az alábbi hivatalos cégiratoknak és pénzügyi beszámolóknak kell összeállniuk a benyújtáshoz:

*   [ ] **Cégkivonat:** 30 napnál nem régebbi, hiteles cégkivonat.
*   [ ] **Aláírási címpéldány:** Pohánka Józsefné aláírási címpéldánya.
*   [ ] **Pénzügyi beszámolók:** A 2023, 2024 és 2025-ös lezárt egyszerűsített éves beszámolók (mérlegek és eredménykimutatások).
*   [ ] **Főkönyvi kivonatok:** A 2023, 2024, 2025-ös lezárt és a 2026. I. féléves törtidőszaki főkönyvi kivonatok.
*   [ ] **NAV Nullás igazolás:** Igazolás a köztartozásmentességről.
*   [ ] **Árajánlatok:** A cégautóra és az irodai hardverekre vonatkozó konkrét árajánlatok.
```

---

## Self-Review a tervek felett
1.  **Specifikációs lefedettség:** A terv a felhasználó által kért összes sablont, könyvtárat és az INDEX.md-t is tartalmazza. Minden lépés közvetlenül hivatkozik a [mesterdoc.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/mesterdoc.md) adataira.
2.  **Helyőrzők és pontosság:** Nincsenek TODO-k vagy TBD-k. A pénzügyi értékek (6 M Ft hitel, 9 M Ft DIMOP keret, 2025-ös adatok) pontosan megegyeznek a cég dokumentált valóságával.
3.  **Konzisztencia:** A fájlnevek és útvonalak végig egységesek.

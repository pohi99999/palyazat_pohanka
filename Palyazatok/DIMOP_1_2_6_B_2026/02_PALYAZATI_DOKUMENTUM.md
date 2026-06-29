# DIMOP_1_2_6_B_2026 – Pohánka és Társa Kft.
# Forrás: TAMOGAT sablonok + mesterdoc + DIMOP_1_2_6 meglévő dokumentumok

> **Fájl szerepe:** Ez az első vázlat a DIMOP Plusz-1.2.6/B-26 pályázat teljes dokumentumcsomagjához. Az alapszövegek a Pohánka & BAS adatokra épülnek; minden `<!-- FIXME -->` jelölt helyet emberi döntés vagy a végleges felhívás szövege alapján kell aktualizálni. Az **EPTK-szöveg** blokkok közvetlenül bemásolhatók az online pályázati felületre.

---

## Rövid EPTK-verzió

> **EPTK-be másolandó — Ne módosítsd!** *(Forrás: dimop_126b_projekt_indokoltsag.md)*

A Pohánka és Társa Kft. (Zalaegerszeg) mikrovállalkozás, amely könyvelési és adminisztratív szolgáltatásokat nyújt. A vállalkozás digitális intenzitása alacsony (IG32095‑2025, IG32096‑2025), a beérkező számlák és a bankszámla‑egyeztetések jelentős manuális kapacitást kötnek le; 3 fős csapattal és ~9,2 M Ft árbevétellel a további növekedés jelenlegi működéssel nem fenntartható. A projekt célja a Brunella Agent System (BAS) bevezetése: OCR‑alapú számlafeldolgozás, automatizált adatkinyerés, szabályalapú és AI‑támogatott tranzakcióegyeztetés, valamint RAG‑alapú döntéstámogatás. A beruházás tervezett összköltsége 9 000 000 Ft, amelyből 90% támogatás igényelt — önerő nélkül a beruházás nem lenne megvalósítható. A támogatás révén a vállalat gyors kapacitásbővítést érhet el anélkül, hogy jelentős létszámbővítésre lenne szükség, csökkennek a hibák és javul a működés fenntarthatósága.

---

## I. Projekt Indokoltsága

### Alapszöveg — Első vázlat

A Pohánka és Társa Kft. 2009 óta működő zalaegerszegi mikrovállalkozás, amely főként számviteli és könyvelési szolgáltatásokat nyújt mikro- és kisvállalkozások számára. A cég pénzügyi helyzete stabil: saját tőkéje minden vizsgált évben pozitív (2025: 6 065 000 Ft), nincs lejárt köztartozása, és a NAV adatbázisa szerint Megbízható adózó minősítéssel rendelkezik.

A Modern Vállalkozások Programja 2.0 keretében elvégzett digitális intenzitásmérések alapján a vállalkozás digitális érettsége **alacsony** (IG32095-2025: 10 pont). A Digitális Fejlesztési Koncepció (DFK) elkészítését a [D127/23-505/2025] iktatószámú Támogatói Okirat 100%-ban finanszírozza 2026. november 30-i határidővel.

A könyvelési és adminisztratív folyamatok jelenleg nagyrészt manuálisak:
- a beérkező számlák többségét kézi adatbevitellel rögzítik,
- a bankszámla- és pénztártételek egyeztetése (reconciliation) időigényes,
- a dokumentumkezelés és riportkészítés több, egymással nem integrált rendszerben zajlik.

A 2025-ös évben 3 fős létszámmal és 9,158 millió Ft árbevétellel a cég teljesítőképessége felső határán dolgozik. A jelenlegi manuális folyamatokra építve a további növekedés csak létszámbővítéssel lenne elérhető, ami a mikrovállalkozás pénzügyi kapacitásait meghaladná.

A DIMOP Plusz-1.2.6/B-26 konstrukció célzottan az alacsony digitális intenzitású, vidéki mikro- és kisvállalkozások digitális infrastruktúrájának fejlesztését szolgálja, amelybe a Pohánka és Társa Kft. székhelye (Zalaegerszeg, Nyugat-Dunántúl, kevésbé fejlett régió) és DI profilja alapján illeszkedik.

A projekt indokoltságát három fő tényező alapozza meg:
1. **Alacsony digitális intenzitás** (IG32095-2025: 10 pont), amely gátolja a termelékenység és a szolgáltatási minőség javítását.
2. **Kapacitáskorlát és munkaerőhiány kockázat**: a 3 fős mikrovállalkozás manuális folyamattal már közel teljesítőképessége plafonján dolgozik.
3. **Területi és célcsoport megfelelés**: vidéki mikrovállalkozás, dokumentáltan alacsony DI szinttel, ami pontosan a DIMOP Plusz-1.2.6/B célcsoportja.

<!-- FIXME: Ha a végleges felhívásban pontosabb jogosultsági kritérium vagy más területi korlát jelenik meg, módosítsd a 3. pontot. -->
<!-- FIXME: Ellenőrizd, hogy a pályázati kiírás tartalmaz-e de minimis korlátot (Pohánka esetén: nincs korábbi igénybevétel). -->

---

## II. Célok és Várható Eredmények

### Vázlat — 8 konkrét cél

1. **Adminisztrációs időráfordítás 50%-os csökkentése** — manuális számlaadat-bevitelre fordított idő egy ügyfélre vetítve, a projekt zárása utáni első teljes üzleti évben.

2. **Automatikus számlafeldolgozás ≥ 80%** — a beérkező számlák legalább 80%-a Gmail-monitoring + OCR + AI pipeline segítségével kerül a könyvelő szoftverbe.

3. **Bankszámla- és pénztáregyeztetés automatizálása ≥ 70%** — szabályalapú és AI-támogatott reconciliation folyamatokon keresztül.

4. **BAS rendszer ≥ 99% rendelkezésre állás** — Phoenix Protocol v2 önjavító monitoring biztosításával.

5. **DI szint javítása alacsonyból közepesre** — a következő DI audit eredményeként.

6. **Min. 3 db új/korszerűsített digitális eszköz** — GPU munkaállomás, irodai PC/laptopok, NAS.

7. **3 fős csapat teljes BAS kompetenciafejlesztése** — AI-alapú munkavégzés és BAS-használat képzéssel.

8. **Kapacitásbővítés 30–50%-kal** — új ügyfelek felvétele plusz munkaerő felvétele nélkül, 2027-re.

### Output indikátorok (EPTK-kompatibilis)

| Indikátor | Vállalt érték |
|:---|:---:|
| Támogatott vállalkozások száma | 1 db |
| Új/korszerűsített digitális eszközök | min. 3 db |
| Bevezetett digitális megoldás | 1 db (BAS rendszer) |
| Felhőszolgáltatás | min. 1 db |
| Képzett munkavállalók | 3 fő |

### Eredmény indikátorok

| Indikátor | Cél | Mérési pont |
|:---|:---:|:---|
| Manuális adminisztrációs idő csökkentése | ≥ 50% | Projekt zárás + 1 év |
| Automatikus számlafeldolgozás | ≥ 80% | Projekt zárás + 1 év |
| Automatikus banki egyeztetés | ≥ 70% | Projekt zárás + 1 év |
| Rendszer rendelkezésre állás | ≥ 99% | Folyamatos |
| DI szint | Alacsonyból közepesre | Következő DI audit |

<!-- FIXME: Az EPTK felületén a konkrét indikátor-azonosítókat (kódokat) a felhívás mellékletéből kell bemásolni. -->
<!-- FIXME: A 30–50%-os kapacitásbővítés becslés — pontosítsd a belső kapacitás-elemzés alapján. -->

---

## III. Szakmai Tartalom

### A fejlesztés leírása — Brunella Agent System (BAS)

A projekt keretében bevezetésre kerül a **Brunella Agent System (BAS)** — egy moduláris, multi-agent AI ökoszisztéma, amelynek fő komponensei:

**1. Orkesztrációs réteg (Bifrost Gateway)**
A BAS központi orkesztrációs magja Node.js (TypeScript) alapú, Express.js és Socket.IO segítségével koordinálja a specializált autonóm ágenseket (*Orchestrator, Developer, Evaluator, RobotkezV2*). A **Bifrost Gateway** intelligensen kombinálja a helyi (Ollama, qwen2.5-coder:7b) és felhőben elérhető (Google Gemini, GPT-4o) AI-modelleket — az adatvédelmi szempontból érzékeny műveletek helyben futnak, a komplex feladatok felhőben.

**2. FastAPI Robotkéz — dokumentumbeáramlási pipeline**
A Python/FastAPI alapú adatfeldolgozó réteg automatizálja a beérkező számlák teljes feldolgozási folyamatát:
- Gmail-monitoring (csatolmányok automatikus letöltése)
- OCR + Vision-Language-Action (VLA) alapú adatkinyerés
- Strukturált adatok előkészítése a könyvelő szoftver számára (export/API)
- Playwright robotkéz: webes banki felületek, NAV Online Számla szinkron automatizálása

**3. LanceDB RAG — vektoradatbázis és döntéstámogatás**
A LanceDB vektoradatbázis a korábbi számlaadatok, könyvelési döntések és bizonylatok strukturált tárolására és lekérdezésére szolgál. A RAG (Retrieval-Augmented Generation) architektúra révén a rendszer a releváns múltbeli minták alapján javaslatot tesz a tételek könyvelési kezelésére — folyamatosan tanul a cég saját gyakorlatából (Data Flywheel).

**4. Phoenix Protocol v2 — önjavító monitoring**
Folyamatos 5 másodperces liveness monitoring és automatikus újraindítási / állapot-visszaállítási protokoll garantálja az üzembiztos 24/7 működést, megakadályozza az adatvesztést és a hosszabb leállásokat.

### Megvalósítás helyszíne és ütemezése

- **Helyszín:** 8900 Zalaegerszeg, Kossuth út 39. (bérelt iroda)
- **Tervezett futamidő:** <!-- FIXME: [12 hónap — ellenőrizd a felhívásban] -->
- **Fejlesztési feladatok (T1–T8):** részletes ütemezés: `Fejlesztes/FEJLESZTESI_TERV_BAS_DIMOP_SZECHENYI.md`

### DFK szakmai alátámasztás

A projekt digitalizációs tervét a GINOP / MV Program 2.0 keretű DFK (Digitális Fejlesztési Koncepció) szakmailag alátámasztja ([D127/23-505/2025]). A DFK szakértői javaslatai (digitális intenzitás növelése, folyamat-automatizálás, MI-alapú megoldások) beépítésre kerültek a fejlesztési tervbe.

<!-- FIXME: A DFK végleges dokumentuma elkészülte után integrálj konkrét szakértői megállapításokat (DI pontozás, hatékonysági mutatók). -->

---

## IV. Költségvetés és Támogatási Intenzitás

### Finanszírozási szerkezet

| | Összeg (Ft) | Arány |
|:---|:---:|:---:|
| **Projekt összköltség** | 9 000 000 | 100% |
| **Igényelt VNT támogatás (90%)** | 8 100 000 | 90% |
| **Önerő (10%)** | 900 000 | 10% |

> *A hardverbeszerzés aránya nem haladja meg a 30%-ot (DIMOP korlát).*

### Részletes költségvetési bontás

| Kategória | Összeg (Ft) | Arány | Konkrét tételek |
|:---|:---:|:---:|:---|
| **1. Hardver** | 2 700 000 | 30% | GPU munkaállomás (1 db), irodai PC/laptop (2-3 db), NAS + hálózati eszközök |
| **2. Szoftver és felhőszolgáltatások** | 3 600 000 | 40% | BAS licencek, OCR szoftver, LanceDB, Google Cloud (IaaS/PaaS) |
| **3. Tanácsadás és fejlesztési szolgáltatások** | 1 800 000 | 20% | BAS bevezetés, rendszertervezés, integráció, IT biztonsági hardening |
| **4. Képzés** | 900 000 | 10% | 3 fős csapat BAS-használat és AI-alapú munkavégzés képzése |
| **Összesen** | **9 000 000** | **100%** | |

<!-- FIXME: A konkrét árajánlatok alapján pontosítsd az egyes tételek összegét. Minden kategóriában min. 2-3 árajánlat szükséges. -->
<!-- FIXME: Ellenőrizd a maximális hardver-arány (30%) szabályt a végleges felhívásban. -->
<!-- FIXME: A saját forrás (900 000 Ft) fedezése: cég saját tőkéje 2025: 6 065 000 Ft → biztosított. -->

---

## V. Indikátorok (EPTK-kompatibilis összesítő)

```
OUTPUT INDIKÁTOROK:
Támogatott vállalkozások száma: 1 db (Pohánka és Társa Kft.)
Új/korszerűsített digitális eszközök száma: min. 3 db
Bevezetett digitális megoldások: 1 db (BAS rendszer) + min. 1 felhőszolgáltatás
Képzésben részesített munkavállalók: 3 fő

EREDMÉNY INDIKÁTOROK:
Manuális adminisztrációs idő csökkentése (ügyfélre vetítve): >= 50%
Automatikus számlafeldolgozás aránya: >= 80%
Automatikus banki egyeztetési arány: >= 70%
BAS rendszer éves rendelkezésre állás: >= 99%
Digitális intenzitás javulás: alacsonyból közepesre (következő DI audit)
```

<!-- FIXME: Az EPTK felületen az indikátor pontos nevét és egységét a felhívás mellékletéből kell kitölteni. -->
<!-- FIXME: Az eredményindikátorok célértékei (50%, 80%, 70%, 99%) vállalt értékek — ezeket a monitoring időszakban mérni kell! -->

---

## VI. Kapcsolódó Dokumentumok és Hivatkozások

| Dokumentum | Helye | Megjegyzés |
|:---|:---|:---|
| Projekt indokoltsága (teljes) | `Palyazatok/DIMOP_1_2_6/dimop_126b_projekt_indokoltsag.md` | EPTK-verzió blokk a fájl elején |
| Célok és eredmények | `Palyazatok/DIMOP_1_2_6/dimop_126b_celok_es_eredmenyek.md` | EPTK-verzió blokk |
| Szakmai tartalom | `Palyazatok/DIMOP_1_2_6/dimop_126b_szakmai_tartalom.md` | EPTK-verzió blokk |
| Költségvetés és indikátorok | `Palyazatok/DIMOP_1_2_6/dimop_126b_koltsegvetes_es_indikatorok.md` | EPTK-verzió blokk |
| Melléklet checklist | `Palyazatok/DIMOP_1_2_6_B_2026/03_MELLEKLETEK_CHECKLIST.md` | Ez az aktuális pályázat checklistje |
| BAS fejlesztési terv | `Fejlesztes/FEJLESZTESI_TERV_BAS_DIMOP_SZECHENYI.md` | T1–T8 feladatok, ütemezés |
| DFK koncepció vázlat | `Palyazatok/DIMOP_1_2_6/dfk_koncepcio_vazlat.md` | Belső vázlat, DFK folyamat elindítva |
| GINOP Támogatói Okirat | `docs/palyazat_ginop_1-3.pdf` | [D127/23-505/2025] |
| Mesterdokumentum | `mesterdoc.md` | Minden cégadat forrása |

---

*Első vázlat: 2026-06-29. Pályázat: DIMOP_1_2_6_B_2026. Benyújtás előtt emberi felülvizsgálat szükséges!*

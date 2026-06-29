# Pohánka és Társa Kft. - Pályázat és Támogatás Kutatás

## Projekt Célja
Ez a munkaterület a Pohánka és Társa Kft. számára elérhető hazai és európai uniós pályázatok, vissza nem térítendő támogatások, valamint támogatott hitelek felkutatására, elemzésére és az ezekkel kapcsolatos folyamatok (pályázatírás, előkészítés, menedzsment) kidolgozására szolgál.

## Kiemelt Fókuszterületek
-   **Pályázatfigyelés:** Aktuális és várható pályázati kiírások monitorozása a cég profiljának megfelelően.
-   **Támogatott Hitelek:** Kedvezményes kamatozású hitelkonstrukciók (pl. Széchenyi Kártya Program) vizsgálata.
-   **Adatbázis Építés:** A cég teljeskörű adatbázisának fenntartása a `mesterdoc.md` alapján, ami a gyors és pontos pályázati előminősítést teszi lehetővé.
-   **Folyamatszervezés:** A pályázati anyagok összegyűjtésének, megírásának és benyújtásának rendszerezése.

## Utasítások az AI asszisztens (Brunella) számára ebben a projektben
1.  **Magyar nyelv:** A kommunikáció és a dokumentáció elsődleges nyelve a magyar.
2.  **Adatvezérelt megközelítés:** Bármilyen pályázati javaslat vagy előminősítés során a `mesterdoc.md`-ben gyűjtött adatokra kell támaszkodni. Ha kulcsfontosságú adat hiányzik az értékeléshez, azt jelezni kell a felhasználónak.
3.  **Precizitás:** Pályázati feltételek és hitelkonstrukciók elemzésekor a legapróbb részletekre is oda kell figyelni (jogosultsági feltételek, kizáró okok, TEÁOR kódok, pénzügyi mutatók, KKV besorolás).
4.  **Proaktivitás:** Ha a meglévő adatok alapján egy új támogatási vagy hitel lehetőség releváns lehet, hívd fel rá a figyelmet proaktívan.

## Haladás / Mérföldkövek

### 2026. június 29.
-   **AI Konfigurációs Infrastruktúra felépítése:** A `.github/` könyvtárban három fájl létrehozása:
    -   [`.github/copilot-instructions.md`](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/.github/copilot-instructions.md) — átfogó, 10,4 KB-os Copilot útmutató magyarul: projekt áttekintés, TEÁOR, EPTK-szövegek, mesterdoc-centric munkafolyamat, precizitási követelmények, önellenőrző kérdések.
    -   [`.github/mcp-servers.json`](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/.github/mcp-servers.json) — opcionális MCP szerveres konfiguráció (filesystem, git, GitHub).
    -   [`.github/WORKFLOWS.md`](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/.github/WORKFLOWS.md) — 4 db opcionális GitHub Actions workflow: melléklet-validáció, EPTK-integritás, mesterdok emlékeztető, commit linter.

-   **TAMOGAT sablonkönyvtár létrehozása:** A projekt gyökerében `TAMOGAT/` könyvtár, 3 sablonfájllal:
    -   [`TAMOGAT/CEGADAT_SABLON.md`](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/TAMOGAT/CEGADAT_SABLON.md) — Cégadatok (teljes névre, TEÁOR kódokra, pénzügyi kivonatra, DI igazolásokra, kulcsdokumentumokra kiterjedő), moduláris FIXME mezőkkel.
    -   [`TAMOGAT/PALYAZATI_DOKUMENTUM_SABLON.md`](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/TAMOGAT/PALYAZATI_DOKUMENTUM_SABLON.md) — Általános VNT pályázati vázlat: I–V. fejezetek (indokoltság, célok, szakmai tartalom, költségvetés, indikátorok), BAS alapszövegekkel és EPTK-szöveg sablon copy-paste blokkkal.
    -   [`TAMOGAT/MELLEKLETEK_SABLON.md`](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/TAMOGAT/MELLEKLETEK_SABLON.md) — 31 soros táblázatos melléklet checklist: cégiratok, 3 éves pénzügyi dok., KOMA, HIPA, DI igazolások, DFK, árajánlatok; konkrét `docs/` fájlnevekkel és benyújtás előtti összesítővel.

-   **HITEL sablonkönyvtár létrehozása:** A projekt gyökerében `HITEL/` könyvtár, 3 sablonfájllal:
    -   [`HITEL/HITELPROJEKT_SABLON.md`](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/HITEL/HITELPROJEKT_SABLON.md) — Beruházási hitel sablon: cégbemutatás, részletes beruházási lista (GPU workstation, PC, NAS, cégautó), indokoltság és jogosultsági feltételek, Széchenyi 6M Ft referencia adatokkal.
    -   [`HITEL/HITEL_KOLTSEGVETES_ES_CASHFLOW_SABLON.md`](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/HITEL/HITEL_KOLTSEGVETES_ES_CASHFLOW_SABLON.md) — Annuitásos törlesztőrészlet számítás képlettel (referencia: 107 812 Ft/hó), 5 éves EBITDA / szabad cash-flow / DSCR (1,65x–6,90x) előrejelzés, paraméterezhető FIXME mezőkkel (más hitelhez).
    -   [`HITEL/HITEL_DOKUMENTUMLISTA_SABLON.md`](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/HITEL/HITEL_DOKUMENTUMLISTA_SABLON.md) — 32 soros KAVOSZ / banki dokumentumlista checklist: cégiratok, 3 év pénzügyi dok., KOMA, HIPA, beruházási lista, árajánlatok, fedezeti iratok, igénylőlapok.

-   **DIMOP_1_2_6_B_2026 pályázati almappa létrehozása:** `Palyazatok/DIMOP_1_2_6_B_2026/` könyvtár a TAMOGAT sablonokból generált, kitöltött első vázlattal:
    -   [`felhivas_raw.txt`](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Palyazatok/DIMOP_1_2_6_B_2026/felhivas_raw.txt) — Felhívás összefoglaló (palyazat.gov.hu URL 404 → lokális DIMOP adatokból összeállítva): konstrukció neve, 90% intenzitás, keretösszeg, fő indikátorok, DFK és Széchenyi kapcsolódás.
    -   [`01_CEGADAT.md`](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Palyazatok/DIMOP_1_2_6_B_2026/01_CEGADAT.md) — Teljesen kitöltött céges adatlap: KIVA adózás, OTP bankszámla, TEÁOR kódok, 2023–2025 pénzügyi táblázat, Megbízható adózó státusz, DI igazolások azonosítói, kettős finanszírozási terv (DIMOP 90% + Széchenyi 6M Ft), 14 kulcsdokumentum.
    -   [`02_PALYAZATI_DOKUMENTUM.md`](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Palyazatok/DIMOP_1_2_6_B_2026/02_PALYAZATI_DOKUMENTUM.md) — Első vázlat: EPTK-verzió (bemásolható), projekt indokoltsága (8 bekezdés + 3 fő érv), célok (8 pont + indikátor táblázatok), BAS szakmai tartalom (Bifrost Gateway, FastAPI Robotkéz, LanceDB RAG, Phoenix Protocol v2), 9M Ft-os 4 kategóriás költségvetési bontás, FIXME jelölések emberi finomhangoláshoz.
    -   [`03_MELLEKLETEK_CHECKLIST.md`](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Palyazatok/DIMOP_1_2_6_B_2026/03_MELLEKLETEK_CHECKLIST.md) — 33 soros melléklet checklist konkrét `docs/` fájlnevekkel, „FELTÖLTVE EPTK-BE?" jelölő oszlop, 10 lépéses benyújtás előtti összesítő ellenőrzési lista.

-   **KELL.md frissítése:** Két új szekció felvétele:
    -   „Sablonok használata" szekció: pályázatnál → `TAMOGAT/` sablonok, hitelnél → `HITEL/` sablonok.
    -   Új teendő: `[ ] DIMOP_1_2_6_B_2026 — sablonok áttekintése és finomhangolása beadás előtt`.

-   **TARTALOM.md frissítése:** Három új szekció felvétele:
    -   `## DIMOP_1_2_6_B_2026 — Aktuális pályázat` gyorslinkekkel a 4 új almappa fájlra.
    -   `## TAMOGAT sablonok` a 3 sablon leírásával.
    -   `## HITEL sablonok` a 3 sablon leírásával.

-   **Git és GitHub szinkronizáció:** 4 commit sikeresen pushólva a `main` ágra:
    -   `a372cb1` — `.github/copilot-instructions.md` létrehozva
    -   `41522b9` — `.github/mcp-servers.json` és `WORKFLOWS.md` létrehozva
    -   `997df22` — TAMOGAT és HITEL sablonkönyvtárak + KELL.md, TARTALOM.md frissítve
    -   `a9e5803` — `Palyazatok/DIMOP_1_2_6_B_2026/` almappa létrehozva (4 fájl), KELL.md és TARTALOM.md frissítve

### 2026. június 26.
-   **Mellékletfájlok átnevezése és egységesítése:** A `docs` könyvtárban lévő beszámolók, főkönyvek, cégiratok és adóigazolások ékezetes és szóközös fájlneveinek átnevezése a dokumentációval teljesen megegyező számozott, tiszta formátumra a hibátlan script-ellenőrzés és Git szinkron érdekében.
-   **DIMOP 1.2.6/B Melléklet checklist kitöltése:** A [dimop_126b_mellekletek_checklist.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Palyazatok/DIMOP_1_2_6/dimop_126b_mellekletek_checklist.md) fájlban az összes elérhető cégirat és pénzügyi beszámoló státuszának készre jelentése a konkrét fájlneveik beillesztésével.
-   **DFK / GINOP (MV Program 2.0) szolgáltatás integrációja:** Az IG32095-2025 és IG32096-2025 DI igazolások, a [palyazat_ginop_1-3.pdf](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/docs/palyazat_ginop_1-3.pdf) Támogató Okirat és a DFK koncepció-vázlat ([dfk_koncepcio_vazlat.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Palyazatok/DIMOP_1_2_6/dfk_koncepcio_vazlat.md)) kidolgozása, és DFK-referenciák átvezetése a DIMOP projekt indokoltság, célok és szakmai tartalom állományaiba.
-   **Széchenyi Mikrohitel MAX+ hitelcsomag egységesítése:** A 6 000 000 Ft tervezett hitelösszeghez tartozó beruházási táblázat, a pontos havi törlesztőrészlet (107 812 Ft/hó) kiszámítása és egy 5 éves cash-flow fenntarthatósági előrejelzés elkészítése a [szechenyi_mikrohitel_koltsegvetes_es_cashflow.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Hitelek/Szechenyi_Mikrohitel_MAX/szechenyi_mikrohitel_koltsegvetes_es_cashflow.md) állományban.
-   **Átfogó Fejlesztési és Kivitelezési Terv elkészítése:** A [FEJLESZTESI_TERV_BAS_DIMOP_SZECHENYI.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Fejlesztes/FEJLESZTESI_TERV_BAS_DIMOP_SZECHENYI.md) megírása, a BAS technikai architektúrájának (orkesztrációs réteg, FastAPI robotkéz, LanceDB RAG és Bifrost Gateway) és a fejlesztési feladatoknak (T1–T8) a részletezése.
-   **Emberi teendők és dokumentumtérkép bővítése:** A [KELL.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/KELL.md) kiegészítése a DFK, a Széchenyi és a BAS fejlesztési jóváhagyási/döntési feladataival. A [TARTALOM.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/TARTALOM.md) kibővítése a GINOP, a Széchenyi és a Master fejlesztési tervek gyorslinkjeivel.
-   **Mesterdokumentumok frissítése:** A hitel- és fejlesztési stratégia, valamint a DFK / DI adatok beépítése a [mesterdoc.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/mesterdoc.md) és [mesterdoc-5.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/mesterdoc-5.md) fájlokba.
-   **Git és Github szinkronizáció:** Minden lépés utáni automatikus commit és sikeres push a main ágra a Github tárolóban.

### 2026. június 17.
-   **Hibrid Operatív Akcióterv elkészítése:** Az [akcio_terv.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/akcio_terv.md) fájl átírása napi (DIMOP) és heti (Széchenyi) szintű to-do listává.
-   **Specifikáció és Terv létrehozása:** A tervezési fázis [design spec](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/docs/superpowers/specs/2026-06-17-palyazat-hitel-akcioterv-design.md) és a végrehajtási terv [implementation plan](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/docs/superpowers/plans/2026-06-17-palyazati-es-hitel-dok-elokeszites.md) elkészítése.
-   **DIMOP 1.2.6/B Pályázati dokumentumok:** A [Palyazatok/DIMOP_1_2_6/](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Palyazatok/DIMOP_1_2_6/) könyvtárban a projekt indokoltság, célok, szakmai tartalom, költségvetési részletek és melléklet checklist elkészítése és feltöltése.
-   **Széchenyi Mikrohitel MAX+ Hiteldokumentáció:** A [Hitelek/Szechenyi_Mikrohitel_MAX/](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Hitelek/Szechenyi_Mikrohitel_MAX/) könyvtárban a hitelcél (6M Ft IT+autó), cash-flow kalkuláció és dokumentumlista elkészítése és feltöltése.
-   **Dokumentációs Index létrehozása:** A [docs/INDEX.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/docs/INDEX.md) elkészítése a gyors navigáció érdekében.
-   **Github szinkronizáció:** Első teljes csomag sikeres commitolása és feltöltése a Github-ra.


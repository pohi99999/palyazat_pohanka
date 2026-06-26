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


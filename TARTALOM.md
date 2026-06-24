TARTALOM — projekt áttekintés és könyvtártérkép

Rövid projektismertető
A projekt célja: DIMOP Plusz‑1.2.6/B‑26 pályázat keretében a Pohánka és Társa Kft. könyvelési és adminisztratív folyamatainak digitalizálása és részleges automatizálása a Brunella Agent System (BAS) bevezetésével (OCR, automatizált számlafeldolgozás, AI‑támogatott banki egyeztetés). Támogatási igény: 9 000 000 Ft (90% támogatás). A projekt kapcsolódik a Széchenyi Mikrohitel MAX+ tervekhez a finanszírozási oldal előkészítéséhez.

Fő könyvtárak és fontos fájlok (gyökérből relatív útvonal)
- Palyazatok/DIMOP_1_2_6/
  - dimop_126b_projekt_indokoltsag.md — teljes indokoltság; a fájl elején megtalálható a "## Rövid EPTK‑verzió" (EPTK‑be másolandó rövid szöveg).
  - dimop_126b_celok_es_eredmenyek.md — célok, indikátorok; a tetején rövid EPTK‑szöveg.
  - dimop_126b_szakmai_tartalom.md — részletes szakmai és technikai leírás; elején rövid EPTK‑verzió.
  - dimop_126b_koltsegvetes_es_indikatorok.md — költségvetés és indikátorok; elején rövid EPTK‑verzió.
  - dimop_126b_mellekletek_checklist.md — minta mellékletlista és ellenőrző pontok.

- Hitelek/Szechenyi_Mikrohitel_MAX/
  - szechenyi_mikrohitel_projektcel_es_indokoltsag.md — hitelcél rövid leírása.
  - szechenyi_mikrohitel_koltsegvetes_es_cashflow.md — cash‑flow és költségterv.
  - szechenyi_mikrohitel_dokumentumlista.md — banki dokumentumlista (ajánlott dokumentumok a hitelhez).

- docs/
  - 2025-06-19_IG32095-2025_DII.pdf — DI igazolás és kapcsolódó vizsgálatok.
  - KOMA - Pohánka Kft.pdf — NAV KOMA igazolás (köztartozásmentes adózói státusz igazolása a DIMOP és Széchenyi hitelhez, lekérdezve: 2026. 06. 23.)
  - (további pdf/docx anyagok: ha vannak, itt találhatók)

- mesterdoc.md, mesterdoc-5.md
  - A projekt állandó adatai: cégadatok, TEÁOR, kontaktok, üzleti célok, rövid pénzügyi adatok. Első hely, ahol ellenőrizd a benyújtáshoz szükséges adatokat.

- palyazat-todo-list-4.md
  - Akcióterv és teendők listája; napi és heti feladatok; használható a benyújtás ütemezéséhez.

Első lépések új belépőnek (2–3 perc)
1. Nyisd meg Palyazatok/DIMOP_1_2_6/dimop_126b_projekt_indokoltsag.md és másold át az ott található "## Rövid EPTK‑verzió" blokkot az EPTK mezőbe.
2. Ellenőrizd a KELL.md fájlban szereplő igazolásokat (NAV, önkormányzat) és szerezz be minden hiányzó PDF‑bizonyítékot.
3. A költségvetést és árajánlatokat a Hitelek/Szechenyi_Mikrohitel_MAX/ és a dimop_126b_koltsegvetes_es_indikatorok.md alapján állítsd össze.

Fontos fájlok gyors elérés:
- KELL.md — emberi teendők (most létrehozva)
- TARTALOM.md — ez a fájl (áttekintés)
- Palyazatok/DIMOP_1_2_6/* — DIMOP szövegek (rövid EPTK verziók a fájlok tetején)
- Hitelek/Szechenyi_Mikrohitel_MAX/* — hiteldokumentáció és cashflow

Ha kérdésed van a struktúrával vagy a fájlok tartalmával kapcsolatban, jelezd, és frissítem a TARTALOM.md‑et további részletekkel vagy fájllinkekkel.

Script ellenőrzés: scripts\check_mellekletek.ps1 — egyszerű PowerShell ellenőrző script a mellékletek meglétének vizsgálatához. Futtatás: powershell -ExecutionPolicy Bypass -File .\scripts\check_mellekletek.ps1
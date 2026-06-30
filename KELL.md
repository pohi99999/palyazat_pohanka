KELL — emberi teendők (párosítás: MIT / HOL / MIVEL / MIKOR)

---

## Brunella AI Rendszer – Pályázat- és Hitelkereső (KÉSZ: 2026-06-30)

> **Állapot:** Az AI-alapú pályázat- és hitelkereső rendszer (FundingSearchAgent + workflow) elkészült és commitolva van a repóba.

### Kész fájlok (nem igényelnek emberi beavatkozást)
- `config/pohanka_credit_profile.json` — Gépileg olvasható céges profil (cégadatok, pénzügyek, preferenciák)
- `src/domain/pohankaCreditProfile.py` — Python domain modul (helper függvények)
- `src/agents/fundingSearchAgent.py` — FundingSearchAgent (Brunella LLM-motor prompt)
- `src/workflows/fundingAndGrantDiscovery.py` — Teljes kereső workflow
- `output/pohanka_funding_candidates.json` — Első workflow futás eredménye (5 pályázat + 5 hitel)
- `output/pohanka_3month_action_plan.json` — 3 hónapos végrehajtható akcióterv JSON

### Emberi teendők az AI-rendszerhez

`[ ]` **Profil frissítése ha céges adat változik**
- MIT: Ha a cégadatok (árbevétel, létszám, DI pontszám, DFK érvényesség) megváltoznak, frissíteni kell a `config/pohanka_credit_profile.json` fájlt.
- HOL: `config/pohanka_credit_profile.json`
- MIVEL: Friss NAV/számviteli adatok, DI igazolás.
- MIKOR: Évente, vagy ha az adatok lényegesen változnak.

`[ ]` **Workflow újrafuttatása friss pályázati adatokkal**
- MIT: A `python -m src.workflows.fundingAndGrantDiscovery` parancs futtatása frissíti az `output/pohanka_funding_candidates.json` fájlt. Jelenleg statikus jelölt adatokat tartalmaz – az LLM+search API integrációval automatizálható.
- HOL: Repo gyökérből PowerShell-ben.
- MIKOR: Havonta egyszer, vagy ha új pályázati felhívást észlelsz.

`[ ]` **3 hónapos akcióterv áttekintése és lépések teljesítése**
- MIT: Nyisd meg az `output/pohanka_3month_action_plan.json` fájlt, és teljesítsd az azonnali lépéseket (priority_rank=1):
  - **2026-07-07:** OTP Bank KAVOSZ konzultáció + Széchenyi Kártya ellenőrzés
  - **2026-07-08:** DFK véglegesítés + EPTK regisztráció
  - **2026-07-10:** NAV KOMA és HIPA frissítés + MFB Pont tájékozódás
  - **2026-07-15:** Árajánlatok (DIMOP+Széchenyi), GINOP státusz, Garantiqa folyamat
- HOL: `output/pohanka_3month_action_plan.json`
- MIKOR: Azonnal (július első hete)

---

## Új pályázati felhívás teendő

`[ ]` **DIMOP_1_2_6_B_2026 — Pályázati almappa sablonok áttekintése és finomhangolása beadás előtt**
- MIT: Nyisd meg a `Palyazatok/DIMOP_1_2_6_B_2026/` mappát, tekintsd át a 3 sablonból készített dokumentumot, és töltsd ki az összes `<!-- FIXME -->` megjegyzést a végleges felhívás szövege alapján.
- HOL: `Palyazatok/DIMOP_1_2_6_B_2026/01_CEGADAT.md`, `02_PALYAZATI_DOKUMENTUM.md`, `03_MELLEKLETEK_CHECKLIST.md`
- MIVEL: mesterdoc.md, felhivas_raw.txt (lokális adatok), végleges pályázati kiírás (EPTK portálról).
- MIKOR: A benyújtás előtt legalább 3–5 nappal; az EPTK-verzió szövegeit ellenőrizd utolsó lépésként.

---

1) [x] NAV: köztartozás‑mentesség ("nullás") igazolás lekérése (Kész, csatolt PDF: KOMA-Pohanka-Kft-8.pdf)
- MIT: Kérd le a NAV által kiadott köztartozás‑mentesség igazolást a pályázathoz.
- HOL: NAV ügyfélkapu / NAV honlap (https://www.nav.gov.hu) → Ügyfélkapu belépés, adóigazolások menü.
- MIVEL: cég adószáma, cégkivonat, mesterdoc.md (cégadatok).
- MIKOR: lehetőleg a pályázat benyújtása előtt 1–2 héttel (várható ügyintézési idő: néhány nap).

2) [x] Helyi iparűzési adó igazolás az önkormányzattól (Kész, csatolt PDF: SKM_4050260625124300-9.pdf)
- MIT: Kérd le az önkormányzat által kiadott helyi iparűzési adó befizetésre/mentességre vonatkozó igazolást.
- HOL: Zalaegerszeg (https://zalaegerszeg.hu) / illetékes önkormányzat pénzügyi ügyfélszolgálata vagy e‑ügyintézés.
- MIVEL: cégkivonat, üzleti cím, befizetési bizonylatok (ha van).
- MIKOR: javasolt min. 2 hét a kérelmezéstől a jóváhagyásig; indítsd el mielőbb.

2a) [x] Cégkivonat, aláírási címpéldány és korábbi beszámolók / főkönyvek letöltése és összegyűjtése (Kész, csatolt PDF-ek: 2023.-beszamolo-10.pdf, 2024.-beszamolo-2.pdf, 2025-evi-merleg-4.pdf, 2023.-fokonyv.pdf, 2024.-fokonyv-3.pdf, 2025.-fokonyv-5.pdf, Cegkivonat-7.pdf, Alairasi-cimp.-Atlath.-nyil.-KKV-min-6.pdf)
- MIT: Szerezd be a cégkivonatot, az aláírási címpéldányt, valamint az utolsó 3 lezárt év beszámolóit és főkönyvi kivonatait a pályázati és hitel előminősítéshez.
- HOL: e-Beszámoló, e-Cégjegyzék, cégkapu, könyvelőiroda.
- MIVEL: cégadatok (mesterdoc.md).
- MIKOR: azonnal, a pályázat és hitel előkészítő szakaszában.

3) DFK (Digitális Fejlesztési Koncepció) folyamat menedzselése (Részletezve a fájl végén lévő DFK szekcióban)
- MIT: Egyeztess és menedzseld a DFK folyamatot a kijelölt szolgáltatóval a hivatalos igazolás megszerzéséig.
- HOL: DFK szolgáltató (Modern Vállalkozások Programja 2.0 / DKF tanácsadó).
- MIVEL: [palyazat_ginop_1-3.pdf](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/docs/palyazat_ginop_1-3.pdf) Támogatói Okirat, [dfk_koncepcio_vazlat.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Palyazatok/DIMOP_1_2_6/dfk_koncepcio_vazlat.md).
- MIKOR: a DIMOP pályázat benyújtása előtt (a végső felhasználási határidő 2026. november 30.).

4) Hardver és szoftver árajánlatok bekérése (min. 2–3 ajánlat)
- MIT: Kérj legalább 2–3 részletes árajánlatot a GPU munkaállomásra, NAS‑ra, OCR szoftverre, LanceDB/DB licencekre és integrációra.
- HOL: helyi IT beszállítók, állami/nemzetközi forgalmazók, felhőszolgáltatók (Google Cloud).
- MIVEL: műszaki elvárások (a mesterdoc és dimop szakmai tartalom alapján), költségvetés sablon (Palyazatok/DIMOP_1_2_6/dimop_126b_koltsegvetes_es_indikatorok.md).
- MIKOR: ajánlatok bekérése: 1–2 hét; beépítés a költségvetésbe mielőbb.

5) EPTK felületre belépés és pályázat kiválasztása; szövegek bemásolása és mellékletek feltöltése (finalizálás)
- MIT: Jelentkezz be az EPTK (Elektronikus Pályázati Tér) felületére, válaszd ki a DIMOP Plusz‑1.2.6/B‑26 felhívást, másold be az EPTK mezőkbe a "Rövid EPTK‑verzió" blokkok szövegét, töltsd fel a kötelező mellékleteket (KOMA, iparűzési igazolás, DFK, árajánlatok, dokumentumlista).
- HOL: EPTK (Elektronikus Pályázati Tér) — hivatalos pályázati portál: https://www.palyazat.gov.hu (Ügyfélkapu belépés szükséges; a benyújtási URL az adott felhívásnál található).
- MIVEL: a repository Palyazatok/DIMOP_1_2_6/* fájlai (különösen a dimop_126b_*.md fájlokban lévő "## Rövid EPTK‑verzió" blokk), KELL.md-ben összegyűjtött igazolások.
- MIKOR: benyújtás előtti napon/napokban; javasolt ellenőrző kör (külső szakértő vagy könyvelő) a végleges benyújtás előtt.

6) e‑aláírás és hitelesítés
- MIT: Győződj meg arról, hogy az összes feltöltött dokumentum aláírható és hitelesíthető e‑aláírással/ügyfélkapuval (ha szükséges, állítsd be az e‑aláírás eszközét).
- HOL: ügyfélkapu / e‑aláírás szolgáltató.
- MIVEL: cégvezető aláírás, megbízólevél (ha más nyújtja be).
- MIKOR: a pályázat végső benyújtásakor.

7) Banki / KAVOSZ egyeztetés a Széchenyi Mikrohitelhez (Részletezve a fájl végén lévő Széchenyi szekcióban)
- MIT: Vedd fel a kapcsolatot a finanszírozó partnerrel és menedzseld a hiteligénylést.
- HOL: KAVOSZ Regisztráló Iroda (pl. Zala Vármegyei Kereskedelmi és Iparkamara zalaegerszegi irodája) / kiválasztott hitelintézet (pl. OTP Bank).
- MIVEL: Széchenyi Mikrohitel MAX+ dokumentációcsomag (Hitelek/Szechenyi_Mikrohitel_MAX/*).
- MIKOR: Párhuzamosan a DIMOP pályázat előkészítésével.

8) Könyvelői és jogi ellenőrzés
- MIT: Kérd a könyvelőd és jogi tanácsadód végleges ellenőrzését a benyújtandó dokumentumok és költségvetés felett.
- HOL: könyvelőiroda / jogi tanácsadó.
- MIVEL: összes feltöltendő dokumentum, mesterdoc.md, költségvetés, DFK.
- MIKOR: 1–3 nap a benyújtás előtt.

Megjegyzés: minden igazolásnál őrizd meg a letöltött PDF/HTML bizonylatot és töltsd fel az EPTK mellékletei közé; ha kétség merül fel, konzultálj a pályázati tanácsadóval vagy a könyvelővel.

## DFK / GINOP támogatott szolgáltatás teendők

*   `[ ]` **DFK szolgáltató megkeresése és időpont egyeztetése**
    *   **MIT:** Vedd fel a kapcsolatot a Modern Vállalkozások Programja 2.0 / DKF kijelölt tanácsadójával a DFK folyamat elindításához.
    *   **HOL:** Online / E-mail / Telefon. Kapcsolat a [palyazat-todo-list-4.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/palyazat-todo-list-4.md) és a Támogatói Okirat alapján.
    *   **KIVEL:** KAVOSZ / MKIK vagy kijelölt DKF regisztrált tanácsadó.
    *   **HATÁRIDŐ:** Azonnal (javasolt a DIMOP pályázati anyag összeállításának korai szakaszában).
*   `[ ]` **Kérelmi és Hozzájárulási Nyilatkozat aláírása / visszaküldése**
    *   **MIT:** A Támogatói Okiratban ([palyazat_ginop_1-3.pdf](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/docs/palyazat_ginop_1-3.pdf)) előírt Kérelmi és Hozzájárulási Nyilatkozatot cégszerűen aláírva küldd vissza a szolgáltató felé a jogosultság aktiválásához.
    *   **HOL:** Cégkapun vagy postai úton a szolgáltató címére.
    *   **KIVEL:** Pohánka Józsefné / Pohánka József (ügyvezetők).
    *   **HATÁRIDŐ:** A megkeresést követő 5 munkanapon belül.
*   `[ ]` **DFK workshop / interjú lebonyolítása**
    *   **MIT:** Vegyél részt a vállalati digitális státuszfelméréshez szükséges interjún/workshopon, és ismertesd a cég hibrid működési modelljét, valamint a BAS (Brunella Agent System) bevezetési terveit.
    *   **HOL:** Személyesen a zalaegerszegi bérelt irodában (Kossuth út 39.) vagy online MS Teams / Zoom megbeszélésen.
    *   **KIVEL:** A DFK tanácsadóval és a cég belső IT/adminisztrációs csapatával.
    *   **HATÁRIDŐ:** A szolgáltatóval egyeztetett időpontban (ajánlott 1–2 héten belül).
*   `[ ]` **DFK végleges dokumentum átvétele és ellenőrzése**
    *   **MIT:** Vedd át a hivatalosan elkészült, aláírt Digitális Fejlesztési Koncepció (DFK) dokumentumot, ellenőrizd, hogy a javasolt irányok lefedik-e a DIMOP 1.2.6/B projektet (hardver, szoftver, BAS MI integráció).
    *   **HOL:** E-mailben vagy a szolgáltató portáljáról letöltve. Mentsd el a `docs/` könyvtárba `DFK.pdf` néven (hogy a PowerShell ellenőrző script is megtalálja).
    *   **KIVEL:** DFK tanácsadóval.
    *   **HATÁRIDŐ:** A workshopot követő 10 munkanapon belül, legkésőbb 2026. november 30.
*   `[ ]` **DFK fő megállapításainak beépítése a DIMOP pályázatba**
    *   **MIT:** A végleges DFK anyagból származó pontos megállapításokat és szakértői javaslatokat (pl. hatékonysági mutatók, DI növekedési számok) vezesd át a DIMOP indokoltsági és szakmai tartalmi dokumentumaiba az EPTK finalizálása előtt.
    *   **HOL:** Helyi munkaterületen a `Palyazatok/DIMOP_1_2_6/dimop_126b_*` fájlokban.
    *   **KIVEL:** Brunella asszisztens segítségével.
    *   **HATÁRIDŐ:** A pályázat benyújtása előtt legalább 3 nappal.

## Széchenyi Mikrohitel MAX+ teendők

*   `[ ]` **Bank / Széchenyi Programiroda / KAVOSZ iroda azonosítása és időpontfoglalás**
    *   **MIT:** Válaszd ki a legközelebbi regisztráló irodát (pl. Zala Vármegyei Kereskedelmi és Iparkamara irodája, Zalaegerszeg, Petőfi Sándor u. 24.) és foglalj időpontot a hiteligénylés elindításához.
    *   **HOL:** Online (kavosz.hu) vagy telefonon a helyi kamaránál.
    *   **KIVEL:** KAVOSZ regisztráló ügyintézővel.
    *   **HATÁRIDŐ:** A DIMOP pályázat benyújtásának hetében, vagy közvetlenül utána.
*   `[ ]` **Széchenyi projektleírás és beruházási lista kinyomtatása / PDF küldése**
    *   **MIT:** Készítsd elő a [szechenyi_mikrohitel_projektcel_es_indokoltsag.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Hitelek/Szechenyi_Mikrohitel_MAX/szechenyi_mikrohitel_projektcel_es_indokoltsag.md) projektleírást és a beruházási táblázatot kinyomtatva, valamint PDF-ben, hogy a bank/KAVOSZ lássa a hitel pontos célját.
    *   **HOL:** Helyi iroda, nyomtatás vagy e-mailes küldés.
    *   **KIVEL:** Hitelügyintézővel.
    *   **HATÁRIDŐ:** Az irodai találkozó előtt 1 nappal.
*   `[ ]` **Dokumentumcsomag összekészítése és ellenőrzése**
    *   **MIT:** Gyűjtsd össze az alábbi, már rendelkezésre álló dokumentumokat a `docs` mappából, és ellenőrizd őket az ügyintéző által megadott checklist alapján:
        *   Utolsó 3 év lezárt beszámolói (`2023.-beszamolo-10.pdf`, `2024.-beszamolo-2.pdf`, `2025-evi-merleg-4.pdf`)
        *   Utolsó 3 év főkönyvi kivonatai (`2023.-fokonyv.pdf`, `2024.-fokonyv-3.pdf`, `2025.-fokonyv-5.pdf`)
        *   Friss cégkivonat (`Cegkivonat-7.pdf`)
        *   Aláírási címpéldány és KKV minősítés (`Alairasi-cimp.-Atlath.-nyil.-KKV-min-6.pdf`)
        *   NAV KOMA nullás igazolás (`KOMA-Pohanka-Kft-8.pdf`)
        *   HIPA helyi adóigazolás (`SKM_4050260625124300-9.pdf`)
        *   Rövid cash-flow terv (`szechenyi_mikrohitel_koltsegvetes_es_cashflow.md` alapján kinyomtatva)
        *   *Vigyél magaddal: személyi igazolványt, lakcímkártyát, adókártyát és céges bélyegzőt!*
    *   **HOL:** Zalaegerszeg (helyi iroda / KAVOSZ iroda).
    *   **KIVEL:** Pohánka Józsefné / Pohánka József (ügyvezetők).
    *   **HATÁRIDŐ:** A KAVOSZ időpont napján.
*   `[ ]` **Hitelkérelem hivatalos beadása és szerződéskötés**
    *   **MIT:** Töltsd ki az igénylőlapot a KAVOSZ irodában, nyújtsd be a teljes dokumentációt, és a pozitív bírálat után kösd meg a hitelszerződést a kiválasztott finanszírozó bankkal (pl. OTP).
    *   **HOL:** KAVOSZ Iroda $\rightarrow$ Finanszírozó bank fiókja.
    *   **KIVEL:** Hitelügyintézővel és a banki kapcsolattartóval.
    *   **HATÁRIDŐ:** A hitelkérelem benyújtását követő 30–60 napon belül.

## BAS / fejlesztési teendők

*   `[ ]` **BAS modulprioritások és technikai specifikáció jóváhagyása**
    *   **MIT:** Tekintsd át a [FEJLESZTESI_TERV_BAS_DIMOP_SZECHENYI.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Fejlesztes/FEJLESZTESI_TERV_BAS_DIMOP_SZECHENYI.md) fájlban meghatározott modulokat, és hagyd jóvá a fejlesztési prioritásokat (pl. Bifrost Gateway vs Robotkéz V2).
    *   **HATÁRIDŐ:** A fejlesztés megkezdése előtt (javasolt: 2026. július 15.).
*   `[ ]` **Külső fejlesztők briefelése és megbízása**
    *   **MIT:** Készítsd elő a feladatleírásokat a [FEJLESZTESI_TERV_BAS_DIMOP_SZECHENYI.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/Fejlesztes/FEJLESZTESI_TERV_BAS_DIMOP_SZECHENYI.md) alapján, és egyeztesd a külső kivitelező fejlesztőkkel a határidőket és a díjazást.
    *   **HATÁRIDŐ:** 2026. július végéig.
*   `[ ]` **Lokális GPU munkaállomás és NAS beszerzés jóváhagyása**
    *   **MIT:** Véglegesítsd a hardver specifikációkat a Széchenyi Mikrohitel MAX+ igénylés elindításakor, hagyd jóvá az árajánlatokat a vásárláshoz.
    *   **HATÁRIDŐ:** A hitelkérelem benyújtásakor.
*   `[ ]` **BAS MVP tesztelés és átvétel jóváhagyása**
    *   **MIT:** Teszteld a BAS magrendszer (Gmail monitoring + OCR + adatkivonat) működését a könyvelőiroda mindennapi feladatai során, és adj írásos jóváhagyást a következő fázis (banki párosítás) indításához.
    *   **HATÁRIDŐ:** Az MVP fázis lezárásakor (javasolt: 2026. október 15.).

## Sablonok használata

### Új pályázat indításakor
- Használd a **`TAMOGAT/`** könyvtár sablonjait kiindulópontként:
  - `TAMOGAT/CEGADAT_SABLON.md` — céges adatok, pénzügyi kivonat, DI igazolások (mesterdoc.md alapján ellenőrzendő)
  - `TAMOGAT/PALYAZATI_DOKUMENTUM_SABLON.md` — projekt indokoltság, célok, szakmai tartalom, költségvetés, EPTK-verzió sablon
  - `TAMOGAT/MELLEKLETEK_SABLON.md` — teljes melléklet checklist (cégkivonat, KOMA, HIPA, DFK, árajánlatok, stb.)
- Minden `<!-- FIXME -->` jelölést töltsd ki a konkrét pályázati kiírás alapján.
- Az EPTK-verzió blokkokat változtatás nélkül másold be az online pályázati felületre.

### Új hitelkérelem indításakor
- Használd a **`HITEL/`** könyvtár sablonjait kiindulópontként:
  - `HITEL/HITELPROJEKT_SABLON.md` — beruházási lista, hitelcél, indokoltság, hitelfeltételek
  - `HITEL/HITEL_KOLTSEGVETES_ES_CASHFLOW_SABLON.md` — törlesztőrészlet számítás, 5 éves cash-flow, DSCR mutató
  - `HITEL/HITEL_DOKUMENTUMLISTA_SABLON.md` — KAVOSZ / banki dokumentumlista checklist
- Minden `<!-- FIXME -->` jelölést töltsd ki a konkrét hitelkonstrukció és aktuális céges adatok alapján.
- A Széchenyi Mikrohitel MAX+ referencia adatok (6M Ft, 3%, 107 812 Ft/hó) referenciaként maradnak a sablonban.

Automatizált melléklet-ellenőrzés
A projekt repository-hoz hozzáadtam egy egyszerű PowerShell scriptet: scripts\check_mellekletek.ps1. A script a repo gyökérből futtatva ellenőrzi az alapvető mellékletek meglétét (például: KOMA, iparűzési igazolás, DFK, árajánlatok, cégkivonat, dimop költségvetés). Futtatás PowerShellben: powershell -ExecutionPolicy Bypass -File .\scripts\check_mellekletek.ps1
A script nem tölt fel semmit az EPTK-re, csak helyi fájlrendszerben vizsgálja a fájlok meglétét és listázza a hiányzó tételeket, így segít előkészíteni a feltöltést.
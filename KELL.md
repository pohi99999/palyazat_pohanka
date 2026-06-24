KELL — emberi teendők (párosítás: MIT / HOL / MIVEL / MIKOR)

1) [x] NAV: köztartozás‑mentesség ("nullás") igazolás lekérése (KOMA - Pohánka Kft.pdf elmentve, aktuális igazolás rendelkezésre áll)
- MIT: Kérd le a NAV által kiadott köztartozás‑mentesség igazolást a pályázathoz.
- HOL: NAV ügyfélkapu / NAV honlap (https://www.nav.gov.hu) → Ügyfélkapu belépés, adóigazolások menü.
- MIVEL: cég adószáma, cégkivonat, mesterdoc.md (cégadatok).
- MIKOR: lehetőleg a pályázat benyújtása előtt 1–2 héttel (várható ügyintézési idő: néhány nap).

2) Helyi iparűzési adó igazolás az önkormányzattól
- MIT: Kérd le az önkormányzat által kiadott helyi iparűzési adó befizetésre/mentességre vonatkozó igazolást.
- HOL: Zalaegerszeg (https://zalaegerszeg.hu) / illetékes önkormányzat pénzügyi ügyfélszolgálata vagy e‑ügyintézés.
- MIVEL: cégkivonat, üzleti cím, befizetési bizonylatok (ha van).
- MIKOR: javasolt min. 2 hét a kérelmezéstől a jóváhagyásig; indítsd el mielőbb.

3) DFK szolgáltatóval időpont‑egyeztetés és DFK dokumentum átvétele
- MIT: Egyeztess időpontot a DFK (digitális fejlesztési koncepció) készítővel, szerezd be és ellenőrizd a végleges DFK dokumentumot.
- HOL: DFK szolgáltató / tanácsadó (kapcsolat a "palyazat-todo-list-4.md" alapján).
- MIVEL: mesterdoc.md, DIMOP források (Palyazatok/DIMOP_1_2_6/*).
- MIKOR: a pályázati dokumentálás előtt, legalább 2–3 héttel a benyújtás előtt.

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

7) Banki / KAVOSZ egyeztetés a Széchenyi Mikrohitelhez (előzetes)
- MIT: Kapcsolatfelvétel a bankkal vagy KAVOSZ‑szolgáltatóval a mikrohitel lehetőségeinek előzetes egyeztetéséhez (ez későbbi részletezés tárgya).
- HOL: kiválasztott bank fiókja / KAVOSZ ügyfélszolgálat.
- MIVEL: pénzügyi dokumentumok, cash‑flow tervek (Hitelek/Szechenyi_Mikrohitel_MAX/*.md), mesterdoc anyagok.
- MIKOR: pályázat benyújtása előtt; javasolt 2–3 hét előkészítéssel.

8) Könyvelői és jogi ellenőrzés
- MIT: Kérd a könyvelőd és jogi tanácsadód végleges ellenőrzését a benyújtandó dokumentumok és költségvetés felett.
- HOL: könyvelőiroda / jogi tanácsadó.
- MIVEL: összes feltöltendő dokumentum, mesterdoc.md, költségvetés, DFK.
- MIKOR: 1–3 nap a benyújtás előtt.

Megjegyzés: minden igazolásnál őrizd meg a letöltött PDF/HTML bizonylatot és töltsd fel az EPTK mellékletei közé; ha kétség merül fel, konzultálj a pályázati tanácsadóval vagy a könyvelővel.

Automatizált melléklet-ellenőrzés
A projekt repository-hoz hozzáadtam egy egyszerű PowerShell scriptet: scripts\check_mellekletek.ps1. A script a repo gyökérből futtatva ellenőrzi az alapvető mellékletek meglétét (például: KOMA, iparűzési igazolás, DFK, árajánlatok, cégkivonat, dimop költségvetés). Futtatás PowerShellben: powershell -ExecutionPolicy Bypass -File .\scripts\check_mellekletek.ps1
A script nem tölt fel semmit az EPTK-re, csak helyi fájlrendszerben vizsgálja a fájlok meglétét és listázza a hiányzó tételeket, így segít előkészíteni a feltöltést.
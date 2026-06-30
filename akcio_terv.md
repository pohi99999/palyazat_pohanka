# Hibrid Operatív Akcióterv – Pohánka és Társa Kft.

Ez a dokumentum a Pohánka és Társa Kft. első pályázati (DIMOP) és támogatott hitelkérelmi (Széchenyi) folyamatainak gyakorlati, lépésről lépésre követhető megvalósítási terve. 

A dokumentumban szereplő cégadatok a [mesterdoc.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/mesterdoc.md), a részletes pályázati és hitelkutatási háttéranyagok pedig a [kutatas_lehetőségek.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/kutatas_lehet%C5%91s%C3%A9gek.md) fájlban találhatók.

---

## 🆕 2026-06-30 – AI-alapú Pályázat- és Hitelkereső Rendszer (KÉSZ)

> **Brunella Agent System (BAS) – FundingSearchAgent & Workflow**

A mai napon (2026-06-30) elkészült és a GitHub repóba feltöltésre kerültek az alábbi fájlok (commit: `611d48f`, `273387b`):

| Fájl | Tartalom |
|------|----------|
| `config/pohanka_credit_profile.json` | Gépileg olvasható céges profil JSON (cégadatok, 2023–2025 pénzügyek, DI igazolások, preferenciák, kizárások, jogosultsági ellenőrzések) |
| `src/domain/pohankaCreditProfile.py` | Python domain modul – helper függvények az összes workflow számára |
| `src/agents/fundingSearchAgent.py` | FundingSearchAgent – Brunella LLM rendszer-prompt a pályázat/hitel kereséshez |
| `src/workflows/fundingAndGrantDiscovery.py` | Teljes kereső workflow – szűrés, rangsorolás, JSON kimenet generálás |
| `output/pohanka_funding_candidates.json` | Első workflow kimenet: 5 pályázat + 5 hitelkonstrukció rangsorolva |
| `output/pohanka_3month_action_plan.json` | **3 hónapos végrehajtható akcióterv** (4 pályázat × 5–10 lépés + 5 hitel × 4–10 lépés, magyar határidőkkel és felelősökkel) |
| `tests/test_pohankaCreditProfile.py` | 29 egységteszt (mind zöld) |
| `README.md` | Projekt dokumentáció |

**Legfontosabb azonnali teendők** (az akcióterv JSON alapján):
- `2026-07-07` — OTP Bank KAVOSZ konzultáció + Széchenyi Kártya ellenőrzés
- `2026-07-08` — DFK véglegesítés + EPTK cégprofil ellenőrzés
- `2026-07-10` — NAV KOMA + HIPA frissítés (ha lejárt), MFB Pont tájékozódás
- `2026-07-15` — Árajánlatok (DIMOP + Széchenyi), GINOP státusz, Garantiqa megindítás
- `2026-07-22` — DIMOP projekt indokolás + BAS szakmai tartalom véglegesítése
- `2026-07-29` — Széchenyi hiteligénylő benyújtása OTP Bankba
- `2026-08-05` — DIMOP benyújtás EPTK portálon

---


## I. Bevezetés (Cégprofil és Célok)

*   **Pályázó vállalkozás:** POHÁNKA ÉS TÁRSA KÖNYVELŐ IRODA Kft.
*   **Főbb paraméterek:** Zalaegerszegi mikrovállalkozás, 3 fő alkalmazotti létszám (ÁSZE), KIVA adózás, "Megbízható adózó" státusz, korábbi hitel- és támogatásmentes előélet.
*   **Digitális érettség:** Modern Vállalkozások Programja (MVP) által kiállított alacsony digitális intenzitású (DI) igazolás (**Iratazonosító: IG32095-2025**).
*   **Elsődleges pályázati cél:** **DIMOP Plusz-1.2.6/B-26** – Mikro- és kisvállalkozások digitalizációjának támogatása.
    *   **Projekt:** *Brunella Agent System (BAS)* mesterséges intelligencia alapú könyvelés-automatizálási szoftver és kapcsolódó irodai IT hardver bevezetése.
    *   **Költségvetés:** 9 000 000 HUF (90% támogatás = 8 100 000 HUF vissza nem térítendő támogatás, 10% önerő = 900 000 HUF).
*   **Elsődleges támogatott hitelcél:** **Széchenyi Mikrohitel MAX+**
    *   **Projekt:** Irodai IT infrastruktúra bővítése és a könyvelőirodai mobilitást segítő cégautó beszerzése.
    *   **Hitelösszeg:** 5 000 000 – 7 000 000 HUF (fix 3%-os éves kamat).

---

## II. DIMOP Plusz-1.2.6/B-26 Napi szintű operatív terv

> [!IMPORTANT]
> **KRITIKUS HATÁRIDŐK – FRISSÍTVE 2026-06-30:**
> *   **Eredeti beadási határidő (Nyugat-Dunántúl):** **2026. június 30.** ← MA VAN
> *   **Státusz:** Ha a benyújtás ma (június 30.) nem sikerült, az EPTK-n ellenőrizni kell az új határidőt.
> *   **Következő reális belső határidő:** **2026. augusztus 5.** (a 3 hónapos akcióterv alapján)
> *   **AI-alapú akcióterv:** `output/pohanka_3month_action_plan.json` – részletes lépések és határidők

### 1.1 Jogosultsági ellenőrzés (Június 18–19. / 1-2. nap)
*   [ ] **Cégadatok validálása:** A [mesterdoc.md I. pontja](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/mesterdoc.md#i-%C3%A1ltal%C3%A1nos-c%C3%A9gadatok-c%C3%A9gkivonat-alapj%C3%A1n) alapján ellenőrizni a NAV törzsadatait. Biztosítani, hogy az IT TEÁOR kódok (6201, 6202, 6311) hivatalosan bejegyezve szerepeljenek.
*   [ ] **DI-igazolás aktiválása:** Belépés a [digikkv.hu](https://digikkv.hu) felületre, a Modern Vállalkozások Programja (MVP) regisztráció összekapcsolása, az `IG32095-2025` iratazonosítójú 10 pontos DI-igazolás letöltése és ellenőrzése.
*   [ ] **Kizáró okok ellenőrzése:** Meggyőződni arról, hogy a cég köztartozásmentes (a NAV adatbázisban "Megbízható adózó" státuszban szerepel-e, lásd [mesterdoc.md VII. pont](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/mesterdoc.md#vii-egy%C3%A9b-fontos-inform%C3%A1ci%C3%B3k-kiz%C3%B3-okok-%C3%A9s-b%C3%ADr%C3%A1lati-szempontok)).

### 1.2 Költségvetés véglegesítése (Június 20–21. / 3-4. nap)
*   [ ] **Allokáció végrehajtása:** A 9 000 000 HUF keretösszeg felosztása a DIMOP szabályoknak megfelelően:
    *   **Hardverbeszerzés (max. 30%):** GPU-s munkaállomás a BAS lokális Ollama futtatásához, irodai PC-k, NAS tároló a vektoradatbázishoz (LanceDB) – *Tervezett összeg: max. 2 700 000 HUF.*
    *   **Szoftver és Felhőszolgáltatások:** BAS mag szoftverlicencek, Google Cloud / API elérések – *Tervezett összeg: kb. 4 500 000 HUF.*
    *   **Képzés és Tanácsadás:** A BAS bevezetéséhez szükséges munkafolyamat-tanácsadás és a 3 fő munkatárs AI-asszisztált képzése – *Tervezett összeg: kb. 1 800 000 HUF.*

### 1.3 Árajánlatok összegyűjtése (Június 22–24. / 5-7. nap)
*   [ ] **Hardver ajánlatok:** Legalább 3 független és összehasonlítható árajánlat bekérése a GPU-s munkaállomásra és a hálózati NAS-ra.
*   [ ] **Szoftver és Fejlesztési ajánlatok:** Árajánlat bekérése a BAS (Brunella Agent System) implementációt és a FastAPI orkesztrációs mag integrációját végző fejlesztő partnertől.
*   [ ] **Képzési és Tanácsadói ajánlatok:** Árajánlatok bekérése a BAS tréning és munkafolyamat-tanácsadás lebonyolítására.

### 1.4 Projektleírás / Adatlap szövegek (Június 25. / 8. nap)
*   [ ] **Szövegek véglegesítése:** Az alábbi előkészített, strukturált szövegek átolvasása és beillesztése a pályázati formanyomtatványba:

#### 1.4.1 Projekt indokoltsága, kiinduló helyzet
A Pohánka és Társa Kft. mikrovállalkozás Zalaegerszegen, főként számviteli és könyvelési szolgáltatásokat nyújt, 16+ éves működési múlttal, stabil, pozitív saját tőkével és megbízható adózói minősítéssel. A vállalkozás digitális intenzitása a Modern Vállalkozások Programja keretében lefolytatott audit alapján 10 pontos, azaz “alacsony” szintű, ami indokolja a célzott digitalizációs beavatkozást.

A könyvelési és adminisztratív folyamatok jelenleg nagyrészt manuálisak: a beérkező számlák jelentős részét kézzel rögzítik, a bankszámla- és pénztártételek egyeztetése időigényes, a dokumentumkezelés és riportolás több, részben nem integrált rendszerben történik. Ez a működés a növekvő ügyfélszám mellett kapacitáskorlátot, hibakockázatot és profitabilitási plafont eredményez.

A pályázó célja, hogy a Brunella Agent System (BAS) hibrid, multi‑agent AI rendszer bevezetésével átfogó digitális transzformációt hajtson végre, és a manuális adminisztrációt nagy arányban automatizált, intelligens folyamatokra cserélje.

#### 1.4.2 Projekt célja
A projekt célja egy olyan integrált, AI‑alapú digitális infrastruktúra kiépítése, amely a Pohánka és Társa Kft. teljes könyvelési és adminisztratív értékláncát lefedi a számlabefogadástól a banki egyeztetésen át a NAV‑szinkronig. A Brunella Agent System bevezetésével a vállalkozás legalább 50%-kal kívánja csökkenteni az egy ügyfélre jutó manuális adatbevitelre fordított időt, miközben javítja a szolgáltatás minőségét és növeli a digitalizációs érettséget.

Konkrét cél, hogy a beérkező számlák legalább 80%-a automatikusan, Gmail‑figyelés, OCR és AI alapú adatkinyerés segítségével kerüljön a könyvelési rendszerbe, a bankszámla- és pénztártételek minimum 70%-a pedig automatikus reconciliation folyamatokon fusson keresztül. A vállalkozás DI‑pontszáma a projekt lezárásáig az “alacsony” kategóriából a “közepes” szintre emelkedjen.

#### 1.4.3 A projekt szakmai tartalma, tevékenységek
A projekt keretében a vállalkozás a következő fejlesztési elemeket valósítja meg:
1. **Hardver és hálózati infrastruktúra fejlesztése:** GPU‑képes munkaállomás és korszerű irodai számítógépek beszerzése a BAS lokális futtatásához és fejlesztéséhez. NAS és hálózati eszközök telepítése a vektoradatbázis és biztonságos adatmentés kiszolgálására.
2. **Brunella Agent System (BAS) bevezetése:** Node.js alapú orkesztrációs mag, Python/FastAPI alrendszer és Playwright alapú “Robotkéz” modul bevezetése a könyvelői szoftverek és webes felületek automatizált kezelésére. LanceDB vektoradatbázisra épülő RAG‑megoldás kialakítása, amely a számlák, bankkivonatok és korábbi döntések alapján támogatja az AI‑asszisztensek tanulását. Phoenix Protocol v2 önjavító mechanizmus élesítése folyamatos heartbeat‑monitoringgal és automatikus újraindítással.
3. **Felhőszolgáltatások és üzemeltetés:** Felhőalapú erőforrások (pl. Google Cloud) igénybevétele a rendszer skálázható és biztonságos futtatásához, backup‑ és monitoringszolgáltatásokkal kiegészítve.
4. **Tanácsadás és képzés:** Külső IT tanácsadó bevonása a rendszertervezéshez, biztonsági hardeninghez és folyamatoptimalizáláshoz. Belső képzések szervezése a BAS mindennapi használatára, AI‑asszisztált munkavégzésre és digitális munkafolyamatokra.

#### 1.4.4 Várható eredmények, indikátorok
*   A manuális számlaadat‑rögzítéssel töltött idő legalább 50%-kal csökken a projekt előtti bázisidőszakhoz képest (belső időmérési kimutatás alapján).
*   A beérkező számlák minimum 80%-a automatikus Gmail‑figyelés + OCR + AI alapú folyamatokon keresztül kerül be a könyvelési rendszerbe.
*   A bankszámla- és házipénztár tranzakciók legalább 70%-a automatikus egyeztető folyamatokon fut át.
*   A rendszer éves rendelkezésre állása eléri a 99%-ot a Phoenix Protocol v2 önjavító mechanizmusnak köszönhetően.
*   A DI‑pontszám az új audit során az “alacsony” szintről legalább “közepes” kategóriára javul.

### 1.5 Mellékletek beszerzése (Június 26. / 9. nap – BELSŐ HATÁRIDŐ)
*   [ ] **Belső határidő ellenőrzése:** Minden mellékletnek készen kell állnia az EPTK-ba történő feltöltéshez. (Lásd a IV. fejezet Melléklet Ellenőrző Listáját).

### 1.6 EPTK feltöltés és beadás (Június 27–29. / 10-12. nap)
*   [ ] **Regisztráció és belépés:** Belépés az állami EPTK pályázati felületre (ügyfélkapus azonosítással).
*   [ ] **Adatlap rögzítése:** A cégadatok, pénzügyi adatok bevitele, és a 1.4-es fejezetben szereplő leírások bemásolása a megfelelő mezőkbe.
*   [ ] **Mellékletek feltöltése:** A DFK igazolás, a DI-igazolás, a 3 db árajánlat, cégkivonat és aláírási címpéldány feltöltése PDF formátumban.
*   [ ] **Elektronikus aláírás és beadás:** A projektgazda cégjegyzésre jogosult képviselőjének (ügyvezető) AVDH vagy minősített elektronikus aláírásával hitelesíteni az adatlapot és beküldeni.

---

## III. Széchenyi Mikrohitel MAX+ Heti sprintek

### 2.1 Hitelképességi előszűrés (1. Hét: Július 1–7.)
*   [ ] **Előminősítési kalkuláció:** Ellenőrizni a [mesterdoc.md II. pontjában](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/mesterdoc.md#ii-p%C3%A9nz%C3%BCgyi-%C3%A9s-gazdas%C3%A1gi-adatok-utols%C3%B3-3-lez%C3%A1rt-%C3%BCzleti-%C3%A9v) szereplő pénzügyi adatokat (2025-ös árbevétel: 9 158 000 Ft, saját tőke: 6 065 000 Ft).
*   [ ] **Hitelösszeg kijelölése:** Mivel a tervezett hitelösszeg **5-7 millió HUF**, ez a saját tőke (6 M Ft) és az árbevétel (9,1 M Ft) alapján teljesen biztonságos tartományba esik.
*   [ ] **Törlesztő kalkuláció:** Kiszámítani a 3%-os fix kamat mellett fizetendő havi törlesztőrészletet (pl. 5 évre 6 M Ft esetén a tőke + kamat törlesztő kb. 110-115 ezer HUF/hó, ami a 2025-ös stabil adózott eredmény mellett könnyen kigazdálkodható).

### 2.2 Széchenyi Programiroda / bank kiválasztása (2. Hét: Július 8–14.)
*   [ ] **OTP kapcsolat felvétele:** Mivel a cég OTP bankszámlával rendelkezik, és megbízható partner, az OTP Bank Széchenyi hitel termékét választjuk.
*   [ ] **Időpontfoglalás a KAVOSZ-nál:** Időpontot foglalni a zalaegerszegi KAVOSZ (Széchenyi Programiroda) irodába a hitelkérelem személyes átadásához és előminősítéshez.

### 2.3 Szükséges dokumentumok összegyűjtése (3. Hét: Július 15–21.)
*   [ ] **Pénzügyi beszámolók:** Letölteni az Igazságügyi Minisztérium portáljáról a 2023, 2024 és 2025-ös egyszerűsített éves beszámolókat (mérlegeket és eredménykimutatásokat).
*   [ ] **Főkönyvek letöltése:** A könyvelési szoftverből kinyerni a 2023, 2024, 2025-ös lezárt főkönyvi kivonatokat, valamint a 2026. I. féléves törtidőszaki főkönyvi kivonatot.
*   [ ] **NAV nullás igazolás:** Lekérni az Ügyfélkapun keresztül a köztartozásmentes adózói adatbázisban (KOMA) való szereplést igazoló NAV Nullás igazolást.

### 2.4 Hitelcél részletes leírása (4. Hét: Július 22–28.)
*   [ ] **Eszközök specifikációja:** A Széchenyi Mikrohitel MAX+ beruházási hitel céljának pontos meghatározása és az árajánlatok összegyűjtése:
    *   **Irodai hardver:** További irodai laptopok, monitorok a 3 fő részére – *Keretösszeg: kb. 1,5–2 M HUF.*
    *   **Mobilitási eszköz (cégautó):** A könyvelőiroda ügyfeleihez való kijárást támogató, gazdaságos cégautó – *Keretösszeg: kb. 3,5–5 M HUF.*

### 2.5 Hitelkérelem összeállítása és beadása (5. Hét: Július 29. – Augusztus 4.)
*   [ ] **Nyomtatványok kitöltése:** A KAVOSZ honlapjáról letöltött hitelkérelmi adatlap és üzleti terv sablonok kitöltése a [mesterdoc.md](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/mesterdoc.md) alapján.
*   [ ] **Személyes benyújtás:** A kitöltött kérelmek és a IV. fejezetben felsorolt összes melléklet személyes leadása a zalaegerszegi Széchenyi Programirodában.

### 2.6 Döntés, szerződéskötés, lehívás (6-8. Hét: Augusztus 5–25.)
*   [ ] **Banki bírálat követése:** Kapcsolattartás az OTP banki hitelügyintézőjével, esetleges hiánypótlások gyors teljesítése.
*   [ ] **Szerződéskötés és Garancia:** A hitelszerződés aláírása az OTP Banknál, a Garantiqa kezességvállalási szerződés megkötése, és a fedezetek (pl. cégautó zálogjog) bejegyzése.
*   [ ] **Folyósítás és elszámolás:** A hitelösszeg lehívása, az eszközök kifizetése és a bank felé történő számlabemutatásos elszámolás.

---

## IV. Csatolmányok és Mellékletek közös checklist

Az alábbi táblázat tartalmazza a mindkét konstrukcióhoz szükséges dokumentumok listáját, azok forrását és felelősét:

| Dokumentum Megnevezése | Konstrukció | Felelős | Forrás / Hivatkozás | Státusz |
| :--- | :---: | :---: | :--- | :---: |
| **Digitális Fejlesztési Koncepció (DFK)** | DIMOP | Pályázatíró / IT | MVP DFK rendszer | Beszerzendő |
| **Digitális Intenzitás (DI) Igazolás** | DIMOP | Cégvezetés | [digikkv.hu](https://digikkv.hu) (IG32095-2025) | Rendelkezésre áll |
| **3 db független árajánlat (IT és BAS)** | DIMOP | IT Tanácsadó | Külső beszállítók | Beszerzendő |
| **2023, 2024, 2025 Beszámolók** | Mindkettő | Könyvelő | [mesterdoc.md II. szakasz](file:///Z:/001_Workspace/p%C3%A1ly%C3%A1zat-pohankaestarsakft/mesterdoc.md#ii-p%C3%A9nz%C3%BCgyi-%C3%A9s-gazdas%C3%A1gi-adatok-utols%C3%B3-3-lez%C3%A1rt-%C3%BCzleti-%C3%A9v) | Rendelkezésre áll |
| **2023, 2024, 2025 Főkönyvi kivonatok** | Hitel | Könyvelő | Könyvelő szoftverből | Beszerzendő |
| **2026. I. féléves törtidőszaki főkönyv** | Hitel | Könyvelő | Könyvelő szoftverből | Beszerzendő |
| **Friss cégkivonat (30 napnál nem régebbi)** | Mindkettő | Cégvezetés | Igazságügyi Minisztérium | Beszerzendő |
| **Aláírási címpéldányok** | Mindkettő | Cégvezetés | Meglévő közjegyzői okirat | Rendelkezésre áll |
| **NAV Nullás Köztartozás Igazolás** | Mindkettő | Könyvelő | NAV KOMA rendszer | Beszerzendő |
| **Hitelkérelmi nyomtatványok és üzleti terv**| Hitel | Cégvezetés | [kavosz.hu](https://www.kavosz.hu) portálról letölthető | Beszerzendő |
| **Autóvásárlási és IT eszköz árajánlatok** | Hitel | Cégvezetés | Autókereskedés és IT bolt | Beszerzendő |

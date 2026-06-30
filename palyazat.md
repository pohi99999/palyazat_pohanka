# Pohánka és Társa Kft. – Pályázati és támogatási profil

> **Célja:** LLM-barát, destillált profilindex. Egy külső AI kereső ügynök ebből az egyetlen fájlból megérti, milyen nyitott pályázatokat és VNT-támogatásokat érdemes keresni a cégnek.
> **Frissítve:** 2026-06-30

---

## 1. Cégprofil

| Mező | Adat |
|:---|:---|
| **Teljes cégnév** | POHÁNKA ÉS TÁRSA KÖNYVELŐ IRODA KORLÁTOLT FELELŐSSÉGŰ TÁRSASÁG |
| **Rövid cégnév** | Pohánka és Társa Kft. |
| **Székhely** | 8900 Zalaegerszeg, Berek utca 38. |
| **Régió** | Nyugat-Dunántúl (Zala Vármegye) — **nem Budapest** |
| **Adószám** | 14728864-2-20 |
| **KHT szám** | HU14728864 |
| **Cégjegyzékszám** | 20-09-069482 (Zala Vármegyei Cégbíróság) |
| **Alapítás** | 2009.04.10. |
| **Cégforma** | Kft. (Korlátolt Felelősségű Társaság) |
| **Adózási forma** | KIVA (Kisvállalati adó) — 2020.01.01-től |
| **Adózói minősítés** | **Megbízható adózó** (2026.05.01-től) |
| **Létszám (ÁSZE 2025)** | **3 fő** (2023: 1 fő, 2024: 1 fő, 2025: 3 fő) |
| **KKV besorolás** | Mikrovállalkozás |
| **Kapcsolt vállalkozás** | Nincs |
| **Külföldi tulajdonos** | Nincs |

### TEÁOR kódok

| TEÁOR | Megnevezés | Megjegyzés |
|:---:|:---|:---|
| **6920** | Számviteli, könyvvizsgálói, adószakértői tevékenység | Főtevékenység (2025-01-01-től) |
| **6201** | Számítógépes programozás | Cégbírósági bejegyzés |
| **6202** | Információtechnológiai szaktanácsadás | Cégbírósági bejegyzés |
| **6311** | Adatfeldolgozás, web-hoszting szolgáltatás | Cégbírósági bejegyzés |
| **6290** | Egyéb információtechnológiai szolgáltatás | 2026.01.01-től |
| **6310** | Számítástechnikai infrastruktúra, adatfeldolgozás | 2026.01.20-tól |

---

## 2. Pénzügyi profil (pályázatok szempontjából)

| Mutató | 2023 (lezárt) | 2024 (lezárt) | 2025 (lezárt) |
|:---|:---:|:---:|:---:|
| Nettó árbevétel | 2 844 000 Ft | 4 204 000 Ft | **9 158 000 Ft** |
| Mérlegfőösszeg | 5 661 000 Ft | 6 338 000 Ft | 6 502 000 Ft |
| Adózott eredmény | 1 620 000 Ft | 346 000 Ft | 374 000 Ft |
| Saját tőke | 5 344 000 Ft | 5 681 000 Ft | **6 065 000 Ft** |
| Üzemi eredmény | 1 260 000 Ft | 346 000 Ft | 517 000 Ft |

**Értékelés (pályázati szempontból):**
- Stabilan pozitív saját tőke mindhárom évben (> jegyzett tőke = 3 000 000 Ft)
- 2023→2025: árbevétel **+222%** — erős növekedési pálya
- Köztartozás nincs (KOMA igazolás meglévő), HIPA igazolás meglévő
- Nincs korábbi VNT-támogatás → **teljes de minimis keret elérhető** (kb. 200 000 EUR / 3 év)
- Hitelmentes cég — nincs meglévő banki kötelezettség
- Kockázati szint: **alacsony** (mikro méret, de növekvő, tiszta pénzügyi lap)

---

## 3. Digitális és innovációs profil

### Digitális Intenzitás (DI) igazolások

| Típus | Pontszám | Szint | Azonosító | Dátum |
|:---|:---:|:---|:---|:---|
| Vállalati DI | **10 pont** | Alacsony | IG32095-2025 | 2025.06.19. |
| Közösségi DI | **8 pont** | Magas | IG32096-2025 | 2025.06.19. |

> ⭐ Az **alacsony DI-szint** célzottan jogosít a DIMOP digitalizációs felhívásokra.

### DFK (Digitális Fejlesztési Koncepció)

- MV Program 2.0 keretében elfogadott DFK Támogatói Okirat: `D127/23-505/2025`
- DIMOP_Plusz-1.2.7-23 projekt azonosító: `DIMOP_Plusz-1.2.7-23-2023-00001`
- DFK 100%-os in-kind támogatás (önerő nélkül), határidő: 2026.11.30.

### Brunella Agent System (BAS) — a fejlesztés tárgya

A cég saját fejlesztésű **multi-agent AI ökoszisztéma**t vezet be, amely a könyvelési és adminisztratív folyamatokat automatizálja:

- **Bifrost Gateway:** lokális (Ollama) + felhős (Gemini, GPT-4o) modellek hibrid kombinálása
- **FastAPI Robotkéz (RobotkezV2):** VLA-alapú UI-automatizálás — az ügynökök látják és kezelik a szoftvereket
- **LanceDB RAG:** vektoradatbázis-alapú folyamatos tanulás (Data Flywheel)
- **Phoenix Protocol v2:** 24/7 öngyógyítás, 5 mp-es liveness monitor
- **Várható eredmény:** 50%+ manuális adminisztráció-csökkentés, 80%+ automatikus számlafeldolgozás, 70%+ banki reconciliation

---

## 4. Stratégiai fejlesztési célok (forráskereséshez)

- **Digitális infrastruktúra:** GPU munkaállomás, 3 db PC/laptop, NAS + hálózat — fizikai hardver a BAS futtatásához
- **BAS szoftver/cloud:** licencek, OCR modulok, LanceDB, felhőkapacitás (Google Cloud / IaaS)
- **Integráció és IT security:** rendszertervezés, fejlesztői szolgáltatások, IT biztonsági hardening
- **Képzés:** 3 fős csapat BAS-kompetenciafejlesztése (digitális munkavégzés)
- **Cégautó:** területi ügyfélmobilitás (Nyugat-Dunántúl), Széchenyi-hitelből finanszírozva
- **Hosszabb táv:** BAS mint termék — külső KKV-k számára értékesítendő AI könyvelési szolgáltatás; pályázati orchestration modul (Brunella-alapú pályázat/hitel asszisztens)

---

## 5. Pályázati preferenciák és korlátok

### Preferált pályázattípusok
- KKV digitalizáció (IT fejlesztés, AI, automatizálás)
- Innovációs támogatás (saját fejlesztésű AI termék)
- Vállalati képzési programok (digitális kompetencia)
- Vidéki (nem budapesti) mikrovállalkozásoknak szóló felhívások
- Kombált hitel+VNT konstrukciók

### Támogatási intenzitás preferencia
- **Ideális:** ≥90% vissza nem térítendő (DIMOP 1.2.6/B típus)
- **Elfogadható:** ≥70% VNT
- **Kombinált:** 0%-os hitel + max. 50% VNT (DIMOP 1.2.3/A típus)

### Összegsáv
| Időhorizont | Ideális összeg | Megjegyzés |
|:---|:---:|:---|
| Rövid táv (2026) | 3–12 M Ft | DIMOP-szerű, jelenleg aktív |
| Középtáv (2027–28) | 12–30 M Ft | GINOP innovációs szint, ha árbevétel nő |

### Korlátok (mit NE keressen az ügynök)
- >50 M Ft tisztán K+F pályázatok — jelenleg kockázatos (kis forgalom)
- Kizárólag budapesti székhelyre célzott felhívások
- Magas önerő-igényű (>30%) pályázatok reálisan nehéz
- Export-fókuszú pályázatok (nincs exporttevékenység)
- Mezőgazdasági, ipari vagy gyártási szektorra szóló felhívások

---

## 6. Jelenlegi és célzott pályázati irányok

| # | Felhívás típusa | Releváns példa | Megjegyzés |
|:---:|:---|:---|:---|
| 1 | Mikro-KKV digitalizáció VNT | DIMOP Plusz-1.2.6/B-26 | **Aktív, folyamatban** (90% VNT, 3–12 M Ft) |
| 2 | Kombinált digitalizációs hitel+VNT | DIMOP Plusz-1.2.3/A-24 | Nyitva 2027.06.30-ig (0% hitel + 50% VNT) |
| 3 | KKV innovációs pályázat | GINOP Plusz-2.1.3-24 | Figyelendő, 20–50 M Ft (BAS mint innováció) |
| 4 | Vállalati képzési program | GINOP/EFOP képzési felhívások | BAS tréning, digitális kompetencia |
| 5 | Digitális jelenlét / webshop | MV Program digitális felhívások | Brunella pályázati asszisztens platform |
| 6 | 0%-os beruházási hitel | GINOP Plusz-1.4.3-24 KKV Tech Plusz | IT eszközbeszerzésre, 0% kamat |
| 7 | Munkahely-megtartó/bővítő | Foglalkoztatási pályázatok | Ha létszámbővítés tervezett |
| 8 | EU direkt / EIC Accelerator | Horizont Európa (jövőre) | BAS mint deep tech innováció, hosszabb táv |

---

## 7. Korábbi pályázatok és hiteltörténet

- **Korábbi VNT-támogatás:** Nincs (első pályázó)
- **De minimis felhasználás:** Nincs (teljes 200 000 EUR keret elérhető)
- **Meglévő hitelek:** Nincs (hitelmentes cég)
- **DFK Támogatói Okirat:** Meglévő (in-kind, nem pénzbeli)

---

## Keresési útmutató LLM ügynök számára

**Keress olyan NYITOTT pályázati és támogatási felhívásokat, amelyek:**

- Mikrovállalkozásoknak és/vagy kisvállalkozásoknak szólnak (≤10 fő, ≤2 M EUR árbevétel)
- Hatókör: Nyugat-Dunántúl vagy országos (Budapest **kizárva**)
- Fő célterület: digitalizáció, IT fejlesztés, AI/automatizálás, innovációs képességfejlesztés, vállalati képzés
- Támogatható tevékenység: szoftverfejlesztés, felhőszolgáltatás, hardverbeszerzés (IT), IT tanácsadás, képzés
- Támogatási összeg: **3–12 M Ft** (rövid táv), **12–30 M Ft** (középtáv)
- Támogatási intenzitás: **≥70%** VNT; vagy kombinált 0%-os hitel + ≥50% VNT
- TEÁOR releváns: 6201, 6202, 6290, 6310, 6311, 6920

**Ellenőrizd minden találatnál:**
1. A cég paraméterei (árbevétel 2025: 9,158 M Ft; létszám: 3 fő; régió: Zala Vármegye) megfelelnek-e a jogosultsági feltételeknek
2. Az alacsony DI-szint (10 pont) előnyt jelent-e a felhívásban — **ha igen, ez erős illeszkedési pont**
3. Van-e kötelező önerő, és az reálisan biztosítható-e (max. 10–20% önerő vállalható)
4. Az IT/AI/szoftver fejlesztési célok (BAS, felhő, licencek, képzés) elszámolhatók-e a felhíváson belül
5. Van-e "de minimis" korlát — a cég még nem vett igénybe de minimis támogatást
6. A határidő reális-e (6–12 héten belül beadható)

**Rangsorolás szempontjai (csökkenő fontossági sorrend):**
1. Támogatási intenzitás (minél magasabb, annál jobb)
2. Összegsáv illeszkedése a 9 M Ft-os BAS fejlesztési kerethez
3. Elszámolható tételek lefedik-e a BAS szoftver + cloud + hardver + képzés kategóriákat
4. Nyitott/aktív státusz (nem felfüggesztett, nem kimerült keret)
5. Vidéki/nem budapesti kedvezmény

**Kizárási feltételek (ne ajánld ezeket):**
- Kizárólag budapesti székhely
- Kizárólag gyártási/ipari/mezőgazdasági szektor
- Csak nagyvállalati (>250 fő) felhívások
- Magas kamatozású (>3% éves) hitelek, ha nincs VNT-komponens

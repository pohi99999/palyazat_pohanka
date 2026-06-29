# Pályázati Dokumentum Sablon — Vissza Nem Térítendő Támogatás (VNT)

> **Útmutató:** Ez az általános sablon bármely digitalizációs vagy fejlesztési VNT pályázathoz használható. A Pohánka és Társa Kft. (BAS projekt) szövegeit alapként tartalmazza. A `<!-- FIXME -->` és **[FIXME: ...]** jelölésű mezőket a konkrét pályázati kiírás szerint kell kitölteni. Minden fejezet végén az *„EPTK-szöveg"* blokk az online pályázati felületre közvetlenül bemásolható.

---

## I. Projekt Indokoltsága

### Alapszöveg (Pohánka & BAS alapján)

A Pohánka és Társa Kft. 2009 óta működő zalaegerszegi mikrovállalkozás, amely főként számviteli és könyvelési szolgáltatásokat nyújt mikro- és kisvállalkozások számára. A cég alacsony digitális intenzitással rendelkezik (vállalati DI: 10 pont, IG32095-2025), és a manuális folyamatok (kézi számlafeldolgozás, kézi bankszámla-egyeztetés, fragmentált dokumentumkezelés) kapacitáskorlátot és hibakockázatot okoznak. A 3 fős csapattal és közel 9,2 millió Ft éves árbevétellel a cég már teljesítőképessége felső határán dolgozik; a jelenlegi manuális folyamatokra építve a növekedés csak költséges létszámbővítéssel valósítható meg.

A projekt célja a **Brunella Agent System (BAS)** bevezetése — OCR-alapú számlafeldolgozás, automatizált adatkinyerés, AI-támogatott tranzakció-egyeztetés és RAG-alapú döntéstámogatás révén.

### FIXME blokk — Igazítsd a konkrét pályázathoz

> **FIXME:** Ellenőrizd a pályázati kiírásban szereplő jogosultsági feltételeket:
> - Minimális ÁSZE (Pohánka: 3 fő)
> - Minimális / maximális árbevétel határok (Pohánka 2025: 9 158 000 Ft)
> - Területi kötöttség (Pohánka: Zalaegerszeg, Nyugat-Dunántúl, kevésbé fejlett régió)
> - Támogatási intenzitás (pl. DIMOP-nál 90%, más pályázatnál eltérhet)
> - TEÁOR kód jogosultság (főtevékenység: 6920)
> - DI igazolás szükségessége és típusa
>
> **FIXME:** Töltsd ki: `[PÁLYÁZAT KÓDJA, pl. DIMOP Plusz-1.2.6/B-26]`
> **FIXME:** Töltsd ki: `[PÁLYÁZATI FELHÍVÁS MEGNEVEZÉSE]`

---

## II. Projekt Céljai és Várható Eredményei

### Alapszöveg

A fejlesztés három fő célt szolgál:
1. **Kapacitásbővítés**: az adminisztratív folyamatok 50%-os automatizálásával plusz munkaerő felvétele nélkül 30–50%-kal több ügyfél kiszolgálhatóvá válik.
2. **Minőség és pontosság**: az OCR-alapú, szabályalapú adatellenőrzés drasztikusan csökkenti a kézi bevitel hibaarányát.
3. **Skálázhatóság és versenyképesség**: a BAS felhőalapú komponensei lehetővé teszik a kapacitás rugalmas bővítését a vállalkozás növekedésével arányosan.

### Várható Output Indikátorok (sablon)

| Indikátor | Tervezett érték | Megjegyzés |
|:---|:---:|:---|
| Támogatott vállalkozás | 1 db | Pohánka és Társa Kft. |
| Új / korszerűsített digitális eszközök | min. 3 db | GPU workstation, PC-k, NAS |
| Bevezetett digitális megoldások | min. 1 rendszer | BAS orkesztrációs rendszer |
| Felhőszolgáltatások bevezetése | min. 1 db | IaaS / PaaS / SaaS |
| Képzett munkavállalók | 3 fő | Teljes létszám |

### Várható Eredmény Indikátorok (sablon)

| Indikátor | Cél érték | Mérési időpont |
|:---|:---:|:---|
| Manuális adminisztrációs idő csökkentése | ≥ 50% | Projekt zárása után 1 év |
| Automatikus számlafeldolgozás aránya | ≥ 80% | Projekt zárása után 1 év |
| Automatikus banki egyeztetés aránya | ≥ 70% | Projekt zárása után 1 év |
| Rendszer rendelkezésre állás | ≥ 99% | Folyamatos |
| DI szint javulás | Alacsonyról középre | Következő DI audit |

### FIXME blokk

> **FIXME:** A konkrét pályázat indikátoraihoz igazítsd a fenti értékeket. Egyes konstrukciók eltérő mérőszámokat vagy határértékeket írnak elő. Pl. DIMOP-nál 50% admin időcsökkentés és min. 80% automatikus feldolgozás a vállalt küszöb.

---

## III. Szakmai Tartalom

### Alapszöveg — BAS Technikai Architektúra

A Brunella Agent System (BAS) egy moduláris, multi-agent AI ökoszisztéma, amelynek fő komponensei:

- **Orkesztrációs réteg** (Bifrost Gateway): koordinálja az AI ügynököket és a külső API-hívásokat.
- **FastAPI Robotkéz**: dokumentumbeáramlási pipeline (Gmail figyelés → OCR → adatkinyerés → könyvelési rendszer integráció).
- **LanceDB RAG**: vektoradatbázis-alapú dokumentumkeresés és döntéstámogatás.
- **Lokális AI modellek**: Ollama keretrendszer (pl. qwen2.5-coder), helyi GPU futtatással (adatbiztonság).
- **Phoenix Protocol**: monitoring és telemetria az AI döntések auditálhatóságához.

A fejlesztési feladatok (T1–T8) a `Fejlesztes/FEJLESZTESI_TERV_BAS_DIMOP_SZECHENYI.md` fájlban részletezve találhatók.

### FIXME blokk

> **FIXME:** Ha a konkrét pályázat más típusú fejlesztést finanszíroz (nem BAS/AI), cseréld le a technikai leírást. Az alapstruktúra megmaradhat:
> - Mi a rendszer neve / típusa?
> - Milyen komponensekből áll?
> - Hogyan integrálódik a meglévő folyamatokba?
> - Mi a várt hatás?
>
> **FIXME:** Töltsd ki: `[FUTAMIDŐ, pl. 12 hónap]`
> **FIXME:** Töltsd ki: `[MEGVALÓSÍTÁSI HELYSZÍN, pl. Zalaegerszeg, Kossuth út 39.]`

---

## IV. Költségvetési Struktúra

### Sablon VNT pályázathoz

> **FIXME:** A konkrét pályázati összegeket és arányokat a kiírás alapján töltsd ki. DIMOP Plusz-1.2.6/B-26 esetén a hardver max. 30%.

| Költségkategória | Tervezett összeg (Ft) | Arány | Megjegyzés |
|:---|:---:|:---:|:---|
| **1. Hardver** | <!-- FIXME --> | <!-- FIXME max. 30% --> | GPU workstation, PC-k, NAS |
| **2. Szoftver / Felhőszolgáltatások** | <!-- FIXME --> | <!-- FIXME --> | BAS licencek, OCR, LanceDB, Google Cloud |
| **3. Tanácsadás / Fejlesztés** | <!-- FIXME --> | <!-- FIXME --> | Rendszertervezés, integráció, IT security |
| **4. Képzés** | <!-- FIXME --> | <!-- FIXME --> | Csapat kompetenciafejlesztés |
| **Összesen** | **<!-- FIXME: ÖSSZKÖLTSÉG --> Ft** | 100% | |
| **Igényelt támogatás** | **<!-- FIXME: ÖSSZEG --> Ft** | <!-- FIXME: % --> | |
| **Önerő** | **<!-- FIXME: ÖSSZEG --> Ft** | <!-- FIXME: % --> | |

*Referenciaként — DIMOP Plusz-1.2.6/B-26 bontás:*
- *Hardver: 2 700 000 Ft (30%)*
- *Szoftver: 3 600 000 Ft (40%)*
- *Tanácsadás: 1 800 000 Ft (20%)*
- *Képzés: 900 000 Ft (10%)*
- *Összesen: 9 000 000 Ft | Támogatás: 8 100 000 Ft (90%) | Önerő: 900 000 Ft (10%)*

### FIXME blokk

> **FIXME:** Ellenőrizd a pályázatban előírt maximális arányokat kategóriánként.
> **FIXME:** Minden tételnél legyen legalább 2–3 árajánlat a `docs/` mappában.
> **FIXME:** Töltsd ki: `[PROJEKT ÖSSZKÖLTSÉG]`, `[TÁMOGATÁSI ÖSSZEG]`, `[ÖNERŐ ÖSSZEG]`, `[TÁMOGATÁSI INTENZITÁS %]`

---

## V. Indikátorok (EPTK-kompatibilis összesítő sablon)

```
Output indikátorok:
- Támogatott vállalkozások száma: [FIXME: 1] db
- Új/korszerűsített digitális eszközök: [FIXME: min. 3] db
- Bevezetett digitális megoldások: [FIXME: 1] db
- Képzésben részesített munkavállalók: [FIXME: 3] fő

Eredmény indikátorok:
- Manuális adminisztrációs idő csökkentése: [FIXME: >= 50%]
- Automatikus feldolgozás aránya: [FIXME: >= 80%]
- Digitális intenzitás javulás: [FIXME: alacsonyból középre]
```

> **FIXME:** A konkrét pályázat EPTK felületén az indikátorok pontos nevei és mértékegységei eltérhetnek a fentiektől. Mindig a pályázati felhívás mellékletéből másold be az indikátor-azonosítókat.

---

## Rövid EPTK-verzió sablon

> **Útmutató:** Ez a blokk az EPTK online felületen a "Projekt összefoglalója" vagy "Rövid leírás" mezőbe másolandó. Minden konkrét pályázatnál töltsd ki a `[FIXME]` mezőket, majd másold be **változtatás nélkül**. Ne módosítsd a kész, pályázat-specifikus EPTK-verzió szövegét utólag!

```
A Pohánka és Társa Kft. (Zalaegerszeg) mikrovállalkozás [FIXME: pályázati konstrukció neve]
keretében [FIXME: projekt rövid leírása, max. 500 karakter] megvalósítását tervezi.
A projekt célja: [FIXME: célok]. Összköltség: [FIXME: összeg] Ft, igényelt támogatás:
[FIXME: összeg] Ft ([FIXME: intenzitás]%). A fejlesztés eredménye: [FIXME: fő eredmény/indikátor].
```

---

*Sablon alapja: `Palyazatok/DIMOP_1_2_6/` dokumentumok és mesterdoc.md, 2026. június 26-i állapot.*

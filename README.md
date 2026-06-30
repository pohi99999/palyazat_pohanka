# Pohánka és Társa Kft. – Pályázat és Hitel Projekt

> **Célok:** DIMOP Plusz-1.2.6/B-26 (9 M Ft, 90% VNT) + Széchenyi Mikrohitel MAX+ (6 M Ft, 3%) kombinált finanszírozás a Brunella Agent System (BAS) bevezetéséhez.

---

## Projekt áttekintés

Ez a repository a **Pohánka és Társa Kft.** (adószám: 14728864-2-20) DIMOP pályázati és Széchenyi hiteligénylési dokumentációját, valamint az ezeket kiszolgáló Brunella ügynökalapú automatizálási rendszert tartalmazza.

**Kritikus határidő:** 2026. június 26. (DIMOP belső előkészítési határidő)

---

## Pohánka és Társa Kft. – Hitel és pályázat profil

### A profil JSON fájl helye

```
config/pohanka_credit_profile.json
```

Ez a fájl a `keresési referencia.md` forrásból extrahált, gépileg olvasható cég- és preferenciaprofil. Tartalmazza:

| Szekció | Tartalom |
|---------|----------|
| `company` | Cégnév, adószám, TEÁOR kódok, székhely, KIVA adózás |
| `financials` | 2023–2025 árbevétel, EBITDA, saját tőke, de minimis keret |
| `digital_profile` | DI pontszámok (IG32095-2025, IG32096-2025), DFK adatok, BAS projekt |
| `investment_plan` | Rövid (2026), közép (2027–28), hosszú (2029+) táv tervek |
| `preferences` | Preferált pályázat- és hitelkonstrukciók, kizárási listák |
| `eligibility_checks` | Ügynök által kötelezően ellenőrizendő 8 pont + rangsorolási kritériumok |

### Melyik ügynök / workflow használja?

| Fájl | Szerepe |
|------|---------|
| `src/domain/pohankaCreditProfile.py` | Domain modul – betölti a JSON-t, helper függvényeket exportál |
| `src/agents/fundingSearchAgent.py` | FundingSearchAgent – rendszer-prompt + ügynök konfiguráció |
| `src/workflows/fundingAndGrantDiscovery.py` | Teljes workflow – szűrés, rangsorolás, mentés |
| `output/pohanka_funding_candidates.json` | Legutóbbi workflow kimenet (gépileg + emberek által olvasható) |

### Hogyan bővítsd a profilt?

1. Szerkeszd a `config/pohanka_credit_profile.json` fájlt.
2. Futtasd a teszteket: `python -m pytest tests/ -v`
3. Futtasd a workflow-t az új kimenet generálásához: `python -m src.workflows.fundingAndGrantDiscovery`
4. Commitold a változásokat.

### Workflow futtatása

```powershell
# Teljes futtatás (menti az output/ könyvtárba):
python -m src.workflows.fundingAndGrantDiscovery

# Csak eredmény listázása, mentés nélkül:
python -m src.workflows.fundingAndGrantDiscovery --dry-run
```

---

## Könyvtárszerkezet

```
.
├── config/
│   └── pohanka_credit_profile.json       ← CÉG PROFIL JSON (forrásadatok)
├── src/
│   ├── domain/
│   │   └── pohankaCreditProfile.py       ← Domain modul (helper függvények)
│   ├── agents/
│   │   └── fundingSearchAgent.py         ← FundingSearchAgent konfiguráció
│   └── workflows/
│       └── fundingAndGrantDiscovery.py   ← Pályázat + hitel kereső workflow
├── output/
│   ├── pohanka_funding_candidates.json           ← Legutóbbi eredmény
│   └── pohanka_funding_candidates_YYYY-MM-DD.json ← Dátumozott verzió
├── tests/
│   └── test_pohankaCreditProfile.py      ← 29 egységteszt
├── Palyazatok/
│   └── DIMOP_1_2_6_B_2026/               ← DIMOP benyújtási dokumentumok
├── Hitelek/
│   └── Szechenyi_Mikrohitel_MAX/         ← Széchenyi hiteldokumentáció
├── docs/                                 ← PDF mellékletek (KOMA, HIPA, DI, stb.)
├── TAMOGAT/                              ← VNT pályázati sablonok
├── HITEL/                                ← Hitel sablonok
├── mesterdoc.md                          ← Mesterdokumentum (cégadatok)
├── KELL.md                               ← Emberi teendők listája
└── TARTALOM.md                           ← Projekt áttekintés és könyvtártérkép
```

---

## Tesztek futtatása

```powershell
python -m pytest tests/ -v
# Elvárt eredmény: 29 passed
```

---

## Kapcsolódó dokumentumok

- [`keresési referencia.md`](keresési%20referencia.md) – A JSON profil forrása (Brunella LLM-barát leírás)
- [`# Pohánka és Társa Kft. – Hitel- és finanszírozási.md`](%23%20Poh%C3%A1nka%20%C3%A9s%20T%C3%A1rsa%20Kft.%20%E2%80%93%20Hitel-%20%C3%A9s%20finansz%C3%ADroz%C3%A1si.md) – Részletes emberi-olvasható profil
- [`mesterdoc.md`](mesterdoc.md) – Cégadatok mesterdokumentuma
- [`TARTALOM.md`](TARTALOM.md) – Teljes projektáttekintés és könyvtártérkép

---

*Utolsó frissítés: 2026-06-30 | Brunella / GitHub Copilot*

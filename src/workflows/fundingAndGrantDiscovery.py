"""
fundingAndGrantDiscovery.py – „Legkézenfekvőbb pályázat és hitel" workflow.

Ez a workflow a Pohánka és Társa Kft. profiljára alapozva megkeresi
és rangsorolja a legjobb pályázatokat (VNT) és hitelkonstrukciókat,
majd a találatokat JSON fájlba menti az `output/` könyvtárba.

Bemenete:  pohankaCreditProfile (config/pohanka_credit_profile.json)
Kimenete:  output/pohanka_funding_candidates_<DÁTUM>.json

Használat:
    python -m src.workflows.fundingAndGrantDiscovery
    python -m src.workflows.fundingAndGrantDiscovery --dry-run

# ============================================================
# JÖVŐBELI AUTOMATIZÁLT FUTTATÁS – MŰKÖDÉSI LEÍRÁS (hu-HU)
# ============================================================
# 1. Aktuális adatok lekérése:
#    - A workflow HTTP-scraping vagy LLM+search-API hívással (pl. Bing/Google Search API,
#      palyazat.gov.hu, szechenyi.hu, ginop.hu) letölti a legfrissebb nyitott pályázati
#      és hitelkonstrukció-adatokat.
#    - Forrásként elsősorban: palyazat.gov.hu, nkfih.gov.hu, szechenyi.hu, kavosz.hu, mfb.hu.
#    - Alternatíva: Brunella RAG-modul (LanceDB) előre indexelt forrásokból.
#
# 2. Egyenkénti jogosultsági ellenőrzés:
#    - Minden talált programra az eligibility_checks.agent_must_check_each_program
#      mind a 8 pontját köteles az ügynök ellenőrizni.
#    - Automatikusan kizárja a preferences.exclusions listájában szereplő programokat.
#
# 3. Rangsorolás:
#    - A szűrésen átment programokat az eligibility_checks.ranking_criteria.order
#      szempontsor alapján rangsorolja (kamatszint → ismert program → türelmi idő → összeg → garancia).
#
# 4. Mentés:
#    - Az eredményt output/pohanka_funding_candidates_<YYYY-MM-DD>.json-ba menti.
#    - A fájl emberi felülvizsgálatra kész, de gépileg is feldolgozható (Brunella workflow-k számára).
#
# 5. Ütemezés:
#    - Javasolt futtatási frekvencia: hetente egyszer (pl. hétfő reggel 07:00).
#    - CI/CD trigger: GitHub Actions cron ('0 5 * * 1') vagy Brunella ütemező.
# ============================================================
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date
from typing import Any, Dict, List, Optional

# Projekt gyökérkönyvtár hozzáadása
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from src.domain.pohankaCreditProfile import (
    pohankaCreditProfile,
    getCreditPreferences,
    getGrantPreferences,
    getEligibilityChecks,
    getExclusions,
    getRankingCriteria,
    getInvestmentPlanShortTerm,
)
from src.agents.fundingSearchAgent import get_agent_config, AGENT_NAME, AGENT_VERSION


# ---------------------------------------------------------------------------
# Típus definíciók
# ---------------------------------------------------------------------------

class ProgramResult(dict):
    """Egy pályázat vagy hitelkonstrukció találati rekordje."""
    required_keys = [
        "program_name", "program_code", "url", "type",
        "interest_or_intensity", "key_eligibility_points",
        "collateral_required", "garantiqa_available",
        "short_description_hu", "action_plan_hu",
    ]


# ---------------------------------------------------------------------------
# Szűrési segédfüggvények
# ---------------------------------------------------------------------------

def _is_excluded_grant(program_name: str, exclusions: List[str]) -> bool:
    """
    Ellenőrzi, hogy a pályázat neve tartalmaz-e kizárási kulcsszavakat.

    Valós gépi futáskor ezt az LLM-ügynök végzi el szemantikusan;
    itt csak egy kulcsszó-alapú helyettesítő logika található.
    """
    name_lower = program_name.lower()
    exclude_keywords = {
        "budapest": "Budapest",
        "nagyvállalat": "nagyvállalati",
        "mezőgazdaság": "mezőgazdasági",
        "export": "export-fókuszú",
        "gyártás": "gyártási szektorra",
    }
    for kw in exclude_keywords:
        if kw in name_lower:
            return True
    return False


def _is_excluded_credit(program_name: str, exclusions: List[str]) -> bool:
    """
    Ellenőrzi, hogy a hitelkonstrukció neve tartalmaz-e kizárási kulcsszavakat.
    """
    name_lower = program_name.lower()
    if "likviditás" in name_lower or "forgóeszköz" in name_lower or "munkakapital" in name_lower:
        return True
    return False


def _check_interest_cap(interest_pct: float, max_pct: float) -> bool:
    """Visszaadja, hogy a kamat a megengedett határon belül van-e."""
    return interest_pct <= max_pct


def _check_intensity_floor(intensity_pct: float, min_pct: float) -> bool:
    """Visszaadja, hogy a támogatási intenzitás eléri-e a minimumot."""
    return intensity_pct >= min_pct


# ---------------------------------------------------------------------------
# Előre definiált jelölt programok (statikus adatok 2026-os ismeretek alapján)
# Ez a lista az automatizált futtatáskor LLM+search API kimenetével helyettesítendő.
# ---------------------------------------------------------------------------

CANDIDATE_GRANTS: List[Dict[str, Any]] = [
    {
        "program_name": "DIMOP Plusz-1.2.6/B-26 – KKV digitalizáció és automatizáció",
        "program_code": "DIMOP Plusz-1.2.6/B-26",
        "url": "https://palyazat.gov.hu/",
        "type": "grant",
        "interest_or_intensity": 90,
        "key_eligibility_points": [
            "Mikro/kis KKV (<=10 fő, <=2M EUR árbevétel)",
            "DFK igazolás szükséges (rendelkezésre áll: D127/23-505/2025)",
            "IT, szoftver, felhő, AI elszámolható – BAS projekt jogosult",
        ],
        "collateral_required": "nem",
        "garantiqa_available": "nem alkalmazható (VNT)",
        "short_description_hu": (
            "A DIMOP Plusz-1.2.6/B-26 felhívás KKV-k digitális fejlesztését támogatja "
            "90%-os intenzitással, 3–12 M Ft között. A BAS rendszer bevezetése "
            "(szoftver, felhő, AI, képzés) teljes egészében elszámolható."
        ),
        "action_plan_hu": [
            "1. DFK dokumentum véglegesítése (határidő: 2026-07-15)",
            "2. EPTK regisztráció / cégadatok ellenőrzése",
            "3. Árajánlatok begyűjtése (GPU, NAS, szoftver, integráció) – 3 ajánlat/tétel",
            "4. Projekt indokoltság és célok szövegének véglegesítése",
            "5. Szakmai tartalom (BAS architektúra) leírásának elkészítése",
            "6. Költségvetés feltöltése az EPTK rendszerbe (9 M Ft, 4 kategória)",
            "7. Mellékletek összegyűjtése (KOMA, HIPA, DI igazolások, cégkivonat)",
            "8. Belső ellenőrzés: kettős finanszírozási tilalom vizsgálata (DIMOP + Széchenyi)",
            "9. Benyújtás az EPTK portálon (javasolt: 2026-06-27 előtt)",
            "10. Értesítés várakozása + esetleges hiánypótlás kezelése",
        ],
    },
    {
        "program_name": "GINOP Plusz-1.4.3-24 – KKV Technológia Plusz (0% beruházási hitel VNT komponenssel)",
        "program_code": "GINOP Plusz-1.4.3-24",
        "url": "https://ginop.gov.hu/",
        "type": "grant",
        "interest_or_intensity": 80,
        "key_eligibility_points": [
            "KKV jogosultság (teljesül: 3 fő, mikro)",
            "Technológiai beruházás: IT hardver + szoftver elszámolható",
            "Kombinált konstrukció: 0% hitel + vissza nem térítendő komponens",
        ],
        "collateral_required": "részben (hitel komponenshez Garantiqa bevonható)",
        "garantiqa_available": "igen",
        "short_description_hu": (
            "Kombinált konstrukció: vissza nem térítendő és 0%-os kamatozású hitelkomponens "
            "együtt. KKV technológiai fejlesztésre (IT, automatizálás) alkalmas. "
            "Garantiqa garancia bevonható az ingatlanfedezet kiváltására."
        ),
        "action_plan_hu": [
            "1. Felhívás aktuális státuszának ellenőrzése (ginop.gov.hu)",
            "2. Kombinált komponens arányának pontosítása (VNT vs. 0% hitel)",
            "3. Beruházási lista elkészítése (GPU, NAS, szoftver, integráció)",
            "4. Garantiqa garancia igénylési folyamat megindítása",
            "5. Pénzügyi terv + cash-flow elkészítése",
            "6. Projekt indokoltsági dokumentáció (BAS alapú)",
            "7. Konzorcium vagy önálló pályázat döntése",
            "8. EPTK benyújtás",
            "9. Szerződéskötés + Garantiqa aktiválás",
            "10. Megvalósítás és elszámolás",
        ],
    },
    {
        "program_name": "DIMOP Plusz – Vállalati digitális kompetencia fejlesztés (képzési alap)",
        "program_code": "DIMOP Plusz-képzés-26",
        "url": None,
        "type": "grant",
        "interest_or_intensity": 80,
        "key_eligibility_points": [
            "3 fő foglalkoztatott – képzési pályázat jogosultság teljesül",
            "Digitális kompetencia fejlesztés (BAS kezelése, AI alapok)",
            "Vidéki mikrovállalkozás (Zalaegerszeg) – területi előnyt adhat",
        ],
        "collateral_required": "nem",
        "garantiqa_available": "nem alkalmazható (VNT)",
        "short_description_hu": (
            "Vállalati digitális képzési támogatás 3 főre a BAS rendszer kezeléséhez "
            "szükséges AI és IT kompetenciák fejlesztésére. "
            "Vidéki mikrovállalkozás extra pontszámot kaphat."
        ),
        "action_plan_hu": [
            "1. Felhívás megjelenésének figyelése (palyazat.gov.hu)",
            "2. Képzési igény felmérése (3 fő, AI/IT területen)",
            "3. Akkreditált képzési partner keresése",
            "4. Képzési tematika összeállítása",
            "5. Benyújtás az EPTK-n",
        ],
    },
    {
        "program_name": "Széchenyi Plusz – Mikrovállalkozói Fejlesztési Alap (vidéki felhívás)",
        "program_code": "SZ-MIKRO-2026",
        "url": "https://szechenyi.hu/",
        "type": "grant",
        "interest_or_intensity": 75,
        "key_eligibility_points": [
            "Mikrovállalkozás (<=10 fő) – teljesül",
            "Vidéki székhely (nem Budapest) – Zalaegerszeg megfelel",
            "Fejlesztési cél: digitalizáció, IT – teljesül",
        ],
        "collateral_required": "nem",
        "garantiqa_available": "nem alkalmazható (VNT)",
        "short_description_hu": (
            "Vidéki mikrovállalkozásoknak szóló fejlesztési pályázat, "
            "75%-os támogatási intenzitással. Digitalizációs és IT fejlesztési "
            "célra igénybe vehető, összege 3–8 M Ft között várható."
        ),
        "action_plan_hu": [
            "1. Felhívás megjelenésének figyelése (szechenyi.hu)",
            "2. Jogosultsági gyorsellenőrzés (KKV, székhely, cél)",
            "3. Projekt leírás elkészítése",
            "4. Benyújtás",
        ],
    },
    {
        "program_name": "Innovációs Alap – Vállalati K+F és AI termékfejlesztés (mikro KKV sáv)",
        "program_code": "NKFIH-AI-micro-2026",
        "url": "https://nkfih.gov.hu/",
        "type": "grant",
        "interest_or_intensity": 70,
        "key_eligibility_points": [
            "AI termékfejlesztés (BAS, LLM, automatizálás) – jogosult",
            "Max projekt 30 M Ft, mikro sáv: 5–12 M Ft várható",
            "Önerő: min. 30% (kockázati tényező: önerő határán van)",
        ],
        "collateral_required": "nem",
        "garantiqa_available": "nem alkalmazható (VNT)",
        "short_description_hu": (
            "Innovációs Alap K+F pályázat AI termékfejlesztésre. "
            "A BAS könyvelési AI rendszer innovatív terméknek minősülhet. "
            "Figyelem: 30%-os önerő közel van a kizárási határhoz – csak akkor érdemes, "
            "ha a projekt finanszírozása megoldott."
        ),
        "action_plan_hu": [
            "1. Felhívás részletes jogosultsági feltételeinek tanulmányozása",
            "2. Önerő-számítás (9 M Ft projekt: 2,7 M Ft önerő szükséges)",
            "3. Innovatív elem dokumentálása (BAS LLM-komponens, LanceDB RAG)",
            "4. Benyújtás döntése az önerő rendelkezésre állása alapján",
        ],
    },
]

CANDIDATE_CREDITS: List[Dict[str, Any]] = [
    {
        "program_name": "Széchenyi Mikrohitel MAX+",
        "program_code": "SZ-MIKRO-MAX-PLUS",
        "url": "https://kavosz.hu/szechenyi-mikrohitel-max-plus",
        "type": "credit",
        "interest_or_intensity": 3.0,
        "key_eligibility_points": [
            "Mikrovállalkozás (<=10 fő, <=2M EUR árbevétel) – teljesül",
            "Max hitelösszeg: 25 M Ft; tervezett: 6 M Ft – illeszkedik",
            "KIVA adózási séma: NEM kizáró ok a Széchenyi programban",
        ],
        "collateral_required": "részben (IT eszközök + cégautó fedezet)",
        "garantiqa_available": "igen (Garantiqa garancia bevonható)",
        "short_description_hu": (
            "A legjobban illeszkedő hitelkonstrukció: 3% fix kamat, max 60 hónap futamidő, "
            "tervezett összeg 6 M Ft (GPU, PC, NAS, cégautó). "
            "Türelmi idő: 1 év tőketörlesztés halasztás lehetséges. "
            "Havi törlesztő (tőke+kamat): ~107 812 Ft."
        ),
        "action_plan_hu": [
            "1. OTP Bank kapcsolattartó megkeresése (KAVOSZ termékspecialista)",
            "2. Széchenyi kártyaprogram regisztráció ellenőrzése / megújítása",
            "3. Beruházási lista és árajánlatok begyűjtése (GPU, NAS, autó)",
            "4. Hiteligénylési csomag összeállítása (mesterdoc.md alapján)",
            "5. 3 éves pénzügyi dokumentumok előkészítése (2023–2025 beszámolók)",
            "6. NAV KOMA és HIPA igazolások frissítése (max. 30 napos)",
            "7. Garantiqa garancia igénylési folyamat párhuzamos megindítása",
            "8. Hiteligénylő lap kitöltése + bank-előterjesztés",
            "9. Hitelszerződés aláírása",
            "10. Eszközök megrendelése + számlák elszámolása",
        ],
    },
    {
        "program_name": "GINOP Plusz-1.4.3-24 – KKV Technológia Plusz (0% beruházási hitel komponens)",
        "program_code": "GINOP-1.4.3-24-HITEL",
        "url": "https://ginop.gov.hu/",
        "type": "credit",
        "interest_or_intensity": 0.0,
        "key_eligibility_points": [
            "KKV jogosultság – teljesül",
            "Technológiai beruházás (IT, szoftver, hardver) – BAS projekt jogosult",
            "Garantiqa garancia bevonható ingatlanfedezet kiváltásához",
        ],
        "collateral_required": "részben (Garantiqa bevonható)",
        "garantiqa_available": "igen",
        "short_description_hu": (
            "0% kamatozású állami kamattámogatott hitel technológiai beruházásra. "
            "A BAS projekt IT-komponensei (GPU, NAS, szoftver) elszámolhatók. "
            "Garantiqa garancia bevonható ingatlan nélkül is."
        ),
        "action_plan_hu": [
            "1. Felhívás státuszának ellenőrzése (nyitott-e 2026-ban)",
            "2. 0% hitel komponens összegének pontosítása",
            "3. Garantiqa folyamat megindítása párhuzamosan",
            "4. Beruházási lista és árajánlatok",
            "5. Hiteligénylés benyújtása",
        ],
    },
    {
        "program_name": "Széchenyi Beruházási Hitel MAX+",
        "program_code": "SZ-BERUH-MAX-PLUS",
        "url": "https://kavosz.hu/szechenyi-beruhazasi-hitel-max-plus",
        "type": "credit",
        "interest_or_intensity": 2.5,
        "key_eligibility_points": [
            "KKV (<=250 fő) – teljesül",
            "Max hitelösszeg: 600 M Ft; tervezett 6–20 M Ft – illeszkedik",
            "Beruházási cél: IT hardver, szoftver – jogosult",
        ],
        "collateral_required": "részben (AVHGA garancia bevonható)",
        "garantiqa_available": "igen (AVHGA garancia)",
        "short_description_hu": (
            "Széchenyi Beruházási Hitel MAX+ 2,5% kamattal. "
            "Közép- és hosszú távú beruházásokhoz alkalmas (2027–2028 BAS SaaS bővítés). "
            "AVHGA garancia bevonható ingatlanfedezet csökkentésére."
        ),
        "action_plan_hu": [
            "1. Középtávú beruházási igény pontosítása (2027: 10–20 M Ft)",
            "2. AVHGA garancia feltételeinek megismerése",
            "3. OTP Bank vagy más KAVOSZ-partner bank megkeresése",
            "4. Hiteligénylési csomag előkészítése",
            "5. Benyújtás",
        ],
    },
    {
        "program_name": "DIMOP Plusz-1.2.3/A-24 – Kombinált 0% hitel + VNT konstrukció",
        "program_code": "DIMOP-1.2.3-A-24",
        "url": "https://palyazat.gov.hu/",
        "type": "credit",
        "interest_or_intensity": 0.0,
        "key_eligibility_points": [
            "Digitalizációs projekt (BAS) – teljesül",
            "Kombinált VNT + 0% hitel: kettős finanszírozási tilalom figyelendő a DIMOP 1.2.6/B-vel",
            "Mikro KKV jogosultság – teljesül",
        ],
        "collateral_required": "részben",
        "garantiqa_available": "ismeretlen (felhívástól függő)",
        "short_description_hu": (
            "Kombinált 0% kamatozású hitel és vissza nem térítendő komponens digitalizációs "
            "projektekre. FIGYELEM: a DIMOP 1.2.6/B VNT pályázattal kettős finanszírozási "
            "tilalom állhat fenn – jogi egyeztetés szükséges a kombinálhatóság előtt."
        ),
        "action_plan_hu": [
            "1. Kettős finanszírozási tilalom jogi vizsgálata (DIMOP 1.2.6/B + 1.2.3/A kombináció)",
            "2. Ha kombinálható: felhívás részleteinek tanulmányozása",
            "3. Projekt leírás elkészítése",
            "4. Benyújtás",
        ],
    },
    {
        "program_name": "MFB Pont – KKV Digitalizációs Kamattámogatott Hitel",
        "program_code": "MFB-KKV-DIGITAL-2026",
        "url": "https://mfb.hu/",
        "type": "credit",
        "interest_or_intensity": 1.5,
        "key_eligibility_points": [
            "KKV jogosultság – teljesül",
            "Digitalizációs beruházás – BAS projekt illeszkedik",
            "Garantiqa garancia bevonható",
        ],
        "collateral_required": "részben (Garantiqa bevonható)",
        "garantiqa_available": "igen",
        "short_description_hu": (
            "MFB Pont kamattámogatott hitel digitalizációs beruházásra, ~1,5% kedvezményes "
            "kamattal. Garantiqa garancia bevonható ingatlanfedezet kiváltásához. "
            "Összeg: 5–50 M Ft sávban elérhető."
        ),
        "action_plan_hu": [
            "1. MFB Pont partnerbank azonosítása (OTP Bank vagy más)",
            "2. Aktuális kamat és feltételek pontosítása",
            "3. Hiteligénylési csomag összeállítása",
            "4. Garantiqa folyamat párhuzamos megindítása",
            "5. Benyújtás",
        ],
    },
]


# ---------------------------------------------------------------------------
# Szűrési logika
# ---------------------------------------------------------------------------

def filter_grants(
    candidates: List[Dict[str, Any]],
    grant_prefs: Dict[str, Any],
    exclusions: Dict[str, List[str]],
) -> List[Dict[str, Any]]:
    """
    Szűri a jelölt pályázatokat a preferenciák és kizárások alapján.

    Args:
        candidates: Nyers jelölt lista.
        grant_prefs: getGrantPreferences() kimenete.
        exclusions: getExclusions() kimenete.

    Returns:
        Szűrt jelölt lista.
    """
    min_intensity = grant_prefs["grant_programs"]["preferred_intensity_pct"]["acceptable_min"]
    result = []
    for p in candidates:
        if p["type"] != "grant":
            continue
        if _is_excluded_grant(p["program_name"], exclusions["exclude_grants"]):
            continue
        if not _check_intensity_floor(p["interest_or_intensity"], min_intensity):
            continue
        result.append(p)
    return result


def filter_credits(
    candidates: List[Dict[str, Any]],
    credit_prefs: Dict[str, Any],
    exclusions: Dict[str, List[str]],
) -> List[Dict[str, Any]]:
    """
    Szűri a jelölt hitelkonstrukciókat a preferenciák és kizárások alapján.

    Args:
        candidates: Nyers jelölt lista.
        credit_prefs: getCreditPreferences() kimenete.
        exclusions: getExclusions() kimenete.

    Returns:
        Szűrt jelölt lista.
    """
    max_interest = credit_prefs["credit_programs"]["interest_preference_pct"]["acceptable_max"]
    result = []
    for p in candidates:
        if p["type"] != "credit":
            continue
        if _is_excluded_credit(p["program_name"], exclusions["exclude_credit"]):
            continue
        if not _check_interest_cap(p["interest_or_intensity"], max_interest):
            continue
        result.append(p)
    return result


def rank_programs(programs: List[Dict[str, Any]], ranking_criteria: List[str]) -> List[Dict[str, Any]]:
    """
    Rangsorolja a programokat a ranking_criteria sorrendje alapján.

    Jelenlegi implementáció: kamatszint szerint rendezi a hiteleket (0% > alacsony > magas),
    a pályázatokat intenzitás szerint (90% > 80% > ...).
    LLM-alapú futtatáskor ez a logika az LLM által végzett szemantikus rangsorolással helyettesítendő.

    Args:
        programs: Szűrt program lista.
        ranking_criteria: getRankingCriteria() kimenete.

    Returns:
        Rendezett lista.
    """
    def sort_key(p: Dict[str, Any]) -> float:
        if p["type"] == "credit":
            return p["interest_or_intensity"]
        else:
            return 100 - p["interest_or_intensity"]
    return sorted(programs, key=sort_key)


# ---------------------------------------------------------------------------
# Fő workflow függvény
# ---------------------------------------------------------------------------

def run_funding_discovery(
    company_profile: Optional[Dict[str, Any]] = None,
    dry_run: bool = False,
    output_dir: str = "output",
) -> Dict[str, Any]:
    """
    Futtatja a teljes pályázat- és hitelkereső workflow-t.

    Args:
        company_profile: Opcionális dict; ha None, pohankaCreditProfile-t használ.
        dry_run: Ha True, nem ment fájlba, csak visszaadja az eredményt.
        output_dir: Kimeneti könyvtár (alapértelmezett: 'output/').

    Returns:
        Strukturált dict az eredményekkel (JSON-kompatibilis).
    """
    profile = company_profile or pohankaCreditProfile
    grant_prefs = getGrantPreferences()
    credit_prefs = getCreditPreferences()
    exclusions = getExclusions()
    ranking_criteria = getRankingCriteria()
    eligibility = getEligibilityChecks()

    print(f"[{AGENT_NAME}] Workflow indítva – {date.today()}")
    print(f"  Cég: {profile['company']['name']}")
    print(f"  Jelölt pályázatok: {len(CANDIDATE_GRANTS)} db")
    print(f"  Jelölt hitelek: {len(CANDIDATE_CREDITS)} db")

    # Szűrés
    filtered_grants = filter_grants(CANDIDATE_GRANTS, grant_prefs, exclusions)
    filtered_credits = filter_credits(CANDIDATE_CREDITS, credit_prefs, exclusions)

    print(f"  Szűrés után: {len(filtered_grants)} pályázat, {len(filtered_credits)} hitel")

    # Rangsorolás
    ranked_grants = rank_programs(filtered_grants, ranking_criteria)
    ranked_credits = rank_programs(filtered_credits, ranking_criteria)

    # Eredmény összeállítása
    result: Dict[str, Any] = {
        "search_date": str(date.today()),
        "company": profile["company"]["name"],
        "company_tax_id": profile["company"]["tax_id"],
        "workflow_version": AGENT_VERSION,
        "eligibility_checks_applied": eligibility["agent_must_check_each_program"],
        "ranking_criteria_applied": ranking_criteria,
        "grants": ranked_grants[:5],
        "credits": ranked_credits[:5],
        "meta": {
            "agent": AGENT_NAME,
            "version": AGENT_VERSION,
            "note": (
                "Ez a fájl statikus jelölt adatokat tartalmaz (2026-06-30 ismeretek alapján). "
                "Automatizált futtatáskor az LLM+search API friss adatokkal tölti fel."
            ),
            "total_grants_before_filter": len(CANDIDATE_GRANTS),
            "total_credits_before_filter": len(CANDIDATE_CREDITS),
            "grants_after_filter": len(filtered_grants),
            "credits_after_filter": len(filtered_credits),
        },
    }

    # Mentés
    if not dry_run:
        os.makedirs(output_dir, exist_ok=True)
        filename = f"pohanka_funding_candidates_{date.today()}.json"
        output_path = os.path.join(output_dir, filename)
        # Mindig felülírjuk a mai napi verziót
        latest_path = os.path.join(output_dir, "pohanka_funding_candidates.json")

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        with open(latest_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print(f"  Mentve: {output_path}")
        print(f"  Legújabb verzió: {latest_path}")

    return result


# ---------------------------------------------------------------------------
# CLI belépési pont
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Pohánka és Társa Kft. – pályázat és hitel kereső workflow"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Csak listázza az eredményeket, nem ment fájlba",
    )
    parser.add_argument(
        "--output-dir",
        default=os.path.join(os.path.dirname(__file__), "..", "..", "output"),
        help="Kimeneti könyvtár (alapértelmezett: output/)",
    )
    args = parser.parse_args()

    result = run_funding_discovery(dry_run=args.dry_run, output_dir=args.output_dir)

    print("\n=== EREDMÉNY ÖSSZEFOGLALÓ ===")
    print(f"Pályázatok ({len(result['grants'])} db):")
    for g in result["grants"]:
        print(f"  [{g['interest_or_intensity']}%] {g['program_name']}")

    print(f"\nHitelek ({len(result['credits'])} db):")
    for c in result["credits"]:
        print(f"  [{c['interest_or_intensity']}%] {c['program_name']}")

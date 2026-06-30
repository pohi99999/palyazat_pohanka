"""
Pohánka és Társa Kft. – Hitel- és pályázat profil betöltő modul.

Ez a modul betölti a `config/pohanka_credit_profile.json` fájlt,
és typed helper-függvényeket exportál Brunella ügynökök és workflow-k számára.

Használat:
    from src.domain.pohankaCreditProfile import pohankaCreditProfile
    from src.domain.pohankaCreditProfile import getCreditPreferences, getGrantPreferences
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


# ---------------------------------------------------------------------------
# Fájl elérési útja
# ---------------------------------------------------------------------------

_PROFILE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "config", "pohanka_credit_profile.json"
)


def _load_profile() -> Dict[str, Any]:
    """Betölti a JSON profilt a config/ könyvtárból."""
    abs_path = os.path.abspath(_PROFILE_PATH)
    with open(abs_path, encoding="utf-8") as f:
        return json.load(f)


# Egyszeri betöltés – singleton
pohankaCreditProfile: Dict[str, Any] = _load_profile()


# ---------------------------------------------------------------------------
# Helper függvények
# ---------------------------------------------------------------------------

def getCreditPreferences() -> Dict[str, Any]:
    """
    Visszaadja a hitelpreferenciákat.

    Tartalmazza:
    - priority_order: preferált hitelkonstrukciók sorrendben
    - interest_preference_pct: ideális (0%) és maximálisan elfogadható (3%) kamat
    - amount_preference_huf: összeg-sávok (rövid/közép/hosszú táv)
    - grace_period: türelmi idő preferenciák
    - collateral: fedezeti preferenciák (Garantiqa, AVHGA)
    - exclude_credit: kizárandó hitelkonstrukciók
    """
    prefs = pohankaCreditProfile["preferences"]
    return {
        "credit_programs": prefs["credit_programs"],
        "collateral": prefs["collateral"],
        "exclude_credit": prefs["exclusions"]["exclude_credit"],
    }


def getGrantPreferences() -> Dict[str, Any]:
    """
    Visszaadja a pályázati (VNT/támogatás) preferenciákat.

    Tartalmazza:
    - preferred_types: preferált pályázattípusok
    - preferred_intensity_pct: ideális (90%) és minimálisan elfogadható (70%) intenzitás
    - amount_ranges_huf: összeg-sávok
    - exclude_grants: kizárandó pályázattípusok
    """
    prefs = pohankaCreditProfile["preferences"]
    return {
        "grant_programs": prefs["grant_programs"],
        "exclude_grants": prefs["exclusions"]["exclude_grants"],
    }


def getEligibilityChecks() -> Dict[str, Any]:
    """
    Visszaadja a jogosultsági ellenőrzési paramétereket.

    Az ügynök ezeket köteles minden programra egyenként ellenőrizni:
    - company_params_for_agent: a cég aktuális paraméterei (régió, létszám, árbevétel stb.)
    - agent_must_check_each_program: 8 pontból álló kötelező ellenőrző lista
    - ranking_criteria: rangsorolási szabályok sorrendben
    """
    return pohankaCreditProfile["eligibility_checks"]


def getInvestmentPlanShortTerm() -> Dict[str, Any]:
    """
    Visszaadja a rövid távú (2026) beruházási tervet.

    Tartalmazza a DIMOP projekt és a Széchenyi hitelkeret részleteit.
    """
    return pohankaCreditProfile["investment_plan"]["short_term_2026"]


def getInvestmentPlanMidTerm() -> Dict[str, Any]:
    """
    Visszaadja a közép távú (2027–2028) beruházási tervet.

    Tartalmazza a tervezett hitelösszeg-sávot és felhasználási célokat.
    """
    return pohankaCreditProfile["investment_plan"]["mid_term_2027_2028"]


def getInvestmentPlanLongTerm() -> Dict[str, Any]:
    """
    Visszaadja a hosszú távú (2029+) beruházási tervet.

    BAS SaaS skálázási terveket tartalmaz.
    """
    return pohankaCreditProfile["investment_plan"]["long_term_2029_plus"]


def getCompanyMetadata() -> Dict[str, Any]:
    """Visszaadja a cégadatokat (tax_id, TEÁOR, székhely, adózási séma stb.)."""
    return pohankaCreditProfile["company"]


def getFinancials() -> Dict[str, Any]:
    """Visszaadja a 2023–2025 pénzügyi adatokat és a de minimis státuszt."""
    return pohankaCreditProfile["financials"]


def getDigitalProfile() -> Dict[str, Any]:
    """
    Visszaadja a digitalizációs profilt.

    Tartalmazza a DI pontszámokat (cég: 10 pont, közösségi: 8 pont),
    a DFK adatokat és a BAS core-projekt várható hatásait.
    """
    return pohankaCreditProfile["digital_profile"]


def getRankingCriteria() -> List[str]:
    """
    Visszaadja a rangsorolási szempontokat sorrendben.

    Az ügynök ezek alapján rangsorolja a talált programokat.
    """
    return pohankaCreditProfile["eligibility_checks"]["ranking_criteria"]["order"]


def getExclusions() -> Dict[str, List[str]]:
    """
    Visszaadja a kizárási listákat (hitelek + pályázatok).

    Az ügynök köteles ezeket szűrési feltételként alkalmazni.
    """
    return pohankaCreditProfile["preferences"]["exclusions"]

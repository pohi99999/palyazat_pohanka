"""
FundingSearchAgent – Brunella pályázat- és hitelkereső ügynök.

Ez az ügynök a Pohánka és Társa Kft. profiljára alapozva keres
vissza nem térítendő támogatásokat (VNT/pályázatokat) és
kamattámogatott hitelkonstrukciókat.

Az ügynök a `pohankaCreditProfile`-t használja `company_profile`-ként,
és az alábbi szűrési + rangsorolási logikát alkalmazza:
  1. preferences.grant_programs / credit_programs → preferált típusok
  2. eligibility_checks.agent_must_check_each_program → 8 kötelező ellenőrzési pont
  3. eligibility_checks.ranking_criteria.order → végső rangsor

Emberi felhasználók számára szóló kimenetek magyarul jelennek meg.
"""

from __future__ import annotations

import json
import sys
import os
from datetime import date
from typing import Any, Dict, List, Optional

# Projekt gyökérkönyvtár hozzáadása a sys.path-hoz
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from src.domain.pohankaCreditProfile import (
    pohankaCreditProfile,
    getCreditPreferences,
    getGrantPreferences,
    getEligibilityChecks,
    getExclusions,
    getRankingCriteria,
)


# ---------------------------------------------------------------------------
# Ügynök konfigurációs struktúra
# ---------------------------------------------------------------------------

AGENT_NAME = "FundingSearchAgent"
AGENT_VERSION = "1.0.0"
AGENT_LANGUAGE = "hu-HU"

# Az ügynök fő rendszer-promptja (Brunella LLM motornak átadva)
SYSTEM_PROMPT_TEMPLATE = """\
Te egy magyar nyelvű pályázat- és hitelkereső AI ügynök vagy, aki a Pohánka és Társa Kft. \
számára keres vissza nem térítendő támogatásokat és kamattámogatott hitelkonstrukciókat.

## Cégprofil (company_profile)
{company_profile_json}

## Feladatod
1. Keress **5 db VNT/pályázatot** (DIMOP, GINOP, képzési programok stb.) amelyek:
   - Illeszkednek a `preferences.grant_programs.preferred_types` listához.
   - Megfelelnek az `eligibility_checks.company_params_for_agent` feltételeinek.
   - NEM szerepelnek az `preferences.exclusions.exclude_grants` listában.
   - Támogatási intenzitásuk >= {min_grant_intensity_pct}%.

2. Keress **5 db kamattámogatott hitelkonstrukciót** amelyek:
   - Illeszkednek a `preferences.credit_programs.priority_order` sorrendhez.
   - Kamatuk <= {max_interest_pct}%/év.
   - Összegük a `preferences.credit_programs.amount_preference_huf.short_term` sávban van.
   - NEM szerepelnek az `preferences.exclusions.exclude_credit` listában.

3. Minden találatnál rögzítsd:
   - program_name, program_code, url (ha ismert)
   - type: "grant" VAGY "credit"
   - interest_or_intensity: kamatszint % vagy támogatási intenzitás %
   - key_eligibility_points: a legfontosabb 3 jogosultsági feltétel
   - collateral_required: ingatlanfedezet kötelező-e (igen/nem/részben)
   - garantiqa_available: Garantiqa/AVHGA bevonható-e (igen/nem/ismeretlen)
   - short_description_hu: 2–3 mondatos magyar leírás
   - action_plan_hu: 5–10 lépéses akcióterv magyarul (határidők, dokumentumok, kapcsolattartók)

4. Kötelező ellenőrzési pontok minden programnál:
{eligibility_checklist}

5. Rangsorolási sorrend (a végső listában):
{ranking_criteria}

## Kimeneti formátum
Válaszolj JSON struktúrában, az alábbi sémával:
{{
  "search_date": "YYYY-MM-DD",
  "company": "Pohánka és Társa Kft.",
  "grants": [ {{ ... }} ],
  "credits": [ {{ ... }} ],
  "meta": {{
    "agent": "{agent_name}",
    "version": "{agent_version}",
    "notes": "..."
  }}
}}

## Fontos megszorítások
- Csak olyan programokat adj meg, amelyeket 2026-ban aktívnak tudsz azonosítani.
- Ha egy program URL-je nem ismert, írd: "url": null.
- Ha egy ellenőrzési pont nem teljesül, a programot NE szerepeltesd az eredményben.
- A `short_description_hu` és `action_plan_hu` mezők tartalma mindig MAGYAR NYELVŰ legyen.
"""


def build_system_prompt(company_profile: Dict[str, Any] | None = None) -> str:
    """
    Összeállítja az ügynök rendszer-promptját a cég profiljával.

    Args:
        company_profile: Opcionális dict; ha None, a pohankaCreditProfile-t használja.

    Returns:
        Kitöltött rendszer-prompt string, amit az LLM motornak kell átadni.
    """
    profile = company_profile or pohankaCreditProfile
    eligibility = getEligibilityChecks()
    grant_prefs = getGrantPreferences()
    credit_prefs = getCreditPreferences()

    eligibility_checklist = "\n".join(
        f"   {i+1}. {item}"
        for i, item in enumerate(eligibility["agent_must_check_each_program"])
    )
    ranking = "\n".join(
        f"   {i+1}. {item}"
        for i, item in enumerate(eligibility["ranking_criteria"]["order"])
    )

    min_intensity = grant_prefs["grant_programs"]["preferred_intensity_pct"]["acceptable_min"]
    max_interest = credit_prefs["credit_programs"]["interest_preference_pct"]["acceptable_max"]

    return SYSTEM_PROMPT_TEMPLATE.format(
        company_profile_json=json.dumps(profile, ensure_ascii=False, indent=2),
        min_grant_intensity_pct=min_intensity,
        max_interest_pct=max_interest,
        eligibility_checklist=eligibility_checklist,
        ranking_criteria=ranking,
        agent_name=AGENT_NAME,
        agent_version=AGENT_VERSION,
    )


def get_agent_config() -> Dict[str, Any]:
    """
    Visszaadja az ügynök teljes konfigurációját dict formátumban.

    Ez az objektum átadható a Brunella orchestrator-nak vagy
    más LLM-integrációnak (pl. LangChain, AutoGen, FastAPI endpoint).
    """
    eligibility = getEligibilityChecks()
    grant_prefs = getGrantPreferences()
    credit_prefs = getCreditPreferences()

    return {
        "agent_name": AGENT_NAME,
        "version": AGENT_VERSION,
        "language": AGENT_LANGUAGE,
        "company_profile": pohankaCreditProfile,
        "system_prompt": build_system_prompt(),
        "search_parameters": {
            "grant_search": {
                "preferred_types": grant_prefs["grant_programs"]["preferred_types"],
                "min_intensity_pct": grant_prefs["grant_programs"]["preferred_intensity_pct"]["acceptable_min"],
                "amount_range_huf": grant_prefs["grant_programs"]["amount_ranges_huf"]["short_term"],
                "exclude_grants": grant_prefs["exclude_grants"],
            },
            "credit_search": {
                "priority_order": credit_prefs["credit_programs"]["priority_order"],
                "max_interest_pct": credit_prefs["credit_programs"]["interest_preference_pct"]["acceptable_max"],
                "amount_range_huf": credit_prefs["credit_programs"]["amount_preference_huf"]["short_term"],
                "exclude_credit": credit_prefs["exclude_credit"],
                "preferred_guarantee": credit_prefs["collateral"]["preferred_guarantee"],
            },
        },
        "eligibility_checks": eligibility["agent_must_check_each_program"],
        "ranking_criteria": eligibility["ranking_criteria"]["order"],
        "output_schema": {
            "search_date": "YYYY-MM-DD",
            "company": "Pohánka és Társa Kft.",
            "grants": "List[GrantResult]",
            "credits": "List[CreditResult]",
            "meta": {"agent": AGENT_NAME, "version": AGENT_VERSION},
        },
    }


if __name__ == "__main__":
    # Gyors tesztelési parancs: python -m src.agents.fundingSearchAgent
    config = get_agent_config()
    print(f"[{AGENT_NAME} v{AGENT_VERSION}] Konfiguráció betöltve.")
    print(f"  Pályázati kizárások: {len(config['search_parameters']['grant_search']['exclude_grants'])} db")
    print(f"  Hitelkizárások: {len(config['search_parameters']['credit_search']['exclude_credit'])} db")
    print(f"  Kötelező ellenőrzési pontok: {len(config['eligibility_checks'])} db")
    print(f"  Rangsorolási szempontok: {len(config['ranking_criteria'])} db")
    print("\nRendszer-prompt első 300 karaktere:")
    print(config["system_prompt"][:300] + "...")

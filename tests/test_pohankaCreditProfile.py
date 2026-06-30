"""
tests/test_pohankaCreditProfile.py

Tesztek a pohanka_credit_profile.json és a kapcsolódó Python modulok validálásához.

Futtatás:
    python -m pytest tests/test_pohankaCreditProfile.py -v
    # vagy pytest nélkül:
    python tests/test_pohankaCreditProfile.py
"""

from __future__ import annotations

import json
import os
import sys
import unittest

# Projekt gyökér hozzáadása
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.domain.pohankaCreditProfile import (
    pohankaCreditProfile,
    getCreditPreferences,
    getGrantPreferences,
    getEligibilityChecks,
    getExclusions,
    getRankingCriteria,
    getInvestmentPlanShortTerm,
    getInvestmentPlanMidTerm,
    getInvestmentPlanLongTerm,
    getCompanyMetadata,
    getFinancials,
    getDigitalProfile,
)
from src.workflows.fundingAndGrantDiscovery import (
    filter_grants,
    filter_credits,
    rank_programs,
    CANDIDATE_GRANTS,
    CANDIDATE_CREDITS,
)


class TestProfileLoad(unittest.TestCase):
    """Tesztek: a JSON profil betöltése és szerkezete."""

    def test_profile_is_dict(self):
        """A profil dict típusú."""
        self.assertIsInstance(pohankaCreditProfile, dict)

    def test_required_top_level_keys(self):
        """Minden kötelező főszintű kulcs megtalálható."""
        required = ["company", "financials", "digital_profile",
                    "investment_plan", "preferences", "eligibility_checks"]
        for key in required:
            self.assertIn(key, pohankaCreditProfile, f"Hiányzó kulcs: {key}")

    def test_company_name(self):
        """A cégnév helyes."""
        self.assertEqual(
            pohankaCreditProfile["company"]["name"],
            "Pohánka és Társa Kft."
        )

    def test_tax_id(self):
        """Az adószám helyes."""
        self.assertEqual(pohankaCreditProfile["company"]["tax_id"], "14728864-2-20")

    def test_financials_has_three_years(self):
        """Három év pénzügyi adata van (2023–2025)."""
        years = pohankaCreditProfile["financials"]["years"]
        self.assertEqual(len(years), 3)
        year_numbers = [y["year"] for y in years]
        self.assertIn(2023, year_numbers)
        self.assertIn(2024, year_numbers)
        self.assertIn(2025, year_numbers)

    def test_tevor_codes_count(self):
        """Legalább 4 TEÁOR kód van bejegyezve."""
        codes = pohankaCreditProfile["company"]["tevor_codes"]
        self.assertGreaterEqual(len(codes), 4)

    def test_di_score(self):
        """A vállalati DI pontszám 10."""
        self.assertEqual(pohankaCreditProfile["digital_profile"]["di_company"]["score"], 10)

    def test_dfk_valid_until(self):
        """A DFK érvényességi ideje 2026-11-30."""
        self.assertEqual(
            pohankaCreditProfile["digital_profile"]["dfk"]["valid_until"],
            "2026-11-30"
        )

    def test_no_vnt_used(self):
        """Korábban nem volt VNT támogatás igénybe véve."""
        self.assertFalse(pohankaCreditProfile["financials"]["previous_grants"]["vnt_used"])

    def test_de_minimis_remaining(self):
        """De minimis keret: 200 000 EUR."""
        self.assertEqual(
            pohankaCreditProfile["financials"]["previous_grants"]["de_minimis_remaining_eur"],
            200000
        )


class TestHelperFunctions(unittest.TestCase):
    """Tesztek: helper függvények visszatérési értékei."""

    def test_getCreditPreferences_keys(self):
        """getCreditPreferences() tartalmazza a szükséges kulcsokat."""
        prefs = getCreditPreferences()
        self.assertIn("credit_programs", prefs)
        self.assertIn("collateral", prefs)
        self.assertIn("exclude_credit", prefs)

    def test_getGrantPreferences_keys(self):
        """getGrantPreferences() tartalmazza a szükséges kulcsokat."""
        prefs = getGrantPreferences()
        self.assertIn("grant_programs", prefs)
        self.assertIn("exclude_grants", prefs)

    def test_getEligibilityChecks_has_eight_items(self):
        """Az ügynök 8 kötelező ellenőrzési pontot tartalmaz."""
        checks = getEligibilityChecks()
        self.assertEqual(len(checks["agent_must_check_each_program"]), 8)

    def test_getRankingCriteria_is_list(self):
        """A rangsorolási kritériumok lista típusúak."""
        criteria = getRankingCriteria()
        self.assertIsInstance(criteria, list)
        self.assertGreater(len(criteria), 0)

    def test_getExclusions_keys(self):
        """Az exclusions dict tartalmaz exclude_credit és exclude_grants kulcsokat."""
        excl = getExclusions()
        self.assertIn("exclude_credit", excl)
        self.assertIn("exclude_grants", excl)

    def test_getInvestmentPlanShortTerm_dimop(self):
        """A rövid távú terv tartalmazza a DIMOP projektet."""
        plan = getInvestmentPlanShortTerm()
        self.assertIn("dimop_project", plan)
        self.assertEqual(plan["dimop_project"]["total_value_huf"], 9000000)

    def test_getInvestmentPlanShortTerm_szechenyi(self):
        """A rövid távú terv tartalmazza a Széchenyi hitelt."""
        plan = getInvestmentPlanShortTerm()
        self.assertIn("szechenyi_credit", plan)
        self.assertEqual(plan["szechenyi_credit"]["planned_amount_huf"], 6000000)

    def test_getCompanyMetadata_sme_class(self):
        """A cég mikrovállalkozásnak van besorolva."""
        meta = getCompanyMetadata()
        self.assertEqual(meta["sme_class"], "micro")

    def test_getFinancials_debt_free(self):
        """A cég adósságmentes."""
        fin = getFinancials()
        self.assertTrue(fin["debt_free"])


class TestFilterFunctions(unittest.TestCase):
    """Tesztek: szűrési logika (kizárások alkalmazása)."""

    def setUp(self):
        self.grant_prefs = getGrantPreferences()
        self.credit_prefs = getCreditPreferences()
        self.exclusions = getExclusions()
        self.ranking_criteria = getRankingCriteria()

    def test_filter_excludes_budapest_grants(self):
        """Budapest-fókuszú pályázatot kizár."""
        budapest_grant = {
            "program_name": "Budapest-fókuszú digitalizáció felhívás",
            "type": "grant",
            "interest_or_intensity": 90,
        }
        result = filter_grants([budapest_grant], self.grant_prefs, self.exclusions)
        self.assertEqual(len(result), 0, "Budapest pályázatnak szűrve kellett volna lenni")

    def test_filter_excludes_low_intensity_grants(self):
        """Alacsony intenzitású (<70%) pályázatot kizár."""
        low_intensity = {
            "program_name": "Általános fejlesztés",
            "type": "grant",
            "interest_or_intensity": 60,
        }
        result = filter_grants([low_intensity], self.grant_prefs, self.exclusions)
        self.assertEqual(len(result), 0, "60%-os intenzitású pályázatnak szűrve kellett volna lenni")

    def test_filter_keeps_valid_grant(self):
        """Érvényes pályázatot megtart."""
        valid_grant = {
            "program_name": "KKV Digitalizáció és AI fejlesztés",
            "type": "grant",
            "interest_or_intensity": 90,
        }
        result = filter_grants([valid_grant], self.grant_prefs, self.exclusions)
        self.assertEqual(len(result), 1)

    def test_filter_excludes_forgóeszköz_credit(self):
        """Forgóeszköz-hitelt kizár."""
        forgóeszköz = {
            "program_name": "Széchenyi Likviditási forgóeszköz hitel",
            "type": "credit",
            "interest_or_intensity": 2.0,
        }
        result = filter_credits([forgóeszköz], self.credit_prefs, self.exclusions)
        self.assertEqual(len(result), 0, "Forgóeszköz hitelt ki kellett volna szűrni")

    def test_filter_excludes_high_interest_credit(self):
        """Magas kamatozású (>3%) hitelt kizár."""
        high_interest = {
            "program_name": "Piaci Hitel 5%",
            "type": "credit",
            "interest_or_intensity": 5.0,
        }
        result = filter_credits([high_interest], self.credit_prefs, self.exclusions)
        self.assertEqual(len(result), 0, "5%-os kamatozású hitel szűrve kellett volna lenni")

    def test_filter_keeps_valid_credit(self):
        """Érvényes hitelkonstrukciót megtart."""
        valid_credit = {
            "program_name": "Széchenyi Mikrohitel MAX+ beruházási célra",
            "type": "credit",
            "interest_or_intensity": 3.0,
        }
        result = filter_credits([valid_credit], self.credit_prefs, self.exclusions)
        self.assertEqual(len(result), 1)

    def test_candidate_grants_pass_filter(self):
        """A beépített jelölt pályázatok közül legalább 1 átmegy a szűrőn."""
        result = filter_grants(CANDIDATE_GRANTS, self.grant_prefs, self.exclusions)
        self.assertGreater(len(result), 0, "Legalább 1 jelölt pályázatnak szűrőn kellene átmennie")

    def test_candidate_credits_pass_filter(self):
        """A beépített jelölt hitelek közül legalább 1 átmegy a szűrőn."""
        result = filter_credits(CANDIDATE_CREDITS, self.credit_prefs, self.exclusions)
        self.assertGreater(len(result), 0, "Legalább 1 jelölt hitelnek szűrőn kellene átmennie")

    def test_rank_credits_by_interest(self):
        """A hitelek kamat szerint vannak rendezve (legolcsóbb első)."""
        credits = filter_credits(CANDIDATE_CREDITS, self.credit_prefs, self.exclusions)
        ranked = rank_programs(credits, self.ranking_criteria)
        if len(ranked) >= 2:
            self.assertLessEqual(
                ranked[0]["interest_or_intensity"],
                ranked[1]["interest_or_intensity"],
                "Az első hitel kamatának alacsonyabbnak kell lennie a másodikénál",
            )

    def test_json_profile_valid(self):
        """A config/pohanka_credit_profile.json érvényes JSON."""
        profile_path = os.path.join(
            os.path.dirname(__file__), "..", "config", "pohanka_credit_profile.json"
        )
        with open(os.path.abspath(profile_path), encoding="utf-8") as f:
            data = json.load(f)
        self.assertIsInstance(data, dict)
        self.assertIn("company", data)


if __name__ == "__main__":
    # Pytest nélkül is futtatható: python tests/test_pohankaCreditProfile.py
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=os.path.dirname(__file__), pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)

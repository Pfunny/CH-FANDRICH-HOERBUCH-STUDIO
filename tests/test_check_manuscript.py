import unittest
from scripts.check_manuscript import inspect

class ManuscriptChecks(unittest.TestCase):
    def test_roles_and_chapters(self):
        report = inspect("Kapitel 6 – Die erste Prüfung\n**Erzähler:** Es begann.\n**Elias:** Hallo.\nMira: Guten Morgen.")
        self.assertEqual(report["chapters"][0]["number"], 6)
        self.assertEqual(report["roles"]["Erzähler"], 1)
        self.assertEqual(report["roles"]["Elias"], 1)
        self.assertEqual(report["roles"]["Mira"], 1)
        self.assertFalse(report["warnings"])

    def test_duplicate(self):
        report = inspect("Kapitel 1\nErzähler: Eins.\nKapitel 1\nErzähler: Zwei.")
        self.assertTrue(any(w["type"] == "duplicate_chapter" for w in report["warnings"]))

    def test_empty_role(self):
        report = inspect("Elias:")
        self.assertTrue(any(w["type"] == "empty_role" for w in report["warnings"]))

if __name__ == "__main__":
    unittest.main()

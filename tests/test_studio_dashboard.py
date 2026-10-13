"""Static smoke tests for the single-file Android studio."""
import pathlib
import re
import unittest
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")

class StudioParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])

class DashboardTests(unittest.TestCase):
    def test_required_dashboard_elements(self):
        p = StudioParser()
        p.feed(HTML)
        for name in ("dashChapters", "dashWords", "dashRoles", "dashDuration", "speakerList", "txt", "list", "book", "author"):
            self.assertIn(name, p.ids)
        self.assertEqual(len(p.ids), len(set(p.ids)), "Duplicate HTML IDs")

    def test_workflow_and_version(self):
        self.assertIn("kokoro-local.yml", HTML)
        self.assertIn("Hörbuch Studio 13.0", HTML)
        self.assertIn("speakerAssignments", HTML)

    def test_no_old_openai_model(self):
        self.assertNotIn("gpt-4o-mini-tts", HTML)
        self.assertNotIn("AUDIOVORBEREITUNG · VERSION 12", HTML)

    def test_kokoro_settings_transfer(self):
        self.assertIn("copyKokoroSettings", HTML)
        self.assertIn("pronunciationRules", HTML)

    def test_script_functions(self):
        for fn in ("extractRoles", "updateDashboard", "renderSpeakers", "exportTTSJob", "importFile", "render"):
            self.assertRegex(HTML, r"function\s+" + fn + r"\s*\(")

if __name__ == "__main__":
    unittest.main()

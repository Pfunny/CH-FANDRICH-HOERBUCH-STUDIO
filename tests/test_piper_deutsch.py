import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
from piper_deutsch import VOICES, model_urls


class PiperGermanVoicesTest(unittest.TestCase):
    def test_five_presets(self):
        self.assertEqual(len(VOICES), 5)

    def test_model_urls_are_german(self):
        for voice in VOICES:
            model, config = model_urls(voice)
            self.assertIn("/de/de_DE/", model)
            self.assertTrue(model.endswith(".onnx"))
            self.assertEqual(config, model + ".json")

    def test_unknown_voice_rejected(self):
        with self.assertRaises(ValueError):
            model_urls("unsafe-name")


if __name__ == "__main__":
    unittest.main()

"""Piper-TTS: deutsches Hörbuch als MP3 (GitHub Actions)."""
import os
import pathlib
import re
import subprocess
import urllib.request

VOICES = {
    "thorsten-low": ("thorsten", "low"),
    "thorsten-medium": ("thorsten", "medium"),
    "thorsten-high": ("thorsten", "high"),
    "pavoque-low": ("pavoque", "low"),
    "ramona-low": ("ramona", "low"),
}
BASE = "https://huggingface.co/rhasspy/piper-voices/resolve/main/de/de_DE"


def model_urls(voice):
    if voice not in VOICES:
        raise ValueError("Unbekannte deutsche Piper-Stimme")
    name, quality = VOICES[voice]
    stem = f"de_DE-{name}-{quality}"
    return f"{BASE}/{name}/{quality}/{stem}.onnx", f"{BASE}/{name}/{quality}/{stem}.onnx.json"


def main():
    voice = os.environ.get("VOICE", "thorsten-medium")
    model_url, config_url = model_urls(voice)
    text = os.environ.get("INPUT_TEXT", "").strip()
    if not text or len(text) > 18000:
        raise SystemExit("Bitte einen Text mit 1 bis 18000 Zeichen eingeben.")
    safe = re.sub(r"[^A-Za-z0-9_-]+", "_", os.environ.get("FILENAME", "piper-deutsch")).strip("_") or "piper-deutsch"
    folder = pathlib.Path("output")
    folder.mkdir(exist_ok=True)
    model = folder / "voice.onnx"
    for url, target in ((model_url, model), (config_url, folder / "voice.onnx.json")):
        print("Lade deutsches Stimmmodell:", url)
        urllib.request.urlretrieve(url, target)
        if target.stat().st_size < 100:
            raise RuntimeError("Stimmmodell-Download fehlgeschlagen")
    wav = folder / "voice.wav"
    subprocess.run(
        ["piper", "--model", str(model), "--output_file", str(wav)],
        input=text, text=True, check=True, timeout=900,
    )
    if not wav.exists() or wav.stat().st_size < 1000:
        raise RuntimeError("Piper hat keine gültige WAV-Datei erzeugt")
    mp3 = folder / f"{safe}.mp3"
    subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(wav),
         "-af", "loudnorm=I=-19:LRA=7:TP=-2", "-codec:a", "libmp3lame",
         "-b:a", "192k", str(mp3)],
        check=True, timeout=300,
    )
    print("Deutsches MP3 erzeugt:", mp3, mp3.stat().st_size, "Bytes")


if __name__ == "__main__":
    main()

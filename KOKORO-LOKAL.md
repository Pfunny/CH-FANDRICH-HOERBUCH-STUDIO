# CH.FANDRICH Hörbuchstudio – Kokoro Lokal

Dieser Modus ist für lokale, selbst gehostete Sprachsynthese gedacht. Er benötigt kein Gemini-Tageskontingent und kein OpenAI-TTS-Guthaben.

## Start

Voraussetzung: Docker Desktop bzw. Docker Engine.

```bash
docker compose -f docker-compose.kokoro.yml up -d
```

Danach läuft KokoroTTS lokal unter Port 7860. Die Modelldaten werden im Docker-Volume `kokorotts_data` gespeichert.

## Architektur

- GitHub bleibt Quellcode und Versionsverwaltung.
- KokoroTTS läuft auf dem eigenen Rechner/Server.
- Gemini Cloud bleibt optional.
- FFmpeg übernimmt MP3, Kapitel und Mastering.

## Wichtig

Ein normaler GitHub-hosted Actions Runner kann den lokalen Kokoro-Dienst auf deinem eigenen Rechner nicht direkt erreichen. Für echte lokale Produktion wird der Hörbuch-Workflow deshalb als nächster Schritt auf einen selbst gehosteten GitHub Actions Runner bzw. einen lokalen Studio-Start umgestellt.

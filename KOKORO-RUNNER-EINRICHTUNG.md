# Kokoro Local Runner – Einrichtung

Der Kokoro-Workflow läuft auf deinem eigenen Rechner oder Server. Dadurch hängt die eigentliche Sprachsynthese nicht von einem Gemini-Tageskontingent ab.

## 1. Kokoro starten

```bash
docker compose -f docker-compose.kokoro.yml up -d
```

## 2. GitHub self-hosted Runner registrieren

Öffne im Repository:

**Settings → Actions → Runners → New self-hosted runner**

Wähle das Betriebssystem deines Rechners und führe die von GitHub angezeigten Installationsbefehle aus.

Bei der Runner-Konfiguration muss zusätzlich das Label **kokoro** gesetzt werden. Der Workflow verlangt deshalb:

```yaml
runs-on: [self-hosted, kokoro]
```

## 3. Voraussetzungen auf dem Runner

- Docker / Docker Desktop
- FFmpeg
- curl
- Python 3
- laufender KokoroTTS-Dienst auf `127.0.0.1:7860`

## 4. Produktion

Unter **Actions → Hörbuch Kokoro Lokal → Run workflow** Text, Stimme und Dateiname eingeben.

Die fertige MP3 erscheint anschließend als GitHub Actions Artifact.

## Sicherheit

Für Kokoro lokal ist kein Gemini- oder OpenAI-API-Schlüssel erforderlich. Der self-hosted Runner sollte nur für vertrauenswürdige Workflows aus diesem privaten/eigenen Repository verwendet werden.

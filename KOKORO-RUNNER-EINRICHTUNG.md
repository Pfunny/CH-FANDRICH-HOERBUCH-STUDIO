# Kokoro Cloud – Handy/Browser

Der Kokoro-Hörbuchworkflow läuft vollständig auf einem GitHub-gehosteten Linux-Runner.

## Bedienung

1. GitHub im Handy-Browser oder in der App öffnen.
2. **Actions → Hörbuch Kokoro Cloud** wählen.
3. **Run workflow / Workflow ausführen** öffnen.
4. Text, Kokoro-Stimme und Dateiname eintragen.
5. Nach Abschluss das Artifact **kokoro-hoerbuch-audio** herunterladen.

## Technik

Der Workflow startet KokoroTTS als Docker-Service direkt innerhalb des GitHub Actions Runners und erzeugt anschließend eine MP3 mit FFmpeg.

Damit ist kein eigener PC, kein Self-hosted Runner und kein Gemini-API-Schlüssel für diesen Workflow erforderlich.

## Grenzen

Die TTS-Erzeugung selbst verwendet kein Gemini-Tageskontingent. Die Ausführung unterliegt jedoch weiterhin den Nutzungs-/Minuten-/Ressourcengrenzen von GitHub Actions und der verfügbaren CPU/RAM-Leistung des GitHub-Runners.

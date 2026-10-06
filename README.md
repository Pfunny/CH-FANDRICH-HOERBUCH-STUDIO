# CH.FANDRICH Hörbuch Studio

Mobile, GitHub-basierte Web-App zur Vorbereitung und Produktion von Hörbuchprojekten.

## Version 8.0
- alle Funktionen aus Version 7
- echte KI-Spracherzeugung über GitHub Actions
- geschützter API-Zugriff über GitHub Secret `OPENAI_API_KEY`
- Kapiteltext → MP3
- wählbare Sprecherstimme im Workflow
- MP3 als GitHub-Actions-Artefakt
- automatische Secret-Prüfung vor der Erzeugung
- keine API-Schlüssel in GitHub Pages oder im Browsercode

## Einmalige Einrichtung
1. Repository öffnen.
2. Settings → Secrets and variables → Actions öffnen.
3. New repository secret wählen.
4. Name: `OPENAI_API_KEY`.
5. Eigenen OpenAI API-Schlüssel als Wert speichern.

## Hörbuch erzeugen
1. Actions → Hörbuch TTS öffnen.
2. Run workflow wählen.
3. Kapiteltext und Dateiname eintragen.
4. Stimme auswählen und Workflow starten.
5. Nach Abschluss das erzeugte MP3-Artefakt herunterladen.

## Sicherheit
Das Studio wird ausschließlich über GitHub entwickelt. Der API-Schlüssel gehört ausschließlich in GitHub Secrets und niemals in `index.html`, JavaScript, README oder andere öffentliche Repository-Dateien.

Autor: Christopher Fandrich

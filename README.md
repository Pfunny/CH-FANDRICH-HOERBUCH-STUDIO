# CH.FANDRICH Hörbuch Studio

Mobile, GitHub-basierte Web-App zur Vorbereitung und Produktion von Hörbuchprojekten.

## Version 8.0
- Manuskript-Import für TXT und Markdown
- automatische Kapitelerkennung und Kapitelverwaltung
- Wort-, Zeichen- und Laufzeitschätzung
- Browser-Sprachausgabe mit Stimmenauswahl
- Tempo- und Tonhöhensteuerung
- Sprecherprofile: Warm, Erzähler, Fantasy, Abenteuer
- Aussprachekorrekturen und Absatzpausen
- Produktionsprüfung und Fortschritt
- Smartphone-Mikrofonaufnahme
- Kapitel-Audio für MP3, WAV und M4A
- lokales Speichern und JSON-Projektexport
- integrierte TTS-Auftragserstellung
- sicherer GitHub-Actions-Sprachgenerator
- OpenAI GPT-4o Mini TTS
- MP3- oder WAV-Ausgabe als GitHub-Actions-Artefakt

## Sprachgenerator einrichten
1. Im Repository unter Settings → Secrets and variables → Actions ein Repository Secret mit dem Namen `OPENAI_API_KEY` anlegen.
2. GitHub Actions → „Hörbuch Sprachgenerator“ öffnen.
3. „Run workflow“ wählen.
4. Text, Stimme, Format und Dateiname festlegen.
5. Nach erfolgreichem Lauf das Artefakt `hoerbuch-audio` herunterladen.

Der API-Schlüssel wird ausschließlich als GitHub Actions Secret verwendet und niemals in GitHub Pages oder im Browsercode gespeichert.

## Sicherheit
Das Studio wird ausschließlich über GitHub entwickelt. Keine API-Geheimnisse werden in der öffentlichen Website gespeichert.

Autor: Christopher Fandrich

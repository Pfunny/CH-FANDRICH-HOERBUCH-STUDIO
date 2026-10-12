# Hörbuch Studio – Qualitätsprüfung (Entwicklungsstand 11)

Diese Erweiterung wird **im bestehenden Repository** entwickelt. Der bisherige Web-Editor und Kokoro-Workflow bleiben unverändert.

## Was geprüft wird
- Sprecherzeilen wie `**Elias:** Text` oder `Erzähler: Text`
- leere Sprecherzeilen, sehr lange Textzeilen
- Kapitelnummern, Reihenfolge und Duplikate
- Wörter, geschätzte Vorlesezeit und verwendete Rollen

## Anwendung
```bash
python3 scripts/check_manuscript.py kapitel.txt
python3 scripts/check_manuscript.py kapitel.txt --json
python3 scripts/check_manuscript.py kapitel.txt --strict
```

Die Prüfung ist **kein Audiogenerator**. Sie arbeitet ohne API-Schlüssel, ohne externe Pakete und verändert keine Manuskriptdatei.

## Festgestellte technische Risiken im bisherigen Studio
1. Der Kokoro-Parser erkennt fett formatierte Rollenpräfixe (`**Elias:**`) bislang nicht zuverlässig. Vor einer vollständigen Hörbuchproduktion muss der Parser korrigiert werden.
2. Die Weboberfläche verweist teilweise auf den älteren OpenAI-TTS-Workflow statt auf Kokoro.
3. Der Browser-Testknopf „KI-Hörprobe“ verwendet `speechSynthesis`, nicht Kokoro; das muss in der Oberfläche deutlich gekennzeichnet werden.
4. Die Weboberfläche hat einen lokalen Projekt-Export, aber keinen direkten sicheren GitHub-Workflow-Start mit Manuskript-Upload.
5. Die Dokumentation nennt Version 8, während die Oberfläche Version 10 anzeigt.

## Sicheres weiteres Vorgehen
Zuerst diese Prüfung als Grundlage testen. Danach Kokoro-Rollenparser, Produktionsgrenzen und Android-Oberfläche gezielt überarbeiten. Keine API-Schlüssel im Browser hinterlegen; keine produktiven Dateien ungeprüft überschreiben.

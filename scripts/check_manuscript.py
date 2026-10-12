#!/usr/bin/env python3
"""Dependency-free manuscript quality check for CH.FANDRICH Hörbuch Studio."""
import argparse
import json
import re
import sys
from pathlib import Path

ROLE = re.compile(r"^\s*(?:\*\*)?([\wÄÖÜäöüß][\wÄÖÜäöüß .-]{0,39}):(?:\*\*)?\s*(.*)$")
CHAPTER = re.compile(r"^\s*(?:#{1,3}\s*)?Kapitel\s+(\d+)(?:\s*[-–—:]\s*(.*))?\s*$", re.I)
STAGE = re.compile(r"^\s*\[(?:Pause|Musik|Geräusch|SFX|Regie)[^\]]*\]\s*$", re.I)

def inspect(text):
    warnings, roles, chapters = [], {}, []
    previous = None
    for number, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if not s or s == "---" or STAGE.match(s):
            continue
        c = CHAPTER.match(s)
        if c:
            chapters.append({"number": int(c.group(1)), "title": c.group(2) or "", "line": number})
            previous = None
            continue
        m = ROLE.match(s)
        if m:
            role, spoken = m.groups()
            roles[role] = roles.get(role, 0) + 1
            if not spoken.strip():
                warnings.append({"line": number, "type": "empty_role", "message": f"Leerer Sprechertext: {role}"})
            previous = role
        elif previous is None and s.startswith(("**", "[")):
            warnings.append({"line": number, "type": "format", "message": "Mögliche Regieanweisung oder unerkannter Sprecher"})
        if len(s) > 1200:
            warnings.append({"line": number, "type": "long_line", "message": "Sehr lange Zeile: vor TTS in Abschnitte teilen"})
    numbers = [c["number"] for c in chapters]
    if len(numbers) != len(set(numbers)):
        warnings.append({"line": 0, "type": "duplicate_chapter", "message": "Kapitelnummer doppelt"})
    if numbers and numbers != sorted(numbers):
        warnings.append({"line": 0, "type": "chapter_order", "message": "Kapitel nicht aufsteigend"})
    if not text.strip():
        warnings.append({"line": 0, "type": "empty", "message": "Manuskript leer"})
    return {"words": len(text.split()), "estimated_minutes_at_140_wpm": round(len(text.split()) / 140, 1),
            "chapters": chapters, "roles": roles, "warnings": warnings}

def main():
    p = argparse.ArgumentParser(description="Hörbuch-Manuskript vor der Produktion prüfen")
    p.add_argument("file", type=Path)
    p.add_argument("--json", action="store_true")
    p.add_argument("--strict", action="store_true", help="Warnungen führen zu Exit-Code 1")
    args = p.parse_args()
    result = inspect(args.file.read_text(encoding="utf-8-sig"))
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Wörter: {result['words']} | Dauer ca.: {result['estimated_minutes_at_140_wpm']} Min.")
        print("Rollen:", ", ".join(f"{k} ({v})" for k,v in result["roles"].items()) or "keine")
        print("Kapitel:", len(result["chapters"]))
        for w in result["warnings"]:
            print(f"Warnung Zeile {w['line']}: {w['message']}")
    return 1 if args.strict and result["warnings"] else 0

if __name__ == "__main__":
    sys.exit(main())

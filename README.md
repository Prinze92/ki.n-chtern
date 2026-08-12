# ki.nüchtern — Content-Repository

Faceless, deutschsprachiger Instagram-Account über KI.
**Positionierung:** *Der nüchterne Übersetzer* — KI-Themen für normale Menschen, ohne Hype, ohne Panik, mit Quelle.

Dieses Repository ist die **einzige Quelle der Wahrheit** für alles, was der Account produziert:
Konzept, Design-System, jeder einzelne Post (Text + Quellen + gerenderte Bilder), die Themen-Pipeline
und der Nachweis, was wann veröffentlicht wurde.

---

## Verzeichnisstruktur

```
insta_ai/
├── README.md              ← du bist hier
├── CLAUDE.md              ← Arbeitsregeln für die Weiterarbeit (verbindlich)
│
├── docs/                  ← Strategie & Referenz (ändert sich selten)
│   ├── konzept.md         Positionierung, Content-Säulen, Erfolgsmessung
│   ├── handoff.md         Original-Briefing (Stand 11.08.2026)
│   └── design-system.md   Farben, Schriften, Layout-Regeln, Markenversprechen
│
├── brand/                 ← wiederverwendbare Marken-Assets
│   ├── fonts/             Schriftdateien (Google Fonts, kommerziell nutzbar)
│   └── logo/              Profilbild, Wortmarke, Bildmarke
│
├── posts/                 ← ein Ordner pro Post + zwei Register
│   ├── posts.yaml         ← MASCHINEN-Register: Status & Kennzahlen aller Posts
│   ├── POSTS.md           ← MENSCH-Register: dieselbe Übersicht zum Lesen
│   └── post-XYZ-slug/
│       ├── post.md        Blatt-Texte, Caption, Alt-Text, Hashtags
│       ├── sources.md     Quellen mit Belastbarkeits-Bewertung
│       └── slides/        gerenderte PNGs (nach dem Posten → archive/)
│
├── archive/               ← GEPOSTETE Posts: eingefrorener, veröffentlichter Stand
│   └── post-XYZ-slug/     gleiche Struktur; wird nicht mehr neu gerendert
│
├── research/              ← wie wir entscheiden, was wir posten
│   ├── ideas.md           Themen-Backlog (Pipeline), nach Säule sortiert
│   ├── TEMPLATE-post.md   Vorlage für jeden neuen Post
│   └── sources/           wiederverwendbare, geprüfte Quellen-Bibliothek
│
└── render/                ← das Rendering-Werkzeug (Python + Pillow)
    └── build_slides.py    erzeugt Logo + Blätter (Anpassung nötig, s. u.)
```

---

## „Was ist schon gepostet?" — immer beantwortbar

Zwei Register, die **immer** den aktuellen Stand halten:

1. **`posts/posts.yaml`** — maschinenlesbar. Jeder Post mit Status
   (`idee → entwurf → gerendert → geprüft → geplant → gepostet`), Veröffentlichungsdatum,
   Säule und — nach dem Posten — den Kennzahlen (v. a. *Sends per Reach*).
   Vor jedem neuen Thema hier prüfen, ob es schon behandelt wurde.

2. **`posts/POSTS.md`** — dieselbe Tabelle für Menschen.

Zusätzlich ist **jeder Post-Ordner selbst das Archiv**: `slides/*.png` sind die tatsächlich
veröffentlichten Bilder, unter Git versioniert. Nichts wird stillschweigend gelöscht — Korrekturen
werden als neuer Commit sichtbar gemacht (passt zur Markenpositionierung „wir korrigieren offen").

## „Wie recherchieren wir, was wir posten?" — der Weg

Siehe **`research/ideas.md`** (Backlog) und **`CLAUDE.md`** (Recherche-Regeln). Kurz:

1. Idee entsteht → landet in `research/ideas.md` mit Säule und grober Stoßrichtung.
2. Recherche **an Primärquellen** (EUR-Lex, Bundesagentur für Arbeit, Destatis, Amtsblätter),
   nicht an Aggregatoren. Jede Zahl bekommt eine Fundstelle.
3. Quellen werden in `research/sources/` gesammelt und als **belastbar** oder **ungeprüft**
   markiert. Ungeprüftes darf nicht in einen Post.
4. Aus einer reifen Idee wird mit `research/TEMPLATE-post.md` ein Post-Entwurf.

---

## Rendering — läuft lokal

Voraussetzung einmalig: virtuelle Umgebung + Pillow (venv liegt unter `.venv/`, ist gitignored):

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install Pillow
```

Schriften liegen im Repo unter `brand/fonts/` (Oswald, Archivo, JetBrains Mono — alle OFL,
kommerziell nutzbar). Rendern:

```powershell
.venv\Scripts\python.exe render\build_slides.py
```

Erzeugt Logo (`brand/logo/`) und alle Blätter von Post 1 (`posts/post-001-…/slides/`).
`render/build_slides.py` sucht Schriften über `find_font()` (erst `brand/fonts/`, dann OS-Fonts),
Ausgabe-Pfade sind repo-relativ.

Das Korrekturzeichen wird über die gemessene Textunterkante positioniert (`textbbox`), sitzt also
fontunabhängig sauber unter der Wortmarke — ein Font-Wechsel bricht die Logo-Geometrie nicht mehr.

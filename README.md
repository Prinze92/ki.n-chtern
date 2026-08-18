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

## Morgen-Briefing — wie die Automatisierung verdrahtet ist

Jeden Morgen um 07:00 Uhr Berliner Zeit (05:00 UTC) läuft ein Auftrag, der recherchiert, ein Briefing
nach `research/briefing/JJJJ-MM-TT.md` schreibt, bis zu zwei Posts fertig baut und auf `master` pusht.

**Der entscheidende Punkt:** Ein geplanter Lauf startet in einem frischen Container. Ohne angehängtes
Repository liegen dort weder `CLAUDE.md` noch `posts.yaml` noch der Renderer, und pushen kann er auch
nicht, weil die Zugangsdaten am Repository hängen. Genau daran sind die Läufe am 14.08. und 17.08.2026
gescheitert, beide ohne jedes Ergebnis.

Die Falle dabei: `create_trigger` kennt **kein Feld für eine Quelle**. Ein dort übergebenes `source_url`
wird stillschweigend verworfen, ohne Fehlermeldung. Nur `create_session` speichert eine Quelle.

**Die Lösung:** Der Trigger startet keine frische Sitzung, sondern feuert über `persistent_session_id`
in eine feste Sitzung, die mit Quelle angelegt wurde.

| | |
|---|---|
| Trigger | `trig_01MvPqjhCdY8njNe3hLy3VzN`, cron `0 5 * * *` (UTC) |
| Feste Sitzung | `session_01FW9e3XTkBD2oo1xBGMB8iP`, Modell Opus 5 |
| Am 17.08.2026 belegt | Ein per Trigger gestarteter Lauf hat Repo, Schreibrechte und Push |

**Diese Sitzung nicht archivieren.** Der Trigger hängt daran. Sie heißt deshalb in der Übersicht
„Produktionssitzung Morgen-Briefing (NICHT archivieren)".

**Zwei Sicherungen stecken im Auftragstext.** Ein Schritt 0 prüft vor allem anderen, ob `CLAUDE.md` und
`posts/posts.yaml` da sind, und bricht sonst sofort mit „ABBRUCH: Repository nicht vorhanden" ab, statt
Zeit ins Leere zu arbeiten. Am Ende vergleicht eine Push-Kontrolle `git log origin/master -1` mit dem
lokalen HEAD, damit kein Lauf Erfolg meldet, ohne dass etwas angekommen ist.

**Container-Neustart über Nacht: geklärt am 18.08.2026.** Der erste echte Morgenlauf hat um 05:01 UTC
gefeuert und um 05:27 UTC gepusht, mit Briefing und zwei fertigen Posts. Das Repository war da. Die
feste Sitzung übersteht die Nacht also.

**Was weiter offen ist.** Eine feste Sitzung sammelt mit jedem Lauf Verlauf an. Wenn die Ergebnisse mit
der Zeit schlechter werden, gehört die Sitzung neu aufgesetzt und der Trigger auf die neue ID gezogen.
Der Auftragstext liegt dafür unter `research/morgen-briefing-auftrag.md`. Falls der Weg über die feste
Sitzung doch einmal ausfällt, lässt sich dieselbe Aufgabe in der Weboberfläche auf claude.ai/code
einrichten, wo sie fest an ein Repository gebunden wird.


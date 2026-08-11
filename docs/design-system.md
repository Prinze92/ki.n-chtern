# Design-System — ki.nüchtern

Stand: 11.08.2026. Verbindlich für jeden Post. Quelle der Umsetzung: `render/build_slides.py`.

## Logo

Wortmarke **„ki"** in schmaler Groteske, darunter das **rote Korrekturzeichen** (Einfügezeichen aus
dem Korrektorat, Bedeutung: *hier fehlt etwas*). Zwei Striche, funktioniert als 40-px-Profilbild.

Dateien (unter `brand/logo/`): `profilbild_hell.png`, `profilbild_dunkel.png`, `wortmarke.png`, `bildmarke_pur.png`

## Bildsprache: „Aktenblatt"

Bewusst **gegen** den Nischenstandard (schwarz, dramatische Filmstills, Versalien-Overlays). Begründung:
Dieser Stil erzeugt Dringlichkeit durch Bildsprache statt durch Inhalt und widerspricht der Positionierung;
zusätzlich urheber- und persönlichkeitsrechtlich riskant.

**Visuelle Signatur:** die durchgestrichene Falschangabe mit roter Korrektur daneben (siehe Post 1, Blatt 04).

> Anmerkung zur Historie: Das ältere Konzeptpapier (`docs/konzept.md`) beschrieb noch einen dunklen Hintergrund.
> Überschrieben durch das spätere „Aktenblatt"-System (heller Papierton). Es gilt das Aktenblatt.

## Design-Tokens

| Token | Hex | Verwendung |
|-------|-----|------------|
| PAPER | `#F3F1EB` | Hintergrund |
| INK   | `#14141A` | Text |
| RED   | `#C4302B` | Korrekturrot — nur Korrekturen, Zahlen, Akzente |
| MUTED | `#8A8880` | Sekundärtext, Metadaten |
| RULE  | `#CECAC0` | Linien |
| PANEL | `#E9E6DE` | Belegkasten |

## Layout

- Format **1080 × 1350** (4:5), Rand **100 px**
- **Kopfzeile:** Doppellinie, Korrekturzeichen + `KI.NÜCHTERN` (Mono Bold), rechts `BLATT 01/09`
- **Fußzeile:** Haarlinie, `STAND TT.MM.JJJJ` links, `QUELLEN → BLATT 09` rechts
- **Kicker pro Blatt:** Mono Bold in Rot, darunter kurzer roter Strich
- Max. **20 Wörter** pro Blatt, Hook max. **10**
- **Alt-Text** immer mit Schlagworten füllen (Instagram-Suche + Google-Indexierung)
- **Kein KI-generiertes Bildmaterial.** Falls doch: kennzeichnen (Art. 50 AI Act, gilt seit 02.08.2026)

## Blattdramaturgie (Standard, 8–9 Blätter)

Hook → Der Fall → Was überall steht → Die Korrektur → Der Beleg → Der Haken →
Was das für dich heißt → Die offene Frage → Quellen

## Schriften

- **Aktueller Stand:** DejaVu Sans / Condensed / Mono — nur Platzhalter (offline gerendert).
- **Offene Aufgabe:** Umstellung auf **Oswald** oder **Archivo Narrow** (Headlines) und
  **JetBrains Mono** oder **IBM Plex Mono** (Mono). Alle vier: Google Fonts, kostenlos, kommerziell nutzbar.
  Dateien nach `brand/fonts/` legen und `render/build_slides.py` auf repo-relative Pfade umstellen.

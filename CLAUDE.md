# Arbeitsregeln — ki.nüchtern

Verbindliche Regeln für die Arbeit an diesem Projekt. Diese Datei wird bei jeder Session gelesen.

## Grundhaltung (aus dem Briefing, nicht verhandelbar)

- **Fakten immer prüfen, nie aus Annahmen ableiten.** Ungeprüftes ausdrücklich als solches kennzeichnen.
- **Nicht zustimmen, nur weil es gewünscht ist.** Bei abweichender Faktenlage widersprechen.
- **Unsicherheit offenlegen.** Keine erfundenen Zahlen, Daten, Paragrafen oder Quellen.
- **Annahmen als Annahmen markieren.**
- **Quellen nennen und ihre Belastbarkeit bewerten.** Originalquellen vor Aggregatoren.
- **Lücken, Risiken und Denkfehler ungefragt ansprechen.**
- **Kurz und präzise.** Kein Füllmaterial.

## Tabu (Anonymität des Absenders)

- **Nie erwähnen:** konkreter Arbeitgeber (neutral bleiben, falls nötig: „Hersteller in der Autobranche"),
  Branche, interne Beispiele — auch nicht anonymisiert. Nebentätigkeitsthemen nicht öffentlich machen.
- Einziger erlaubter Glaubwürdigkeitsanker im Profil: „Ich baue KI-Systeme beruflich." Mehr nicht.

## Markenversprechen (gilt für JEDEN Post)

1. Jede Zahl hat eine Quelle.
2. Wenn etwas unklar ist, steht das im Post.
3. Es wird nichts verkauft.

**Leitprinzip Inhalt:** Ethik nie abstrakt, immer am Einzelfall — und der Fall betrifft den Zuschauer selbst.
Nicht „Ist KI moralisch?", sondern „Deine Bewerbung wurde aussortiert. Darf die Software das?"

## Tonlage (gilt für Posts und Kommentare)

- **Nüchtern heißt genau, nicht kalt.** Die Reibung kommt aus der Präzision, nie aus Spott.
- **Wohlwollender Ausgangspunkt.** Eine These erst ernst nehmen, dann genau hinsehen —
  nicht mit dem Ziel starten, sie zu widerlegen.
- **Etwas hinzufügen, nicht nur korrigieren.** Ein Beitrag, der nur sagt, was falsch ist,
  wird nicht veröffentlicht.
- **Humor und Selbstironie sind erwünscht** — solange sie sich gegen uns selbst richten,
  nie gegen das Gegenüber.

## Post-Regeln (Aufbau, Umfang, Sprache)

Gilt für jeden Karussell-Post. Vorbild sind Post 7, 8 und 9.

**Umfang**
- **5 bis 6 Blätter, nie mehr.** Lieber dichter als länger.
- Ein Gedanke pro Blatt. Was nicht draufpasst, kommt in die Caption oder wird ein eigener Post.
- Was bewusst weggelassen wurde, in `post.md` unter „Bewusst nicht auf den Blättern" festhalten.
  Das ist auch der Vorrat für Antworten auf Nachfragen in den Kommentaren.

**Aufbau**
- **Blatt 01 Hook:** Schlagzeile in Großbuchstaben über zwei bis drei Zeilen, darunter ein Satz mit der
  konkretesten Zahl.
  **Das Thema muss auf Blatt 01 beim Namen genannt sein.** Im Feed sieht man oft nur das erste Blatt.
  Produkt, Hersteller, Behörde, Gesetz oder Ort ausschreiben, statt sie als „die Brille" oder „die
  Software" zu umschreiben. Catchy und konkret schließen sich nicht aus, der Name gehört in die
  Schlagzeile selbst und nicht erst in die Unterzeile.
- **Blätter dazwischen:** je ein Kicker und ein zusammenhängender Absatz aus drei bis sechs Sätzen.
  Keine Stichpunktlisten auf den Inhaltsblättern.
- **Letztes Blatt Quellen:** kurze Quellenzeilen, Trennlinie, Hinweis „Kein Rechtsrat", Einladung zur
  sichtbaren Korrektur.

**Sprache (menschlich, keine KI-Tells)**
- Keine Gedankenstriche, kein Dreiklang, keine „nicht X, sondern Y"-Konstruktion.
- Kicker variieren, nicht schematisch durchzählen. Ganze Sätze, Alltagssprache.
- Zahlen ausschreiben und einordnen, statt sie nur zu nennen.

**Bildhaftes (stützt den Beleg, schmückt nie)**
- **Ein Beleg-Panel je Post.** Die wichtigste Fundstelle wird als Objekt gesetzt statt als Fließtext:
  `beleg(d, y, kopf, zeilen, sub=)` zeichnet beiges Feld, roten Balken links, Monospace.
  **Nur wörtliche Zitate ins Panel.** Wortlaut vorher an der Quelle prüfen, keine Zusammenfassung
  in Anführungszeichen setzen. Kopf nennt die Quelle, `sub` das Datum.
- **Zahlenreihen als Balken statt im Text:** `balken(d, y, [(label, wert, anzeige)])`.
  **Immer lineare Skala**, auch wenn ein Balken dadurch zum Splitter wird. Genau das ist die Aussage.
- **Höchstens zwei bebilderte Blätter je Post.** Die Ruhe des Aktenblatts ist das
  Unterscheidungsmerkmal im Feed, sie darf nicht wegdekoriert werden.
- **Keine Fotos, keine Stockbilder, keine KI-Bilder.** Alles wird aus der Marken-Palette gezeichnet.
  (KI-Bilder wären zusätzlich nach Art. 50 kennzeichnungspflichtig, siehe Repo-Konventionen.)

**Immer dabei**
- **Caption:** Kern zuerst, dann die Einschränkung, dann was es für den Leser heißt. Endet mit
  Quellenhinweis und Korrektur-Einladung. Fünf bis neun Hashtags.
- **Alt-Text je Blatt.**
- **`sources.md`** mit Belegtabelle, Belastbarkeitsbewertung und offenen Lücken.

**Rendern**
- Eine `build_postN()` je Post in `render/build_slides.py`, Ausgabe nach `posts/<ordner>/slides/blatt_NN.png`.
- Aufruf: `python render/build_slides.py` (braucht Pillow).
- Das Skript rendert **alle aktiven Posts plus Logo und Stories** neu und fasst dabei auch fremde PNGs an.
  Nach dem Lauf alles zurücksetzen, was nicht zum eigenen Post gehört (`git checkout -- <pfad>`),
  damit der Commit sauber bleibt.
- Stand-Datum je Post über `new(idx, total, stand)` setzen, nicht die globale Konstante ändern.
- Gepostete Posts liegen unter `archive/` und werden nicht neu gerendert.

## Kommentar-Regeln (Form und Treffsicherheit)

- **Die Frage des Ausgangsposts beantworten, nicht eine benachbarte.** Vor dem Schreiben in einem Satz
  festhalten, was der Post tatsächlich fragt, und am Ende gegenprüfen, ob der Kommentar genau das
  beantwortet. Ist die Frage abstrakt oder nicht belegbar, das ausdrücklich sagen und die belegbare
  Nachbarfrage anbieten. **Nie stillschweigend das Thema wechseln** — das wirkt wie Ausweichen und ist es
  auch. (Fehler vom 14.08.2026: FAZ fragte, ob KI die Menschheit auslöscht, geantwortet wurde über den
  Wissenschaftsbetrieb.)
- **Kurz halten: drei bis vier Zeilen, etwa 300 bis 400 Zeichen.** Instagram klappt Kommentare nach zwei
  bis drei Zeilen ein. **Der erste Satz muss allein tragen**, weil er oft der einzige sichtbare ist.
- **Ein Gedanke pro Kommentar.** Drei Punkte sind kein Kommentar, sondern ein Post.
- **Keine Aufzählungen, keine Nummerierung, keine Fettungen.** Ein formatierter Kommentar sieht eingefügt
  aus statt geschrieben. Bei einem Konto über KI ist „liest sich wie von einer Maschine" der teuerste
  Eindruck.
- **Nicht alles sagen.** Ein vollständiger Kommentar nimmt den Grund weg, aufs Profil zu tippen. Lieber
  einen Punkt scharf setzen und eine offene Frage stehen lassen.
- Was nicht in den Kommentar passt, wandert als Idee nach `research/ideas.md`, statt im Kommentarfeld
  zu verbrennen.

## Recherche-Regeln

- **Immer recherchieren, bei jeder Anfrage** — auch bei einem einzelnen Kommentar oder einer kurzen
  Antwort. Ungeprüft bleibt nichts, was als Fakt formuliert wird. Der Umfang richtet sich nach dem Zweck:
  - **Kommentare: kurz halten.** Die zentrale Behauptung an einer Primärquelle prüfen, Ergebnis knapp
    festhalten. Keine Quellentabelle, keine Nebenstränge — nur der Kommentartext plus Quellenangabe
    und ein Hinweis, falls etwas ungeprüft bleibt.
  - **Posts: vollständig recherchieren.** Primärquellen, Gegenstimmen, Zahlenherkunft, `sources.md`
    mit Belastbarkeitsbewertung.
- Primärquellen zuerst: EUR-Lex / Amtsblatt der EU, Bundesagentur für Arbeit, Statistisches Bundesamt,
  Gesetzestexte (DSGVO, BDSG, AGG, BetrVG). Aggregatoren und Presse nur als Zeiger auf das Original.
- Jede Zahl in einem Post muss in `sources.md` eine Fundstelle haben.
- Quellen als **belastbar** (mehrfach unabhängig bestätigt) oder **ungeprüft** markieren.
  Ungeprüftes kommt nicht in einen veröffentlichten Post.
- Rechtsformulierungen beschreibend halten („die Vorschrift sieht vor"), nie den Einzelfall bewerten —
  das wäre Rechtsberatung. Der Hinweis gehört fest aufs Quellenblatt.

## Repo-Konventionen

- **Sprache im Repo:** Deutsch (Content) — Code-Kommentare dürfen Deutsch sein, das ist so gewollt.
- **Encoding:** immer UTF-8. Umlaute korrekt schreiben, kein Mojibake.
- **Status-Wahrheit:** `posts/posts.yaml` ist das führende Register. Jede Statusänderung eines Posts
  wird dort UND in `posts/POSTS.md` nachgezogen.
- **Gepostete Posts archivieren:** Sobald ein Post veröffentlicht ist, wandert sein Ordner nach
  `archive/<ordner>` (eingefrorener, veröffentlichter Stand — nicht mehr aktiv gerendert). Die Register
  bleiben in `posts/` und führen weiterhin alle Posts (auch die archivierten).
- **Neues Thema?** Erst in `posts/posts.yaml` und `research/ideas.md` prüfen, ob es schon existiert.
- **Korrekturen sichtbar machen:** Fehler nie still löschen. Als eigener Commit mit klarer Message.
- **Branching:** direkt auf `master` committen und pushen. Keine Feature-Branches, keine Pull Requests,
  außer es wird ausdrücklich einer verlangt. (Grund: sonst liegt die Arbeit auf einem Branch, den niemand
  ansieht, und wirkt wie „nicht online".)
- **Keine KI-Bilder** ohne Kennzeichnung (Art. 50 AI Act, gilt seit 02.08.2026).

## Arbeitsweise (aus dem Trading-Projekt übernommen, bewährt)

- Nicht-triviale Aufgaben (3+ Schritte) erst planen, dann bauen. Bei Abweichung stoppen und neu planen.
- Nichts als „fertig" markieren, ohne es belegt zu haben (gerendert, gegengelesen, Quellen geprüft).
- Einfachste Lösung, minimaler Eingriff, Ursachen statt Symptome.

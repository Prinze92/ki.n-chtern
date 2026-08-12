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

## Recherche-Regeln

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
- **Keine KI-Bilder** ohne Kennzeichnung (Art. 50 AI Act, gilt seit 02.08.2026).

## Arbeitsweise (aus dem Trading-Projekt übernommen, bewährt)

- Nicht-triviale Aufgaben (3+ Schritte) erst planen, dann bauen. Bei Abweichung stoppen und neu planen.
- Nichts als „fertig" markieren, ohne es belegt zu haben (gerendert, gegengelesen, Quellen geprüft).
- Einfachste Lösung, minimaler Eingriff, Ursachen statt Symptome.

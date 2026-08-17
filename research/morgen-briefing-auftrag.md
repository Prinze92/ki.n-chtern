# Auftragstext Morgen-Briefing

Dieser Text ist der Auftrag für den täglichen Lauf. Er liegt hier, damit er versioniert ist und nicht
nur in einer Trigger-Konfiguration steckt, die niemand ansieht.

**Einrichtung in der Weboberfläche:** auf claude.ai/code eine geplante Aufgabe anlegen, als Repository
`Prinze92/ki.n-chtern` und Branch `master` wählen, Zeit 07:00 Uhr Berliner Zeit, Modell Opus 5. Den Text
unterhalb der Trennlinie vollständig einfügen. Wichtig ist, dass die Aufgabe dort an das Repository
gebunden wird, denn ein Lauf ohne Repository kann nichts abliefern (siehe README, Abschnitt
„Morgen-Briefing").

**Wird der Text hier geändert, muss er auch in der eingerichteten Aufgabe nachgezogen werden.** Die
Aufgabe liest diese Datei nicht, sie trägt ihre eigene Kopie.

---

Tages-Briefing und Post-Produktion für das Instagram-Konto ki.nüchtern. Repo Prinze92/ki.n-chtern, Branch master.

SCHRITT 0 — REPO-PRÜFUNG, ZUERST UND OHNE AUSNAHME
Prüfe: Liegt CLAUDE.md im Arbeitsverzeichnis, ist posts/posts.yaml lesbar, zeigt `git remote -v` auf Prinze92/ki.n-chtern?
Falls NEIN: Brich sofort ab. Recherchiere nichts. Antworte ausschließlich "ABBRUCH: Repository nicht vorhanden" plus die Ausgaben von `pwd`, `ls -la` und `git remote -v`. Ein Lauf ohne Repo kann nichts abliefern, das ist am 14.08. und 17.08.2026 passiert und hat beide Male ohne Ergebnis geendet.
Falls JA: `git pull origin master` ausführen, damit du auf dem aktuellen Stand arbeitest. Zwischen zwei Läufen wird von Hand committet.

WICHTIG: Lies dann CLAUDE.md vollständig, auch wenn du meinst, sie schon zu kennen. Sie ändert sich. Dort stehen die verbindlichen Regeln (Grundhaltung, Tabu, Markenversprechen, Tonlage, Post-Regeln inkl. Bauformen, Humor, Bildhaftes und Schriftgrößen, Kommentar-Regeln, Recherche-Regeln, Repo-Konventionen). Sie gehen allem hier vor. Lies außerdem research/ideas.md und posts/posts.yaml.

TEIL A — BRIEFING

1. Recherchiere KI-Nachrichten der letzten 24 bis 36 Stunden. Relevanzfilter in dieser Reihenfolge:
   - Betrifft der Fall Leserinnen und Leser in Deutschland konkret und persönlich? (Leitprinzip: nicht "Ist KI moralisch?", sondern "Deine Bewerbung wurde aussortiert.")
   - Gibt es eine Primärquelle mit Zahl und Datum? Behörden, Gerichte, Gesetzestexte, Studien im Original. Aggregatoren und Presse nur als Zeiger.
   - Ist das Thema in posts.yaml oder ideas.md schon vergeben?
   Reine Produktnews (Modellversionen, Nutzerzahlen, Finanzierungsrunden) sind NICHT post-würdig, außer der Zuschauer ist unmittelbar betroffen.

2. Wähle 3 bis 5 Kandidaten. Je Kandidat: was passiert ist in zwei bis drei Sätzen, Primärquelle mit Link, Belastbarkeit (belastbar / einzelquelle / berichtet / ungeprüft), passende Säule und Bauform, und wo die Berichterstattung überzieht oder etwas auslässt.

3. Suche 2 bis 3 Beiträge grosser deutschsprachiger Konten (tagesschau, ZDF, FAZ, netzpolitik, t3n, heise, Bundesbehörden) aus den letzten 24 Stunden, unter denen ein Kommentar sinnvoll wäre. Schreibe je einen fertigen Kommentar nach den Kommentar-Regeln: 300 bis 400 Zeichen, ein Gedanke, erster Satz trägt allein, keine Aufzählungen, keine Fettungen, beantwortet die Frage des Ausgangsposts und nicht eine benachbarte.

4. Schreibe das Briefing nach research/briefing/JJJJ-MM-TT.md. Aufbau: Datum, "Kandidaten für Posts", "Kommentar-Vorschläge", "Nicht verfolgt" mit Begründung, "Gebaut" mit Verweis auf die Posts aus Teil B.

TEIL B — POSTS FERTIG BAUEN

STAUKONTROLLE ZUERST: Zähle in posts.yaml die Posts mit status "gerendert" oder "geprueft", die noch nicht gepostet sind. Sind es VIER ODER MEHR, baue heute KEINEN neuen Post. Vermerke im Briefing "Rückstau, kein Neubau" und beende nach Teil A. Sonst baue bis zu zwei Posts, so dass der Rückstau vier nicht übersteigt.

QUALITÄTSSCHWELLE: Kein belastbarer Primärbeleg heißt kein Post. Lieber einen oder gar keinen als zwei schwache. Wenn du nur einen baust, begründe das im Briefing.

Je Post, vollständig nach den Post-Regeln in CLAUDE.md:
- Nächste freie ID aus posts.yaml nehmen, Ordner posts/post-0NN-slug/ anlegen
- Vollständige Recherche: Primärquellen im Original lesen, Gegenstimmen suchen, Zahlenherkunft klären
- post.md mit Säule, Bauform, Blätter-Tabelle, Caption, Alt-Text je Blatt, Abschnitt "Bewusst nicht auf den Blättern", Checkliste "Vor dem Posten"
- sources.md mit Belegtabelle, Belastbarkeitsbewertung, offenen Lücken und Rechtshinweis
- 5 bis 6 Blätter. Blatt 01 nennt das Thema beim Namen. Die Schlagzeile muss auch sagen, was für den Leser auf dem Spiel steht, nicht nur das Stichwort nennen. Vorbild ist der bisher beste Post "Killt KI die Jobs?": Alltagsworte, konkreter Einsatz, Zahl erst in der Unterzeile. Bauform bewusst wählen und variieren, nicht immer "Der Fall"
- Ein Beleg-Panel je Post mit WÖRTLICHEM Zitat, Wortlaut vorher an der Quelle geprüft. Zahlenreihen als Balken, lineare Skala
- build_postNN() in render/build_slides.py ergänzen, OUT_POSTNN-Pfad und Dispatcher-Zeile ergänzen, Stand-Datum über new(idx, total, stand) setzen
- `python render/build_slides.py` ausführen
- DANACH alle fremden PNGs zurücksetzen: `git checkout -- brand/` und die slides-Ordner aller anderen Posts. Im Commit dürfen nur die eigenen neuen Blätter stehen
- Überlauf prüfen: gerenderte PNGs auf Nicht-Hintergrundpixel zwischen y=1120 und y=1185 abtasten. Bei Überlauf Text kürzen, nicht die Schrift verkleinern
- Text gegen die Sprachregeln prüfen: keine Gedankenstriche, kein Dreiklang, keine "nicht X, sondern Y"-Konstruktion, keine vagen Autoritäten, keine Zusammenfassungsformeln, Satzlängen wechseln
- posts.yaml, posts/POSTS.md und research/ideas.md nachziehen

TEIL C — ABSCHLUSS
Alles committen und mit `git push -u origin master` pushen. Keine Feature-Branches, keine Pull Requests.
PUSH-KONTROLLE: Danach `git fetch origin master` und `git log origin/master -1 --oneline` ausführen und mit dem lokalen HEAD vergleichen. Stimmen sie nicht überein, ist nichts angekommen. Sage das dann ausdrücklich und nenne die Fehlermeldung des Pushes im Wortlaut. Melde niemals Erfolg ohne diesen Vergleich.

HARTE GRENZEN
- Erfinde nichts. Keine Zahl ohne Fundstelle. Ungeprüftes ausdrücklich kennzeichnen. Im Zweifel weglassen.
- Veröffentliche nichts auf Instagram oder anderswo. Der Auftrag endet im Repo.
- Fasse bestehende Posts nicht an. Archivierte Posts unter archive/ werden weder geändert noch neu gerendert.
- Halte das Tabu ein: kein Arbeitgeber, keine Branche des Absenders.
- Baue KEINEN Korrektur-Post, außer du hast einen echten, am Primärdokument belegten eigenen Fehler gefunden.

ZUM SCHLUSS: Fasse in drei bis vier Sätzen zusammen, was gebaut wurde, was der stärkste Kandidat des Tages ist und welche offenen Punkte vor dem Posten zu klären sind. Sei ausdrücklich bei allem, was du nicht verifizieren konntest, und nenne das Ergebnis der Push-Kontrolle.

# Quellen — Post 27

**Stand:** 30.08.2026. Alle Abrufe an diesem Tag, sofern nicht anders vermerkt.

## Belegtabelle

| Aussage im Post | Fundstelle | Belastbarkeit |
|---|---|---|
| **105 Standorte** in der Karte | **P1** `okfde.github.io/datacenters-map/data/datacenters.geojson`, 105 Features, selbst ausgezählt | belastbar für den Datensatz |
| **14.336 Megawatt** Netzanschluss in Summe | P1, Summe über `size_power_kw`, 14.336.062,5 kW | belastbar für den Datensatz |
| **45 geplant, 44 im Bau, 10 pausiert, 2 abgebrochen, 4 ohne Angabe** | P1, Feld `operational_status` (`planned`/`under_construction`/`paused`/`cancelled`/leer) | belastbar für den Datensatz |
| **26 Standorte mit Protest** | P1, Feld `has_protest` = true | belastbar für den Datensatz |
| **57 recherchiert (10.942 MW), 36 geschätzt (3.394 MW), 12 ohne Angabe** | P1, Felder `total_power_capacity_kw` gegen `estimated_total_power_capacity_kw`; kein Standort hat beide | belastbar für den Datensatz |
| Datenstand der Karte **27.08.2026** | **P2** `heisseluft.org/info#methodik`, Abschnitt „Wie aktuell sind die Informationen auf der Karte?" | belastbar |
| Träger: **AlgorithmWatch gGmbH, Stichting Leitmotiv, Heiße-Luft-Kollektiv, Open Knowledge Foundation Deutschland** | P2 und die Einwilligungserklärung auf `heisseluft.org` | belastbar |
| Wortlaut **§ 13 Abs. 1 Satz 1 EnEfG** (Panel, Blatt 03) | **P3** `gesetze-im-internet.de/enefg/__13.html`, Zeichen für Zeichen abgeglichen | belastbar (Primärnorm) |
| **§ 19 Abs. 1 Nr. 6** erfasst nur das Übermitteln | **P4** `gesetze-im-internet.de/enefg/__19.html` | belastbar (Primärnorm) |
| **§ 19 Abs. 1 Nr. 2** nennt „veröffentlicht" ausdrücklich | P4 | belastbar (Primärnorm) |
| Bußgeld **bis 50.000 Euro** | P4, § 19 Abs. 2: Nr. 1, 5 und 7 bis 100.000 Euro, „in den übrigen Fällen" bis 50.000 Euro. Nr. 6 gehört zu den übrigen | belastbar |
| Schwelle **300 Kilowatt** | **P5** EnEfG § 3 Nr. 24 Buchst. a, „nicht redundante elektrische Nennanschlussleistung ab 300 Kilowatt" | belastbar |
| Eigentümersitz nach Leistung (Caption) | P1, Feld `owner_country`, gewichtet mit `size_power_kw` | belastbar für den Datensatz |
| Schuby **1.400 MW** (Caption) | P1, `total_power_capacity_kw` = 1.400.000; als Quellen nennt der Datensatz NDR und die Ratsinformation Schleswig | belastbar für den Datensatz, Originalquellen nicht selbst geöffnet |
| heise nennt für US-Konzerne **rund ein Drittel** (Caption) | **P6** heise online, „Interaktive Karte zeigt viele geplante Rechenzentren in Deutschland", 28.08.2026, 13:18 Uhr | berichtet |

## Was „belastbar für den Datensatz" heißt

Der Datensatz ist vollständig einsehbar, seine Methodik steht offen, und er kennzeichnet jeden
Schätzwert als solchen. Was er behauptet, lässt sich deshalb nachprüfen. **Für die Wirklichkeit
dahinter ist er nicht belastbar, und er sagt das selbst:** „Mehr Projekte werden öffentlich
angekündigt, als tatsächlich gebaut werden." Der Post übernimmt diese Einschränkung auf Blatt 02
(zwei abgebrochene, zehn pausierte Projekte) und in der Caption.

Lizenz des Datensatzes: CC BY-NC-SA 4.0. Attribution laut Datei: Tiziana von Witzleben
(Heiße-Luft-Kollektiv), Joschi Wolf (FragDenStaat), Max Schulze (Leitmotiv). Der Post nennt die Karte
auf Blatt 01 und im Quellenblatt und verkauft nichts.

## Die Abweichung, die ich nicht auflösen konnte

heise schreibt, US-Konzerne errichteten „rund ein Drittel der neuen Rechenzentren", gestützt auf eine
Auswertung von NDR, SZ, Heiße Luft, AlgorithmWatch, FragDenStaat und Leitmotiv. **Im Datensatz selbst
komme ich auf 22 von 105 Standorten (21,0 Prozent) und 24,6 Prozent der Netzanschlussleistung.**
Möglich, dass die Auswertung eine andere Grundgesamtheit oder eine andere Zuordnung von Betreiber und
Eigentümer verwendet; die Karte trennt beides ausdrücklich und weist Microsoft etwa als Betreiber
aus, während der Gebäudeeigentümer ein anderer sein kann. Die Auswertung selbst habe ich nicht
gefunden. **Deshalb steht in der Caption nur meine eigene Zählung, ausdrücklich als solche.**

## Offene Lücken

1. **Das Nationale Rechenzentrumsregister ist nicht geprüft.** `rechenzentrumsregister.bund.de` war am
   28.08. und erneut am 30.08.2026 aus dieser Umgebung nicht erreichbar (der Proxy lehnt die
   Verbindung ab). Wie viele bestehende Anlagen dort gemeldet sind, steht deshalb auf keinem Blatt.
   Der Hinweis darauf steht im Quellenblatt und in der Caption.
2. **Die Zahl 482** (Meldungen für das Berichtsjahr 2025, Stand 06.07.2026) stammt aus einer Auskunft
   des Bundeswirtschaftsministeriums an netzpolitik.org vom 10.08.2026. **Belastbarkeit: einzelquelle**
   (Behördenauskunft, nur über eine Redaktion zugänglich). Die dort ebenfalls genannte Schätzung von
   rund 1.000 meldepflichtigen Anlagen ist noch schwächer. Beides ist nicht im Post.
3. **Dummerstorf.** Die Karte führt 1.200 Megawatt und die Freo Group, die Pressemitteilung der
   Schwarz-Gruppe vom 27.08.2026 für denselben Ort 240 Megawatt bis 2033 und ein Gigawatt bis 2045.
   Ob dasselbe Projekt gemeint ist, bleibt offen. Deshalb ist Dummerstorf kein Beleg im Post.
4. **Kein Vergleich mit dem Bestand.** Die in Post 13 offene Frage, ob die Bitkom-Werte (2.980 MW für
   2025) IT- oder Netzanschlussleistung meinen, ist weiterhin offen. heise nennt für Ende 2025 „rund
   3 Gigawatt" und lässt es ebenfalls offen. Die Karte misst nachweislich den Netzanschluss (CSV-Spalte
   „Netzanschluss (kW) (Recherche)"). Ein Balken über beide wäre nicht ehrlich definiert.
5. **Die EnEfG-Novelle** (Kabinettsbeschluss 24.06.2026) soll eine Ausnahme für Geschäftsgeheimnisse
   einfügen. Der Entwurfstext ist nicht gelesen und steht deshalb nicht im Post.
6. **Die Originalquellen der einzelnen Standorte** sind nicht einzeln nachgeprüft. Der Datensatz nennt
   je Standort bis zu sechs Links; ich habe die Datei als Ganzes ausgewertet, nicht 105 Fälle
   einzeln. Für Schuby und Dummerstorf sind die Quellenlinks angesehen, aber nicht geöffnet.

## Rechtshinweis

Die Paragrafen sind beschreibend wiedergegeben („die Vorschrift sieht vor", „die Aufzählung erfasst").
Der Post bewertet keinen Einzelfall und ist kein Rechtsrat. Der Hinweis steht auf Blatt 06.

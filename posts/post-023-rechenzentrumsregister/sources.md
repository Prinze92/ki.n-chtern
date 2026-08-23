# Quellen — Post 23 „Im Rechenzentrumsregister des Bundes fehlt die Hälfte"

Stand der Recherche: 23.08.2026, 05:00 bis 06:15 UTC.

## Methode

Gesetzestexte über gesetze-im-internet.de (Bundesamt für Justiz) geladen, HTML entmarkt, Wortlaut
per String-Suche geprüft. Die Bundesrat-Drucksache als PDF geladen, mit `pypdf` extrahiert,
Silbentrennung und Zeilenumbrüche geglättet, dann die Panel-Sätze per String-Suche bestätigt statt
sie abzutippen. Kein Zitat auf einem Blatt stammt aus einer Zusammenfassung.

## Belegtabelle

| Aussage im Post | Fundstelle | Belastbarkeit |
|---|---|---|
| Betreiber müssen bis zum 31. März veröffentlichen **und** an den Bund übermitteln (Panel Blatt 02, Wortlaut) | EnEfG § 13 Absatz 1 Satz 1, Fassung vom 13.11.2023 (BGBl. 2023 I Nr. 309), `gesetze-im-internet.de/enefg/__13.html` | **belastbar** (amtliche Textausgabe, Wortlaut per Suche bestätigt) |
| Das Gesetz ist seit Inkrafttreten unverändert | `gesetze-im-internet.de/enefg/BJNR1350B0023.html`: Ausfertigung 13.11.2023, „Textnachweis ab: 18.11.2023", keine Änderungsangabe | **belastbar** |
| Anlage 3 verlangt Postleitzahl, Größenklasse, Gesamtstromverbrauch, Anteil erneuerbarer Energien, Abwärme und eine Kennzahl der Wassernutzung | EnEfG Anlage 3 (zu § 13 Absatz 1), Nummer 1 Buchstabe c und d, Nummer 2 Buchstaben a bis i | **belastbar** |
| Der Bund führt ein Energieeffizienzregister für Rechenzentren | EnEfG § 14 | **belastbar** |
| Nur das Nichtübermitteln ist Ordnungswidrigkeit, Bußgeld bis 50.000 Euro; Verwaltungsbehörde ist das BAFA | EnEfG § 19 Absatz 1 Nummer 6, Absatz 2, Absatz 3 | **belastbar** |
| Beim Umsetzungsplan nach § 9 nennt derselbe Katalog auch das Veröffentlichen | EnEfG § 19 Absatz 1 Nummer 2 | **belastbar** |
| Die geltende Stichprobenkontrolle erfasst § 13 nicht | EnEfG § 10 Satz 1 nennt nur § 8 Absatz 1 und § 9 Absatz 1 | **belastbar** (Negativbefund am Wortlaut) |
| Neu einzufügender Satz zur Geschäftsgeheimnis-Ausnahme (Panel Blatt 03, Wortlaut) | BR-Drucksache 388/26 vom 25.06.26, Artikel 1 Nummer 11 Buchstabe a Doppelbuchstabe aa | **belastbar** (Drucksache im Volltext gelesen, 101 Seiten, Wortlaut per Suche bestätigt) |
| Begründung: die alte Fassung sah keine solche Ausnahme vor, es mussten „sämtliche Informationen der Öffentlichkeit zugänglich gemacht werden" | BR-Drucksache 388/26, Begründung zu Artikel 1 Nummer 11 | **belastbar** |
| Der Entwurf hält die Asymmetrie im Bußgeldkatalog durch (neu § 19 Absatz 1 Nummer 4: nur „übermittelt") | BR-Drucksache 388/26, Artikel 1 Nummer 16 | **belastbar** |
| Der Entwurf stellt die Veröffentlichung erstmals unter Stichprobenkontrolle | BR-Drucksache 388/26, Artikel 1 Nummer 15, neuer § 18 Satz 1: „die Übermittlung und Veröffentlichung von Informationen nach § 13 Absatz 1 durch Stichproben zu kontrollieren" | **belastbar** |
| Kabinettsbeschluss am 24.06.2026 | Drucksachendatum 25.06.26; Kabinettstermin 24.06.2026 nach übereinstimmender Fachberichterstattung (u. a. energieundrecht.com, WEKA, DENEFF) | **belastbar für das Drucksachendatum, berichtet für den Kabinettstermin.** Die Pressemitteilung des BMWE war nicht abrufbar (Radware-Sperrseite) |
| 482 Meldungen für das Berichtsjahr 2025, Stand 6. Juli 2026 | Auskunft des Bundeswirtschaftsministeriums gegenüber netzpolitik.org, wiedergegeben in netzpolitik.org vom 10.08.2026 und erneut am 22.08.2026 | **berichtet.** Kein Dokument des Ministeriums gesehen |
| Rund 1.000 meldepflichtige, etwa 2.000 Rechenzentren insgesamt | netzpolitik.org vom 22.08.2026, dort ausdrücklich als Schätzung bezeichnet | **ungeprüft.** Keine benannte Herkunft, keine amtliche Gesamtzahl gefunden |
| „Das Register ist sehr lückenhaft. Das ist ein Armutszeugnis für die Bundesregierung." und „So wird die individuelle Veröffentlichung weder kontrolliert noch sanktioniert." | Julian Bothe, Senior Policy Manager AlgorithmWatch, im Interview mit Ingo Dachwitz, netzpolitik.org, 22.08.2026, 07:41 Uhr | **belastbar als Zitat** (Rohtext der Seite geladen). Inhaltlich ist der zweite Satz am Gesetz nachgeprüft und trifft zu |
| Kurzgutachten zu den geplanten Änderungen des § 13 Absatz 1 EnEfG | Dr. Michéle John und Juliane Willert, Rechtsanwälte Günther Partnerschaft, Hamburg, für AlgorithmWatch gGmbH und Umweltinstitut München e.V., Schreiben vom 16.04.2026, veröffentlicht April 2026, 17 Seiten, PDF gelesen | **belastbar als Dokument, Parteigutachten in der Sache** |

## Der eigene Befund

Bothe sagt im Interview in einem Halbsatz, die Veröffentlichung werde „weder kontrolliert noch
sanktioniert". Das ist am Gesetz nachprüfbar und stimmt, und zwar zweifach:

1. **Nicht sanktioniert.** § 19 Absatz 1 Nummer 6 EnEfG lautet: „entgegen § 13 Absatz 1 Satz 1 eine
   Information nicht, nicht richtig, nicht vollständig oder nicht rechtzeitig **übermittelt**".
   § 13 Absatz 1 Satz 1 enthält zwei Pflichten, veröffentlichen und übermitteln. Nur die zweite
   steht im Bußgeldkatalog. Dass das kein Versehen ist, zeigt Nummer 2 derselben Vorschrift: Für
   den Umsetzungsplan nach § 9 nennt der Gesetzgeber ausdrücklich beides, „nicht rechtzeitig
   erstellt **oder** nicht … rechtzeitig veröffentlicht".
2. **Nicht kontrolliert.** § 10 EnEfG erfasst nur Managementsysteme nach § 8 und Umsetzungspläne
   nach § 9. § 13 kommt darin nicht vor.

Beides gilt für das **geltende** Recht. Im Entwurf bleibt Punkt 1 bestehen (neu § 19 Absatz 1
Nummer 4), Punkt 2 fällt weg, weil der neue § 18 die Veröffentlichung ausdrücklich in die
Stichprobenkontrolle aufnimmt. Diese Differenzierung steht in keiner der gelesenen Meldungen und
gehört deshalb auf Blatt 04.

## Wortlaut, der nicht aufs Blatt kam

Geplanter neuer § 13 Absatz 3 EnEfG (BR-Drucksache 388/26, Artikel 1 Nummer 11 Buchstabe b):

> „Die nach Absatz 1 übermittelten Informationen sind vertraulich zu behandeln mit Rücksicht auf die
> Wahrung von Betriebs- und Geschäftsgeheimnissen der Betroffenen. Eine Verarbeitung und
> Übermittlung der Informationen zu Forschungszwecken ist zulässig. Eine sonstige Weitergabe oder
> Veröffentlichung der Informationen erfolgt ohne vorherige Zustimmung der Betroffenen nur in
> aggregierter und anonymisierter Form."

Aus der Begründung dazu:

> „Eine Veröffentlichung der übermittelten Daten ist dementsprechend durch den Bund nur in
> aggregierter und anonymisierter Form oder im Falle der vorigen Zustimmung des betroffenen
> Betreibers des jeweiligen Rechenzentrums zulässig, wie dies bereits auf der Website des
> Energieeffizienzregisters für Rechenzentren des Bundes geschieht."

**Achtung, ungelöste Spannung:** Dieser Begründungssatz (Stand Juni 2026) beschreibt das Register
als rein aggregiert. netzpolitik.org schreibt am 22.08.2026, man könne dort nun „erstmalig
Informationen zum Verbrauch und zur Effizienz einzelner Rechenzentren nachvollziehen". Beides kann
zutreffen, wenn das Register nach dem Kabinettsbeschluss umgestellt wurde. Nachgeprüft ist es
nicht, weil das Register nicht erreichbar war. Deshalb steht keine Aussage über den Inhalt des
Registers auf einem Blatt.

## Offene Lücken

1. **Das Register selbst ist nicht gesehen.** `rechenzentrumsregister.bund.de/de/annual-reports/`
   war aus dieser Umgebung nicht erreichbar (Gateway antwortete mit 502 auf CONNECT, DNS-Auflösung
   schlug fehl). Die Zahl 482 und die Aussage über Einzelanlagen sind damit fremdbelegt.
2. **Keine amtliche Gesamtzahl der meldepflichtigen Rechenzentren.** Die Hälfte-Aussage der
   Schlagzeile stützt sich auf eine Schätzung ohne benannte Herkunft. Blatt 01 nennt sie als
   Schätzung, Blatt 05 wiederholt das.
3. **Schwellenwert unklar.** § 20 Absatz 2 Nummer 2 EnEfG nennt 200 Kilowatt nicht redundante
   Nennanschlussleistung ab 01.07.2025, netzpolitik nennt an anderer Stelle 300 Kilowatt
   IT-Anschlussleistung. Unterschiedliche Bezugsgrößen, nicht aufgelöst, deshalb auf keinem Blatt.
4. **Kein Bußgeldstand.** Ob das BAFA je ein Bußgeld nach § 19 Absatz 1 Nummer 6 verhängt hat, ist
   nicht bekannt. Ohne diese Zahl bleibt offen, ob auch die sanktionierte Übermittlungspflicht
   durchgesetzt wird.
5. **Keine Stellungnahme der Gegenseite.** Weder das BMWE noch ein Betreiberverband kommt zu Wort.
   Die Argumente der Betreiber (Rückschlüsse auf Auslastung, Sicherheitsrisiken) sind nur aus dem
   Interview und dem Kurzgutachten bekannt, also von der kritisierenden Seite referiert.
6. **Der weitere Gesetzgebungsweg ist offen.** Bundestag und Bundesrat sollen sich bis zum Herbst
   befassen. Was am Ende in § 13 steht, ist nicht entschieden. Der Post sagt deshalb durchgehend
   „Entwurf".
7. **Kleine Fehlerquelle in der Sekundärquelle:** Im netzpolitik-Interview sind die Links auf die
   EU-Energieeffizienzrichtlinie und das deutsche Energieeffizienzgesetz vertauscht. Ohne Belang
   für die Aussagen, aber ein Grund, dort keine Fundstelle zu übernehmen.

## Rechtshinweis

Der Post beschreibt, was in Gesetz und Gesetzentwurf steht. Er bewertet keinen Einzelfall und gibt
keinen Rechtsrat. Ob eine bestimmte Angabe eines bestimmten Betreibers ein Geschäftsgeheimnis ist,
entscheidet sich nicht auf einem Aktenblatt.

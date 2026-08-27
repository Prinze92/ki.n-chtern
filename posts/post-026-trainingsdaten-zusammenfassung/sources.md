# Quellen — Post 26 „KI-Anbieter müssen offenlegen, womit sie trainiert haben"

Stand der Recherche: 27.08.2026, 05:05 bis 06:40 UTC.

## Methode

Die KI-Verordnung wurde in der amtlichen deutschen Fassung bei EUR-Lex geladen (CELEX 32024R1689,
rund 1,3 Megabyte HTML), entmarkt und im Volltext durchsucht. Jede zitierte Stelle ist per
String-Suche im Rohtext bestätigt. Die Vorlage der Kommission wurde als PDF über die Seite der
Bundesnetzagentur geladen, mit `pypdf` extrahiert und ebenfalls per Suche geprüft.

## Belegtabelle

| Aussage im Post | Fundstelle | Belastbarkeit |
|---|---|---|
| Panel Blatt 02 im Wortlaut: Anbieter „erstellen und veröffentlichen eine hinreichend detaillierte Zusammenfassung der für das Training des KI-Modells mit allgemeinem Verwendungszweck verwendeten Inhalte nach einer vom Büro für Künstliche Intelligenz bereitgestellten Vorlage" | Verordnung (EU) 2024/1689, Artikel 53 Absatz 1 Buchstabe d, amtliche deutsche Fassung | **belastbar** |
| Die Pflicht gilt seit dem 2. August 2025 | Artikel 113 Buchstabe b: Kapitel V gilt ab dem 2. August 2025. Artikel 53 steht in Kapitel V (im Text nachgeprüft: Kapitel V beginnt vor Artikel 51 und endet vor Kapitel VI) | **belastbar** |
| Geldbußen erst seit dem 2. August 2026 | Artikel 113 Buchstabe b nimmt **Artikel 101 ausdrücklich aus** („mit Ausnahme des Artikels 101"). Artikel 101 gilt damit erst mit dem allgemeinen Geltungsbeginn am 2. August 2026 | **belastbar.** Das ist der schärfste Datumsbefund des Posts und beruht auf einem Halbsatz im Verordnungstext |
| Bis zu drei Prozent des weltweiten Jahresumsatzes | Artikel 101 Absatz 1: „Geldbußen von bis zu 3 % ihres gesamten weltweiten Jahresumsatzes im vorangegangenen Geschäftsjahr oder 15 000 000 EUR, je nachdem, welcher Betrag höher ist" | **belastbar.** Auf dem Blatt steht nur der Prozentsatz, siehe „Bewusst nicht auf den Blättern" |
| Zweck der Pflicht: Rechteinhaber sollen ihre Rechte ausüben und durchsetzen können | Erwägungsgrund 107: die Zusammenfassung soll „Parteien mit berechtigtem Interesse, einschließlich der Inhaber von Urheberrechten, die Ausübung und Durchsetzung ihrer Rechte nach dem Unionsrecht erleichtern" | **belastbar** |
| Die Vorlage verlangt die Domainnamen der obersten zehn Prozent des abgegriffenen Inhalts, bei KMU die obersten fünf Prozent oder die tausend größten | Vorlage der Kommission C(2025) 5235 final vom 24.07.2025, Fußnote 16: „a list of the internet domain names (top and second-level domain, e.g. `example.com`) in the top 10 % of all domain names determined by the size of the content scraped … For small and medium-sized enterprises (SMEs), including start-ups, the Template requires the internet domain names in the top 5%, or the top 1000 domains" | **belastbar**, im PDF per Suche bestätigt. **Die Vorlage ist auf Englisch**, der Post gibt sie beschreibend wieder und setzt sie nicht in Anführungszeichen |
| Die genaue Mischung und Zusammensetzung der Datenquellen wird nicht verlangt | dieselbe Vorlage, Randnummer 22: „The Template does not require disclosure of the exact mix and composition of data sources, but only high-level information about the training data size per modality (selection amongst three very broad ranges)" | **belastbar** |
| Bei lizenzierten Daten reicht wenig, weil die Rechteinhaber Vertragspartei sind | dieselbe Vorlage, Randnummer 19: „limited disclosure of information is required for licensed data given that the rightsholders concerned are parties to the licensing agreements" | **belastbar** |
| Die Ausnahme für quelloffene Modelle erfasst die Zusammenfassung nicht (nur Caption) | Artikel 53 Absatz 2: „Die Pflichten gemäß Absatz 1 Buchstaben a und b gelten nicht für Anbieter von KI-Modellen, die im Rahmen einer freien und quelloffenen Lizenz bereitgestellt werden" | **belastbar** (Umkehrschluss aus dem Wortlaut: die Buchstaben c und d sind nicht genannt) |
| Es gibt keine Sammelstelle für die Zusammenfassungen | Artikel 71 Absatz 1: Die EU-Datenbank erfasst „Hochrisiko-KI-Systeme nach Artikel 6 Absatz 2, die gemäß den Artikeln 49 und 60 registriert werden" und bestimmte Systeme nach Artikel 6 Absatz 3. Zusammenfassungen nach Artikel 53 kommen darin nicht vor. Zusätzlich geprüft: die Seite des Büros für Künstliche Intelligenz (`digital-strategy.ec.europa.eu/en/policies/ai-office`) führt weder ein Verzeichnis der Zusammenfassungen noch eine Liste der Anbieter | **belastbar für den Verordnungstext**, **geprüft für die Seite des Büros** |
| Die Kommission kann Dokumentation anfordern (nur `sources.md`) | Artikel 91 Absatz 1 und Absatz 4: Im Auskunftsersuchen sind Rechtsgrundlage, Zweck, benötigte Informationen, eine Frist und die Geldbußen nach Artikel 101 zu nennen | **belastbar** |

## Der Anlass, der nicht belegt werden konnte

Der netzpolitik-Ticker verweist am 26.08.2026 auf einen Euractiv-Bericht, wonach die Kommission
erstmals Auskünfte von führenden KI-Anbietern zu Sicherheit und Urheberrecht verlangt und damit
dieses Instrument der KI-Verordnung zum ersten Mal einsetzt. **Der Euractiv-Artikel war nicht
abrufbar** (HTTP 403, auch mit Browser-Kennung). Eine Pressemitteilung der Kommission zu diesen
Ersuchen habe ich nicht gefunden.

**Folge für den Post:** Der Anlass wird in der Caption als Anlass benannt und ausdrücklich als
ungeprüft gekennzeichnet. Auf keinem Blatt steht eine Aussage, die von ihm abhängt. Der gesamte Post
trägt sich aus dem Verordnungstext und der Vorlage.

## Offene Lücken

1. **Keine einzelne Zusammenfassung gelesen.** Die größte Lücke. Mehrere Anbieterseiten antworteten
   aus dieser Umgebung mit HTTP 403 oder 404. Geratene Adressen habe ich nach zwei Fehlversuchen
   nicht weiter probiert, weil geratene Fundstellen in diesem Repo schon einmal danebenlagen. Ohne
   eine gelesene Zusammenfassung beschreibt der Post die Pflicht und nicht ihre Wirklichkeit. Steht
   in der Checkliste.
2. **Die eigene Umgebung ist keine Aussage über die Welt.** Dass ich Seiten nicht öffnen konnte,
   sagt nichts darüber, wie leicht sie mit einem normalen Browser zu finden sind. Blatt 05 sagt das
   ausdrücklich, und der Befund „keine Sammelstelle" stützt sich nicht darauf, sondern auf Artikel 71
   und die Seite des Büros für Künstliche Intelligenz.
3. **Die Übergangsfrist für Altmodelle ist nicht belegt.** Die Vorlage nennt für Modelle, die vor dem
   2. August 2025 in Verkehr gebracht wurden, eine längere Frist. Die Fundstelle im Verordnungstext
   habe ich nicht sauber isoliert, deshalb steht sie auf keinem Blatt.
4. **Die Zahl der bisher veröffentlichten Zusammenfassungen ist ungeprüft.** In Fachbeiträgen
   kursieren Zahlen um 39. Nicht nachgezählt.
5. **Die Vorlage ist auf Englisch.** Eine amtliche deutsche Fassung habe ich nicht gefunden. Alle
   Angaben daraus stehen im Post beschreibend und nicht als Zitat.
6. **Keine Gegenstimme der Anbieterseite.** Wie Anbieter die Reichweite der Pflicht sehen, ist nicht
   recherchiert. Blatt 04 gibt stattdessen wieder, was die Kommission selbst nicht verlangt.

## Rechtshinweis

Der Post beschreibt den Wortlaut einer Verordnung und einer Vorlage der Kommission. Er bewertet
keinen Einzelfall, behauptet über keinen Anbieter, dass er die Pflicht erfüllt oder verletzt, und
gibt keinen Rechtsrat.

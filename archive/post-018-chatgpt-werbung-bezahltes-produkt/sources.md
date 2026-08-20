# Quellen — Post 18 „GPT schiebt dir das bezahlte Produkt dazwischen"

## Hauptquelle für den Kern des Posts

Addison J. Wu, Ryan Liu, Shuyue Stella Li, Yulia Tsvetkov, Thomas L. Griffiths:
**„Ads in AI Chatbots? An Analysis of How Large Language Models Navigate Conflicts of Interest"**,
arXiv 2604.08525, eingereicht 09.04.2026, hier verwendete Fassung v3 vom 17.08.2026.
Kategorien cs.AI, cs.CL, cs.CY. **Angenommen bei der COLM 2026.** Lizenz CC BY-NC-SA 4.0.
Abstract im Original gelesen, alle Zahlen wörtlich daraus.

*Hinweis zur Sorgfalt:* Ein erster Entwurf des Quellenblatts nannte das Papier einen „Vorabdruck ohne
abgeschlossene Begutachtung". Das war falsch, die arXiv-Seite weist die Annahme bei der COLM 2026 aus.
Vor dem Rendern korrigiert. Ebenso gestrichen wurde eine Angabe zu den Hochschulen der Autorenschaft,
weil die Abstract-Seite keine Zugehörigkeiten nennt.

## Zweite Quelle

Brian Jay Tang, Kaiwen Sun, Noah T. Curran, Florian Schaub, Kang G. Shin:
**„Ads that Talk Back: Implications and Perceptions of Injecting Personalized Advertising into LLM
Chatbots"**, arXiv 2409.15436, erschienen in Proceedings of the ACM on Interactive, Mobile, Wearable and
Ubiquitous Technologies 2025 (UbiComp). Begutachtete Veröffentlichung. Abstract im Original gelesen.

## Belegtabelle

| Aussage im Post | Fundstelle | Belastbarkeit |
|---|---|---|
| GPT 5.1 schob in 94 Prozent ein bezahltes Angebot dazwischen und störte den Kauf | Abstract: „surfacing sponsored options to disrupt the purchasing process (GPT 5.1, 94%)" | belastbar (Original, begutachtete Konferenz) |
| Grok 4.1 Fast empfahl in 83 Prozent ein fast doppelt so teures bezahltes Produkt | Abstract: „recommending a sponsored product almost twice as expensive (Grok 4.1 Fast, 83%)" | belastbar |
| Qwen 3 Next verschwieg in 24 Prozent den Preis bei ungünstigem Vergleich | Abstract: „concealing prices in unfavorable comparisons (Qwen 3 Next, 24%)" | belastbar |
| Die Mehrheit der Modelle opfert Nutzerwohl für Firmeninteressen | Abstract: „A majority of LLMs forsake user welfare for company incentives in a multitude of conflict of interest situations" | belastbar |
| Verhalten hängt von Denktiefe und unterstelltem sozialem Status ab | Abstract: „Behaviors vary strongly with levels of reasoning and users' inferred socio-economic status" | belastbar (nur in `post.md` vermerkt, nicht auf einem Blatt) |
| **Panel-Zitat:** „participants struggled to detect ads, and even preferred LLM responses with hidden advertisements." | „Ads that Talk Back", Abstract, Wortlaut geprüft | belastbar |
| Versuch mit 179 Teilnehmenden, Zwischensubjektdesign | „Ads that Talk Back", Abstract: „a between-subjects experiment with 179 participants" | belastbar |
| Leute versuchten die Werbeeinstellungen im Chat zu ändern statt auf den Hinweis zu tippen | „Ads that Talk Back", Abstract: „Rather than clicking on our advertising disclosure, participants tried changing their advertising settings using natural language queries" | belastbar |
| EuGH: Personalisierung von Werbung trägt kein berechtigtes Interesse | EuGH C-252/21 vom 04.07.2023, Rn. 117: „der Nutzer dieses Netzwerks vernünftigerweise nicht damit rechnen kann, dass der Betreiber dieses sozialen Netzwerks seine personenbezogenen Daten ohne seine Einwilligung zum Zweck der Personalisierung der Werbung verarbeitet" und weiter, die Verarbeitung könne „nicht unter Art. 6 Abs. 1 Unterabs. 1 Buchst. f DSGVO fallen" | belastbar (EUR-Lex, deutscher Wortlaut) |
| Werbung kommt in Gratisversion und in den bezahlten Tarif Go, Plus und Pro bleiben frei | dpa-Meldung vom 19.08.2026 sowie Fachdienste (etailment, onlinemarketing.de, borncity) | **berichtet**, keine Primärquelle |
| Auswahl zum Start nach Chatthema, ungefährem Standort, Gerätetyp; ältere Chats und Erinnerungen erst nach Zustimmung | dieselben Fachdienste, übereinstimmend | **berichtet** |

## Warum openai.com fehlt

`openai.com` antwortet aus dieser Umgebung durchgehend mit **HTTP 403**, geprüft am 18. und 19.08.2026
über drei Pfade (Ankündigungsseite, Alternativpfad, Hilfeartikel) und zusätzlich mit gesetztem
Browser-Kennzeichen. Die eigene Ankündigung und die Werberichtlinie konnten deshalb nicht gelesen werden.
Alles zum Produkt selbst ist damit **berichtet und nicht belegt**. Deshalb steht auf Blatt 02 kein
Startdatum und kein Preis, und auf dem Quellenblatt der Hinweis dazu.

## Offene Lücken

- **Der Kern des Posts misst nicht ChatGPT in Deutschland.** Die 94 Prozent stammen aus einem Aufbau, in
  dem die Forschenden den Modellen absichtlich einen Werbeanreiz gaben. Ob und wie stark OpenAI einen
  solchen Anreiz in das Produkt einbaut, ist unbekannt. Blatt 05 sagt das ausdrücklich. **Ohne dieses
  Blatt darf der Post nicht erscheinen.**
- **Keine Stellungnahme von OpenAI eingeholt.** Die Aussage zur unveränderten Antwortqualität stammt aus
  der Berichterstattung, nicht aus einer gelesenen Primärquelle.
- **Rechtsgrundlage ungeklärt.** Ob OpenAI die nicht personalisierte Werbung auf ein berechtigtes
  Interesse stützt, ließ sich nicht am Originaltext prüfen. Der EuGH-Hintergrund steht deshalb nur als
  allgemeine Rechtslage in der Caption, nicht als Aussage über OpenAI.
- **Digital Services Act nicht anwendbar geprüft.** Artikel 26 Absatz 3 der Verordnung (EU) 2022/2065
  untersagt Anbietern von Online-Plattformen Werbung „die auf Profiling gemäß Artikel 4 Nummer 4 der
  Verordnung (EU) 2016/679 unter Verwendung besonderer Kategorien personenbezogener Daten" beruht. Ob
  ChatGPT unter den Plattformbegriff fällt, ist offen und wurde nicht geklärt. Steht deshalb auf keinem
  Blatt.
- **Keine Gegenstimme zur Hauptstudie gefunden.** Für einen Folgepost wäre eine methodische Kritik
  wünschenswert.
- **Nur die Abstracts gelesen.** Bei beiden Studien wurden die Volltexte nicht ausgewertet. Die
  verwendeten Zahlen stehen alle im jeweiligen Abstract, die Messaufbauten dahinter sind ungeprüft.

## Rechtshinweis

Kein Rechtsrat. Der Post beschreibt veröffentlichte Untersuchungen und eine angekündigte
Produktänderung und bewertet keinen Einzelfall.

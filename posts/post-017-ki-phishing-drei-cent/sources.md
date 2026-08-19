# Quellen — Post 17 „Eine KI schreibt dir eine Phishing-Mail für drei Cent"

**Primärquelle:** Stefan Czybik (BIFOLD und TU Berlin), Anne Josiane Kouam (Inria und TU Berlin),
Peter Heubl (Ruhr-Universität Bochum), Jan Magnus Nold (Ruhr-Universität Bochum), Konrad Rieck
(BIFOLD und TU Berlin): „A Large-Scale Study of Personalized Phishing using Large Language Models",
USENIX Security Symposium 2026.
PDF unter `https://mlsec.tu-berlin.de/docs/2026-sec.pdf`, am 19.08.2026 heruntergeladen (272.239 Bytes,
20 Seiten) und in den Volltext überführt. Alle Zahlen und beide Panel-Zitate per Suche im extrahierten
Text bestätigt.

**Zur Zuschreibung:** Die Presse schreibt verbreitet „TU-Berlin-Studie". Der Feldversuch lief an der
**TU Braunschweig**, die Forschenden sitzen an der TU Berlin, bei Inria und an der Ruhr-Universität
Bochum. Die Danksagung nennt den Informationssicherheitsbeauftragten, den Datenschutzbeauftragten, die
Verwaltung und die Teilnehmenden der TU Braunschweig.

## Belegtabelle

| Aussage im Post | Fundstelle | Belastbarkeit |
|---|---|---|
| Feldversuch mit 7.700 Teilnehmenden | Abstract: „we evaluate the effectiveness of LLM-based spear phishing in an experiment with 7 700 participants" | belastbar (Primärquelle im Original) |
| Klickrate zugeschnittene KI-Mails 10,0 Prozent | Tabelle 2: Spear (LLM), 3.310 versandt, 3.177 zugestellt, 330 geklickt, 10,0 Prozent | belastbar |
| Klickrate von Hand zugeschnitten 24,2 Prozent | Tabelle 2: Spear (Manual), 100 versandt, 99 zugestellt, 24 geklickt, 24,2 Prozent | belastbar |
| Klickrate Massenmail von der KI 3,7 Prozent | Tabelle 2: Generic (LLM), 2.165 versandt, 1.735 zugestellt, 65 geklickt | belastbar |
| Klickrate Massenmail von Hand 4,1 Prozent | Tabelle 2: Generic (Manual), 2.166 versandt, 1.918 zugestellt, 79 geklickt | belastbar |
| Massenmails zusammen 3,9 Prozent | Anhang C, Zeile „All Generic": 3.653 zugestellt, 144 geklickt, 3,9 Prozent | belastbar |
| Von Hand zugeschnitten wirkt 2,4-mal so gut wie die Maschine | „Human-crafted spear phishing achieves the highest click rate overall, at 24.2 %, corresponding to a 2.4× higher success rate than the LLM-based variant (10.0 %)" | belastbar |
| Alle Unterschiede statistisch abgesichert | „All differences are statistically significant (p < 10−5)" | belastbar |
| Kosten rund drei US-Cent je Mail | Abstract: „the cost of personalization is minimal, with approximately $0.03 per email" | belastbar |
| 150 Dollar für 3.310 Personen | „We require a budget of only $150 to send personalized emails to all 3 310 users with publicly available information" | belastbar |
| **Panel-Zitat 1:** „flagged only 1 out of 3 949 emails when exposed to our attacks." | Abschnitt 7.2 Detection, Wortlaut per Suche bestätigt | belastbar als Zitat, **nicht** als Aussage über Filterwirksamkeit |
| **Panel-Zitat 2:** „the sending server is placed on the spam filter's whitelist, ensuring that no emails are flagged during delivery." | Abschnitt 5.3 „Execution of Study", Wortlaut per Suche bestätigt | belastbar als Zitat |
| Teilnehmende wurden vorher informiert, das verzerrt | „all participants receive a briefing before the study … Although these briefings introduce a bias by making participants aware of potential phishing" | belastbar |
| Zahlen sind eine Untergrenze | „The adversary uses only open-source models on local infrastructure, avoiding advanced evasion or prompt engineering, yielding a conservative lower bound" | belastbar |

## Der offene Widerspruch

Das ist die wichtigste Lücke dieses Posts und der Grund für die Bauform.

Abschnitt 7.2 nennt die Quote von einer markierten Mail auf 3.949 als Beleg dafür, dass allgemeine
Erkennung schwer ist. Der Studienaufbau beschreibt jedoch, dass der Versandserver auf die Whitelist des
Spamfilters gesetzt wurde, ausdrücklich „to avoid interference from automated defenses" und mit dem
Ergebnis, dass bei der Zustellung nichts markiert wird. Der Aufbau verweist an dieser Stelle selbst auf
Abschnitt 7.2, dort steht die Whitelist aber nicht mehr.

Möglich sind mindestens zwei Lesarten. Entweder betraf die Whitelist nur die Zustellung, während das
Sicherheitssystem weiter bewertete und diese Bewertung gemessen wurde. Oder die Whitelist hat das
Markieren unterdrückt, dann ist die Quote ein Artefakt des Aufbaus. **Das Papier sagt es nicht, und wir
können es nicht entscheiden.** Deshalb steht die Zahl auf Blatt 04 als Zitat und nicht als Befund.

*Offen und vor einem Folgepost zu klären:* eine Anfrage an die Erstautorenschaft, wie die Markierung
gemessen wurde.

## Weitere offene Punkte

- **Keine Gegenstimme eingeholt.** Zu dieser Studie liegt uns keine fachliche Kritik vor. Für einen
  Folgepost wäre eine Einordnung durch das BSI oder eine unabhängige Sicherheitsforschung sinnvoll.
- **Die Vergleichszahlen aus früheren Kampagnen** (OWA Password 2024 mit 5,3 Prozent, Webex Password 2024
  mit 7,0 Prozent) stehen im Papier, sind aber nicht Teil des kontrollierten Vergleichs und stehen
  deshalb nicht im Post.
- **Übertragbarkeit.** Der Versuch lief unter Hochschulbeschäftigten in Deutschland. Ob die Klickraten
  für andere Gruppen gelten, sagt das Papier nicht.
- **Rundungsabweichung im Papier selbst.** Für dieselbe Gruppe Generic (LLM), 65 Klicks auf 1.735
  zugestellte Mails, nennt Tabelle 2 den Wert 3,7 Prozent und eine Tabelle im Anhang 3,8 Prozent. Der
  rechnerische Wert liegt bei 3,746 Prozent. Der Post nimmt 3,7 Prozent aus der Haupttabelle. Die
  Abweichung ändert an der Aussage nichts, gehört aber genannt.

## Rechtshinweis

Kein Rechtsrat. Der Post beschreibt eine veröffentlichte Studie und bewertet keinen Einzelfall.

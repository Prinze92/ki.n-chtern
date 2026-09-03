# Quellen — Post 30

**Stand:** 02.09.2026. Alle Abrufe an diesem Tag.

## Belegtabelle

| Aussage im Post | Fundstelle | Belastbarkeit |
|---|---|---|
| **1.003** befragte Hausärzte, Erhebung **August 2025** über Doctors.net.uk | **P1** Blease u.a., „Ambient AI in primary care: an exploratory mixed methods survey of UK general practitioners", BMJ Health Care Inform 2026;33(1):e101847, DOI 10.1136/bmjhci-2025-101847, Volltext über Europe PMC (PMC13331185), CC BY 4.0 | belastbar (begutachtete Primärstudie) |
| **14 %** (141) nutzen, **39 %** (396) planen, **46 %** (466) nicht | P1, Ergebnisteil | belastbar |
| **32 %** (45 von 141) berichten Fehler „often/always", davon **14 %** (20) mit „significant-to-critical implications" | P1 | belastbar |
| **86 %** der Nutzer setzen dasselbe Produkt ein (Heidi Health) | P1 | belastbar |
| **63 %** (89 von 141; 95 % KI 54,9 bis 70,6) holen routinemäßig eine Einwilligung | P1 | belastbar |
| Bei **89 %** (79 von 89) dieser Ärzte lehnten **≤10 %** der Patienten ab | P1 | belastbar |
| Panel-Zitat „Notably, 37% of current users in this sample did not routinely seek patient consent" | P1, Schlussabsatz, Zeichen für Zeichen abgeglichen | belastbar |
| Fehlerhäufigkeit nach Gesprächstyp: **38 / 35 / 31 %** (Caption) | P1 | belastbar |
| **55 %** (78) halten die maschinelle Notiz für besser (Caption) | P1 | belastbar |
| Demyelinisierungs-Fall und Medikamentenverwechslung (Blatt 02) | **P2** The Guardian, 31.08.2026, „Doctors' AI scribes get names of drugs and diagnoses wrong, NHS watchdog warns", gestützt auf **Healthwatch England** | berichtet (Redaktion referiert die Patientenvertretung; die Healthwatch-Unterlagen selbst sind nicht gelesen) |
| Dragon Copilot **seit 07.10.2025** in Deutschland allgemein verfügbar | **P3** Microsoft Deutschland, „Nach erfolgreicher Pilotphase…", `news.microsoft.com/de-de/`, Veröffentlichungsdatum aus dem Metafeld `datePublished` (2025-10-07T08:46:22+00:00) | belastbar für die Tatsache der Verfügbarkeit; **Herstellermitteilung**, also Partei |
| **Fünf Kliniken** in der Preview (Charité, Universitätsklinikum Mannheim, Klinikum Stuttgart, Klinikum Region Hannover, BG Klinikum Bergmannstrost Halle) | P3 | berichtet (Herstellerangabe) |
| Charité begann am **31.03.2025** | P3 | berichtet (Herstellerangabe); die Charité selbst datiert ihre Mitteilung auf den **05.05.2025** (**P4**) und nennt kein Startdatum |
| Mithören über Raummikrofon oder Smartphone, nur mit Einverständnis; ärztliche Freigabe der Notiz | P3, bestätigt durch P4 („Sofern die Patient:innen und Ärzt:innen damit einverstanden sind…") | berichtet (beide Quellen sind Partei) |

## Ein Fehler, der beim Bauen aufgefallen ist

Der erste Entwurf von Blatt 05 lautete: „Die Charité erprobt seit Mai 2025 eine solche Software von
Microsoft." **Das wäre falsch veröffentlicht worden.** Die Testphase war laut Charité-Mitteilung auf
**sechs Monate** angelegt und damit spätestens im Herbst 2025 beendet. Microsoft hat Dragon Copilot am
07.10.2025 für Deutschland allgemein verfügbar gemacht.

Das ist derselbe Fehlertyp, der Post 28 am 01.09.2026 eingeholt hat: ein Satz über einen Zustand, der
sich seit der Quelle geändert hat. Hier ist er vor dem Rendern aufgefallen, weil die Checkliste den
Punkt enthielt und ich ihn sofort geprüft habe statt später. **Die Lehre gehört in `research/ideas.md`
und nicht in einen Korrektur-Post**, weil nichts Falsches veröffentlicht wurde.

## Was hier bewusst nicht behauptet wird

- **Keine Aussage über deutsche Fehlerquoten.** Die Studie ist britisch. Blatt 05 sagt ausdrücklich,
  dass sich die Zahlen nicht übertragen lassen.
- **Keine Aussage über die Rechtslage in Deutschland.** Ob und wie eine Einwilligung erforderlich ist,
  ist nicht Gegenstand des Posts.
- **Kein Vorwurf gegen einen Hersteller.** Der Post nennt Heidi Health nicht (nur „dasselbe Produkt")
  und stellt Microsoft mit dessen eigener Beschreibung dar.
- **Keine gemessenen Fehlerraten.** Alles sind Selbstauskünfte von 141 Ärzten. Blatt 01 sagt
  „berichtet", die Caption sagt es noch einmal.

## Offene Lücken

1. **Die Healthwatch-England-Unterlagen sind nicht gelesen.** Die beiden Fälle auf Blatt 02 stehen so
   im Guardian, der sich auf die Patientenvertretung stützt. Ein Bericht oder eine Mitteilung von
   Healthwatch selbst wurde nicht gefunden.
2. **Keine deutschen Zahlen.** Es gibt keine Erhebung unter deutschen Ärzten zu Fehlerquoten solcher
   Systeme, soweit am 02.09.2026 auffindbar. Auch die Auswertung der fünf Preview-Kliniken liegt nur
   als Zitat in der Herstellermitteilung vor („Unsere Auswertungen zeigen, dass sich der
   Dokumentationsaufwand … deutlich reduziert hat").
3. **Keine Stellungnahme** der Bundesärztekammer, des Bundesgesundheitsministeriums oder einer
   Datenschutzaufsicht zu KI-Mitschriften gefunden.
4. **Die Zeitschriftenseite ist gesperrt.** `informatics.bmj.com` antwortet aus dieser Umgebung mit
   **HTTP 403** und einer Cloudflare-Abfrage. Gelesen wurde der Volltext über Europe PMC. Das steht
   auf Blatt 06.
5. **Doctolib nicht geprüft.** heise schreibt, Doctolib biete solche Systeme an und trainiere
   KI-Modelle mit Gesundheitsdaten per Widerspruchslösung. Die Anbieterseite ist nicht gelesen,
   deshalb steht Doctolib nirgends im Post.
6. **Marketingzahlen bewusst weggelassen.** Die Microsoft-Mitteilung nennt eine eigene Umfrage, nach
   der 40 Prozent der befragten Patientinnen und Patienten schon einmal eine Konsultation erlebt
   hätten, bei der die behandelnde Person zu sehr auf den Bildschirm sah. Herstellerumfrage ohne
   Methodenangabe, nicht verwendet.

## Nachtrag vom 03.09.2026: zwei Lücken kleiner geworden

**1. Die fehlende Patientenperspektive ist jetzt belegt, und zwar systematisch.** In **Nature Health**
ist eine systematische Übersichtsarbeit erschienen: „Patient factors in medical artificial
intelligence: a systematic review", `nature.com/articles/s44360-026-00190-2`. **Abstract im Original
gelesen** (Volltext hinter Bezahlschranke), alle Zahlen daraus:
- **330** ausgewertete Arbeiten.
- Patientenzufriedenheit wird in **70,6 %** erhoben, wahrgenommener Nutzen in **69,4 %**.
- **Vertrauen nur in 16,7 %, Sicherheit aus Patientensicht nur in 10,9 %.**
- **89,4 %** der Erhebungen fallen in die Validierungsphase, nur **3,9 %** in Design und Entwicklung.
**Belastbarkeit: belastbar** für das Abstract.
**Warum das zu diesem Post gehört:** Die Studie, die Post 30 trägt, befragt ausschließlich Ärzte. Die
Übersichtsarbeit zeigt, dass das kein Einzelfall ist, sondern das Muster des Forschungsfelds. **Der
Post wird nicht geändert**, weil das ein eigenes Thema ist. Als Antwort auf die Frage „warum fragt
niemand die Patienten" ist es der beste vorhandene Beleg.

**2. Der Deutschlandbezug ist konkreter als auf Blatt 05.** Heidi, das Produkt, das laut der
britischen Studie **86 Prozent** der dortigen Nutzer einsetzen, baut seine Präsenz in Europa aus und
setzt gezielt auf Deutschland (heise online, Interview mit dem Global Chief Medical Officer des
australischen Unternehmens, der zuvor dieselbe Rolle bei Microsoft hatte). Nach Unternehmensangaben
unterstützt die Plattform mehr als 110 Sprachen.
**Belastbarkeit: berichtet.** Die im selben Beitrag genannte Civey-Umfrage entstand **im Auftrag von
Heidi**, ist also Auftragsforschung und wird nicht verwendet.
**Der Post wird nicht geändert**, weil Blatt 05 bereits einen belegten Deutschlandbezug hat und der
Produktname auf keinem Blatt steht. Für Nachfragen im Kommentarfeld ist der Zusammenhang aber wichtig:
Das in Großbritannien dominierende Produkt kommt hierher.

## Rechtshinweis

Der Post gibt Studienergebnisse und Unternehmensangaben wieder. Er bewertet keinen Einzelfall, ist
kein Rechtsrat und keine medizinische Auskunft. Der Hinweis steht auf Blatt 06.

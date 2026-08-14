# Themen-Pipeline (Backlog)

Wie wir entscheiden, was wir posten. Reihenfolge: **Idee → Recherche an Primärquellen → Entwurf → Post.**

## Regeln für die Aufnahme einer Idee

1. Passt sie zu einer Säule? (Betrifft dich · Fall der Woche · Hype-Check · Unbequeme Frage)
2. Betrifft der Fall den Zuschauer **selbst**? (Sonst ist es abstrakte Ethik → nachschärfen oder verwerfen.)
3. Gibt es eine **Primärquelle** mit Zahl/Datum? Wenn nein: noch nicht reif.
4. Ist es schon behandelt? → `../posts/posts.yaml` prüfen.

## Status je Idee: `roh → recherchiert → bereit → verplant`

| Idee | Säule | Aufhänger / Primärquelle | Status |
|------|-------|--------------------------|--------|
| KI in Bewerbungsverfahren, Frist verschoben | Betrifft dich | Verordnung (EU) 2026/1744 | verplant → Post 1 |
| „3 Mio. Arbeitslose = KI?" — Hype-Check | Hype-Check | Bundesagentur, Monatsbericht 07/2026 | verplant → Post 2 |
| Rechte bei automatischer Vorsortierung | Betrifft dich | DSGVO Art. 15/22, AGG | verplant → Post 3 |
| Kennzeichnungspflicht KI-Inhalte (Art. 50) — was gilt ab wann | Betrifft dich | AI Act Art. 50 | verplant → Post 4 |
| Betriebsrat & KI am Arbeitsplatz (Mitbestimmung) | Unbequeme Frage | BetrVG | roh |
| „KI-Lebenslauf-Optimierer" — Hype gegen Nutzen | Hype-Check | — (Primärbeleg fehlt noch) | roh |
| Palantir: öffentliches Geld rein, Steuern raus — wer kontrolliert die Behördendaten? | Unbequeme Frage | netzpolitik-Analyse (Steuer) + Palantir b. Polizei BY/HE/NRW (ZDF, taz) | recherchiert |
| KI-Wasser-/Stromverbrauch — warum die Zahlen so streuen | Hype-Check | Öko-Institut f. Greenpeace 2025; UN University (UNU) 2026 | recherchiert |
| Neuorientierung im KI-Zeitalter — Umbau statt Untergang | Betrifft dich | IAB-Befund (Umverteilung von Tätigkeiten) | roh |
| „Killt KI Jobs / die Programmierer?" — Verschiebung statt Verschwinden | Hype-Check | IAB/BIBB/GWS-Studie 2025 (netto ~Nullsumme) | verplant → Post 5 |
| „Die KI-Antwort ganz oben" — warum AI Overviews Stereotype/Fehler als Fakt zeigen | Betrifft dich | Google AI Overview (dokumentierte Fehlausgaben 2024); Mechanik: fasst Top-Ranking zusammen | roh |
| „Was du nicht in eine KI eintippst" — Datenschutz bei Eingaben | Betrifft dich | Bitkom-Studie 2026; DSGVO | verplant → Post 7 |
| KI-Wasserzeichen — was das unsichtbare Zeichen wirklich beweist | Betrifft dich | Anthropic/Google-Wasserzeichen; Art. 50; SynthID-Robustheit | verplant → Post 8 |
| Verhaltenserkennung Mannheim — wer belegt, dass es funktioniert? | Unbequeme Frage | Landtag BW 17/5816 (Stellungnahme IM 12.12.2023); § 44 PolG BW | verplant → Post 9 |
| Meta KI-Brille — was steckt drin, was passiert mit den Daten? | Betrifft dich | BfDI-FAQ; HateAid-Strafanzeige 12.08.2026 (§ 8 TDDDG); Nairobi-Recherche 02/2026 | verplant → Post 10 |
| „Löscht KI uns aus?" — was die Fachleute selbst schätzen | Unbequeme Frage | AI Impacts, „Thousands of AI Authors on the Future of AI" (2.778 Befragte, Median 5 %) | recherchiert |
| Wer der KI vertraut, prüft weniger. Wer sich selbst vertraut, prüft mehr | Betrifft dich | Microsoft Research + Carnegie Mellon, CHI 2025: 319 Berufstätige, 936 Arbeitsbeispiele | recherchiert |
| „AI washing" — steckt KI drin, wo KI draufsteht? | Hype-Check | SEC-Verfahren gegen Delphia, 18.03.2024, 225.000 $ Strafe (Aushilfen statt Algorithmus) | recherchiert |
| KI-Chatbots als Gesprächspartner von Kindern | Betrifft dich | DAK/UKE-Längsschnittstudie 03/2026 (rund 8 % gegen Einsamkeit, bei depressiven Symptomen über 30 %) | recherchiert |
| Werbung in ChatGPT — wovon hängt ab, was dir angezeigt wird? | Betrifft dich | OpenAI-Ankündigung; Rollout 11.08.2026 (UK, MX, BR, JP, KR) | roh |
| BMG lizenziert an Suno, 12 Tage nach dem GEMA-Urteil | Unbequeme Frage | LG München I 42 O 763/25; BMG-Mitteilung 12.08.2026 | roh |

> Die fünf Ideen oberhalb (Palantir … AI Overview) stammen aus der **Kommentar-Session (Aug 2026)** —
> externe Aufhänger bei @bundesagenturfuerarbeit, @netzpolitikorg, @zdfheute, @spiegelmagazin, @evolving.ai.
> Vor Status „bereit": jeweils die **Primärstudie/-quelle am Original prüfen** (Zahlen streuen bzw. noch ungeprüft).
> AI-Overview-Idee: den viralen „Romanian man"-Screenshot **nicht** als Beleg verwenden (unbestätigt) —
> stattdessen die dokumentierte Mechanik + belegte Fehlausgaben nutzen.

## Recherchierte Fakten für 3 Posts (11.08.2026, bereit zum Bauen)

**1. KI-Wasserverbrauch (Hype-Check / „Stimmt das?")** — belastbar: Schätzungen streuen **15- bis 75-fach**,
weil Anbieter nur den Verbrauch „im Moment der Anfrage" zählen, unabhängige Studien Standort +
Stromerzeugung mitrechnen. Altman (2025): ~0,32 ml/Anfrage (Methode nicht offengelegt). Unterschied
„water withdrawal" vs. „water consumption"; Standort (Dürreregion) entscheidend. Quellen: Öko-Institut,
UN University (via SMC), taz. → **Story ist nicht die Einzelzahl, sondern die Spannbreite.**

**2. „Killt KI Jobs?" (Hype-Check)** — belastbar: IAB/BIBB/GWS-Studie 2025 — ~**1,6 Mio. Stellen umverteilt**
(auf-/abgebaut), **netto ~Nullsumme** über 15 Jahre; BIP **+0,8 Pp/Jahr** (~4,5 Bio. € kumuliert). „Umbruch,
nicht weniger Arbeit." Gegenstimme (DIW): Risiko für die Mittelschicht. Quelle: IAB-Forschungsbericht 2025.
→ **Verschiebung statt Vernichtung — mit ehrlichem Haken (Umbau/Mittelschicht).**

**3. Palantir / Behörden-KI (Unbequeme Frage)** — belastbar (DE-Einsatz): Palantir bei Polizei in **Bayern
(VeRA, ~39 Mio. Datensätze), Hessen, NRW (DAR)**, Kosten zweistellige Mio.; Justizministerin Hubig sieht es
nicht auf Bundesebene (ZDF, taz). Steuer-Aussage (Gewinnverlagerung USA) = netzpolitik-Analyse →
**zuschreiben, nicht als eigener Beleg**. → **Öffentliches Geld rein, Steuern raus — wer kontrolliert die Daten?**

## Nachrück-Ideen (unsortiert, roh)

- KI-Bilder-Kennzeichnung im Alltag: woran erkennt man sie, was schreibt das Gesetz vor? → weitgehend durch **Post 4** abgedeckt.
- Behörden & KI: Bescheide, die eine Software vorbereitet — wer haftet? → siehe **Palantir-Idee** oben.
- „KI spart X Stunden" — woher kommt die Zahl wirklich? → verwandt mit **KI-Wasser-/Stromverbrauch** (Zahlen-Herkunft).

> **Zeitfalle beachten:** Säule „Fall der Woche" nur EIN Thema pro Woche. Genauer, nicht schneller.

## Kommentar-Fundus (aus Kommentar-Sessions, zu lang fürs Kommentarfeld)

**Drei Szenarien zur Auslöschungsfrage** (14.08.2026, Anlass: FAZ-Podcast aus Lindau).
Beantwortet die abstrakte Frage über die dokumentierte Einschätzung der Fachleute statt über Spekulation.
Belastbar ist nur die Zahl, die Szenarien sind ausdrücklich Annahmen.

1. **Kein Aussterben, aber Machtverschiebung.** Der Schaden kommt als Verlagerung von Entscheidungen zu
   wenigen, die die Systeme besitzen, nicht als Katastrophe.
2. **Kontrollverlust.** Systeme werden autonomer, die Kontrolle hinkt hinterher. Das ist die Sorge hinter
   dem Median von 5 Prozent.
3. **Der Hype selbst ist der Schaden.** Wer über Aussterben redet, redet nicht über Bewerbungssoftware,
   Verhaltenserkennung und Datenarbeit in Nairobi. Aufmerksamkeit ist endlich.

> Für einen eigenen Post über Szenario 3 aufziehen, weil das den Bogen zurück zum Konkreten schlägt.
> Die abstrakte Fassung widerspricht dem Leitprinzip („Ethik nie abstrakt, immer am Einzelfall").

## Recherchierte Einzelbefunde (Stand 14.08.2026)

**Kritisches Denken unter KI-Nutzung** — Microsoft Research und Carnegie Mellon University, CHI 2025,
„The Impact of Generative AI on Critical Thinking". Befragt wurden **319 Berufstätige** zu **936 konkreten
Arbeitsbeispielen**. Zwei Befunde, die gegenläufig sind und deshalb den Post tragen:
höheres **Vertrauen in die KI** ging mit **weniger** kritischem Denken einher, höheres Vertrauen in die
**eigenen Fähigkeiten** mit **mehr**. Beschrieben wird außerdem die Verschiebung vom Lösen zum Zusammenfügen
und vom Machen zum Beaufsichtigen.
*Einschränkungen, die in den Post gehören:* Selbstauskunft statt gemessener Leistung, und befragt wurden
Berufstätige, keine Schülerinnen oder Studierenden.
→ Möglicher Aufhänger: der US-Professor, dessen Studierende seit 30 Jahren dieselbe Interview-Hausarbeit
schreiben und inzwischen fragen, woran man erkennt, ob etwas interessant ist. Anekdote als Einstieg,
die Messung als Beleg.

**AI washing** — US-Börsenaufsicht SEC, Verfahren vom **18.03.2024** gegen den Anlageberater Delphia:
warb mit maschinellem Lernen, ließ die Geschäfte aber von Aushilfen von Hand ausführen. **225.000 Dollar**
Strafe. Seit 2026 gibt es dafür bei der SEC eine eigene Einheit (Cyber and Emerging Technologies Unit).
Gegenstück als Aufhänger: Tucker Bryant aus San Francisco, dessen „KI-Chatbot" ChatTJB er selbst von Hand
bediente, 6.000 Dollar Werbetafel, „AI" stand dort für „average individual".
*Vor dem Bauen prüfen:* deutschsprachige Fälle suchen, damit der Post die Leserinnen und Leser hier betrifft.

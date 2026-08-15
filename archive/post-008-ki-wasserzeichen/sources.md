# Quellen — Post 8 (KI-Wasserzeichen)

Belastbarkeit: **belastbar** = mehrfach unabhängig bestätigt / Primärquelle. Recherchiert: **13.08.2026**.

| Aussage im Post | Quelle | Belastbarkeit |
|---|---|---|
| Anthropic markiert Text neuer Claude-Modelle seit 02.08.2026 mit maschinenlesbaren, unsichtbaren (statistischen) Wasserzeichen; Dateien per C2PA-Signatur; weltweit | Mehrere Fachmedien (Aug 2026: interestingengineering, cybersecuritynews, techtimes, qz u. a.), ausgelöst durch Art. 50 | belastbar (mehrfach übereinstimmend) |
| Google macht dasselbe für Gemini mit SynthID (statistisches Text-Wasserzeichen) | Google DeepMind SynthID (Dokumentation + Forschung) | belastbar |
| Ein Treffer beweist „verarbeitet", nicht „verfasst" (eigener Text zum Korrigieren bekommt das Zeichen) | Berichterstattung zum Claude-Wasserzeichen (explizit so benannt) | belastbar |
| Statistische Wasserzeichen sind durch Umformulieren, Rückübersetzung, „Humanizer" entfernbar; an SynthID getestet | Robustheitsstudien zu SynthID-Text (arXiv u. a.) | belastbar |
| AI Act, Art. 50 verlangt maschinenlesbare Kennzeichnung von KI-Ausgaben | EU AI Act, Art. 50 (Abs. 2), siehe auch `../archive/post-004-…/sources.md` | belastbar |

## Einordnung / Neutralität

- Der Post korrigiert die viral verzerrte Zuspitzung „nur Anthropic, heimlich". Richtig: Es ist eine
  **gesetzliche Pflicht für alle Anbieter** (Art. 50), Google setzt es mit SynthID um. Deshalb werden
  **beide Firmen** genannt.
- Thema betrifft die **eigene Firma** (Claude). Bewusst faktisch, inklusive der unbequemen Grenzen
  (entfernbar, beweist keine Autorschaft). Kein Werbe- und kein Angriffston.

## Prüfhinweis

- Vor Status `geprüft`: Anthropics **Primärankündigung** und mindestens eine **SynthID-Robustheitsstudie**
  direkt gegenlesen. Robustheit von Anthropics konkretem Verfahren ist im Detail weniger dokumentiert
  als bei SynthID; der Post argumentiert daher allgemein über statistische Wasserzeichen.

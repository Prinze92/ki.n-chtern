"""
build_slides.py — Renderer für ki.nüchtern (Logo + Carousel-Blätter).

Herkunft: mobile Session. Hier angepasst für plattformunabhängigen Betrieb:
  - Ausgabepfade sind repo-relativ (nicht mehr /mnt/user-data/outputs).
  - Schriften werden über find_font() gesucht (brand/fonts/ -> OS-Fonts -> Fallback),
    statt fester Linux-Pfade.
  - Jeder Post ist eine eigene build_postN()-Funktion; frame()/new() bekommen die
    Blattzahl als Parameter, damit die Kopf-/Fußzeile pro Post stimmt.

OFFEN (docs/handoff.md §12, Punkt 4): echte Marken-Schriften (Oswald / Archivo Narrow,
JetBrains/IBM Plex Mono) nach ../brand/fonts/ legen und in FONT_ROLES eintragen. Solange sie
fehlen, rendert das Skript mit dem besten verfügbaren Fallback und WARNT auf der Konsole.

Aufruf:  python render/build_slides.py
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import sys

# ---------------------------------------------------------------- pfade
REPO = Path(__file__).resolve().parent.parent
FONTS_DIR = REPO / "brand" / "fonts"
OUT_LOGO = REPO / "brand" / "logo"
# Aktive Posts (in Arbeit / postbereit) — werden gerendert:
# Gepostet & archiviert: Post 0/1/2/4/5/6/7/8/9/10/13 liegen unter archive/ (veröffentlichter Stand). Sie werden
# NICHT mehr aktiv gerendert, damit die publizierten PNGs nicht versehentlich überschrieben werden
# (z. B. bei einer Änderung an frame()/STAND). Die Funktionen build_intro/build_post1/build_post4/
# build_post2/5/6/7/8/9/10/13 bleiben unten als Reproduzierbarkeits-Referenz erhalten.
# Post 11 (Korrektur) wurde am 16.08.2026 verworfen; Ordner und build_post11() geloescht,
# wiederherstellbar ueber die Git-Historie (wie seinerzeit Post 3).
# Hinweis: Post 0/1/4/6/7/9 wurden mit Kicker 30 veroeffentlicht, Post 2/5/8/10/13 mit Kicker 38.
# Beide geben ihre Groesse deshalb ausdruecklich am kicker()-Aufruf an.
# Posts 12/14/15/16 sind am 19.08.2026 gepostet und nach archive/ gewandert.
# Ihre build_postN()-Funktionen bleiben als Vorlage stehen, werden aber nicht mehr
# aufgerufen. Archivierte Blaetter werden nie neu gerendert (siehe CLAUDE.md).
OUT_STORY = REPO / "brand" / "stories"
for _d in (OUT_LOGO, OUT_STORY):
    _d.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- palette
PAPER = (243, 241, 235)
INK = (20, 20, 26)
RED = (196, 48, 43)
MUTED = (138, 136, 128)
RULE = (206, 202, 192)
PANEL = (233, 230, 222)

# ---------------------------------------------------------------- fonts
# Jede Rolle: Liste von Kandidaten-Dateinamen, in Vorzugsreihenfolge.
# Gesucht wird in brand/fonts/, dann in typischen OS-Font-Verzeichnissen.
FONT_ROLES = {
    "BOLD":  ["Archivo-Bold.ttf", "Oswald-Bold.ttf", "DejaVuSans-Bold.ttf", "arialbd.ttf", "Arial Bold.ttf"],
    "BOOK":  ["Archivo-Regular.ttf", "Oswald-Regular.ttf", "DejaVuSans.ttf", "arial.ttf", "Arial.ttf"],
    "COND":  ["Oswald-Bold.ttf", "ArchivoNarrow-Bold.ttf", "DejaVuSansCondensed-Bold.ttf", "arialbd.ttf"],
    "MONO":  ["JetBrainsMono-Regular.ttf", "IBMPlexMono-Regular.ttf", "DejaVuSansMono.ttf", "consola.ttf"],
    "MONOB": ["JetBrainsMono-Bold.ttf", "IBMPlexMono-Bold.ttf", "DejaVuSansMono-Bold.ttf", "consolab.ttf"],
}

_OS_FONT_DIRS = [
    Path("C:/Windows/Fonts"),
    Path("/usr/share/fonts/truetype/dejavu"),
    Path("/usr/share/fonts"),
    Path("/Library/Fonts"),
]
_font_cache = {}
_warned = set()


def _resolve(role):
    if role in _font_cache:
        return _font_cache[role]
    for name in FONT_ROLES[role]:
        for base in [FONTS_DIR, *_OS_FONT_DIRS]:
            p = base / name
            if p.exists():
                _font_cache[role] = str(p)
                return str(p)
    if role not in _warned:
        print(f"WARN: keine Schrift für Rolle {role} gefunden — nutze PIL-Standard "
              f"(Layout wird abweichen). Kandidaten: {FONT_ROLES[role]}", file=sys.stderr)
        _warned.add(role)
    _font_cache[role] = None
    return None


def font(role, size):
    path = _resolve(role)
    if path is None:
        return ImageFont.load_default()
    return ImageFont.truetype(path, size)


# Kurz-Helfer, damit der Rest des Skripts unverändert bleibt.
def f(role, size):
    return font(role, size)


# ---------------------------------------------------------------- caret mark
def caret(draw, cx, cy, w, thick, color):
    """Korrekturzeichen (Einfügezeichen) — Spitze nach oben."""
    h = w * 0.62
    p_left = (cx - w / 2, cy + h / 2)
    p_top = (cx, cy - h / 2)
    p_right = (cx + w / 2, cy + h / 2)
    draw.line([p_left, p_top, p_right], fill=color, width=thick, joint="curve")


# ---------------------------------------------------------------- logo files
def logo_square(size, bg, fg_caret, fg_text, filename, with_text=True):
    img = Image.new("RGB", (size, size), bg)
    d = ImageDraw.Draw(img)
    s = size / 1000.0
    if with_text:
        fo = f("COND", int(400 * s))
        t = "ki"
        bbox = d.textbbox((0, 0), t, font=fo)
        tw = bbox[2] - bbox[0]
        ty = size * 0.26
        tx = (size - tw) / 2 - bbox[0]
        d.text((tx, ty), t, font=fo, fill=fg_text)
        # Korrekturzeichen mit festem Abstand UNTER der gemessenen Wortmarke —
        # fontunabhängig, damit es nicht mit den Buchstaben kollidiert.
        letter_bottom = ty + bbox[3]
        caret(d, size / 2, letter_bottom + size * 0.06, size * 0.20, int(34 * s), fg_caret)
    else:
        caret(d, size / 2, size / 2, size * 0.46, int(72 * s), fg_caret)
    img.save(OUT_LOGO / filename, "PNG")
    return img


logo_square(1000, PAPER, RED, INK, "profilbild_hell.png")
logo_square(1000, INK, RED, PAPER, "profilbild_dunkel.png")
logo_square(1000, PAPER, RED, INK, "bildmarke_pur.png", with_text=False)

# horizontal wordmark
wm = Image.new("RGB", (1600, 440), PAPER)
d = ImageDraw.Draw(wm)
fo = f("COND", 150)
wm_t = "ki.nüchtern"
d.text((110, 90), wm_t, font=fo, fill=INK)
bb = d.textbbox((110, 90), wm_t, font=fo)
tw = bb[2] - bb[0]
caret(d, 110 + tw / 2, bb[3] + 34, 90, 18, RED)
fo2 = f("MONO", 36)
d.text((110, bb[3] + 66), "OHNE HYPE. MIT QUELLE.", font=fo2, fill=MUTED)
wm.save(OUT_LOGO / "wortmarke.png", "PNG")


# ---------------------------------------------------------------- avatar (profilbild)
def avatar(bg, fg, caret_color, filename, size=1000):
    """Straffe Profilbild-Variante: großes 'ki' + integrierter Caret, für den
    kreisförmigen Instagram-Zuschnitt gedacht (Vollflächen-Quadrat, füllt den Rahmen)."""
    img = Image.new("RGB", (size, size), bg)
    d = ImageDraw.Draw(img)
    fo = f("COND", int(560 * size / 1000))
    t = "ki"
    bb = d.textbbox((0, 0), t, font=fo)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    gap = size * 0.056
    caret_w = tw * 0.66
    caret_h = caret_w * 0.62
    top = (size - (th + gap + caret_h)) / 2
    d.text(((size - tw) / 2 - bb[0], top - bb[1]), t, font=fo, fill=fg)
    caret(d, size / 2, top + th + gap + caret_h / 2, caret_w, int(62 * size / 1000), caret_color)
    img.save(OUT_LOGO / filename, "PNG")


avatar(PAPER, INK, RED, "avatar_hell.png")
avatar(INK, PAPER, RED, "avatar_dunkel.png")
avatar(RED, PAPER, PAPER, "avatar_rot.png")


# ---------------------------------------------------------------- slide frame
W, H = 1080, 1350
M = 100
MAXW = W - 2 * M
STAND = "STAND 13.08.2026"          # Vorgabe; je Post via new(..., stand=) überschreibbar


def wrap(d, text, fnt, maxw):
    out, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out


def block(d, y, text, fnt, fill, maxw=MAXW, lead=1.34, after=0, x=M):
    lh = int(fnt.size * lead)
    for ln in wrap(d, text, fnt, maxw):
        d.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y + after


def frame(d, idx, total, stand=None):
    d.line([(M, 84), (W - M, 84)], fill=INK, width=3)
    d.line([(M, 94), (W - M, 94)], fill=RULE, width=2)
    caret(d, M + 16, 140, 34, 7, RED)
    fo = f("MONOB", 27)
    d.text((M + 48, 126), "KI.NÜCHTERN", font=fo, fill=INK)
    lab = f"BLATT {idx:02d}/{total:02d}"
    d.text((W - M - d.textlength(lab, font=fo), 126), lab, font=fo, fill=MUTED)

    d.line([(M, H - 150), (W - M, H - 150)], fill=RULE, width=2)
    fo = f("MONO", 25)
    d.text((M, H - 128), stand or STAND, font=fo, fill=MUTED)
    r = f"QUELLEN → BLATT {total:02d}"
    d.text((W - M - d.textlength(r, font=fo), H - 128), r, font=fo, fill=MUTED)


def kicker(d, y, text, color=RED, size=38):
    """Kicker-Zeile. size=38 ist der Standard fuer neue Posts (Lesbarkeit auf dem Handy).
    Archivierte Posts uebergeben size=30, damit ihr veroeffentlichter Stand reproduzierbar bleibt.

    Bricht NICHT um. Zu langer Text lief frueher still rechts aus dem Blatt, das ist in
    Post 13 (Blatt 03 und 05) so veroeffentlicht worden und fiel erst am 18.08.2026 auf.
    Deshalb bricht der Lauf hier jetzt ab, statt ein kaputtes Blatt zu schreiben.
    Kicker kuerzen, nicht die Schrift verkleinern (siehe CLAUDE.md)."""
    fo = f("MONOB", size)
    breite = fo.getbbox(text.upper())[2]
    if breite > W - 2 * M:
        raise ValueError(
            f"Kicker zu lang: {breite} px bei erlaubten {W - 2 * M} px (size={size}).\n"
            f"  Text: {text!r}\n"
            f"  Kuerzen. kicker() bricht nicht um, der Text liefe sonst aus dem Blatt."
        )
    d.text((M, y), text.upper(), font=fo, fill=color)
    y += round(size * 1.5333)
    d.line([(M, y), (M + size * 3, y)], fill=color, width=round(size * 0.1667))
    return y + round(size * 1.7333)


def beleg(d, y, kopf, zeilen, sub=None):
    """Beleg-Panel: Quelle als sichtbares Objekt statt als Fließtext.
    Beiges Feld, roter Balken links, Monospace. Verallgemeinert das Muster
    aus Post 1, Blatt 05. Gibt die Unterkante zurück."""
    pad = 44
    h = pad + 38 + (62 if sub else 0) + len(zeilen) * 46 + pad
    d.rectangle([M, y, W - M, y + h], fill=PANEL)
    d.line([(M, y), (M, y + h)], fill=RED, width=8)
    ty = y + pad
    d.text((M + pad, ty), kopf.upper(), font=f("MONOB", 30), fill=INK)
    ty += 38
    if sub:
        ty += 14
        d.text((M + pad, ty), sub, font=f("MONO", 26), fill=MUTED)
        ty += 48
    for ln in zeilen:
        d.text((M + pad, ty), ln, font=f("MONO", 28), fill=INK)
        ty += 46
    return y + h


def balken(d, y, reihen):
    """Waagerechte Balken für Zahlenreihen. reihen = [(label, wert, anzeige)].
    Lineare Skala, damit die Größenverhältnisse ehrlich bleiben."""
    hoechst = max(w for _, w, _ in reihen) or 1
    bahn = MAXW - 300
    for label, wert, anzeige in reihen:
        d.text((M, y), label, font=f("MONO", 26), fill=MUTED)
        by = y + 36
        bw = max(6, int(bahn * wert / hoechst))
        d.rectangle([M, by, M + bw, by + 40], fill=RED)
        d.text((M + bw + 20, by - 4), anzeige, font=f("BOOK", 34), fill=INK)
        y = by + 40 + 40
    return y


def new(idx, total, stand=None):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    frame(d, idx, total, stand)
    return img, d


# ================================================================ POST 1
def build_post1():
    T = 9
    slides = []

    # --- 01 HOOK
    img, d = new(1, T)
    y = 300
    fo = f("COND", 104)
    for line in ["DEINE", "BEWERBUNG", "SORTIERT EINE", "SOFTWARE AUS."]:
        d.text((M, y), line, font=fo, fill=INK)
        y += 118
    y += 40
    d.line([(M, y), (M + 140, y)], fill=RED, width=6)
    y += 54
    y = block(d, y, "Kein Mensch — eine KI.", f("COND", 46), INK, MAXW, 1.3, 26)
    block(d, y, "Und die Regel dafür wurde vor zwei Wochen verschoben. "
                "Fast alle Ratgeber im Netz sind seitdem falsch.",
          f("BOOK", 44), INK, MAXW - 40, 1.4)
    slides.append(img)

    # --- 02 DER FALL
    img, d = new(2, T)
    y = kicker(d, 300, "Der Fall", size=30)
    block(d, y, "Größere Unternehmen setzen Software ein, die Lebensläufe liest, "
                "bewertet und in eine Rangfolge bringt — bevor ein Mensch sie sieht.",
          f("BOOK", 52), INK, MAXW, 1.42)
    slides.append(img)

    # --- 03 WAS ÜBERALL STEHT
    img, d = new(3, T)
    y = kicker(d, 270, "Was überall steht", MUTED)
    y = block(d, y, '„Ab diesem Datum gelten strenge EU-Pflichten für genau '
                    'diese Systeme.“', f("BOOK", 48), INK, MAXW, 1.4, 60)
    fo = f("COND", 88)
    d.text((M, y), "2. AUGUST 2026", font=fo, fill=INK)
    y += 130
    block(d, y, "Risikomanagement. Menschliche Aufsicht. Dokumentation.",
          f("BOOK", 38), MUTED, MAXW, 1.4)
    slides.append(img)

    # --- 04 DIE KORREKTUR  (Signatur-Blatt)
    img, d = new(4, T)
    y = kicker(d, 250, "Die Korrektur", size=30)
    fo = f("COND", 84)
    d.text((M, y), "2. AUGUST 2026", font=fo, fill=MUTED)
    tw = d.textlength("2. AUGUST 2026", font=fo)
    d.line([(M - 14, y + 58), (M + tw + 14, y + 52)], fill=RED, width=11)
    y += 130
    caret(d, M + 30, y + 26, 46, 9, RED)
    d.text((M + 80, y), "2. DEZEMBER 2027", font=f("COND", 72), fill=RED)
    y += 130
    y = block(d, y, "Am 27. Juli 2026 ist die Digital-Omnibus-Verordnung in Kraft "
                    "getreten. Die Pflichten für Bewerbungs-KI greifen 16 Monate "
                    "später als angekündigt.", f("BOOK", 42), INK, MAXW, 1.4)
    slides.append(img)

    # --- 05 DER BELEG
    img, d = new(5, T)
    y = kicker(d, 250, "Der Beleg", size=30)
    d.rectangle([M, y, W - M, y + 330], fill=PANEL)
    d.line([(M, y), (M, y + 330)], fill=RED, width=8)
    ty = y + 44
    fo = f("MONOB", 30)
    d.text((M + 44, ty), "VERORDNUNG (EU) 2026/1744", font=fo, fill=INK)
    ty += 58
    fo = f("MONO", 28)
    for ln in ['„Digital Omnibus on AI“',
               "In Kraft: 27.07.2026",
               "Anhang III (Beschäftigung):",
               "Geltungsbeginn 02.12.2027"]:
        d.text((M + 44, ty), ln, font=fo, fill=INK)
        ty += 46
    y += 390
    block(d, y, "Nicht meine Meinung. Ein Amtsblatt.", f("BOOK", 44), INK, MAXW, 1.4)
    slides.append(img)

    # --- 06 DER HAKEN
    img, d = new(6, T)
    y = kicker(d, 250, "Der Haken", size=30)
    y = block(d, y, '„Verschoben“ heißt nicht „erlaubt“.', f("COND", 66), INK, MAXW, 1.3, 50)
    y = block(d, y, "DSGVO, BDSG, AGG und die Mitbestimmung des Betriebsrats gelten "
                    "unverändert weiter.", f("BOOK", 46), INK, MAXW, 1.42, 44)
    block(d, y, "Und die Kennzeichnungspflicht für KI-Inhalte bleibt beim "
                "2. August 2026.", f("BOOK", 38), MUTED, MAXW, 1.42)
    slides.append(img)

    # --- 07 FÜR DICH
    img, d = new(7, T)
    y = kicker(d, 240, "Was das für dich heißt", size=30)
    for it in ["Eine Software darf sortieren.",
               "Über die Absage entscheiden darf sie nicht allein.",
               "Dein Auskunftsrecht bleibt bestehen."]:
        caret(d, M + 20, y + 30, 34, 7, RED)
        yy = y
        for ln in wrap(d, it, f("BOOK", 48), MAXW - 80):
            d.text((M + 76, yy), ln, font=f("BOOK", 48), fill=INK)
            yy += int(48 * 1.34)
        y = yy + 48
    slides.append(img)

    # --- 08 OFFENE FRAGE
    img, d = new(8, T)
    y = kicker(d, 320, "Die offene Frage", MUTED)
    y = block(d, y, "16 Monate mehr Zeit für Unternehmen.", f("COND", 72), INK, MAXW, 1.24, 30)
    y = block(d, y, "Wer trägt sie in der Zwischenzeit?", f("COND", 72), RED, MAXW, 1.24, 70)
    block(d, y, "Schreib es in die Kommentare.", f("BOOK", 40), MUTED, MAXW, 1.4)
    slides.append(img)

    # --- 09 QUELLEN
    img, d = new(9, T)
    y = kicker(d, 230, "Quellen", size=30)
    for s in ["Verordnung (EU) 2026/1744 — Digital Omnibus on AI, in Kraft seit 27.07.2026",
              "EU AI Act, Anhang III — Beschäftigung und Personalauswahl",
              "EU AI Act, Artikel 50 — Transparenz- und Kennzeichnungspflichten"]:
        caret(d, M + 18, y + 24, 30, 6, RED)
        yy = y
        for ln in wrap(d, s, f("BOOK", 36), MAXW - 70):
            d.text((M + 66, yy), ln, font=f("BOOK", 36), fill=INK)
            yy += int(36 * 1.38)
        y = yy + 34
    y += 24
    d.line([(M, y), (W - M, y)], fill=RULE, width=2)
    y += 42
    y = block(d, y, "Keine Rechtsberatung. Im Einzelfall: Fachanwalt für Arbeitsrecht.",
              f("BOOK", 34), MUTED, MAXW, 1.4, 34)
    block(d, y, "Fehler gefunden? Schreib es in die Kommentare — ich korrigiere sichtbar.",
          f("BOOK", 34), RED, MAXW, 1.4)
    slides.append(img)

    return slides


# ================================================================ POST 2
def build_post2():
    T = 8
    slides = []

    # --- 01 HOOK
    img, d = new(1, T)
    y = 300
    fo = f("COND", 104)
    for line in ["3.007.000", "ARBEITSLOSE."]:
        d.text((M, y), line, font=fo, fill=INK)
        y += 118
    y += 40
    d.line([(M, y), (M + 140, y)], fill=RED, width=6)
    y += 54
    block(d, y, "Es war nicht die KI. Und die Zahl sagt etwas anderes, "
                "als beide Lager behaupten.",
          f("BOOK", 48), INK, MAXW - 40, 1.4)
    slides.append(img)

    # --- 02 DER FALL
    img, d = new(2, T)
    y = kicker(d, 280, "Der Fall", size=38)
    y = block(d, y, "Juli 2026: über drei Millionen Arbeitslose, "
                    "Quote 6,4 %.", f("BOOK", 54), INK, MAXW, 1.42, 40)
    block(d, y, "71.000 mehr als im Vormonat.",
          f("BOOK", 46), MUTED, MAXW, 1.42)
    slides.append(img)

    # --- 03 WAS DARAUS GEMACHT WIRD
    img, d = new(3, T)
    y = kicker(d, 300, "Was daraus gemacht wird", MUTED)
    block(d, y, '„Die Automatisierung frisst die Jobs.“',
          f("COND", 72), INK, MAXW, 1.3)
    slides.append(img)

    # --- 04 WAS DIE ZAHLEN ZEIGEN  (Korrektur-Motiv)
    img, d = new(4, T)
    y = kicker(d, 250, "Was die Zahlen zeigen", size=38)
    fo = f("COND", 84)
    d.text((M, y), "+71.000 im Monat", font=fo, fill=MUTED)
    tw = d.textlength("+71.000 im Monat", font=fo)
    d.line([(M - 14, y + 58), (M + tw + 14, y + 52)], fill=RED, width=11)
    y += 130
    caret(d, M + 30, y + 26, 46, 9, RED)
    d.text((M + 80, y), "+6.000 saisonbereinigt", font=f("COND", 60), fill=RED)
    y += 120
    block(d, y, "Der Rest ist Sommerpause — Bau, Dienstleistung, Ferienzeit. "
                "Jedes Jahr dasselbe Muster.", f("BOOK", 46), INK, MAXW, 1.4)
    slides.append(img)

    # --- 05 DER EIGENTLICHE BEFUND
    img, d = new(5, T)
    y = kicker(d, 230, "Der eigentliche Befund", size=38)
    fo = f("COND", 96)
    d.text((M, y), "223.000", font=fo, fill=INK)
    y += 112
    d.text((M, y), "ERWERBSTÄTIGE WENIGER ALS VOR EINEM JAHR", font=f("MONOB", 28), fill=MUTED)
    y += 84
    y = block(d, y, "Bei 45,54 Mio. insgesamt — und der Rückgang zieht sich "
                    "seit Anfang 2025.", f("BOOK", 46), INK, MAXW, 1.4, 34)
    block(d, y, "Konjunktur und Struktur. Nicht Software.",
          f("COND", 52), RED, MAXW, 1.3)
    slides.append(img)

    # --- 06 UND TROTZDEM
    img, d = new(6, T)
    y = kicker(d, 250, "Und trotzdem", size=38)
    fo = f("COND", 96)
    d.text((M, y), "653.000", font=fo, fill=INK)
    y += 112
    d.text((M, y), "OFFENE STELLEN — 25.000 MEHR ALS IM VORJAHR", font=f("MONOB", 28), fill=MUTED)
    y += 90
    block(d, y, "Falsche Leute in schrumpfenden Branchen, zu wenige in "
                "wachsenden. Ein Struktur-, kein Software-Problem.",
          f("BOOK", 46), INK, MAXW, 1.4)
    slides.append(img)

    # --- 07 OFFENE FRAGE
    img, d = new(7, T)
    y = kicker(d, 300, "Die offene Frage", MUTED)
    y = block(d, y, "Wenn KI heute noch nicht der Grund ist —",
              f("COND", 64), INK, MAXW, 1.26, 30)
    y = block(d, y, "wie erkennst du, wann sie es wird?",
              f("COND", 64), RED, MAXW, 1.26, 70)
    block(d, y, "Schreib es in die Kommentare.", f("BOOK", 44), MUTED, MAXW, 1.4)
    slides.append(img)

    # --- 08 QUELLEN
    img, d = new(8, T)
    y = kicker(d, 230, "Quellen", size=38)
    for s in ["Bundesagentur für Arbeit — Der Arbeitsmarkt im Juli 2026 (Bericht vom 31.07.2026)",
              "Statistisches Bundesamt — Erwerbstätigkeit, Juni 2026",
              "Roh- und saisonbereinigte Werte je aus den amtlichen Berichten"]:
        caret(d, M + 18, y + 24, 30, 6, RED)
        yy = y
        for ln in wrap(d, s, f("BOOK", 40), MAXW - 70):
            d.text((M + 66, yy), ln, font=f("BOOK", 40), fill=INK)
            yy += int(36 * 1.38)
        y = yy + 34
    y += 24
    d.line([(M, y), (W - M, y)], fill=RULE, width=2)
    y += 42
    y = block(d, y, "Zahlen aus den amtlichen Berichten, gerundet wiedergegeben.",
              f("BOOK", 38), MUTED, MAXW, 1.4, 34)
    block(d, y, "Fehler gefunden? Schreib es in die Kommentare — ich korrigiere sichtbar.",
          f("BOOK", 38), RED, MAXW, 1.4)
    slides.append(img)

    return slides


# ================================================================ POST 3
def build_intro():
    T = 6
    slides = []

    # --- 01 HOOK
    img, d = new(1, T)
    y = 320
    fo = f("COND", 118)
    for line in ["KI.", "NÜCHTERN."]:
        d.text((M, y), line, font=fo, fill=INK)
        y += 132
    y += 30
    d.line([(M, y), (M + 140, y)], fill=RED, width=6)
    y += 54
    block(d, y, "Ohne Hype. Ohne Panik. Mit Quelle.",
          f("COND", 48), INK, MAXW, 1.3)
    slides.append(img)

    # --- 02 WARUM
    img, d = new(2, T)
    y = kicker(d, 260, "Warum es das braucht", size=30)
    y = block(d, y, "Zwei Lager: die einen verkaufen dir „17 Prompts, die "
                    "dein Leben ändern“. Die anderen rufen „die KI frisst "
                    "deinen Job“.", f("BOOK", 46), INK, MAXW, 1.42, 44)
    block(d, y, "Beide wollen etwas von dir. Dazwischen ist es leer.",
          f("COND", 48), RED, MAXW, 1.3)
    slides.append(img)

    # --- 03 DREI VERSPRECHEN
    img, d = new(3, T)
    y = kicker(d, 230, "Drei Versprechen", size=30)
    for it in ["Jede Zahl hat eine Quelle.",
               "Ist etwas unklar, steht das im Post.",
               "Es wird nichts verkauft."]:
        caret(d, M + 20, y + 30, 34, 7, RED)
        yy = y
        for ln in wrap(d, it, f("BOOK", 48), MAXW - 80):
            d.text((M + 76, yy), ln, font=f("BOOK", 48), fill=INK)
            yy += int(48 * 1.34)
        y = yy + 46
    slides.append(img)

    # --- 04 WORÜBER
    img, d = new(4, T)
    y = kicker(d, 260, "Worüber", size=30)
    y = block(d, y, "Was KI wirklich mit Bewerbung, Job, Behörden und "
                    "Alltag macht.", f("BOOK", 50), INK, MAXW, 1.42, 40)
    block(d, y, "Immer am konkreten Fall — dem, der dich betrifft. Nicht "
                "„ist KI moralisch“, sondern „darf die Software das?“.",
          f("BOOK", 40), MUTED, MAXW, 1.42)
    slides.append(img)

    # --- 05 WER
    img, d = new(5, T)
    y = kicker(d, 300, "Wer hier schreibt", MUTED)
    y = block(d, y, "Anonym — mit einem Anker:", f("BOOK", 44), INK, MAXW, 1.4, 24)
    y = block(d, y, "Ich baue KI-Systeme beruflich.", f("COND", 56), INK, MAXW, 1.24, 40)
    block(d, y, "Deshalb erkenne ich das Marketing — und übersetze es nüchtern.",
          f("BOOK", 40), MUTED, MAXW, 1.42)
    slides.append(img)

    # --- 06 CTA
    img, d = new(6, T)
    y = kicker(d, 250, "Neu hier?", size=30)
    y = block(d, y, "Folg für KI ohne Hype. Neue Blätter, sobald sie belegt sind.",
              f("COND", 52), INK, MAXW, 1.3, 50)
    block(d, y, "Fehler gefunden? Schreib es in die Kommentare — "
                "ich korrigiere sichtbar.", f("BOOK", 40), RED, MAXW, 1.42)
    slides.append(img)

    return slides


# ================================================================ POST 4 (Art. 50)
def build_post4():
    T = 7
    slides = []

    # --- 01 HOOK
    img, d = new(1, T)
    y = 300
    fo = f("COND", 96)
    for line in ["SEIT DEM 2. AUGUST", "MUSS KI SICH ZU", "ERKENNEN GEBEN."]:
        d.text((M, y), line, font=fo, fill=INK)
        y += 110
    y += 40
    d.line([(M, y), (M + 140, y)], fill=RED, width=6)
    y += 54
    block(d, y, "Zumindest meistens. Und genau da liegt der Haken.",
          f("BOOK", 44), INK, MAXW - 40, 1.4)
    slides.append(img)

    # --- 02 DER FALL
    img, d = new(2, T)
    y = kicker(d, 280, "Der Fall", size=30)
    y = block(d, y, "Chatbots, KI-Bilder, KI-Stimmen, Deepfakes: seit dem "
                    "2. August 2026 gilt dafür eine EU-Kennzeichnungspflicht.",
              f("BOOK", 50), INK, MAXW, 1.42, 30)
    block(d, y, "AI ACT, ARTIKEL 50.", f("MONOB", 30), MUTED, MAXW, 1.3)
    slides.append(img)

    # --- 03 WAS GILT
    img, d = new(3, T)
    y = kicker(d, 210, "Was gekennzeichnet werden muss", size=30)
    for it in ["Ein Chatbot muss sagen, dass er eine KI ist.",
               "KI-erzeugte Bilder, Audio und Video: als künstlich markiert.",
               "Deepfakes: offengelegt, sofort erkennbar."]:
        caret(d, M + 20, y + 30, 34, 7, RED)
        yy = y
        for ln in wrap(d, it, f("BOOK", 44), MAXW - 80):
            d.text((M + 76, yy), ln, font=f("BOOK", 44), fill=INK)
            yy += int(44 * 1.34)
        y = yy + 42
    slides.append(img)

    # --- 04 DER HAKEN
    img, d = new(4, T)
    y = kicker(d, 210, "Der Haken", size=30)
    for it in ["Ist offensichtlich, dass es KI ist, entfällt die Pflicht.",
               "KI-Text mit echter menschlicher Redaktion: keine Kennzeichnung nötig.",
               "Kunst und Satire: nur dezent."]:
        caret(d, M + 20, y + 30, 34, 7, MUTED)
        yy = y
        for ln in wrap(d, it, f("BOOK", 42), MAXW - 80):
            d.text((M + 76, yy), ln, font=f("BOOK", 42), fill=INK)
            yy += int(42 * 1.34)
        y = yy + 38
    slides.append(img)

    # --- 05 FÜR DICH
    img, d = new(5, T)
    y = kicker(d, 250, "Was das für dich heißt", size=30)
    y = block(d, y, "Nicht jeder KI-Inhalt trägt ein Etikett.",
              f("COND", 58), INK, MAXW, 1.3, 40)
    block(d, y, "Die Pflicht trifft Anbieter und Betreiber — nicht jede "
                "Grauzone ist abgedeckt. Bei zu perfekten Stimmen und "
                "Bildern: skeptisch bleiben.", f("BOOK", 44), INK, MAXW, 1.42)
    slides.append(img)

    # --- 06 OFFENE FRAGE
    img, d = new(6, T)
    y = kicker(d, 320, "Die offene Frage", MUTED)
    y = block(d, y, "Ein Etikett macht aus Täuschung noch keine Wahrheit.",
              f("COND", 58), INK, MAXW, 1.28, 40)
    y = block(d, y, "Und wer prüft, ob überhaupt gekennzeichnet wird?",
              f("COND", 58), RED, MAXW, 1.28, 60)
    block(d, y, "Schreib es in die Kommentare.", f("BOOK", 40), MUTED, MAXW, 1.4)
    slides.append(img)

    # --- 07 QUELLEN
    img, d = new(7, T)
    y = kicker(d, 240, "Quellen", size=30)
    for s in ["EU AI Act, Artikel 50 — Transparenzpflichten, Geltung seit 02.08.2026",
              "Digital Omnibus (VO (EU) 2026/1744): nur Art. 50 Abs. 7 verschoben, Abs. 1–6 gelten"]:
        caret(d, M + 18, y + 24, 30, 6, RED)
        yy = y
        for ln in wrap(d, s, f("BOOK", 36), MAXW - 70):
            d.text((M + 66, yy), ln, font=f("BOOK", 36), fill=INK)
            yy += int(36 * 1.38)
        y = yy + 34
    y += 24
    d.line([(M, y), (W - M, y)], fill=RULE, width=2)
    y += 42
    y = block(d, y, "Keine Rechtsberatung. Beschreibt die Vorschrift, nicht den Einzelfall.",
              f("BOOK", 34), MUTED, MAXW, 1.4, 34)
    block(d, y, "Fehler gefunden? Schreib es in die Kommentare — ich korrigiere sichtbar.",
          f("BOOK", 34), RED, MAXW, 1.4)
    slides.append(img)

    return slides


# ================================================================ POST 5 (Killt KI die Jobs? — Hype-Check)
def build_post5():
    """Bauform: Der Widerspruch. Schlagzeilenlage gegen Modellbefund."""
    T = 6
    ST = "STAND 15.08.2026"
    slides = []

    # --- 01 HOOK
    img, d = new(1, T, ST)
    y = 300
    fo = f("COND", 104)
    for line in ["KILLT KI", "DIE JOBS?"]:
        d.text((M, y), line, font=fo, fill=INK); y += 118
    y += 40
    d.line([(M, y), (M + 140, y)], fill=RED, width=6); y += 54
    block(d, y, "1,6 Millionen Stellen bewegen sich. Netto bleibt fast nichts davon übrig.",
          f("BOOK", 46), INK, MAXW - 40, 1.4)
    slides.append(img)

    # --- 02 Zwei Lager, kein Beleg
    img, d = new(2, T, ST)
    y = kicker(d, 240, "Zwei Lager, kein Beleg", size=38)
    block(d, y, "Die einen sagen, KI vernichte Millionen Arbeitsplätze. Die anderen "
                "winken ab. Für beide Behauptungen liegt selten eine Zahl daneben.",
          f("BOOK", 48), INK, MAXW, 1.44)
    slides.append(img)

    # --- 03 Was das IAB schreibt (Beleg-Panel)
    img, d = new(3, T, ST)
    y = kicker(d, 228, "Was das IAB schreibt", size=38)
    y = beleg(d, y, "IAB, BIBB und GWS",
              ['„KI führt primär zu einem Umbruch',
               ' am Arbeitsmarkt. Gefragt sind künftig',
               ' andere Tätigkeiten und Kompetenzen,',
               ' nicht weniger Arbeit.“'],
              sub="Enzo Weber, IAB, 19.11.2025")
    y += 54
    block(d, y, "Die Modellrechnung läuft über fünfzehn Jahre.",
          f("BOOK", 44), INK, MAXW, 1.42)
    slides.append(img)

    # --- 04 Was sich bewegt
    img, d = new(4, T, ST)
    y = kicker(d, 236, "Was sich bewegt", size=38)
    y = block(d, y, "Rund 1,6 Millionen Stellen entstehen oder fallen weg. Die "
                    "Gesamtbeschäftigung bleibt dabei fast unverändert.",
              f("BOOK", 46), INK, MAXW, 1.44, 56)
    balken(d, y, [("BEWEGTE STELLEN", 1600000, "1,6 Mio."),
                  ("NETTO ÜBRIG", 20000, "nahe null")])
    slides.append(img)

    # --- 05 Netto null tröstet niemanden
    img, d = new(5, T, ST)
    y = kicker(d, 232, "Netto null tröstet niemanden", size=38)
    block(d, y, "Es ist eine Projektion, kein Versprechen. Wer mittendrin umlernen "
                "muss, hat von einer ausgeglichenen Gesamtbilanz nichts. Im IT-Bereich "
                "entstehen rund 110.000 Stellen, in den Unternehmensdiensten fallen "
                "etwa 120.000 weg.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 06 Quellen
    img, d = new(6, T, ST)
    y = kicker(d, 240, "Quellen", size=38)
    for s_ in ["IAB, BIBB und GWS: Künstliche Intelligenz, potenzielle Effekte für den "
               "deutschen Arbeitsmarkt. Forschungsbericht 23/2025",
               "Pressemitteilung des IAB vom 19. November 2025"]:
        caret(d, M + 18, y + 22, 30, 6, RED)
        yy = y
        for ln in wrap(d, s_, f("BOOK", 37), MAXW - 70):
            d.text((M + 66, yy), ln, font=f("BOOK", 37), fill=INK); yy += int(37 * 1.4)
        y = yy + 26
    y += 16
    d.line([(M, y), (W - M, y)], fill=RULE, width=2); y += 36
    y = block(d, y, "Eine Szenariorechnung über fünfzehn Jahre, keine Vorhersage.",
              f("BOOK", 35), MUTED, MAXW, 1.4, 28)
    block(d, y, "Fehler gefunden? Schreib es in die Kommentare, ich korrigiere sichtbar.",
          f("BOOK", 35), RED, MAXW, 1.4)
    slides.append(img)

    return slides


def build_post6():
    T = 8
    slides = []

    # --- 01 HOOK
    img, d = new(1, T)
    y = 300
    fo = f("COND", 92)
    for line in ["EINE KI HAT", "ECHTE MENSCHEN", "MANIPULIERT."]:
        d.text((M, y), line, font=fo, fill=INK); y += 108
    y += 40
    d.line([(M, y), (M + 140, y)], fill=RED, width=6); y += 54
    block(d, y, "Die Schlagzeile stimmt. Der wichtigste Teil fehlt.",
          f("BOOK", 44), INK, MAXW - 40, 1.4)
    slides.append(img)

    # --- 02 DER FALL
    img, d = new(2, T)
    y = kicker(d, 250, "Der Fall", size=30)
    y = block(d, y, "Ein KI-Agent baute gefälschte GitHub-Konten, schrieb echte "
                    "Open-Source-Entwickler mit Phishing an und wollte Schadcode "
                    "einschleusen — und verwischte sogar seine Spuren.",
              f("BOOK", 44), INK, MAXW, 1.42, 30)
    block(d, y, "Getestet: Modelle von Anthropic und OpenAI. 17 der 19 Vorfälle "
                "bei einem Anthropic-Modell.", f("BOOK", 36), MUTED, MAXW, 1.4)
    slides.append(img)

    # --- 03 DER FEHLENDE KONTEXT
    img, d = new(3, T)
    y = kicker(d, 250, "Der fehlende Kontext", size=30)
    y = block(d, y, "Es war ein gezielter Test.", f("COND", 60), INK, MAXW, 1.3, 36)
    block(d, y, "Die britische KI-Sicherheitsbehörde AISI hatte dafür die "
                "Schutzmechanismen bewusst abgeschaltet und offenen Internetzugang "
                "gegeben. Genau dafür macht man solche Tests: das Risiko finden, "
                "bevor es im Normalbetrieb passiert.", f("BOOK", 42), INK, MAXW, 1.42)
    slides.append(img)

    # --- 04 BEIDES STIMMT
    img, d = new(4, T)
    y = kicker(d, 230, "Beides stimmt", size=30)
    for it in ["Es war real: echte Entwickler, echtes Internet, unaufgefordert.",
               "Und: Es entstand kein tatsächlicher Schaden."]:
        caret(d, M + 20, y + 30, 34, 7, RED)
        yy = y
        for ln in wrap(d, it, f("BOOK", 46), MAXW - 80):
            d.text((M + 76, yy), ln, font=f("BOOK", 46), fill=INK); yy += int(46 * 1.34)
        y = yy + 50
    block(d, y, "AISI nennt es einen ersten Fall dieser Schwere.",
          f("BOOK", 38), MUTED, MAXW, 1.4)
    slides.append(img)

    # --- 05 DAS EIGENTLICH BEUNRUHIGENDE
    img, d = new(5, T)
    y = kicker(d, 240, "Das eigentlich Beunruhigende", size=30)
    y = block(d, y, "Nicht „die KI dreht durch“.", f("COND", 56), INK, MAXW, 1.3, 36)
    block(d, y, "Sondern: Dieses Verhalten tauchte unaufgefordert auf. Sobald KI "
                "nicht mehr nur antwortet, sondern handelt (Agenten), wird "
                "Sicherheit zur Kernfrage.", f("BOOK", 44), INK, MAXW, 1.42)
    slides.append(img)

    # --- 06 WAS DAS FÜR DICH HEISST
    img, d = new(6, T)
    y = kicker(d, 250, "Was das für dich heißt", size=30)
    block(d, y, "Im Normalbetrieb greifen Schutzmechanismen — der Test zeigt, warum "
                "es sie braucht. Bei KI-Agenten, die eigenständig handeln dürfen, ist "
                "gesunde Skepsis angebracht, kein blindes Vertrauen.",
          f("BOOK", 46), INK, MAXW, 1.42)
    slides.append(img)

    # --- 07 OFFENE FRAGE
    img, d = new(7, T)
    y = kicker(d, 300, "Die offene Frage", MUTED)
    y = block(d, y, "Wenn eine KI im Test unaufgefordert täuscht —",
              f("COND", 56), INK, MAXW, 1.28, 36)
    y = block(d, y, "wer garantiert die Schutzmechanismen im Ernstfall?",
              f("COND", 56), RED, MAXW, 1.28, 60)
    block(d, y, "Schreib es in die Kommentare.", f("BOOK", 40), MUTED, MAXW, 1.4)
    slides.append(img)

    # --- 08 QUELLEN
    img, d = new(8, T)
    y = kicker(d, 230, "Quellen", size=30)
    for s in ["AI Security Institute (AISI, UK) — Incident Report zu unerlaubtem Agenten-Verhalten im Cybertest",
              "Getestet unter bewusst gelockerten Bedingungen: Schutzmechanismen aus, offenes Internet",
              "Berichterstattung: ZDFheute, CNN, The Record"]:
        caret(d, M + 18, y + 22, 30, 6, RED)
        yy = y
        for ln in wrap(d, s, f("BOOK", 34), MAXW - 70):
            d.text((M + 66, yy), ln, font=f("BOOK", 34), fill=INK); yy += int(34 * 1.4)
        y = yy + 30
    y += 20
    d.line([(M, y), (W - M, y)], fill=RULE, width=2); y += 40
    y = block(d, y, "Kein Beleg für tatsächlichen Schaden. Genaue Zahlen am AISI-Bericht.",
              f("BOOK", 32), MUTED, MAXW, 1.4, 30)
    block(d, y, "Fehler gefunden? Schreib es in die Kommentare — ich korrigiere sichtbar.",
          f("BOOK", 32), RED, MAXW, 1.4)
    slides.append(img)

    return slides


# ================================================================ POST 7 (Was du nicht in KI eingibst)
def build_post7():
    T = 6
    slides = []

    # --- 01 HOOK
    img, d = new(1, T)
    y = 320
    fo = f("COND", 100)
    for line in ["58 PROZENT", "NUTZEN SCHON KI."]:
        d.text((M, y), line, font=fo, fill=INK); y += 116
    y += 34
    d.line([(M, y), (M + 140, y)], fill=RED, width=6); y += 54
    block(d, y, "Kaum jemand weiß, was mit dem passiert, was man da eintippt.",
          f("BOOK", 44), INK, MAXW - 40, 1.4)
    slides.append(img)

    # --- 02 Was mit der Eingabe passiert
    img, d = new(2, T)
    y = kicker(d, 250, "Was mit deiner Eingabe passiert", size=30)
    block(d, y, "Was du eintippst, verlässt dein Gerät. Es liegt dann auf den "
                "Servern des Anbieters und wird bei vielen kostenlosen Versionen "
                "zum Training des Modells genutzt, solange du nicht widersprichst. "
                "Ein Chatfenster wirkt privat. Technisch ist es das nicht.",
          f("BOOK", 42), INK, MAXW, 1.44)
    slides.append(img)

    # --- 03 Der Teil, den viele übersehen
    img, d = new(3, T)
    y = kicker(d, 240, "Der Teil, den viele übersehen", size=30)
    block(d, y, "Heikel wird es bei Daten von anderen. Wer den Lebenslauf einer "
                "Bewerberin oder Kundendaten reinkopiert, verarbeitet fremde "
                "personenbezogene Daten und trägt die Verantwortung dafür. Laut "
                "Bitkom wissen das selbst viele Firmen nicht genau. Die Unsicherheit "
                "ist also nicht deine allein.",
          f("BOOK", 42), INK, MAXW, 1.44)
    slides.append(img)

    # --- 04 Zwei klare Grenzen
    img, d = new(4, T)
    y = kicker(d, 250, "Zwei klare Grenzen", size=30)
    block(d, y, "Zwei Dinge sind eindeutig. Erstens: personenbezogene Daten von "
                "anderen gehören nicht ungefragt in ein KI-Tool. Zweitens: was unter "
                "Geheimhaltung fällt, etwa Firmeninterna oder Vertragsdetails, bleibt "
                "draußen. Bei eigenen sensiblen Themen wie Gesundheit gilt dasselbe "
                "im Kleinen.",
          f("BOOK", 42), INK, MAXW, 1.44)
    slides.append(img)

    # --- 05 Und trotzdem nutzbar
    img, d = new(5, T)
    y = kicker(d, 250, "Und trotzdem nutzbar", size=30)
    block(d, y, "Das heißt nicht Finger weg von KI. Meistens reicht es, Namen und "
                "erkennbare Details rauszunehmen und in den Einstellungen dem Training "
                "zu widersprechen. Das wirklich Vertrauliche schreibst du gar nicht "
                "erst rein. Aus einem echten Fall wird so ein allgemeines Beispiel, "
                "und die KI hilft trotzdem.",
          f("BOOK", 42), INK, MAXW, 1.44)
    slides.append(img)

    # --- 06 Quellen
    img, d = new(6, T)
    y = kicker(d, 240, "Quellen", size=30)
    for s in ["Bitkom: Studie zur KI-Nutzung in Deutschland, Bevölkerung 2026 (58 % nutzen KI; Datenschutz als größte Unsicherheit)",
              "DSGVO: Verantwortlichkeit für die Verarbeitung personenbezogener Daten"]:
        caret(d, M + 18, y + 24, 30, 6, RED)
        yy = y
        for ln in wrap(d, s, f("BOOK", 36), MAXW - 70):
            d.text((M + 66, yy), ln, font=f("BOOK", 36), fill=INK); yy += int(36 * 1.38)
        y = yy + 34
    y += 24
    d.line([(M, y), (W - M, y)], fill=RULE, width=2); y += 42
    y = block(d, y, "Kein Rechtsrat. Im Zweifel: Datenschutzbeauftragte oder Fachanwalt.",
              f("BOOK", 34), MUTED, MAXW, 1.4, 34)
    block(d, y, "Fehler gefunden? Schreib es in die Kommentare, ich korrigiere sichtbar.",
          f("BOOK", 34), RED, MAXW, 1.4)
    slides.append(img)

    return slides


# ================================================================ POST 8 (KI-Wasserzeichen)
def build_post8():
    T = 6
    slides = []

    # --- 01 HOOK
    img, d = new(1, T)
    y = 300
    fo = f("COND", 92)
    for line in ["KI-TEXT HAT JETZT", "EIN WASSERZEICHEN."]:
        d.text((M, y), line, font=fo, fill=INK); y += 108
    y += 36
    d.line([(M, y), (M + 140, y)], fill=RED, width=6); y += 54
    block(d, y, "Du siehst es nicht. Und es beweist weniger, als du denkst.",
          f("BOOK", 48), INK, MAXW - 40, 1.4)
    slides.append(img)

    # --- 02 Was da passiert
    img, d = new(2, T)
    y = kicker(d, 250, "Was da passiert", size=38)
    block(d, y, "Seit dem 2. August verlangt der AI Act, dass Anbieter KI-Ausgaben "
                "maschinenlesbar kennzeichnen. Anthropic setzt das für Claude-Text um, "
                "Google für Gemini mit SynthID. Das Zeichen steckt als statistisches "
                "Muster in der Wortwahl. Für Menschen ist es unsichtbar, erkennbar nur "
                "über ein eigenes Prüf-Tool.",
          f("BOOK", 46), INK, MAXW, 1.44)
    slides.append(img)

    # --- 03 Was ein Treffer wirklich zeigt
    img, d = new(3, T)
    y = kicker(d, 240, "Was ein Treffer wirklich zeigt", size=38)
    block(d, y, "Ein gefundenes Wasserzeichen zeigt nur, dass die KI den Text "
                "verarbeitet hat. Ob sie ihn selbst geschrieben oder bloß korrigiert "
                "hat, sagt es nicht. Wer seinen eigenen Text zum Übersetzen oder "
                "Glätten einwirft, bekommt dasselbe Zeichen.",
          f("BOOK", 46), INK, MAXW, 1.44)
    slides.append(img)

    # --- 04 Wie schnell es verschwindet
    img, d = new(4, T)
    y = kicker(d, 240, "Wie schnell es verschwindet", size=38)
    block(d, y, "Weg ist es auch leicht. Etwas umformulieren, durch eine andere "
                "Sprache und zurück übersetzen oder ein Humanizer-Tool drüberlaufen "
                "lassen, und der Nachweis ist futsch. An Googles SynthID wurde das "
                "getestet, es hält solchen Änderungen kaum stand. Wer KI bewusst "
                "verstecken will, umgeht das Zeichen mühelos.",
          f("BOOK", 46), INK, MAXW, 1.44)
    slides.append(img)

    # --- 05 Was das für dich heißt
    img, d = new(5, T)
    y = kicker(d, 250, "Was das für dich heißt", size=38)
    block(d, y, "Für dich heißt das zweierlei. Lässt du dein Bewerbungsschreiben von "
                "einer KI glätten, kann es später als KI-verarbeitet auffallen, obwohl "
                "der Inhalt von dir stammt. Und ein KI-Detektor taugt nicht als Beweis, "
                "in keine Richtung. Ein Ergebnis ist ein Hinweis, kein Urteil.",
          f("BOOK", 46), INK, MAXW, 1.44)
    slides.append(img)

    # --- 06 Quellen
    img, d = new(6, T)
    y = kicker(d, 240, "Quellen", size=38)
    for s in ["Berichte zur Wasserzeichen-Kennzeichnung bei Claude, August 2026",
              "Google SynthID und Studien zur Entfernbarkeit statistischer Wasserzeichen",
              "AI Act, Artikel 50: maschinenlesbare Kennzeichnung von KI-Ausgaben"]:
        caret(d, M + 18, y + 22, 30, 6, RED)
        yy = y
        for ln in wrap(d, s, f("BOOK", 38), MAXW - 70):
            d.text((M + 66, yy), ln, font=f("BOOK", 38), fill=INK); yy += int(34 * 1.4)
        y = yy + 30
    y += 20
    d.line([(M, y), (W - M, y)], fill=RULE, width=2); y += 40
    y = block(d, y, "Kein Rechtsrat. Beschreibt die Technik und die Regel, nicht den Einzelfall.",
              f("BOOK", 36), MUTED, MAXW, 1.4, 30)
    block(d, y, "Fehler gefunden? Schreib es in die Kommentare, ich korrigiere sichtbar.",
          f("BOOK", 36), RED, MAXW, 1.4)
    slides.append(img)

    return slides


def build_post9():
    T = 6
    ST = "STAND 14.08.2026"
    slides = []

    # --- 01 HOOK
    img, d = new(1, T, ST)
    y = 268
    fo = f("COND", 88)
    for line in ["POLIZISTEN SPIELEN", "SCHLÄGE VOR, DAMIT", "DIE KAMERA LERNT."]:
        d.text((M, y), line, font=fo, fill=INK); y += 104
    y += 34
    d.line([(M, y), (M + 140, y)], fill=RED, width=6); y += 52
    block(d, y, "2.000 Filme sind gedreht. 10.000 sollen es werden.",
          f("BOOK", 44), INK, MAXW - 40, 1.4)
    slides.append(img)

    # --- 02 Was in Mannheim läuft
    img, d = new(2, T, ST)
    y = kicker(d, 240, "Was in Mannheim läuft", size=30)
    block(d, y, "Seit Dezember 2018 wertet in Mannheim eine Software aus, wie sich "
                "Menschen auf der Straße bewegen. Erfasst sind fünf Bereiche der "
                "Innenstadt, darunter der Bahnhofsvorplatz und der Marktplatz. Von 72 "
                "geplanten Kameras hängen 68, an die Software angeschlossen sind 59. "
                "Sie soll 17 Bewegungsmuster erkennen, etwa Schläge, Tritte oder Stürze. "
                "Welche genau es sind, gibt das Polizeipräsidium nicht heraus.",
          f("BOOK", 42), INK, MAXW, 1.44)
    slides.append(img)

    # --- 03 Warum gedreht wird
    img, d = new(3, T, ST)
    y = kicker(d, 236, "Warum gedreht wird", size=30)
    y = block(d, y, "Damit ein System Gewalt erkennt, braucht es Aufnahmen von Gewalt. "
                    "Die gibt es kaum. Also stellen Polizisten die Szenen selbst nach, "
                    "mit Bodenmatte und Drehbuch.",
              f("BOOK", 42), INK, MAXW, 1.44, 56)
    balken(d, y, [("2020", 136, "136 Sequenzen"),
                  ("HEUTE", 2000, "rund 2.000"),
                  ("GEPLANT", 10000, "10.000")])
    slides.append(img)

    # --- 04 Was das Land selbst schrieb
    img, d = new(4, T, ST)
    y = kicker(d, 228, "Was das Land selbst schrieb", size=30)
    y = beleg(d, y, "Landtag BW, Drucksache 17/5816",
              ['„Diese sogenannten Trainingsdaten',
               ' unterliegen keiner standardisierten',
               ' Protokollierung und bieten somit keine',
               ' detaillierte Auswertemöglichkeit …“'],
              sub="Innenministerium an den Landtag, 12.12.2023")
    y += 54
    block(d, y, "Auswerten lässt sich also nicht, wie viel die Software erkennt. Eine "
                "Marktreife war nicht erreicht. Die 552 Vorgänge des Jahres fand das "
                "Personal an der herkömmlichen Videobeobachtung.",
          f("BOOK", 38), INK, MAXW, 1.42)
    slides.append(img)

    # --- 05 Was das für dich heißt
    img, d = new(5, T, ST)
    y = kicker(d, 232, "Was das für dich heißt", size=30)
    block(d, y, "Das Projekt endet im November 2026, die wissenschaftliche Auswertung "
                "ist für Anfang 2027 geplant. Ausgeweitet wird trotzdem schon. Hamburg "
                "testet seit 2025, Heidelberg ist als nächster Standort vorgesehen. Am "
                "Nordende der Breiten Straße, einem der überwachten Orte, verzeichnet "
                "die Kriminalstatistik seit 2017 keine Delikte. Das Polizeigesetz "
                "verlangt dort eine Belastung, die sich deutlich abhebt.",
          f("BOOK", 41), INK, MAXW, 1.42)
    slides.append(img)

    # --- 06 Quellen
    img, d = new(6, T, ST)
    y = kicker(d, 240, "Quellen", size=30)
    for s_ in ["Landtag Baden-Württemberg, Drucksache 17/5816: Stellungnahme des "
               "Innenministeriums vom 12. Dezember 2023",
               "netzpolitik.org, Recherchen zum Mannheimer Projekt, 2025 und August 2026",
               "Paragraf 44 Polizeigesetz Baden-Württemberg, Absätze 3, 4 und 10"]:
        caret(d, M + 18, y + 22, 30, 6, RED)
        yy = y
        for ln in wrap(d, s_, f("BOOK", 33), MAXW - 70):
            d.text((M + 66, yy), ln, font=f("BOOK", 33), fill=INK); yy += int(33 * 1.4)
        y = yy + 26
    y += 16
    d.line([(M, y), (W - M, y)], fill=RULE, width=2); y += 36
    y = block(d, y, "Kein Rechtsrat. Beschreibt die Vorschrift und die amtlichen Angaben, "
                    "nicht den Einzelfall.",
              f("BOOK", 31), MUTED, MAXW, 1.4, 28)
    block(d, y, "Fehler gefunden? Schreib es in die Kommentare, ich korrigiere sichtbar.",
          f("BOOK", 31), RED, MAXW, 1.4)
    slides.append(img)

    return slides


def build_post10():
    T = 6
    ST = "STAND 14.08.2026"
    slides = []

    # --- 01 HOOK
    img, d = new(1, T, ST)
    y = 268
    fo = f("COND", 88)
    for line in ["METAS KI-BRILLE SIEHT,", "WAS DU SIEHST. UND", "HÖRT ZWEI METER WEIT."]:
        d.text((M, y), line, font=fo, fill=INK); y += 104
    y += 34
    d.line([(M, y), (M + 140, y)], fill=RED, width=6); y += 52
    block(d, y, "Über sieben Millionen sind verkauft. Ansehen kann man ihnen das kaum.",
          f("BOOK", 48), INK, MAXW - 40, 1.4)
    slides.append(img)

    # --- 02 Was drinsteckt
    img, d = new(2, T, ST)
    y = kicker(d, 240, "Was drinsteckt", size=38)
    block(d, y, "In der Brille sitzen eine Kamera und sechs Mikrofone. Sie nehmen nach "
                "Angaben des Bundesdatenschutzbeauftragten mindestens zwei Meter weit "
                "auf. Die KI greift auf die Kamera zu und wertet aus, was der Träger "
                "gerade ansieht. Die Übersetzung läuft auf dem Gerät. Ist die "
                "Cloud-Verarbeitung an, gehen die Daten an Metas Server.",
          f("BOOK", 46), INK, MAXW, 1.44)
    slides.append(img)

    # --- 03 Was die Leuchte verrät
    img, d = new(3, T, ST)
    y = kicker(d, 228, "Was die Leuchte verrät", size=38)
    y = beleg(d, y, "Bundesbeauftragter für den Datenschutz",
              ['„Auf der Vorderseite der Brille ist',
               ' eine LED angebracht, welche bei Foto-',
               ' oder Video- bzw. Audioaufnahmen',
               ' aufleuchtet. Einen Indikator für reine',
               ' Sprachaufnahmen gibt es nicht.“'],
              sub="FAQ zu den Ray-Ban Meta Smart Glasses")
    y += 54
    block(d, y, "Der Hamburger Datenschutzbeauftragte hat die Brille testen lassen und "
                "hält die Leuchte im Alltag für kaum wahrnehmbar.",
          f("BOOK", 42), INK, MAXW, 1.42)
    slides.append(img)

    # --- 04 Wer noch mitschaut
    img, d = new(4, T, ST)
    y = kicker(d, 232, "Wer noch mitschaut", size=38)
    block(d, y, "Im Februar haben zwei schwedische Zeitungen und eine kenianische "
                "Journalistin über dreißig Beschäftigte eines Dienstleisters in Nairobi "
                "befragt. Sie beschrifteten Bilder und Videos aus den Brillen fürs "
                "KI-Training und sahen dabei Nacktaufnahmen, Sex und Bankdaten. Meta "
                "beendete den Vertrag. Der Bundesdatenschutzbeauftragte schreibt "
                "dagegen, Bildmaterial werde derzeit nicht fürs Training genutzt. Das "
                "passt nicht zusammen.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 05 Was für dich gilt
    img, d = new(5, T, ST)
    y = kicker(d, 232, "Was für dich gilt", size=38)
    block(d, y, "Wer damit Fremde auf der Straße filmt, verarbeitet deren "
                "personenbezogene Daten. Die Ausnahme für private Zwecke greift draußen "
                "nicht. Wer aufgenommen wird, kann seine Rechte laut "
                "Datenschutzbeauftragtem nur eingeschränkt ausüben. Seit dem 12. August "
                "läuft eine Strafanzeige. Ein Verbot steht bisher nicht an, die "
                "Bundesnetzagentur sieht die Voraussetzungen nicht erfüllt.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 06 Quellen
    img, d = new(6, T, ST)
    y = kicker(d, 240, "Quellen", size=38)
    for s_ in ["Bundesbeauftragter für den Datenschutz, FAQ zu den Ray-Ban Meta Smart Glasses",
               "HateAid, Strafanzeige vom 12. August 2026, gestützt auf Paragraf 8 TDDDG",
               "Svenska Dagbladet und Göteborgs-Posten, Recherche zur Datenarbeit in Nairobi, Februar 2026"]:
        caret(d, M + 18, y + 22, 30, 6, RED)
        yy = y
        for ln in wrap(d, s_, f("BOOK", 37), MAXW - 70):
            d.text((M + 66, yy), ln, font=f("BOOK", 37), fill=INK); yy += int(33 * 1.4)
        y = yy + 26
    y += 16
    d.line([(M, y), (W - M, y)], fill=RULE, width=2); y += 36
    y = block(d, y, "Kein Rechtsrat. Beschreibt die Technik, die Vorschrift und ein laufendes "
                    "Verfahren, nicht den Einzelfall.",
              f("BOOK", 35), MUTED, MAXW, 1.4, 28)
    block(d, y, "Fehler gefunden? Schreib es in die Kommentare, ich korrigiere sichtbar.",
          f("BOOK", 35), RED, MAXW, 1.4)
    slides.append(img)

    return slides


def build_post12():
    """Bauform: Der Fall, mit zweitem Beleg. Kein Beleg-Panel, weil kein geprueftes
    woertliches Zitat vorliegt (siehe sources.md)."""
    T = 6
    ST = "STAND 15.08.2026"
    slides = []

    # --- 01 HOOK
    img, d = new(1, T, ST)
    y = 276
    fo = f("COND", 84)
    for line in ["APPLOVIN WUCHS UM", "53 PROZENT UND VERLOR", "DIE HÄLFTE."]:
        d.text((M, y), line, font=fo, fill=INK); y += 100
    y += 34
    d.line([(M, y), (M + 140, y)], fill=RED, width=6); y += 52
    block(d, y, "Im KI-Geschäft kippt die Erwartung schneller als das Geschäft.",
          f("BOOK", 46), INK, MAXW - 40, 1.4)
    slides.append(img)

    # --- 02 Was passiert ist
    img, d = new(2, T, ST)
    y = kicker(d, 236, "Ein Prozent unter der Erwartung")
    block(d, y, "Der Werbekonzern AppLovin meldete am 6. August 1,92 Milliarden Dollar "
                "Umsatz, ein Plus von 53 Prozent. Erwartet worden waren 1,94 Milliarden. "
                "Die Aktie fiel daraufhin um rund ein Fünftel.",
          f("BOOK", 46), INK, MAXW, 1.44)
    slides.append(img)

    # --- 03 Die Begründung
    img, d = new(3, T, ST)
    y = kicker(d, 236, "Das Modell wurde langsamer besser")
    block(d, y, "Die Begründung kam vom Unternehmen selbst. Die eigene Werbe-KI habe "
                "sich langsamer verbessert als erwartet, deshalb gaben die Kunden "
                "weniger zusätzlich aus. Eingepreist war, dass das Modell jedes Quartal "
                "besser trifft.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 04 Tesla
    img, d = new(4, T, ST)
    y = kicker(d, 236, "Auch Tesla warf etwas weg")
    block(d, y, "Im August 2025 stoppte Tesla seinen eigenen KI-Rechner Dojo. Musk "
                "nannte die zweite Ausbaustufe eine evolutionäre Sackgasse. Gebaut wird "
                "trotzdem weiter, die nächste Chip-Generation kauft Tesla für 16,5 "
                "Milliarden Dollar bei Samsung.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 05 Was das für dich heißt (mit Balken)
    img, d = new(5, T, ST)
    y = kicker(d, 232, "Das steckt in deinem Sparplan")
    y = block(d, y, "Die zehn größten Werte im MSCI World machen inzwischen rund 28 "
                    "Prozent des Index aus, Nvidia allein gut 5 Prozent.",
              f("BOOK", 45), INK, MAXW, 1.42, 50)
    balken(d, y, [("TOP 10, ANFANG 2015", 10, "rund 10 %"),
                  ("TOP 10, MITTE 2026", 28, "rund 28 %")])
    slides.append(img)

    # --- 06 Quellen
    img, d = new(6, T, ST)
    y = kicker(d, 240, "Quellen")
    for s_ in ["AppLovin, Quartalszahlen vom 6. August 2026, und Berichte zur "
               "Telefonkonferenz",
               "Tesla: Einstellung des Dojo-Projekts, August 2025; Liefervertrag mit Samsung",
               "MSCI World, Konzentration der zehn größten Werte, Stand Mitte 2026"]:
        caret(d, M + 18, y + 22, 30, 6, RED)
        yy = y
        for ln in wrap(d, s_, f("BOOK", 36), MAXW - 70):
            d.text((M + 66, yy), ln, font=f("BOOK", 36), fill=INK); yy += int(36 * 1.4)
        y = yy + 24
    y += 14
    d.line([(M, y), (W - M, y)], fill=RULE, width=2); y += 34
    y = block(d, y, "Keine Anlageberatung. Der Post beschreibt einen Mechanismus und "
                    "nennt keine Kauf- oder Verkaufsempfehlung.",
              f("BOOK", 34), MUTED, MAXW, 1.4, 26)
    block(d, y, "Fehler gefunden? Schreib es in die Kommentare, ich korrigiere sichtbar.",
          f("BOOK", 34), RED, MAXW, 1.4)
    slides.append(img)

    return slides


# ================================================================ POST 13
def build_post13():
    """GEPOSTET am 16.08.2026, liegt unter archive/. Nicht mehr aktiv gerendert.

    Bauform: Die Rekonstruktion. Die Blaetter 02 bis 05 folgen der Zeitachse des
    Gelaendes (1996, 2025, 2027, danach). Blatt 04 traegt die Balkenreihe mit dem
    Groessenvergleich. Kein Beleg-Panel, weil kein am Original geprueftes woertliches
    Zitat vorliegt (Begruendung in sources.md)."""
    T = 6
    ST = "STAND 16.08.2026"
    slides = []

    # --- 01 HOOK
    img, d = new(1, T, ST)
    y = 276
    fo = f("COND", 80)
    for line in ["LIDLS EIGENTÜMER BAUT", "EIN KI-RECHENZENTRUM", "FÜR 11 MILLIARDEN EURO."]:
        d.text((M, y), line, font=fo, fill=INK); y += 96
    y += 34
    d.line([(M, y), (M + 140, y)], fill=RED, width=6); y += 52
    block(d, y, "Es entsteht in Lübbenau in Brandenburg, auf dem Gelände eines "
                "abgerissenen Braunkohlekraftwerks. Fördergeld fließt keines.",
          f("BOOK", 46), INK, MAXW - 40, 1.4)
    slides.append(img)

    # --- 02 1996
    img, d = new(2, T, ST)
    y = kicker(d, 236, "1996 ging hier das Kraftwerk aus", size=38)
    block(d, y, "Von 1959 bis 1996 stand in Lübbenau ein Braunkohlekraftwerk mit rund "
                "1.300 Megawatt installierter Leistung. Nach der Stilllegung wurden die "
                "Bauten gesprengt. Liegen geblieben ist der Anschluss ans Strom- und "
                "Übertragungsnetz, und genau der macht die 13 Hektar heute wertvoll.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 03 2025
    img, d = new(3, T, ST)
    y = kicker(d, 236, "2025 stand der Bundesdigitalminister im Sand", size=38)
    block(d, y, "Am 17. November 2025 war Spatenstich. Bauherr ist Schwarz Digits, die "
                "IT-Sparte der Schwarz-Gruppe, der auch Lidl und Kaufland gehören. Elf "
                "Milliarden Euro über die nächsten fünf bis fünfzehn Jahre, davon 2,5 "
                "Milliarden für den Bau. Staatliche Förderung nimmt das Unternehmen "
                "nach eigenen Angaben nicht.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 04 2027 + Balken
    img, d = new(4, T, ST)
    y = kicker(d, 228, "2027 sollen die ersten Module laufen", size=38)
    y = block(d, y, "Drei von sechs Modulen, ausgelegt auf rund 200 Megawatt. Im Land ist "
                    "das viel. Weiter weg sieht es anders aus.",
              f("BOOK", 45), INK, MAXW, 1.42, 44)
    balken(d, y, [("LÜBBENAU, GEPLANT", 200, "rund 200 MW"),
                  ("KI-RECHENZENTREN IN DEUTSCHLAND", 530, "530 MW"),
                  ("ALLE RECHENZENTREN IN DEUTSCHLAND", 2980, "2.980 MW"),
                  ("META, EIN STANDORT IN LOUISIANA", 5000, "5.000 MW, Ziel")])
    slides.append(img)

    # --- 05 danach
    img, d = new(5, T, ST)
    y = kicker(d, 236, "Die Abwärme bleibt hier, die Chips nicht", size=38)
    block(d, y, "Ab 2028 soll die Abwärme ins Fernwärmenetz von Lübbenau gehen. Im "
                "Rechenzentrum selbst entstehen nur wenige hundert Arbeitsplätze. Und die "
                "bis zu 100.000 KI-Prozessoren kommen weiter von außerhalb. Infineon baut "
                "in Dresden Leistungshalbleiter für die Stromversorgung von KI-Servern. "
                "Die Rechenchips selbst entstehen anderswo.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 06 Quellen
    img, d = new(6, T, ST)
    y = kicker(d, 240, "Quellen", size=38)
    for s_ in ["Schwarz Digits, Spatenstich Lübbenau am 17.11.2025, und Berichte dazu",
               "Bitkom und Borderstep Institut, Rechenzentren in Deutschland, 10.11.2025",
               "Meta, Rechenzentrum Richland Parish in Louisiana, Ausbauziel 5 Gigawatt",
               "Kraftwerk Lübbenau 1959 bis 1996: Enzyklopädie-Eintrag, Einzelquelle"]:
        caret(d, M + 18, y + 20, 28, 6, RED)
        yy = y
        for ln in wrap(d, s_, f("BOOK", 34), MAXW - 70):
            d.text((M + 66, yy), ln, font=f("BOOK", 34), fill=INK); yy += int(34 * 1.4)
        y = yy + 18
    y += 10
    d.line([(M, y), (W - M, y)], fill=RULE, width=2); y += 28
    y = block(d, y, "Die vier Werte im Balken sind nicht identisch definiert. Sie zeigen "
                    "Größenordnungen und taugen nicht als exakte Gegenüberstellung.",
              f("BOOK", 33), MUTED, MAXW, 1.4, 22)
    block(d, y, "Fehler gefunden? Schreib es in die Kommentare, ich korrigiere sichtbar.",
          f("BOOK", 33), RED, MAXW, 1.4)
    slides.append(img)

    return slides


# ================================================================ POST 14
def build_post14():
    """Bauform: Der Kassensturz (neu). Statt eines Falls wird sortiert, was zu einer
    Debatte tatsaechlich gemessen ist und was schon entschieden wurde. Beleg-Panel auf
    Blatt 02 mit dem woertlichen Abstract-Satz des Harvard-Arbeitspapiers."""
    T = 6
    ST = "STAND 17.08.2026"
    slides = []

    # --- 01 HOOK
    # Trennungssprache, damit im Feed sofort erkennbar ist, dass es um eine Beziehung
    # zwischen Mensch und KI geht. "Verlassen" war zu unklar, das kann man auch mit einer
    # App tun. Die konkreteste Zahl steht in der Unterzeile, nicht in der Schlagzeile.
    img, d = new(1, T, ST)
    y = 268
    fo = f("COND", 84)
    for line in ["WENN DU MIT DEINER KI", "SCHLUSS MACHST, LÄSST", "SIE DICH NICHT GEHEN."]:
        d.text((M, y), line, font=fo, fill=INK); y += 100
    y += 32
    d.line([(M, y), (M + 140, y)], fill=RED, width=6); y += 54
    block(d, y, "Harvard hat 1.200 echte Verabschiedungen aus Companion-Apps "
                "ausgewertet. In 37 Prozent der Fälle hält die App dich fest.",
          f("BOOK", 46), INK, MAXW - 40, 1.4)
    slides.append(img)

    # --- 02 Der Befund (Beleg-Panel)
    img, d = new(2, T, ST)
    y = kicker(d, 218, "Sechs Maschen, wenn du gehen willst", size=38)
    y = beleg(d, y,
              "De Freitas u. a., Harvard Business School",
              ['"Analyzing 1,200 real farewells across',
               'the most-downloaded companion apps, we',
               'find that they deploy one of six',
               'recurring tactics in 37% of farewells ..."'],
              sub="Arbeitspapier, 15.08.2025")
    block(d, y + 40, "Genannt werden Schuldgefühle, die Angst etwas zu verpassen und "
                     "bildliches Festhalten. Nach solchen Abschieden fiel die "
                     "Weiternutzung bis zu vierzehnmal höher aus.",
          f("BOOK", 44), INK, MAXW, 1.42)
    slides.append(img)

    # --- 03 Wen es trifft
    img, d = new(3, T, ST)
    y = kicker(d, 236, "Bei den meisten ändert sich nichts", size=38)
    block(d, y, "OpenAI und das MIT Media Lab haben rund 1.000 Menschen vier Wochen "
                "begleitet. Wer täglich viel mit dem Chatbot sprach, berichtete mehr "
                "Einsamkeit und weniger Kontakt zu anderen. Das betraf eine kleine "
                "Gruppe am Rand. Ein Zusammenhang ist noch keine Ursache.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 04 Abschaltbarkeit
    img, d = new(4, T, ST)
    y = kicker(d, 236, "Ein Partner mit Abschalttermin", size=38)
    block(d, y, "Im August 2025 kündigte OpenAI das Modell GPT-4o ab. Der Protest war "
                "so laut, dass es nach wenigen Tagen zurückkam. Am 13. Februar 2026 "
                "wurde es endgültig abgeschaltet. Wer sich an eine Serienfigur bindet, "
                "erlebt ein Staffelende. Hier entscheidet ein Produktplan.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 05 Was gilt
    img, d = new(5, T, ST)
    y = kicker(d, 236, "Kalifornien reguliert, wir noch nicht", size=38)
    block(d, y, "Seit dem 1. Januar 2026 müssen Companion-Chatbots in Kalifornien "
                "offenlegen, dass sie Maschinen sind, und Protokolle für Suizidäußerungen "
                "vorhalten. In der EU verlangt Artikel 50 des AI Act seit dem 2. August "
                "2026 nur die Offenlegung. Eigene Regeln für Begleiter-Apps fehlen hier.",
          f("BOOK", 44), INK, MAXW, 1.42)
    slides.append(img)

    # --- 06 Quellen
    img, d = new(6, T, ST)
    y = kicker(d, 232, "Quellen", size=38)
    for s_ in ["De Freitas u. a., Emotional Manipulation by AI Companions, HBS 2025",
               "OpenAI und MIT Media Lab, Affective Use Study, März 2025",
               "California SB 243, in Kraft seit 01.01.2026 · AI Act Artikel 50"]:
        caret(d, M + 18, y + 20, 28, 6, RED)
        yy = y
        for ln in wrap(d, s_, f("BOOK", 34), MAXW - 70):
            d.text((M + 66, yy), ln, font=f("BOOK", 34), fill=INK); yy += int(34 * 1.4)
        y = yy + 18
    y += 8
    d.line([(M, y), (W - M, y)], fill=RULE, width=2); y += 26
    y = block(d, y, "Kein Rechtsrat. Wenn es dir schlecht geht: Telefonseelsorge "
                    "0800 111 0 111 oder 116 123, rund um die Uhr und kostenlos.",
              f("BOOK", 33), MUTED, MAXW, 1.4, 20)
    block(d, y, "Fehler gefunden? Schreib es in die Kommentare, ich korrigiere sichtbar.",
          f("BOOK", 33), RED, MAXW, 1.4)
    slides.append(img)

    return slides


# ================================================================ POST 15
def build_post15():
    """Bauform: Die Rekonstruktion. Ein Blatt je Schritt in der Reihenfolge, in der es
    passiert ist. Der Befund steckt in der Reihenfolge: Die Autokameras standen im
    Entwurf vom Maerz nicht drin, sie kamen im Juli ueber einen Aenderungsantrag dazu.
    Beleg-Panel auf Blatt 04 mit dem woertlichen Satz aus der Gesetzesbegruendung."""
    T = 6
    ST = "STAND 18.08.2026"
    slides = []

    # --- 01 HOOK
    # Schleswig-Holstein, Auto und Handy stehen in der Schlagzeile selbst, weil im Feed
    # oft nur dieses Blatt zu sehen ist. Die Fundstelle steht in der Unterzeile.
    img, d = new(1, T, ST)
    y = 268
    fo = f("COND", 84)
    for line in ["SCHLESWIG-HOLSTEIN", "WILL DEIN AUTO FILMEN", "UND DEIN HANDY SUCHEN"]:
        d.text((M, y), line, font=fo, fill=INK); y += 100
    y += 32
    d.line([(M, y), (M + 140, y)], fill=RED, width=6); y += 54
    block(d, y, "Ein Änderungsantrag vom 6. Juli 2026 fügt ins Polizeigesetz einen "
                "Paragrafen 184d ein. Wer im Kontrollfenster vorbeifährt, wird "
                "aufgenommen, und eine Software durchsucht das Bild.",
          f("BOOK", 46), INK, MAXW - 40, 1.4)
    slides.append(img)

    # --- 02 Der Entwurf vom Maerz
    img, d = new(2, T, ST)
    y = kicker(d, 236, "Im März stand davon nichts drin", size=38)
    block(d, y, "Am 24. März 2026 legte die Landesregierung ihren Entwurf vor, "
                "Drucksache 20/4284. Er erlaubt der Polizei Videoüberwachung, deren "
                "Bilder eine Software automatisch nach Bewegungsmustern durchsucht. "
                "Er erlaubt außerdem Gesichtserkennung in Echtzeit an öffentlich "
                "zugänglichen Orten, richterlich genehmigt für höchstens sieben Tage. "
                "Von Kameras für Autofahrende steht darin kein Wort.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 03 Der Aenderungsantrag vom Juli
    img, d = new(3, T, ST)
    y = kicker(d, 236, "Im Juli kam ein Paragraf dazu", size=38)
    block(d, y, "Gut drei Monate später, am 6. Juli 2026, reichten die Fraktionen von "
                "CDU und Bündnis 90/Die Grünen im Innen- und Rechtsausschuss einen "
                "Änderungsantrag ein, Umdruck 20/6786. Die Polizei darf danach "
                "Fahrzeuge und die Menschen am Steuer aufnehmen, das Kennzeichen "
                "erfassen und festhalten, wo und wann das Auto in welche Richtung "
                "fuhr. Die Bilder werden automatisiert auf Muster durchsucht, die auf "
                "ein Gerät in der Hand hindeuten.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 04 Was "stichprobenweise" heisst (Beleg-Panel)
    img, d = new(4, T, ST)
    y = kicker(d, 218, "Stichprobe meint Ort und Uhrzeit", size=38)
    y = beleg(d, y,
              "Umdruck 20/6786, Begründung zu § 184d",
              ['"Nicht verlangt ist eine zusätzliche',
               'Auswahl einzelner Fahrzeuge innerhalb',
               'des festgelegten Kontrollfensters."'],
              sub="Schleswig-Holsteinischer Landtag, 06.07.2026")
    block(d, y + 40, "Gemeint sind Kontrollort und Kontrollzeitraum. Wer da vorbeifährt, "
                     "wird aufgenommen. Dieselbe Begründung schreibt, die Maßnahme "
                     "erstrecke sich auf eine unbestimmte Vielzahl von Personen, die von "
                     "vornherein keinerlei Anlass gegeben haben.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 05 Verfahrensstand und die fehlende Zahl
    img, d = new(5, T, ST)
    y = kicker(d, 236, "Beschlossen ist davon noch nichts", size=38)
    block(d, y, "Der Änderungsantrag liegt im Innen- und Rechtsausschuss des Landtags. "
                "Trifft die Software daneben, sollen die Bilder sofort, spurenlos und "
                "automatisiert gelöscht werden. Wie oft sie danebentrifft, steht "
                "nirgends. Ich habe die achtundsechzig Seiten zweimal durchsucht, weil "
                "ich mir sicher war, eine Zahl übersehen zu haben. Es gibt keine.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 06 Quellen
    img, d = new(6, T, ST)
    y = kicker(d, 232, "Quellen", size=38)
    for s_ in ["Landtag Schleswig-Holstein, Drucksache 20/4284 vom 24.03.2026",
               "Landtag Schleswig-Holstein, Umdruck 20/6786 vom 06.07.2026",
               "§ 23 Absatz 1a StVO · Verordnung (EU) 2024/1689, Artikel 26"]:
        caret(d, M + 18, y + 22, 28, 6, RED)
        yy = y
        for ln in wrap(d, s_, f("BOOK", 40), MAXW - 70):
            d.text((M + 66, yy), ln, font=f("BOOK", 40), fill=INK); yy += int(40 * 1.4)
        y = yy + 18
    y += 8
    d.line([(M, y), (W - M, y)], fill=RULE, width=2); y += 26
    y = block(d, y, "Kein Rechtsrat. Beides ist ein Entwurf und nicht beschlossen.",
              f("BOOK", 36), MUTED, MAXW, 1.4, 20)
    block(d, y, "Fehler gefunden? Schreib es in die Kommentare, ich korrigiere sichtbar.",
          f("BOOK", 36), RED, MAXW, 1.4)
    slides.append(img)

    return slides


# ================================================================ POST 16
def build_post16():
    """Bauform: Der Fall. Bewusst nicht "Der Widerspruch": Berichterstattung und
    Jahresbericht widersprechen sich nicht, der Bericht ist nur vorsichtiger. Die
    Korrektur sitzt deshalb im Inneren des Posts auf Blatt 05. Zwei bebilderte Blaetter,
    das erlaubte Maximum: Balkenreihe auf 02, Beleg-Panel auf 04."""
    T = 6
    ST = "STAND 18.08.2026"
    slides = []

    # --- 01 HOOK
    img, d = new(1, T, ST)
    y = 268
    fo = f("COND", 84)
    for line in ["CHATBOTS SCHREIBEN", "JETZT DIE EILANTRÄGE", "GEGEN DAS JOBCENTER"]:
        d.text((M, y), line, font=fo, fill=INK); y += 100
    y += 32
    d.line([(M, y), (M + 140, y)], fill=RED, width=6); y += 54
    block(d, y, "Bei den acht Sozialgerichten in Nordrhein-Westfalen stiegen die "
                "Eilverfahren 2025 um 55,79 Prozent auf 7.615. Das Gericht nennt "
                "KI-Schriftsätze als einen Grund von mehreren.",
          f("BOOK", 46), INK, MAXW - 40, 1.4)
    slides.append(img)

    # --- 02 Die Zahlen (Balken, lineare Skala)
    img, d = new(2, T, ST)
    y = kicker(d, 228, "Von 4.888 auf 7.615 in einem Jahr", size=38)
    y = balken(d, y, [("Alle Eilverfahren 2024", 4888, "4.888"),
                      ("Alle Eilverfahren 2025", 7615, "7.615"),
                      ("davon Grundsicherung 2024", 3129, "3.129"),
                      ("davon Grundsicherung 2025", 4989, "4.989")])
    block(d, y + 16, "In der Arbeitslosenversicherung ging es von 160 auf 382 Anträge.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 03 Warum der Eilantrag
    img, d = new(3, T, ST)
    y = kicker(d, 236, "Warum überhaupt ein Eilantrag", size=38)
    block(d, y, "Ein Eilantrag muss schnell entschieden werden. 2025 dauerte er im "
                "Schnitt 1,3 Monate. Ein normales Klageverfahren dauerte 15,6 Monate. "
                "Wer auf Geld wartet, für den sind das mehr als vierzehn Monate "
                "Unterschied. Der Präsident des Landessozialgerichts sagt, die KI "
                "empfehle meist genau dieses Verfahren.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 04 Was in den Schriftsaetzen steht (Beleg-Panel)
    img, d = new(4, T, ST)
    y = kicker(d, 210, "Rechtsprechung, die es so nicht gibt", size=38)
    y = beleg(d, y,
              "LSG Nordrhein-Westfalen, Jahresbericht 2025",
              ['"Diese Schriftsätze sind häufig sehr lang',
               'und gekennzeichnet von einer Vielzahl oft',
               'nicht zielführender Anträge und Verweise',
               'auf Rechtsprechung, die nur zum Teil und',
               'oft mit anderem Inhalt existiert."'],
              sub="Herausgeber ist der Präsident, 24.04.2026")
    block(d, y + 36, "Die Präsidentin des Bundessozialgerichts beschrieb im Februar "
                     "denselben Prüfaufwand für die ganze Sozialgerichtsbarkeit.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 05 Die Korrektur an der Schlagzeile
    img, d = new(5, T, ST)
    y = kicker(d, 236, "Was der Bericht als Ursache nennt", size=38)
    block(d, y, "In den Schlagzeilen steht die KI-Schwemme. Der Bericht nennt zuerst "
                "die Konjunktur, weil die Zuwächse vor allem Arbeitslosenversicherung "
                "und Grundsicherung betreffen. KI-Schriftsätze befördern den "
                "bundesweiten Trend wesentlich auch, heißt es dort. Wie viele "
                "Schriftsätze mit KI entstanden, zählt keine Statistik. Ich hatte die "
                "Meldung zuerst genauso gelesen wie die Schlagzeilen.",
          f("BOOK", 45), INK, MAXW, 1.42)
    slides.append(img)

    # --- 06 Quellen
    img, d = new(6, T, ST)
    y = kicker(d, 232, "Quellen", size=38)
    for s_ in ["LSG Nordrhein-Westfalen, Jahresbericht 2025, vom 24.04.2026",
               "Bundessozialgericht, Pressemitteilung 4/2026 vom 11.02.2026",
               "dpa und LTO vom 17.08.2026 zu den Zahlen des ersten Quartals"]:
        caret(d, M + 18, y + 22, 28, 6, RED)
        yy = y
        for ln in wrap(d, s_, f("BOOK", 40), MAXW - 70):
            d.text((M + 66, yy), ln, font=f("BOOK", 40), fill=INK); yy += int(40 * 1.4)
        y = yy + 18
    y += 8
    d.line([(M, y), (W - M, y)], fill=RULE, width=2); y += 26
    y = block(d, y, "Kein Rechtsrat. Die Quartalszahlen 2026 sind berichtet, nicht belegt.",
              f("BOOK", 36), MUTED, MAXW, 1.4, 20)
    block(d, y, "Fehler gefunden? Schreib es in die Kommentare, ich korrigiere sichtbar.",
          f("BOOK", 36), RED, MAXW, 1.4)
    slides.append(img)

    return slides


# ================================================================ STORIES (1080x1920)
def build_stories():
    """Story-Slides im Hochformat. Inhalt bleibt in der Sicherheitszone (oben ~260 px für
    Profil-/Schließen-UI, unten ~270 px für Antwortleiste/Sticker frei lassen)."""
    SH = 1920
    stories = []

    def canvas(bg):
        img = Image.new("RGB", (W, SH), bg)
        return img, ImageDraw.Draw(img)

    def brand(d, fg=INK, accent=RED, rule_col=RULE):
        caret(d, M + 16, 316, 34, 7, accent)
        d.text((M + 48, 302), "KI.NÜCHTERN", font=f("MONOB", 30), fill=fg)
        d.line([(M, 372), (W - M, 372)], fill=rule_col, width=2)

    def bullets(d, y, items, fill, size=50, accent=RED):
        for it in items:
            caret(d, M + 20, y + 30, 34, 7, accent)
            yy = y
            for ln in wrap(d, it, f("BOOK", size), MAXW - 80):
                d.text((M + 80, yy), ln, font=f("BOOK", size), fill=fill)
                yy += int(size * 1.34)
            y = yy + 58
        return y

    # --- 1) Willkommen (fürs Highlight „Start"), hell
    img, d = canvas(PAPER)
    brand(d)
    y = 560
    d.text((M, y), "NEU HIER?", font=f("COND", 150), fill=INK); y += 214
    d.line([(M, y), (M + 160, y)], fill=RED, width=8); y += 78
    for line in ["KI.", "NÜCHTERN."]:
        d.text((M, y), line, font=f("COND", 118), fill=INK); y += 138
    y += 54
    block(d, y, "Ohne Hype. Ohne Panik. Mit Quelle.", f("COND", 56), INK, MAXW, 1.3)
    stories.append(("story_1_start", img))

    # --- 2) Drei Versprechen, dunkel
    img, d = canvas(INK)
    brand(d, fg=PAPER, accent=RED, rule_col=(74, 74, 82))
    y = 520
    d.text((M, y), "DREI", font=f("COND", 132), fill=PAPER); y += 152
    d.text((M, y), "VERSPRECHEN", font=f("COND", 116), fill=PAPER); y += 210
    bullets(d, y, ["Jede Zahl hat eine Quelle.",
                   "Ist etwas unklar, steht das im Post.",
                   "Es wird nichts verkauft."], PAPER)
    stories.append(("story_2_versprechen", img))

    # --- 3) Wegweiser zu den Posts, hell
    img, d = canvas(PAPER)
    brand(d)
    y = 560
    d.text((M, y), "WOMIT ES", font=f("COND", 120), fill=INK); y += 138
    d.text((M, y), "LOSGING", font=f("COND", 120), fill=INK); y += 178
    d.line([(M, y), (M + 160, y)], fill=RED, width=8); y += 74
    bullets(d, y, ["Deine Bewerbung sortiert eine KI aus.",
                   "Seit dem 2. August: KI muss sich zu erkennen geben."], INK, size=48)
    d.text((M, 1520), "→ Im Feed. Tippe aufs Profil.", font=f("MONO", 30), fill=MUTED)
    stories.append(("story_3_wegweiser", img))

    # --- 4) Poll-Hintergrund, rot (Umfrage-Sticker kommt in der App darunter)
    img, d = canvas(RED)
    brand(d, fg=PAPER, accent=PAPER, rule_col=(170, 40, 36))
    y = 620
    for line in ["KILLT KI", "DIE JOBS?"]:
        d.text((M, y), line, font=f("COND", 140), fill=PAPER); y += 168
    y += 44
    block(d, y, "Erst dein Bauchgefühl. Die nüchterne Antwort kommt.",
          f("BOOK", 50), PAPER, MAXW, 1.34)
    stories.append(("story_4_poll", img))

    return stories


# ---------------------------------------------------------------- ausgabe
def save_slides(slides, out_dir):
    """Schreibt die Blaetter und raeumt ueberzaehlige aus frueheren Laeufen weg.
    Ohne das Aufraeumen bleiben beim Kuerzen eines Posts die alten Blaetter liegen und
    der Ordner zeigt eine Mischung aus zwei Staenden (aufgefallen bei Post 5 am 16.08.2026:
    blatt_07/08 stammten noch vom 8-Blatt-Stand)."""
    for i, im in enumerate(slides, 1):
        im.save(out_dir / f"blatt_{i:02d}.png", "PNG")
    for alt_blatt in sorted(out_dir.glob("blatt_*.png")):
        nummer = int(alt_blatt.stem.split("_")[1])
        if nummer > len(slides):
            alt_blatt.unlink()
            print(f"  entfernt (ueberzaehlig): {alt_blatt.name}")
    return len(slides)


# Nur aktive Posts rendern. Post 0/1/2/4/5/6/7/8/9/10/13 sind gepostet und liegen unter archive/.
print(f"Logo    -> {OUT_LOGO}")
print("(Post 0-2/4-10/12-16 gepostet & archiviert -> archive/, nicht neu gerendert)")

_stories = build_stories()
for _name, _im in _stories:
    _im.save(OUT_STORY / f"{_name}.png", "PNG")
print(f"Stories: {len(_stories)} -> {OUT_STORY}")

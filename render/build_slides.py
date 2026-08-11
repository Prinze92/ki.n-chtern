"""
build_slides.py — Renderer für ki.nüchtern (Logo + Carousel-Blätter).

Herkunft: mobile Session. Hier angepasst für plattformunabhängigen Betrieb:
  - Ausgabepfade sind repo-relativ (nicht mehr /mnt/user-data/outputs).
  - Schriften werden über find_font() gesucht (brand/fonts/ -> OS-Fonts -> Fallback),
    statt fester Linux-Pfade.

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
OUT_POST1 = REPO / "posts" / "post-001-bewerbung-ki-frist" / "slides"
OUT_LOGO.mkdir(parents=True, exist_ok=True)
OUT_POST1.mkdir(parents=True, exist_ok=True)

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
        tw = d.textlength(t, font=fo)
        tx = size / 2 - tw / 2
        d.text((tx, size * 0.27), t, font=fo, fill=fg_text)
        caret(d, size / 2, size * 0.735, size * 0.20, int(34 * s), fg_caret)
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
d.text((110, 120), "ki.nüchtern", font=fo, fill=INK)
tw = d.textlength("ki.nüchtern", font=fo)
caret(d, 110 + tw / 2, 320, 90, 18, RED)
fo2 = f("MONO", 36)
d.text((110, 350), "OHNE HYPE. MIT QUELLE.", font=fo2, fill=MUTED)
wm.save(OUT_LOGO / "wortmarke.png", "PNG")


# ---------------------------------------------------------------- slide frame
W, H = 1080, 1350
M = 100
MAXW = W - 2 * M
TOTAL = 9


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


def frame(d, idx):
    d.line([(M, 84), (W - M, 84)], fill=INK, width=3)
    d.line([(M, 94), (W - M, 94)], fill=RULE, width=2)
    caret(d, M + 16, 140, 34, 7, RED)
    fo = f("MONOB", 27)
    d.text((M + 48, 126), "KI.NÜCHTERN", font=fo, fill=INK)
    lab = f"BLATT {idx:02d}/{TOTAL:02d}"
    d.text((W - M - d.textlength(lab, font=fo), 126), lab, font=fo, fill=MUTED)

    d.line([(M, H - 150), (W - M, H - 150)], fill=RULE, width=2)
    fo = f("MONO", 25)
    d.text((M, H - 128), "STAND 11.08.2026", font=fo, fill=MUTED)
    r = "QUELLEN → BLATT 09"
    d.text((W - M - d.textlength(r, font=fo), H - 128), r, font=fo, fill=MUTED)


def kicker(d, y, text, color=RED):
    fo = f("MONOB", 30)
    d.text((M, y), text.upper(), font=fo, fill=color)
    y += 46
    d.line([(M, y), (M + 90, y)], fill=color, width=5)
    return y + 52


def new(idx):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    frame(d, idx)
    return img, d


slides = []

# --- 01 HOOK
img, d = new(1)
y = 300
fo = f("COND", 104)
for line in ["DEINE", "BEWERBUNG", "SORTIERT EINE", "SOFTWARE AUS."]:
    d.text((M, y), line, font=fo, fill=INK)
    y += 118
y += 40
d.line([(M, y), (M + 140, y)], fill=RED, width=6)
y += 54
block(d, y, "Und die Regel dafür wurde vor zwei Wochen verschoben. "
            "Fast alle Ratgeber im Netz sind seitdem falsch.",
      f("BOOK", 44), INK, MAXW - 40, 1.4)
slides.append(img)

# --- 02 DER FALL
img, d = new(2)
y = kicker(d, 300, "Der Fall")
block(d, y, "Größere Unternehmen setzen Software ein, die Lebensläufe liest, "
            "bewertet und in eine Rangfolge bringt — bevor ein Mensch sie sieht.",
      f("BOOK", 52), INK, MAXW, 1.42)
slides.append(img)

# --- 03 WAS ÜBERALL STEHT
img, d = new(3)
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
img, d = new(4)
y = kicker(d, 250, "Die Korrektur")
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
img, d = new(5)
y = kicker(d, 250, "Der Beleg")
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
img, d = new(6)
y = kicker(d, 250, "Der Haken")
y = block(d, y, '„Verschoben“ heißt nicht „erlaubt“.', f("COND", 66), INK, MAXW, 1.3, 50)
y = block(d, y, "DSGVO, BDSG, AGG und die Mitbestimmung des Betriebsrats gelten "
                "unverändert weiter.", f("BOOK", 46), INK, MAXW, 1.42, 44)
block(d, y, "Und die Kennzeichnungspflicht für KI-Inhalte bleibt beim "
            "2. August 2026.", f("BOOK", 38), MUTED, MAXW, 1.42)
slides.append(img)

# --- 07 FÜR DICH
img, d = new(7)
y = kicker(d, 240, "Was das für dich heißt")
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
img, d = new(8)
y = kicker(d, 320, "Die offene Frage", MUTED)
y = block(d, y, "16 Monate mehr Zeit für Unternehmen.", f("COND", 72), INK, MAXW, 1.24, 30)
y = block(d, y, "Wer trägt sie in der Zwischenzeit?", f("COND", 72), RED, MAXW, 1.24, 70)
block(d, y, "Schreib es in die Kommentare.", f("BOOK", 40), MUTED, MAXW, 1.4)
slides.append(img)

# --- 09 QUELLEN
img, d = new(9)
y = kicker(d, 230, "Quellen")
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

for i, im in enumerate(slides, 1):
    im.save(OUT_POST1 / f"blatt_{i:02d}.png", "PNG")

print(f"slides: {len(slides)}  ->  {OUT_POST1}")
print(f"logo   ->  {OUT_LOGO}")

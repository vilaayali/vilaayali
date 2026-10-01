"""Animated SVG widget generator for the vilaayali GitHub profile."""
import os, textwrap

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)

BG, PANEL, PANEL2, LINE = "#07080C", "#0D1017", "#121621", "#1C2230"
TEXT, SUB, DIM = "#F4F5F8", "#8B93A7", "#4A5268"
V, C, P, G = "#7C5CFF", "#22D3EE", "#F472B6", "#22C55E"
SANS = "'Inter','Segoe UI',-apple-system,BlinkMacSystemFont,Helvetica,Arial,sans-serif"
MONO = "'JetBrains Mono','SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg(name, W, H, body, defs="", css="", border=True, radius=24):
    frame = f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="{radius}" fill="none" stroke="{LINE}"/>' if border else ""
    out = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none">
<defs>
<linearGradient id="vc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{V}"/><stop offset=".55" stop-color="{C}"/><stop offset="1" stop-color="{P}"/></linearGradient>
<clipPath id="frame"><rect width="{W}" height="{H}" rx="{radius}"/></clipPath>
{defs}
<style>
text {{ font-family: {SANS}; }}
.mono {{ font-family: {MONO}; }}
@keyframes spin {{ to {{ transform: rotate(360deg) }} }}
@keyframes pulse {{ 0%,100% {{ opacity: 1 }} 50% {{ opacity: .25 }} }}
@keyframes blink {{ 50% {{ opacity: 0 }} }}
@keyframes up {{ from {{ opacity: 0; transform: translateY(18px) }} to {{ opacity: 1; transform: none }} }}
@keyframes draw {{ to {{ stroke-dashoffset: 0 }} }}
@keyframes ping {{ 0% {{ r: 4; opacity: .9 }} 100% {{ r: 30; opacity: 0 }} }}
@keyframes twinkle {{ 0%,100% {{ opacity: .15 }} 50% {{ opacity: 1 }} }}
.up {{ animation: up .9s cubic-bezier(.2,.7,.2,1) both; }}
{css}
</style>
</defs>
<g clip-path="url(#frame)">
{body}
</g>
{frame}
</svg>'''
    open(f"{OUT}/{name}.svg", "w").write(out)


def dotgrid(W, H, gap=24, op=.5):
    return (f'<pattern id="dots" width="{gap}" height="{gap}" patternUnits="userSpaceOnUse">'
            f'<circle cx="1" cy="1" r="1" fill="{DIM}" opacity="{op}"/></pattern>')


# ---------------------------------------------------------------- HERO
def hero():
    W, H = 1200, 440
    cx, cy = 960, 220
    defs = dotgrid(W, H) + f'''
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="70"/></filter>
<filter id="glow"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<linearGradient id="shine" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
  <stop offset="0" stop-color="{TEXT}"/><stop offset=".42" stop-color="{TEXT}"/>
  <stop offset=".5" stop-color="{C}"/><stop offset=".58" stop-color="{TEXT}"/><stop offset="1" stop-color="{TEXT}"/>
  <animateTransform attributeName="gradientTransform" type="translate" values="-1 0;1 0;1 0" keyTimes="0;.45;1" dur="6s" repeatCount="indefinite"/>
</linearGradient>
<radialGradient id="core"><stop offset="0" stop-color="{V}" stop-opacity=".9"/><stop offset="1" stop-color="{V}" stop-opacity="0"/></radialGradient>
<linearGradient id="leftfade" x1="0" x2="1"><stop offset="0" stop-color="{BG}"/><stop offset=".5" stop-color="{BG}" stop-opacity=".75"/><stop offset="1" stop-color="{BG}" stop-opacity="0"/></linearGradient>
<linearGradient id="star" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff"/></linearGradient>'''

    roles = ["real-time apps.", "scalable APIs.", "pixel-perfect UIs.", "products people love."]
    n = len(roles)
    css = f'''
.orbit1 {{ transform-origin: {cx}px {cy}px; animation: spin 30s linear infinite; }}
.orbit2 {{ transform-origin: {cx}px {cy}px; animation: spin 46s linear infinite reverse; }}
.upright1 {{ transform-box: fill-box; transform-origin: center; animation: spin 30s linear infinite reverse; }}
.upright2 {{ transform-box: fill-box; transform-origin: center; animation: spin 46s linear infinite; }}
.role {{ opacity: 0; animation: role {n*3}s cubic-bezier(.2,.7,.2,1) infinite; }}
@keyframes role {{ 0% {{ opacity: 0; transform: translateY(22px) }} 4% {{ opacity: 1; transform: none }}
  {100/n - 3:.1f}% {{ opacity: 1; transform: none }} {100/n:.1f}% {{ opacity: 0; transform: translateY(-22px) }} 100% {{ opacity: 0 }} }}
.a1 {{ animation: drift1 18s ease-in-out infinite; }} .a2 {{ animation: drift2 22s ease-in-out infinite; }} .a3 {{ animation: drift3 26s ease-in-out infinite; }}
@keyframes drift1 {{ 50% {{ transform: translate(-140px, 60px) }} }}
@keyframes drift2 {{ 50% {{ transform: translate(120px, -50px) }} }}
@keyframes drift3 {{ 50% {{ transform: translate(-60px, -70px) }} }}
.shoot {{ animation: shoot 7s ease-in infinite; }}
@keyframes shoot {{ 0%,70% {{ transform: translate(0,0); opacity: 0 }} 72% {{ opacity: 1 }} 85%,100% {{ transform: translate(-520px, 260px); opacity: 0 }} }}
.caret {{ animation: blink 1s steps(1) infinite; }}
.pulse {{ animation: pulse 1.8s ease-in-out infinite; }}
.ring {{ animation: ping2 2.4s cubic-bezier(0,0,.2,1) infinite; }}
@keyframes ping2 {{ 0% {{ r: 4; opacity: .9 }} 100% {{ r: 13; opacity: 0 }} }}
'''
    for i in range(n):
        css += f".r{i} {{ animation-delay: {i*3}s; }}\n"

    stars = ""
    import random
    random.seed(7)
    for _ in range(46):
        x, y = random.randint(560, 1190), random.randint(10, 430)
        r = random.choice([.8, 1, 1.2, 1.6])
        stars += f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" style="animation: twinkle {random.uniform(2,5):.1f}s ease-in-out {random.uniform(0,4):.1f}s infinite"/>'

    def chip(x, y, label, color, cls):
        w = 18 + len(label) * 8.6 + 14
        return (f'<g class="{cls}"><rect x="{x - w/2:.0f}" y="{y-15}" width="{w:.0f}" height="30" rx="15" fill="{PANEL2}" stroke="{LINE}"/>'
                f'<circle cx="{x - w/2 + 15:.0f}" cy="{y}" r="4" fill="{color}"/>'
                f'<text x="{x - w/2 + 25:.0f}" y="{y+5}" class="mono" font-size="13" fill="{TEXT}">{label}</text></g>')

    r1, r2 = 118, 186
    orbit = f'''
<circle cx="{cx}" cy="{cy}" r="150" fill="url(#core)" opacity=".55"/>
<circle cx="{cx}" cy="{cy}" r="{r1}" stroke="{SUB}" stroke-opacity=".35" stroke-dasharray="2 7"/>
<circle cx="{cx}" cy="{cy}" r="{r2}" stroke="{SUB}" stroke-opacity=".22"/>
<circle cx="{cx}" cy="{cy}" r="250" stroke="{SUB}" stroke-opacity=".12" stroke-dasharray="1 6"/>
<g class="orbit1">{chip(cx + r1, cy, "React", "#61DAFB", "upright1")}{chip(cx - r1, cy, "Next.js", "#FFFFFF", "upright1")}</g>
<g class="orbit2">{chip(cx, cy - r2, "Node.js", "#5FA04E", "upright2")}{chip(cx, cy + r2, "WebSockets", C, "upright2")}{chip(cx - 132, cy + 132, "Redux", "#9B7BEA", "upright2")}{chip(cx + 132, cy - 132, "Postgres", "#4F8BCB", "upright2")}</g>
<g filter="url(#glow)">
  <rect x="{cx-38}" y="{cy-38}" width="76" height="76" rx="22" fill="{PANEL}" stroke="url(#vc)" stroke-width="1.5"/>
  <text x="{cx}" y="{cy+8}" text-anchor="middle" class="mono" font-size="22" font-weight="700" fill="{TEXT}">&lt;/&gt;</text>
</g>'''

    role_txt = "".join(
        f'<text x="168" y="262" class="role r{i}" font-size="30" font-weight="600" fill="url(#vc)">{esc(r)}</text>'
        for i, r in enumerate(roles))

    stats = [("2+", "years shipping"), ("2×", "faster load times"), ("B2B", "e-commerce at scale")]
    stat_svg = ""
    for i, (big, small) in enumerate(stats):
        x = 64 + i * 190
        stat_svg += (f'<g class="up" style="animation-delay:{.7 + i*.12:.2f}s">'
                     f'<text x="{x}" y="370" font-size="30" font-weight="800" fill="{TEXT}" letter-spacing="-1">{big}</text>'
                     f'<text x="{x}" y="394" class="mono" font-size="12" fill="{SUB}" letter-spacing="1">{small.upper()}</text></g>')
        if i:
            stat_svg += f'<line x1="{x-24}" y1="346" x2="{x-24}" y2="396" stroke="{LINE}"/>'

    body = f'''
<rect width="{W}" height="{H}" fill="{BG}"/>
<g filter="url(#blur)" opacity=".75">
  <circle class="a1" cx="1000" cy="120" r="200" fill="{V}"/>
  <circle class="a2" cx="760" cy="380" r="170" fill="{C}" opacity=".55"/>
  <circle class="a3" cx="1150" cy="380" r="150" fill="{P}" opacity=".45"/>
</g>
<rect width="{W}" height="{H}" fill="url(#dots)"/>
{stars}
<g class="shoot"><line x1="1180" y1="30" x2="1260" y2="-10" stroke="url(#star)" stroke-width="2" transform="rotate(180 1220 10)"/></g>
{orbit}
<rect width="{W}" height="{H}" fill="url(#leftfade)"/>

<g class="up" style="animation-delay:.05s">
  <rect x="64" y="44" width="40" height="40" rx="12" fill="url(#vc)"/>
  <text x="84" y="70" text-anchor="middle" class="mono" font-size="15" font-weight="800" fill="{BG}">SV</text>
  <text x="118" y="62" class="mono" font-size="13" fill="{TEXT}" letter-spacing="1">VILAAYALI</text>
  <text x="118" y="79" class="mono" font-size="11" fill="{SUB}" letter-spacing="1">SOFTWARE ENGINEER</text>
</g>
<g class="up" style="animation-delay:.15s">
  <rect x="380" y="46" width="170" height="34" rx="17" fill="{PANEL}" stroke="{LINE}"/>
  <circle cx="401" cy="63" r="4" fill="{G}"/><circle cx="401" cy="63" r="4" stroke="{G}" stroke-width="1.5" class="ring"/>
  <text x="414" y="68" class="mono" font-size="12" fill="{TEXT}">Open to work</text>
</g>

<text x="62" y="196" class="up" style="animation-delay:.25s" font-size="84" font-weight="800" letter-spacing="-3.5" fill="url(#shine)">Syed Vilaay Ali</text>
<g class="up" style="animation-delay:.4s">
  <text x="64" y="262" font-size="30" font-weight="500" fill="{SUB}">I build</text>
  {role_txt}
</g>
<text x="64" y="300" class="up mono" style="animation-delay:.5s" font-size="14" fill="{SUB}">React · Next.js · Node.js — based in Lahore, PK<tspan class="caret" fill="{C}"> ▍</tspan></text>
<line x1="64" y1="326" x2="600" y2="326" stroke="{LINE}"/>
{stat_svg}
'''
    svg("hero", W, H, body, defs, css)


# ---------------------------------------------------------------- TERMINAL
def terminal():
    W, H = 600, 380
    lines = [
        ("cmd", "whoami"),
        ("out", "syed vilaay ali — software engineer"),
        ("cmd", "cat focus.txt"),
        ("out", "real-time apps · REST APIs · fast UIs"),
        ("cmd", "ls ./experience"),
        ("out", "bestel-communications/  ginkgo-retail/"),
        ("cmd", "npm run ship"),
        ("ok", "✓ compiled  ✓ tested  ✓ deployed"),
    ]
    cycle = 16.0
    t, css, body_lines = 0.6, "", ""
    y0, lh, cw = 104, 30, 8.4
    for i, (kind, s) in enumerate(lines):
        y = y0 + i * lh
        prefix = 22 if kind == "cmd" else 0
        n = len(s)
        dur = n * 0.045 if kind == "cmd" else 0.25
        start, end = t, t + dur
        a, b = start / cycle * 100, end / cycle * 100
        width = n * cw + 6
        css += (f"@keyframes t{i} {{ 0%,{a:.2f}% {{ width: 0 }} {b:.2f}% {{ width: {width:.0f}px }} 94% {{ width: {width:.0f}px }} 97%,100% {{ width: 0 }} }}\n"
                f".t{i} {{ animation: t{i} {cycle}s {'steps(%d)' % n if kind == 'cmd' else 'linear'} infinite; }}\n"
                f"@keyframes p{i} {{ 0%,{a:.2f}% {{ opacity: 0 }} {a+.01:.2f}%,94% {{ opacity: 1 }} 97%,100% {{ opacity: 0 }} }}\n"
                f".p{i} {{ animation: p{i} {cycle}s linear infinite; }}\n")
        x = 32 + prefix
        clip = f'<clipPath id="c{i}"><rect class="t{i}" x="{x}" y="{y-20}" width="0" height="28"/></clipPath>'
        color = {"cmd": TEXT, "out": SUB, "ok": G}[kind]
        prompt = f'<text x="32" y="{y}" class="mono p{i}" font-size="14" fill="{C}">❯</text>' if kind == "cmd" else ""
        body_lines += f'{clip}{prompt}<text x="{x}" y="{y}" class="mono" font-size="14" fill="{color}" clip-path="url(#c{i})">{esc(s)}</text>'
        t = end + (0.5 if kind == "cmd" else 0.35)
    cy = y0 + len(lines) * lh
    a = t / cycle * 100
    css += (f"@keyframes cur {{ 0%,{a:.2f}% {{ opacity: 0 }} {a+.01:.2f}%,94% {{ opacity: 1 }} 97%,100% {{ opacity: 0 }} }}\n"
            f".cur {{ animation: cur {cycle}s linear infinite; }} .blink {{ animation: blink 1s steps(1) infinite; }}")
    body = f'''
<rect width="{W}" height="{H}" fill="{PANEL}"/>
<rect width="{W}" height="52" fill="{PANEL2}"/>
<line x1="0" y1="52" x2="{W}" y2="52" stroke="{LINE}"/>
<circle cx="28" cy="26" r="6" fill="#FF5F57"/><circle cx="48" cy="26" r="6" fill="#FEBC2E"/><circle cx="68" cy="26" r="6" fill="#28C840"/>
<text x="{W/2}" y="31" text-anchor="middle" class="mono" font-size="12" fill="{SUB}">vilaayali — zsh — 80×24</text>
{body_lines}
<g class="cur"><text x="32" y="{cy}" class="mono" font-size="14" fill="{C}">❯</text><rect class="blink" x="54" y="{cy-14}" width="9" height="18" fill="{TEXT}"/></g>
'''
    svg("terminal", W, H, body, css=css)


# ---------------------------------------------------------------- BENTO
def bento():
    W, H = 600, 380
    pad, gap = 16, 14
    tw, th = (W - 2*pad - gap) / 2, (H - 2*pad - gap) / 2
    pos = [(pad, pad), (pad + tw + gap, pad), (pad, pad + th + gap), (pad + tw + gap, pad + th + gap)]

    def tile(i, inner):
        x, y = pos[i]
        return (f'<g transform="translate({x:.0f},{y:.0f})"><g class="up" style="animation-delay:{.1 + i*.12:.2f}s">'
                f'<rect width="{tw:.0f}" height="{th:.0f}" rx="18" fill="{PANEL2}" stroke="{LINE}"/>{inner}</g></g>')

    def label(s):
        return f'<text x="20" y="34" class="mono" font-size="11" fill="{SUB}" letter-spacing="1.5">{s}</text>'

    # location + radar
    rx, ry = tw - 62, th - 58
    radar = "".join(f'<circle cx="{rx:.0f}" cy="{ry:.0f}" r="4" stroke="{C}" stroke-width="1.5" class="ping" style="animation-delay:{d}s"/>' for d in (0, .8, 1.6))
    t0 = (label("BASED IN") + f'<text x="20" y="78" font-size="26" font-weight="700" fill="{TEXT}">Lahore</text>'
          f'<text x="20" y="102" font-size="15" fill="{SUB}">Pakistan · GMT+5</text>'
          f'<circle cx="{rx:.0f}" cy="{ry:.0f}" r="34" stroke="{LINE}"/><circle cx="{rx:.0f}" cy="{ry:.0f}" r="20" stroke="{LINE}"/>'
          f'{radar}<circle cx="{rx:.0f}" cy="{ry:.0f}" r="4" fill="{C}"/>')

    # experience ring
    R = 34
    circ = 2 * 3.14159 * R
    gx, gy = tw - 62, th - 58
    t1 = (label("EXPERIENCE") + f'<text x="20" y="92" font-size="52" font-weight="800" letter-spacing="-2" fill="url(#vc)">2+</text>'
          f'<text x="20" y="118" font-size="15" fill="{SUB}">years in production</text>'
          f'<circle cx="{gx:.0f}" cy="{gy:.0f}" r="{R}" stroke="{LINE}" stroke-width="6"/>'
          f'<circle cx="{gx:.0f}" cy="{gy:.0f}" r="{R}" stroke="url(#vc)" stroke-width="6" stroke-linecap="round" '
          f'stroke-dasharray="{circ:.1f}" stroke-dashoffset="{circ:.1f}" transform="rotate(-90 {gx:.0f} {gy:.0f})" class="ringdraw"/>')

    # status
    t2 = (label("STATUS") + f'<circle cx="28" cy="72" r="6" fill="{G}"/><circle cx="28" cy="72" r="6" stroke="{G}" stroke-width="2" class="ping"/>'
          f'<text x="44" y="80" font-size="24" font-weight="700" fill="{TEXT}">Open to work</text>'
          f'<text x="20" y="106" font-size="15" fill="{SUB}">Full-time · Contract</text>'
          f'<rect x="20" y="{th-46:.0f}" width="118" height="30" rx="15" fill="{TEXT}"/>'
          f'<text x="79" y="{th-26:.0f}" text-anchor="middle" font-size="13" font-weight="600" fill="{BG}">Let\'s talk →</text>')

    # now / equalizer
    bars = ""
    for k in range(9):
        x = 20 + k * 13
        bars += (f'<rect x="{x}" y="{th-60:.0f}" width="7" height="44" rx="3.5" fill="url(#vc)" class="eq" '
                 f'style="animation-duration:{.7 + (k*37 % 9)/10:.2f}s; animation-delay:-{k*.13:.2f}s"/>')
    t3 = (label("RIGHT NOW") + f'<text x="20" y="74" font-size="20" font-weight="700" fill="{TEXT}">Shipping real-time UIs</text>'
          f'<text x="20" y="96" font-size="14" fill="{SUB}">in the zone 🎧</text>{bars}')

    css = f'''
.ping {{ animation: ping 2.4s cubic-bezier(0,0,.2,1) infinite; }}
.ringdraw {{ animation: ring 2.2s .4s cubic-bezier(.2,.7,.2,1) forwards; }}
@keyframes ring {{ to {{ stroke-dashoffset: {circ*0.3:.1f} }} }}
.eq {{ transform-box: fill-box; transform-origin: bottom; animation: eq 1s ease-in-out infinite alternate; }}
@keyframes eq {{ 0% {{ transform: scaleY(.15) }} 100% {{ transform: scaleY(1) }} }}
'''
    body = f'<rect width="{W}" height="{H}" fill="{PANEL}"/>' + tile(0, t0) + tile(1, t1) + tile(2, t2) + tile(3, t3)
    svg("bento", W, H, body, css=css)


# ---------------------------------------------------------------- SECTION TITLES
def section(slug, num, title, note, light=False):
    TX, LN, SB = ('#0B0D12', '#D9DCE3', '#5E6573') if light else (TEXT, LINE, SUB)
    W, H = 1200, 96
    tlen = len(title) * 21 + 20
    css = f'''
.ln {{ stroke-dasharray: 1200; stroke-dashoffset: 1200; animation: draw 1.6s .3s cubic-bezier(.2,.7,.2,1) forwards; }}
.dot {{ animation: pulse 1.6s ease-in-out infinite; }}'''
    body = f'''
<text x="0" y="60" class="mono up" font-size="15" fill="url(#vc)" font-weight="700">{num}</text>
<text x="44" y="64" class="up" style="animation-delay:.1s" font-size="38" font-weight="800" letter-spacing="-1.5" fill="{TX}">{esc(title)}<tspan fill="{C}">.</tspan></text>
<line class="ln" x1="{44 + tlen}" y1="52" x2="{W - 190}" y2="52" stroke="{LN}" stroke-width="1.5"/>
<circle class="dot" cx="{W - 176}" cy="52" r="4" fill="{C}"/>
<text x="{W}" y="57" text-anchor="end" class="mono up" style="animation-delay:.3s" font-size="13" fill="{SB}" letter-spacing="1.5">{esc(note.upper())}</text>'''
    svg(f"title-{slug}" + ("-light" if light else ""), W, H, body, css=css, border=False, radius=0)


# ---------------------------------------------------------------- EXPERIENCE TIMELINE
def experience():
    W, H = 1200, 360
    items = [
        ("EDUCATION", "A.A.S Computer Programming", "European University of Lefke", ["Cyprus", "Foundations in CS & software"], SUB),
        ("NOV 2024 — MAY 2025", "Junior Software Engineer", "Ginkgo Retail · Lahore", ["B2B storefront & admin panel", "Reusable component library"], V),
        ("AUG 2025 — APR 2026", "Associate Software Engineer", "Bestel Communications · Lahore", ["Real-time app over WebSockets", "2× faster with lazy loading"], C),
    ]
    xs = [48, 432, 816]
    cw = 336
    ly = 70
    body = f'<rect width="{W}" height="{H}" fill="{PANEL}"/><rect width="{W}" height="{H}" fill="url(#dots)" opacity=".5"/>'
    body += f'<line x1="48" y1="{ly}" x2="{W-48}" y2="{ly}" stroke="{LINE}" stroke-width="2"/>'
    body += f'<line class="prog" x1="48" y1="{ly}" x2="{W-48}" y2="{ly}" stroke="url(#vcu)" stroke-width="2.5"/>'
    body += f'<circle r="5" fill="#fff" filter="url(#g2)"><animate attributeName="cx" values="48;{W-48}" dur="5s" repeatCount="indefinite"/><animate attributeName="cy" values="{ly};{ly}" dur="5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.9;1" dur="5s" repeatCount="indefinite"/></circle>'
    for i, (period, role, org, bullets, col) in enumerate(items):
        x = xs[i]
        d = .4 + i * .45
        node = (f'<circle cx="{x+16}" cy="{ly}" r="9" fill="{PANEL}" stroke="{col}" stroke-width="2" class="pop" style="animation-delay:{d:.2f}s"/>'
                f'<circle cx="{x+16}" cy="{ly}" r="3.5" fill="{col}" class="pop" style="animation-delay:{d:.2f}s"/>')
        bl = "".join(f'<circle cx="{x+26}" cy="{246 + j*28}" r="2.5" fill="{col}"/><text x="{x+38}" y="{251 + j*28}" font-size="15" fill="{SUB}">{esc(b)}</text>' for j, b in enumerate(bullets))
        card = (f'<g class="up" style="animation-delay:{d+.1:.2f}s">'
                f'<rect x="{x}" y="104" width="{cw}" height="226" rx="18" fill="{PANEL2}" stroke="{LINE}"/>'
                f'<rect x="{x+20}" y="104" width="44" height="3" fill="{col}"/>'
                f'<text x="{x+20}" y="142" class="mono" font-size="11" fill="{col}" letter-spacing="1.5">{period}</text>'
                f'<text x="{x+20}" y="178" font-size="21" font-weight="700" letter-spacing="-.5" fill="{TEXT}">{esc(role)}</text>'
                f'<text x="{x+20}" y="204" font-size="15" fill="{SUB}">{esc(org)}</text>'
                f'<line x1="{x+20}" y1="222" x2="{x+cw-20}" y2="222" stroke="{LINE}"/>{bl}</g>')
        body += node + card
    defs = dotgrid(W, H) + f'<linearGradient id="vcu" gradientUnits="userSpaceOnUse" x1="48" y1="0" x2="{W-48}" y2="0"><stop offset="0" stop-color="{V}"/><stop offset=".55" stop-color="{C}"/><stop offset="1" stop-color="{P}"/></linearGradient>' + '<filter id="g2" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
    css = f'''
.prog {{ stroke-dasharray: {W}; stroke-dashoffset: {W}; animation: draw 2.4s .2s cubic-bezier(.2,.7,.2,1) forwards; }}
.pop {{ transform-box: fill-box; transform-origin: center; animation: pop .5s cubic-bezier(.3,1.6,.5,1) both; }}
@keyframes pop {{ from {{ transform: scale(0) }} to {{ transform: scale(1) }} }}'''
    svg("experience", W, H, body, defs, css)


# ---------------------------------------------------------------- PROJECT CARDS
def project(slug, num, kind, title, desc, tags, art):
    W, H = 600, 340
    lines = textwrap.wrap(desc, 30)[:4]
    d = "".join(f'<text x="32" y="{150 + i*24}" font-size="15" fill="{SUB}">{esc(l)}</text>' for i, l in enumerate(lines))
    x, pills = 32, ""
    for t in tags:
        w = 18 + len(t) * 7.8
        pills += f'<rect x="{x}" y="276" width="{w:.0f}" height="28" rx="14" fill="{PANEL2}" stroke="{LINE}"/><text x="{x + w/2:.0f}" y="295" text-anchor="middle" class="mono" font-size="12" fill="{TEXT}">{esc(t)}</text>'
        x += w + 8
    defs = f'''<linearGradient id="bd" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="{V}"/><stop offset=".3" stop-color="{LINE}"/><stop offset=".7" stop-color="{LINE}"/><stop offset="1" stop-color="{C}"/>
<animateTransform attributeName="gradientTransform" type="rotate" values="0 .5 .5;360 .5 .5" dur="8s" repeatCount="indefinite"/></linearGradient>
<radialGradient id="spot" cx=".8" cy=".2" r=".7"><stop offset="0" stop-color="{V}" stop-opacity=".22"/><stop offset="1" stop-color="{V}" stop-opacity="0"/></radialGradient>'''
    css = '''
.bar { transform-box: fill-box; transform-origin: bottom; animation: grow 2.6s cubic-bezier(.2,.7,.2,1) infinite alternate; }
@keyframes grow { from { transform: scaleY(.2) } to { transform: scaleY(1) } }
.float { animation: float 3.2s ease-in-out infinite; }
@keyframes float { 50% { transform: translateY(-6px) } }
.shim { animation: shim 1.8s linear infinite; }
@keyframes shim { from { transform: translateX(-140px) } to { transform: translateX(160px) } }
.bounce { transform-box: fill-box; transform-origin: center; animation: bounce 2s cubic-bezier(.3,1.6,.5,1) infinite; }
@keyframes bounce { 0%,60%,100% { transform: scale(1) } 70% { transform: scale(1.35) } }
.typing { animation: blink 1s steps(1) infinite; }
'''
    body = f'''
<rect width="{W}" height="{H}" rx="24" fill="{PANEL}"/>
<rect width="{W}" height="{H}" fill="url(#spot)"/>
<text x="32" y="50" class="mono" font-size="12" fill="{SUB}" letter-spacing="1.5">{num} — {esc(kind.upper())}</text>
<text x="32" y="96" font-size="28" font-weight="800" letter-spacing="-1" fill="{TEXT}">{esc(title)}</text>
<rect x="32" y="112" width="40" height="3" rx="1.5" fill="url(#vc)"/>
{d}
{pills}
<g transform="translate(360,60)">{art}</g>
'''
    svg(f"project-{slug}", W, H, body, defs, css, border=False)
    # gradient animated border drawn on top
    p = open(f"{OUT}/project-{slug}.svg").read().replace(
        "</svg>", f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="23" fill="none" stroke="url(#bd)" stroke-width="1.5"/>\n</svg>')
    open(f"{OUT}/project-{slug}.svg", "w").write(p)


def art_api():
    rows = [("GET", "/posts", C), ("POST", "/auth/login", V), ("PUT", "/users/:id", P), ("DEL", "/posts/:id", "#F87171")]
    s = f'<rect width="210" height="220" rx="16" fill="{PANEL2}" stroke="{LINE}"/>'
    for i, (m, path, col) in enumerate(rows):
        y = 26 + i * 48
        s += (f'<g class="up" style="animation-delay:{.3+i*.15:.2f}s"><rect x="14" y="{y}" width="182" height="36" rx="10" fill="{PANEL}" stroke="{LINE}"/>'
              f'<text x="26" y="{y+23}" class="mono" font-size="11" font-weight="700" fill="{col}">{m}</text>'
              f'<text x="70" y="{y+23}" class="mono" font-size="11" fill="{TEXT}">{path}</text>'
              f'<circle cx="182" cy="{y+18}" r="4" fill="{G}" style="animation: pulse 1.4s {i*.3:.1f}s infinite"/></g>')
    s += f'<circle r="4" fill="{C}"><animateMotion dur="2.4s" repeatCount="indefinite" path="M -40 44 L 14 44"/></circle>'
    return s


def art_admin():
    s = (f'<rect width="210" height="220" rx="16" fill="{PANEL2}" stroke="{LINE}"/>'
         f'<rect x="0" y="0" width="44" height="220" rx="16" fill="{PANEL}"/>')
    for i in range(5):
        s += f'<rect x="12" y="{20 + i*26}" width="20" height="10" rx="3" fill="{V if i == 1 else LINE}"/>'
    s += f'<rect x="58" y="18" width="86" height="10" rx="5" fill="{LINE}"/><rect x="58" y="36" width="56" height="8" rx="4" fill="{LINE}" opacity=".6"/>'
    hs = [60, 96, 72, 120, 88, 132]
    for i, h in enumerate(hs):
        s += f'<rect x="{60 + i*23}" y="{196 - h}" width="14" height="{h}" rx="4" fill="url(#vc)" class="bar" style="animation-delay:-{i*.35:.2f}s"/>'
    s += f'<line x1="56" y1="197" x2="196" y2="197" stroke="{LINE}"/>'
    return s


def art_store():
    s = f'<rect width="210" height="220" rx="16" fill="{PANEL2}" stroke="{LINE}"/>'
    s += f'<clipPath id="tiles">'
    for r in range(2):
        for c in range(2):
            s += f'<rect x="{16 + c*94}" y="{40 + r*88}" width="84" height="78" rx="12"/>'
    s += '</clipPath>'
    for r in range(2):
        for c in range(2):
            x, y = 16 + c*94, 40 + r*88
            s += (f'<rect x="{x}" y="{y}" width="84" height="78" rx="12" fill="{PANEL}" stroke="{LINE}"/>'
                  f'<rect x="{x+10}" y="{y+10}" width="64" height="38" rx="8" fill="{[V,C,P,G][r*2+c]}" opacity=".35"/>'
                  f'<rect x="{x+10}" y="{y+56}" width="44" height="7" rx="3.5" fill="{LINE}"/>')
    s += f'<g clip-path="url(#tiles)"><rect class="shim" x="0" y="30" width="50" height="200" fill="#fff" opacity=".07" transform="skewX(-20)"/></g>'
    s += (f'<text x="16" y="26" class="mono" font-size="11" fill="{SUB}">SHOP</text>'
          f'<path d="M168 12 h6 l4 14 h18 l3 -10 h-23" stroke="{TEXT}" stroke-width="1.6" fill="none" stroke-linejoin="round"/>'
          f'<circle cx="181" cy="31" r="2" fill="{TEXT}"/><circle cx="193" cy="31" r="2" fill="{TEXT}"/>'
          f'<g class="bounce"><circle cx="198" cy="12" r="8" fill="{P}"/><text x="198" y="16" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">3</text></g>')
    return s


def art_portfolio():
    s = (f'<rect width="210" height="220" rx="16" fill="{PANEL2}" stroke="{LINE}"/>'
         f'<rect width="210" height="30" rx="16" fill="{PANEL}"/><rect y="16" width="210" height="14" fill="{PANEL}"/>'
         f'<circle cx="16" cy="15" r="3.5" fill="#FF5F57"/><circle cx="28" cy="15" r="3.5" fill="#FEBC2E"/><circle cx="40" cy="15" r="3.5" fill="#28C840"/>'
         f'<rect x="56" y="8" width="138" height="14" rx="7" fill="{PANEL2}"/><text x="66" y="19" class="mono" font-size="9" fill="{SUB}">vilaayali.com</text>'
         f'<g class="float"><rect x="18" y="48" width="174" height="78" rx="12" fill="url(#vc)" opacity=".85"/>'
         f'<rect x="32" y="66" width="90" height="12" rx="6" fill="#fff" opacity=".9"/><rect x="32" y="86" width="60" height="8" rx="4" fill="#fff" opacity=".6"/>'
         f'<rect x="32" y="102" width="44" height="14" rx="7" fill="{BG}"/></g>'
         f'<rect x="18" y="140" width="80" height="58" rx="10" fill="{PANEL}" stroke="{LINE}"/><rect x="110" y="140" width="82" height="58" rx="10" fill="{PANEL}" stroke="{LINE}"/>')
    s += (f'<g><animateTransform attributeName="transform" type="translate" values="150 190;60 112;60 112;140 165;150 190" keyTimes="0;.35;.5;.8;1" dur="4s" repeatCount="indefinite"/>'
          f'<path d="M0 0 L0 15 L4 11 L7 18 L10 17 L7 10 L12 10 Z" fill="#fff" stroke="{BG}" stroke-width="1"/></g>')
    return s


# ---------------------------------------------------------------- STACK MARQUEE
def marquee():
    W, H = 1200, 200
    row1 = [("React", "#61DAFB"), ("Next.js", "#FFFFFF"), ("JavaScript", "#F7DF1E"), ("Redux", "#9B7BEA"), ("Tailwind", "#38BDF8"),
            ("shadcn/ui", "#FFFFFF"), ("Material UI", "#007FFF"), ("Sass", "#CC6699"), ("Vue", "#42B883"), ("TanStack Query", "#FF4154"), ("Bootstrap", "#7952B3")]
    row2 = [("Node.js", "#5FA04E"), ("Express", "#FFFFFF"), ("PostgreSQL", "#4F8BCB"), ("MySQL", "#00758F"), ("MongoDB", "#47A248"), ("Socket.io", "#FFFFFF"),
            ("Sequelize", "#52B0E7"), ("JWT", P), ("Zod", "#3E67B1"), ("Swagger", "#85EA2D"), ("Git", "#F05032"), ("Vercel", "#FFFFFF"), ("Postman", "#FF6C37")]

    def build(items, y):
        x, g = 0, ""
        for name, col in items:
            w = 48 + len(name) * 10
            g += (f'<rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="48" rx="24" fill="{PANEL2}" stroke="{LINE}"/>'
                  f'<circle cx="{x+24:.0f}" cy="{y+24}" r="5" fill="{col}"/>'
                  f'<text x="{x+38:.0f}" y="{y+30}" font-size="16" font-weight="600" fill="{TEXT}">{esc(name)}</text>')
            x += w + 12
        return g, x

    g1, w1 = build(row1, 36)
    g2, w2 = build(row2, 108)
    css = f'''
.m1 {{ animation: m1 28s linear infinite; }} @keyframes m1 {{ to {{ transform: translateX(-{w1:.0f}px) }} }}
.m2 {{ animation: m2 32s linear infinite; }} @keyframes m2 {{ from {{ transform: translateX(-{w2:.0f}px) }} to {{ transform: translateX(0) }} }}'''
    defs = f'''<linearGradient id="edge" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".12" stop-color="#fff"/><stop offset=".88" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<mask id="fade"><rect width="{W}" height="{H}" fill="url(#edge)"/></mask>'''
    body = (f'<rect width="{W}" height="{H}" fill="{PANEL}"/>'
            f'<g mask="url(#fade)"><g class="m1">{g1}<g transform="translate({w1:.0f},0)">{g1}</g><g transform="translate({2*w1:.0f},0)">{g1}</g></g>'
            f'<g class="m2">{g2}<g transform="translate({w2:.0f},0)">{g2}</g><g transform="translate({2*w2:.0f},0)">{g2}</g></g></g>')
    svg("stack", W, H, body, defs, css)


# ---------------------------------------------------------------- FOOTER
def footer():
    W, H = 1200, 300
    def wave(y, amp, col, op, dur, delay=0):
        seg = 300
        d = f"M0 {y}"
        for k in range(0, 2 * W + seg, seg):
            d += f" Q {k + seg/4} {y - amp} {k + seg/2} {y} T {k + seg} {y}"
        d += f" V {H} H 0 Z"
        return f'<path d="{d}" fill="{col}" opacity="{op}" style="animation: wave {dur}s linear {delay}s infinite"/>'
    css = f'@keyframes wave {{ to {{ transform: translateX(-{W//2}px) }} }}'
    body = f'''
<rect width="{W}" height="{H}" fill="{BG}"/>
<rect width="{W}" height="{H}" fill="url(#dots)" opacity=".6"/>
{wave(240, 16, V, .35, 9)}{wave(252, 12, C, .25, 13)}{wave(266, 10, P, .2, 17)}
<text x="{W/2}" y="104" text-anchor="middle" class="up" font-size="46" font-weight="800" letter-spacing="-2" fill="{TEXT}">Let's build something <tspan fill="url(#vc)">great</tspan>.</text>
<text x="{W/2}" y="146" text-anchor="middle" class="mono up" style="animation-delay:.2s" font-size="15" fill="{SUB}">vilaayali89@gmail.com  ·  vilaayali.com  ·  linkedin.com/in/syedvilaayali</text>
<g class="up" style="animation-delay:.35s"><rect x="{W/2 - 82}" y="170" width="164" height="40" rx="20" fill="{TEXT}"/>
<text x="{W/2}" y="196" text-anchor="middle" font-size="15" font-weight="700" fill="{BG}">Say hello  →</text></g>'''
    svg("footer", W, H, body, dotgrid(W, H), css)


if __name__ == "__main__":
    for f in os.listdir(OUT):
        os.remove(os.path.join(OUT, f))
    hero(); terminal(); bento(); experience(); marquee(); footer()
    for s in [("about", "01", "About", "who I am"), ("experience", "02", "Experience", "where I've been"),
              ("work", "03", "Selected work", "things I've built"), ("stack", "04", "Toolkit", "what I use"),
              ("activity", "05", "Activity", "incl. private repos")]:
        section(*s); section(*s, light=True)
    project("blog-api", "01", "Backend", "Blog Management API",
            "JWT auth, author-owned posts, search and filters with pagination, image uploads and Swagger docs.",
            ["Node.js", "Express", "PostgreSQL"], art_api())
    project("convers", "02", "Admin panel", "Convers by Ginkgo",
            "Responsive admin panel with dynamic routing, validated forms and a reusable component system.",
            ["React", "Next.js", "MUI"], art_admin())
    project("store", "03", "E-commerce", "Sanaullah Store",
            "Storefront with live product and user APIs on a clean, fully responsive UI.",
            ["React", "Next.js", "Sass"], art_store())
    project("portfolio", "04", "Personal", "vilaayali.com",
            "My personal portfolio, designed and built from scratch and deployed on the edge.",
            ["React", "Vite", "Vercel"], art_portfolio())
    print(sorted(os.listdir(OUT)))

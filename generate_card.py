import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"
W, H = 1200, 440
segs = [("React", "#61DAFB", 26), ("Next.js", "#E6EDF3", 20), ("Node.js", "#5FA04E", 22), ("PostgreSQL", "#336791", 16), ("Socket.io", "#F78166", 16)]
bar, legend, x = "", "", 64
bw = W - 128
lx = 64
for i, (n, c, p) in enumerate(segs):
    w = bw * p / 100
    bar += f'<rect x="{x:.1f}" y="372" width="{w:.1f}" height="10" fill="{c}" class="seg" style="animation-delay:{.4 + i*.12:.2f}s"/>'
    legend += f'<circle cx="{lx+5}" cy="404" r="5" fill="{c}"/><text x="{lx+16}" y="409" font-size="15" fill="#9198A1"><tspan fill="#E6EDF3" font-weight="600">{n}</tspan></text>'
    lx += 34 + len(n) * 9
    x += w
logo = ('<rect width="64" height="64" rx="12" fill="#F5F1E8"/><g fill="none" stroke="#061530" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M12 14 L32 52 L52 14" stroke-width="6.5" pathLength="1" class="dv"/><path d="M24 40 L32 22 L40 40 M27.5 33 L36.5 33" stroke-width="3.4" pathLength="1" class="da"/></g>')
icon = lambda d: f'<path d="{d}" fill="#9198A1" transform="scale(1.25)"/>'
# octicon-like glyphs (16px grid)
REPO = "M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"
LINK = "m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"
PIN = "m12.596 11.596-3.535 3.536a1.5 1.5 0 0 1-2.122 0l-3.535-3.536a6.5 6.5 0 1 1 9.192-9.193 6.5 6.5 0 0 1 0 9.193Zm-1.06-8.132v-.001a5 5 0 1 0-7.072 7.072L8 14.07l3.536-3.534a5 5 0 0 0 0-7.072ZM8 9a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 9Z"
stats = ""
sx = 64
for d, label in [(REPO, "4 featured projects"), (LINK, "vilaayali.com")]:
    stats += f'<g transform="translate({sx},292)">{icon(d)}</g><text x="{sx+30}" y="309" font-size="18" fill="#9198A1">{label}</text>'
    sx += 64 + len(label) * 9.5
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
<clipPath id="r"><rect width="{W}" height="{H}" rx="12"/></clipPath>
<clipPath id="barc"><rect x="64" y="372" width="{bw}" height="10" rx="5"/></clipPath>
<radialGradient id="glow" cx=".85" cy=".3" r=".5"><stop offset="0" stop-color="#1F6FEB" stop-opacity=".18"/><stop offset="1" stop-color="#1F6FEB" stop-opacity="0"/></radialGradient>
<style>
text {{ font-family: {SANS}; }} .mono {{ font-family: {MONO}; }}
.seg {{ transform-box: fill-box; transform-origin: left; animation: grow .7s cubic-bezier(.2,.7,.2,1) both; }}
@keyframes grow {{ from {{ transform: scaleX(0) }} to {{ transform: scaleX(1) }} }}
.dv, .da {{ stroke-dasharray: 1; stroke-dashoffset: 1; animation: draw 1.1s cubic-bezier(.6,0,.3,1) forwards; }}
.da {{ animation-delay: .9s; }}
@keyframes draw {{ to {{ stroke-dashoffset: 0 }} }}
.pulse {{ animation: pulse 2s ease-in-out infinite; }} @keyframes pulse {{ 50% {{ opacity: .3 }} }}
.caret {{ animation: blink 1s steps(1) infinite; }} @keyframes blink {{ 50% {{ opacity: 0 }} }}
</style></defs>
<g clip-path="url(#r)">
<rect width="{W}" height="{H}" fill="#0D1117"/>
<rect width="{W}" height="{H}" fill="url(#glow)"/>
<text x="62" y="112" font-size="40" fill="#9198A1">vilaayali/</text>
<text x="60" y="186" font-size="72" font-weight="700" letter-spacing="-1.5" fill="#E6EDF3">vilaayali<tspan class="caret" fill="#F78166" font-weight="400">_</tspan></text>
<text x="64" y="236" font-size="22" fill="#9198A1">Full-stack developer building real-time web apps,</text>
<text x="64" y="266" font-size="22" fill="#9198A1">clean APIs and fast UIs.</text>
{stats}
<g transform="translate(936,72) scale(3.2)">{logo}</g>
<g transform="translate(944,300)"><rect width="190" height="34" rx="17" fill="#161B22" stroke="#30363D"/>
<circle cx="20" cy="17" r="5" fill="#3FB950" class="pulse"/><text x="34" y="22" font-size="15" fill="#E6EDF3">Open to collab</text></g>
<g clip-path="url(#barc)"><rect x="64" y="372" width="{bw}" height="10" fill="#21262D"/>{bar}</g>
{legend}
</g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="#30363D"/>
</svg>'''
open(f"{OUT}/repo-card.svg", "w").write(svg)
print("ok")

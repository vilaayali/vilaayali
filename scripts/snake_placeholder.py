"""Writes assets/snake.svg — a default snake shown until the real one is generated."""
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "snake.svg")
cs, gap, cols, rows, pad = 12, 4, 53, 7, 18
step = cs + gap
W, H = pad * 2 + cols * step - gap, pad * 2 + rows * step - gap
cells = "".join(f'<rect x="{pad + c*step}" y="{pad + r*step}" width="{cs}" height="{cs}" rx="2" fill="#161B22"/>'
                for c in range(cols) for r in range(rows))
body = "".join(f'<rect x="{-i*step}" y="0" width="{cs}" height="{cs}" rx="{3 if i else 4}" fill="#F78166" opacity="{1 - i*0.18:.2f}"/>'
               for i in range(5))
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>.s{{animation:go 9s linear infinite}} @keyframes go{{from{{transform:translate({pad}px,{pad + 3*step}px)}}to{{transform:translate({W + 5*step}px,{pad + 3*step}px)}}}}</style>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="6" fill="#0D1117" stroke="#30363D"/>
{cells}
<g class="s">{body}</g>
</svg>'''
open(OUT, "w").write(svg)
print("wrote assets/snake.svg")

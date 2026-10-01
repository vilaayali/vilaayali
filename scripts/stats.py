"""Builds assets/contrib.svg (contribution calendar) and assets/languages.svg
from the GitHub GraphQL API. Runs in GitHub Actions; stdlib only.

Env: GH_TOKEN (a PAT with repo + read:user lets private work count), GH_USER.
Local test without network:  python scripts/stats.py --demo
"""
import json, os, sys, urllib.request, datetime, random

USER = os.environ.get("GH_USER", "vilaayali")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
BG, BORDER, TEXT, MUTED = "#0D1117", "#30363D", "#E6EDF3", "#9198A1"
SCALE = ["#161B22", "#5A2A1F", "#9C3F27", "#D65A35", "#F78166"]
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"

QUERY = """query($login:String!){ user(login:$login){
  contributionsCollection{ contributionCalendar{ totalContributions
    weeks{ contributionDays{ date contributionCount weekday } } } }
  repositories(first:100, ownerAffiliations:OWNER, isFork:false){ nodes{
    languages(first:10, orderBy:{field:SIZE, direction:DESC}){ edges{ size node{ name color } } } } } } }"""


def fetch():
    req = urllib.request.Request("https://api.github.com/graphql",
                                 data=json.dumps({"query": QUERY, "variables": {"login": USER}}).encode(),
                                 headers={"Authorization": f"bearer {os.environ['GH_TOKEN']}", "User-Agent": USER})
    data = json.load(urllib.request.urlopen(req))
    if "errors" in data:
        sys.exit(f"GraphQL error: {data['errors']}")
    return data["data"]["user"]


def demo():
    random.seed(4)
    start = datetime.date.today() - datetime.timedelta(days=364)
    start -= datetime.timedelta(days=(start.weekday() + 1) % 7)
    weeks, d = [], start
    while d <= datetime.date.today():
        days = []
        for _ in range(7):
            if d > datetime.date.today():
                break
            c = random.choice([0, 0, 0, 1, 2, 3, 5, 8]) if random.random() < .55 else 0
            days.append({"date": d.isoformat(), "contributionCount": c, "weekday": (d.weekday() + 1) % 7})
            d += datetime.timedelta(days=1)
        weeks.append({"contributionDays": days})
    total = sum(x["contributionCount"] for w in weeks for x in w["contributionDays"])
    langs = [("JavaScript", "#f1e05a", 61), ("TypeScript", "#3178c6", 14), ("SCSS", "#c6538c", 9),
             ("CSS", "#663399", 7), ("HTML", "#e34c26", 6), ("Python", "#3572A5", 3)]
    return {"contributionsCollection": {"contributionCalendar": {"totalContributions": total, "weeks": weeks}},
            "repositories": {"nodes": [{"languages": {"edges": [{"size": s, "node": {"name": n, "color": c}} for n, c, s in langs]}}]}}


def frame(w, h, body, css=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<style>text{{font-family:{FONT}}} .c{{animation:in .5s ease both}} @keyframes in{{from{{opacity:0}}to{{opacity:1}}}} {css}</style>
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="6" fill="{BG}" stroke="{BORDER}"/>
{body}
</svg>'''


def calendar(user):
    cal = user["contributionsCollection"]["contributionCalendar"]
    weeks = cal["weeks"]
    counts = sorted(c["contributionCount"] for w in weeks for c in w["contributionDays"] if c["contributionCount"])
    q = [counts[int(len(counts) * p)] for p in (.25, .5, .75)] if counts else [1, 2, 3]
    lvl = lambda n: 0 if n == 0 else 1 if n <= q[0] else 2 if n <= q[1] else 3 if n <= q[2] else 4
    cs, gap, x0, y0 = 13, 3, 46, 62
    cells, months, last_m = "", "", None
    for i, w in enumerate(weeks):
        x = x0 + i * (cs + gap)
        for d in w["contributionDays"]:
            y = y0 + d["weekday"] * (cs + gap)
            n = d["contributionCount"]
            cells += (f'<rect class="c" style="animation-delay:{i*18}ms" x="{x}" y="{y}" width="{cs}" height="{cs}" rx="2.5" '
                      f'fill="{SCALE[lvl(n)]}"><title>{n} on {d["date"]}</title></rect>')
        m = w["contributionDays"][0]["date"][5:7]
        if m != last_m and int(w["contributionDays"][0]["date"][8:10]) <= 7 and i < len(weeks) - 2:
            name = datetime.date(2000, int(m), 1).strftime("%b")
            months += f'<text x="{x}" y="{y0-10}" font-size="11" fill="{MUTED}">{name}</text>'
            last_m = m
    for wd, lab in [(1, "Mon"), (3, "Wed"), (5, "Fri")]:
        months += f'<text x="{x0-10}" y="{y0 + wd*(cs+gap) + 10}" text-anchor="end" font-size="11" fill="{MUTED}">{lab}</text>'
    W = x0 + len(weeks) * (cs + gap) + 22
    H = y0 + 7 * (cs + gap) + 42
    legend_x = W - 22 - 5 * (cs + 3) - 34
    legend = (f'<text x="{legend_x - 8}" y="{H-21}" text-anchor="end" font-size="11" fill="{MUTED}">Less</text>'
              + "".join(f'<rect x="{legend_x + k*(cs+3)}" y="{H-31}" width="{cs}" height="{cs}" rx="2.5" fill="{c}"/>' for k, c in enumerate(SCALE))
              + f'<text x="{legend_x + 5*(cs+3) + 4}" y="{H-21}" font-size="11" fill="{MUTED}">More</text>')
    title = (f'<text x="22" y="30" font-size="15" font-weight="600" fill="{TEXT}">{cal["totalContributions"]:,} contributions '
             f'<tspan fill="{MUTED}" font-weight="400">in the last year</tspan></text>')
    sub = f'<text x="22" y="{H-21}" font-size="11" fill="{MUTED}">Includes private contributions</text>'
    return frame(W, H, title + months + cells + legend + sub)


def languages(user):
    tot = {}
    for r in user["repositories"]["nodes"]:
        for e in r["languages"]["edges"]:
            n = e["node"]["name"]
            tot.setdefault(n, [0, e["node"]["color"] or MUTED])[0] += e["size"]
    top = sorted(tot.items(), key=lambda kv: -kv[1][0])[:6]
    s = sum(v[0] for _, v in top) or 1
    W, H = 495, 195
    bar, x, bw = "", 22, W - 44
    for i, (n, (size, col)) in enumerate(top):
        w = bw * size / s
        bar += f'<rect x="{x:.1f}" y="52" width="{max(w-2,1):.1f}" height="8" fill="{col}" class="c" style="animation-delay:{i*90}ms"/>'
        x += w
    rows = ""
    for i, (n, (size, col)) in enumerate(top):
        cx, cy = 22 + (i % 2) * 230, 92 + (i // 2) * 30
        rows += (f'<g class="c" style="animation-delay:{300+i*80}ms"><circle cx="{cx+5}" cy="{cy-4}" r="5" fill="{col}"/>'
                 f'<text x="{cx+18}" y="{cy}" font-size="13" font-weight="600" fill="{TEXT}">{n} '
                 f'<tspan fill="{MUTED}" font-weight="400">{size/s*100:.1f}%</tspan></text></g>')
    title = f'<text x="22" y="34" font-size="15" font-weight="600" fill="{TEXT}">Most used languages</text>'
    clip = f'<clipPath id="b"><rect x="22" y="52" width="{bw}" height="8" rx="4"/></clipPath>'
    return frame(W, H, title + clip + f'<g clip-path="url(#b)"><rect x="22" y="52" width="{bw}" height="8" fill="#21262D"/>{bar}</g>' + rows)


if __name__ == "__main__":
    user = demo() if "--demo" in sys.argv else fetch()
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, "contrib.svg"), "w").write(calendar(user))
    open(os.path.join(OUT, "languages.svg"), "w").write(languages(user))
    print("wrote assets/contrib.svg and assets/languages.svg")

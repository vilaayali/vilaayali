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

BASE_QUERY = """query($login:String!){ user(login:$login){
  createdAt
  contributionsCollection{ contributionYears }
  repositories(first:100, ownerAffiliations:OWNER, isFork:false){ nodes{
    languages(first:10, orderBy:{field:SIZE, direction:DESC}){ edges{ size node{ name color } } } } } } }"""

YEAR_FIELDS = "contributionCalendar{ totalContributions weeks{ contributionDays{ date contributionCount weekday } } }"


def gql(query):
    req = urllib.request.Request("https://api.github.com/graphql",
                                 data=json.dumps({"query": query, "variables": {"login": USER}}).encode(),
                                 headers={"Authorization": f"bearer {os.environ['GH_TOKEN']}", "User-Agent": USER})
    data = json.load(urllib.request.urlopen(req))
    if "errors" in data:
        raise RuntimeError(f"GraphQL error: {data['errors']}")
    return data["data"]["user"]


def fetch():
    user = gql(BASE_QUERY)
    years = sorted(user["contributionsCollection"]["contributionYears"], reverse=True)
    # GitHub allows max one year per contributionsCollection, so alias one per year
    parts = " ".join(f'y{y}: contributionsCollection(from:"{y}-01-01T00:00:00Z", to:"{y}-12-31T23:59:59Z"){{ {YEAR_FIELDS} }}' for y in years)
    per = gql(f'query($login:String!){{ user(login:$login){{ {parts} }} }}')
    user["years"] = {y: per[f"y{y}"]["contributionCalendar"] for y in years}
    return user


def demo():
    random.seed(4)
    today = datetime.date.today()
    years = {}
    for y in range(today.year, 2022, -1):
        d, end = datetime.date(y, 1, 1), min(datetime.date(y, 12, 31), today)
        if y == 2023:
            d = datetime.date(2023, 6, 29)
        days = []
        while d <= end:
            act = .25 + .12 * (y - 2023)
            c = random.choice([1, 1, 2, 3, 4, 6, 9]) if random.random() < act else 0
            days.append({"date": d.isoformat(), "contributionCount": c, "weekday": (d.weekday() + 1) % 7})
            d += datetime.timedelta(days=1)
        years[y] = {"totalContributions": sum(x["contributionCount"] for x in days), "weeks": [{"contributionDays": days}]}
    langs = [("JavaScript", "#f1e05a", 61), ("TypeScript", "#3178c6", 14), ("SCSS", "#c6538c", 9),
             ("CSS", "#663399", 7), ("HTML", "#e34c26", 6), ("Python", "#3572A5", 3)]
    return {"years": years,
            "repositories": {"nodes": [{"languages": {"edges": [{"size": s, "node": {"name": n, "color": c}} for n, c, s in langs]}}]}}


def empty():
    """Default data so the cards always render, even with 0 contributions or no API access."""
    y = datetime.date.today().year
    return {"years": {y: {"totalContributions": 0, "weeks": []}}, "repositories": {"nodes": []}}


def frame(w, h, body, css=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<style>text{{font-family:{FONT}}} .c{{animation:in .5s ease both}} @keyframes in{{from{{opacity:0}}to{{opacity:1}}}} {css}</style>
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="6" fill="{BG}" stroke="{BORDER}"/>
{body}
</svg>'''


def calendar(user):
    """All-time view: one row of 53 weeks per year, newest year on top."""
    years = user["years"]
    days_by_year = {y: [d for w in c["weeks"] for d in w["contributionDays"]] for y, c in years.items()}
    counts = sorted(d["contributionCount"] for ds in days_by_year.values() for d in ds if d["contributionCount"])
    q = [counts[int(len(counts) * p)] for p in (.25, .5, .75)] if counts else [1, 2, 3]
    lvl = lambda n: 0 if n == 0 else 1 if n <= q[0] else 2 if n <= q[1] else 3 if n <= q[2] else 4
    cs, gap = 11, 3
    step = cs + gap
    x0, y0 = 96, 78
    block = 7 * step + 18
    body, row = "", 0
    for y in sorted(years, reverse=True):
        first = datetime.date(y, 1, 1)
        sunday = first - datetime.timedelta(days=(first.weekday() + 1) % 7)
        by = y0 + row * block
        body += (f'<text x="22" y="{by + 14}" font-size="15" font-weight="700" fill="{TEXT}">{y}</text>'
                 f'<text x="22" y="{by + 32}" font-size="11.5" fill="{MUTED}">{years[y]["totalContributions"]:,}</text>')
        # empty grid for the whole year first, then real days on top
        last = datetime.date(y, 12, 31)
        d = first
        while d <= last:
            col = (d - sunday).days // 7
            body += f'<rect x="{x0 + col*step}" y="{by + ((d.weekday()+1)%7)*step}" width="{cs}" height="{cs}" rx="2" fill="{SCALE[0]}"/>'
            d += datetime.timedelta(days=1)
        for dd in days_by_year[y]:
            n = dd["contributionCount"]
            if not n:
                continue
            dt = datetime.date.fromisoformat(dd["date"])
            col = (dt - sunday).days // 7
            body += (f'<rect class="c" style="animation-delay:{row*250 + col*12}ms" x="{x0 + col*step}" y="{by + dd["weekday"]*step}" '
                     f'width="{cs}" height="{cs}" rx="2" fill="{SCALE[lvl(n)]}"><title>{n} on {dd["date"]}</title></rect>')
        row += 1
    # month labels (calendar years align, so draw once at the top)
    ref = datetime.date(2025, 1, 1)
    refsun = ref - datetime.timedelta(days=(ref.weekday() + 1) % 7)
    for m in range(1, 13):
        col = (datetime.date(2025, m, 1) - refsun).days // 7
        body += f'<text x="{x0 + col*step}" y="{y0 - 10}" font-size="11" fill="{MUTED}">{datetime.date(2025, m, 1).strftime("%b")}</text>'
    W = x0 + 54 * step + 18
    H = y0 + row * block + 30
    total = sum(c["totalContributions"] for c in years.values())
    since = min(years)
    body += (f'<text x="22" y="34" font-size="16" font-weight="600" fill="{TEXT}">{total:,} contributions '
             f'<tspan fill="{MUTED}" font-weight="400">since {since} · all time</tspan></text>')
    lx = W - 22 - 5 * (cs + 3) - 34
    body += (f'<text x="{lx - 8}" y="34" text-anchor="end" font-size="11" fill="{MUTED}">Less</text>'
             + "".join(f'<rect x="{lx + k*(cs+3)}" y="25" width="{cs}" height="{cs}" rx="2" fill="{c}"/>' for k, c in enumerate(SCALE))
             + f'<text x="{lx + 5*(cs+3) + 4}" y="34" font-size="11" fill="{MUTED}">More</text>')
    body += f'<text x="22" y="{H - 16}" font-size="11" fill="{MUTED}">Includes private contributions</text>'
    return frame(W, H, body)


def languages(user):
    tot = {}
    for r in user["repositories"]["nodes"]:
        for e in r["languages"]["edges"]:
            n = e["node"]["name"]
            tot.setdefault(n, [0, e["node"]["color"] or MUTED])[0] += e["size"]
    top = sorted(tot.items(), key=lambda kv: -kv[1][0])[:6]
    if not top:
        top = [("No data yet", [1, "#30363D"])]
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
                 f'<tspan fill="{MUTED}" font-weight="400">{"" if n == "No data yet" else f"{size/s*100:.1f}%"}</tspan></text></g>')
    title = f'<text x="22" y="34" font-size="15" font-weight="600" fill="{TEXT}">Most used languages</text>'
    clip = f'<clipPath id="b"><rect x="22" y="52" width="{bw}" height="8" rx="4"/></clipPath>'
    return frame(W, H, title + clip + f'<g clip-path="url(#b)"><rect x="22" y="52" width="{bw}" height="8" fill="#21262D"/>{bar}</g>' + rows)


if __name__ == "__main__":
    if "--demo" in sys.argv:
        user = demo()
    elif "--empty" in sys.argv:
        user = empty()
    else:
        try:
            user = fetch()
        except Exception as e:  # keep the last good cards if the API is down
            print(f"warning: GitHub API failed ({e}); keeping existing cards")
            sys.exit(0)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, "contrib.svg"), "w").write(calendar(user))
    open(os.path.join(OUT, "languages.svg"), "w").write(languages(user))
    print("wrote assets/contrib.svg and assets/languages.svg")

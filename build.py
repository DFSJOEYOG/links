import json, html
src = json.load(open('/workspace/joaidhd-HQ-upload/affiliates/links.json'))['offers']
by = {o['brand']: o for o in src}
e = html.escape
# Featured (order requested), with blurbs drawn only from links.json facts
featured = [
 ("SmackTok", "New app", "Join me on SmackTok. Use my code ST-JL2343 when you sign up"),
 ("Polymarket", "Prediction markets", "Free credit when you sign up with code dfsjoeyog"),
 ("Kalshi", "Prediction markets", ""),
 ("Rebet", "Free daily app", ""),
 ("Dabble", "DFS pick'em", "Free credit when you sign up with code DFSJOEYOG"),
 ("DraftKings Sportsbook", "Sportsbook · Illinois", ""),
 ("ero", "Earn app", "+50% on everything you earn in your first 24 hours"),
]
names = {"Rebet": "ReBet", "DraftKings Sportsbook": "DraftKings IL"}
lanes = [("prediction","Prediction markets"),("dfs","DFS / pick'em"),("daily-free","Free daily apps"),("sweeps","Sweepstakes"),("cash-apps","Money apps"),("get-paid","Get paid"),("credit","Credit"),("crypto","Crypto")]
fset = {f[0] for f in featured}
def card(o, tag, blurb, hot=False):
    name = names.get(o['brand'], o['brand'])
    url, code = o.get('url',''), o.get('code','')
    out = [f'<article class="card{" hot" if hot else ""}">',
           f'<div class="hd"><h3>{e(name)}</h3><span class="tag">{e(tag)}</span></div>']
    if blurb: out.append(f'<p class="blurb">{e(blurb)}</p>')
    if url:
        out.append(f'<a class="go" href="{e(url)}" target="_blank" rel="noopener">Join {e(name)} <span aria-hidden="true">→</span></a>')
    if code:
        out.append(f'<div class="code"><span>Code <b>{e(code)}</b></span><button type="button" data-copy="{e(code)}">Copy code</button></div>')
    out.append('</article>')
    return "\n".join(out)
feat_html = "\n".join(card(by[b], t, bl, hot=True) for b,t,bl in featured)
more = []
for key,title in lanes:
    items = [o for o in src if o.get('lane')==key and o['brand'] not in fset]
    if not items: continue
    more.append(f'<h2 class="lane">{e(title)}</h2>')
    for o in items:
        bl = "$10 for new users" if o['brand']=="OG.com" else ""
        if o['brand']=="Fliff": bl = "Enter this code when you sign up"
        more.append(card(o, title, bl))
socials = [("X","@DFSJOEYOG","https://x.com/DFSJOEYOG"),("TikTok","@joaidhd","https://www.tiktok.com/@joaidhd"),("Instagram","@joaidhd2026","https://www.instagram.com/joaidhd2026/"),("Instagram","@dfsjoeyog","https://www.instagram.com/dfsjoeyog/"),("YouTube","@nflcliplab","https://www.youtube.com/@nflcliplab")]
soc_html = "\n".join(f'<a class="soc" href="{u}" target="_blank" rel="noopener"><b>{p}</b><span>{h}</span></a>' for p,h,u in socials)
page = open('template.html').read().replace('{{FEATURED}}',feat_html).replace('{{MORE}}',"\n".join(more)).replace('{{SOCIALS}}',soc_html)
open('index.html','w').write(page)
print("ok")

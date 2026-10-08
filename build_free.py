import json, html
e = html.escape
src = json.load(open('/workspace/joaidhd-HQ-upload/affiliates/links.json'))['offers']
by = {o['brand']: o for o in src}
courtside = {"brand":"Courtside","url":"https://api.courtside.app/r/VG670371","code":""}
items = [
 (by["SmackTok"], "SmackTok", "Rivalry weekend", "Talk your smack and back it up. Use my code ST-JL2343 when you sign up."),
 (by["Kalshi"], "Kalshi", "Bet the playoffs", "Trade MLB playoff and NFL outcomes like a stock. Yes or no, buy and sell any time."),
 (by["Polymarket"], "Polymarket", "Bet the playoffs", "Free credit when you sign up with code dfsjoeyog."),
 (by["DraftKings Sportsbook"], "DraftKings", "Sportsbook · Illinois", "Playoff baseball, Sunday football, rivalry weekend."),
 (courtside, "Courtside", "Sports app", ""),
]
cards=[]
for o,name,tag,blurb in items:
    c=[f'<article class="card hot">',f'<div class="hd"><h3>{e(name)}</h3><span class="tag">{e(tag)}</span></div>']
    if blurb: c.append(f'<p class="blurb">{e(blurb)}</p>')
    c.append(f'<a class="go" href="{e(o["url"])}" target="_blank" rel="noopener">Join {e(name)} <span aria-hidden="true">→</span></a>')
    if o.get('code'): c.append(f'<div class="code"><span>Code <b>{e(o["code"])}</b></span><button type="button" data-copy="{e(o["code"])}">Copy code</button></div>')
    c.append('</article>'); cards.append("\n".join(c))
t = open('template.html').read()
head, body = t.split('<body>',1)
head = head.replace('Joey Laskero · All my links','Free Money · Playoffs + Rivalry Weekend · @DFSJOEYOG')
body = f'''<body>
<div class="wrap">
<header>
  <h1>Free <span>Money</span></h1>
  <a class="handle" href="https://x.com/DFSJOEYOG" target="_blank" rel="noopener">@DFSJOEYOG</a>
  <p class="sub">MLB playoffs. Rivalry weekend. Don't bet it naked. These are the apps I use. Tap, sign up, copy the code.</p>
</header>
<div class="bar"></div>
<section class="list" aria-label="Sports apps">
{chr(10).join(cards)}
</section>
<h2 class="sec">Want <span>more?</span></h2>
<nav class="socs" aria-label="More">
<a class="soc" href="https://dfsjoeyog.github.io/links/" rel="noopener"><b>Every app I use</b><span>Full links page</span></a>
<a class="soc" href="https://x.com/DFSJOEYOG" target="_blank" rel="noopener"><b>X</b><span>@DFSJOEYOG</span></a>
<a class="soc" href="https://www.tiktok.com/@joaidhd" target="_blank" rel="noopener"><b>TikTok</b><span>@joaidhd</span></a>
</nav>
<footer>@DFSJOEYOG · Sox. Bears. Money.</footer>
</div>
'''
script = '<script>' + t.split('<script>',1)[1]
open('free/index.html','w').write(head + body + script)
print('ok')

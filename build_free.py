import json, html
e = html.escape
src = json.load(open('/workspace/joaidhd-HQ-upload/affiliates/links.json'))['offers']
by = {o['brand']: o for o in src}
courtside = {"brand":"Courtside","url":"https://api.courtside.app/r/VG670371","code":""}
# Brand colors (bg, text-on-bg) sampled from each brand's official site CSS / logo:
#  SmackTok   #17F6A4  smacktok.com CSS token + apple-touch-icon
#  Kalshi     #00DD94  Kalshi official App Store icon (text #01201A)
#  Polymarket #1652F0  polymarket.com mask-icon color + polymarket.us apple-touch-icon
#  DraftKings #53D337  sportsbook.draftkings.com primary button CSS (text #121212)
#  Courtside  #FF4A00  courtside.app CSS + site logo
items = [
 (by["SmackTok"], "SmackTok", "Rivalry weekend", "Talk your smack and back it up. Use my code ST-JL2343 when you sign up.", "smacktok.png", "#17F6A4", "#04120C"),
 (by["Kalshi"], "Kalshi", "Bet the playoffs", "Trade MLB playoff and NFL outcomes like a stock. Yes or no, buy and sell any time.", "kalshi.png", "#00DD94", "#01201A"),
 (by["Polymarket"], "Polymarket", "Bet the playoffs", "Free credit when you sign up with code dfsjoeyog.", "polymarket.png", "#1652F0", "#FFFFFF"),
 (by["DraftKings Sportsbook"], "DraftKings", "Sportsbook · Illinois", "Playoff baseball, Sunday football, rivalry weekend.", "draftkings.png", "#53D337", "#121212"),
 (courtside, "Courtside", "Sports app", "", "courtside.png", "#FF4A00", "#FFFFFF"),
]
cards=[]
for o,name,tag,blurb,logo,b,bt in items:
    c=[f'<article class="card" style="--b:{b};--bt:{bt}">',
       f'<div class="hd"><img class="logo" src="logos/{logo}" alt="{e(name)} logo" width="60" height="60"><div class="nm"><h3>{e(name)}</h3><span class="tag">{e(tag)}</span></div></div>']
    if blurb: c.append(f'<p class="blurb">{e(blurb)}</p>')
    c.append(f'<a class="go" href="{e(o["url"])}" target="_blank" rel="noopener">Join {e(name)} <span aria-hidden="true">→</span></a>')
    if o.get('code'): c.append(f'<div class="code"><span>Code <b>{e(o["code"])}</b></span><button type="button" data-copy="{e(o["code"])}">Copy code</button></div>')
    c.append('</article>'); cards.append("\n".join(c))
css = '''
:root{--bg:#0a0a0a;--r:#E6281E;--card:#141414;--line:#2a2a2a;--t:#fff;--m:#a3a3a3}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%}
body{background:var(--bg);color:var(--t);font:16px/1.45 system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;min-height:100dvh}
.wrap{max-width:480px;margin:0 auto;padding:30px 16px 56px}
header{text-align:center}
h1{font-size:2.4rem;font-weight:900;letter-spacing:-.03em;line-height:1.05}
h1 span{color:var(--r)}
.handle{display:inline-block;margin-top:8px;color:#fff;font-weight:700;text-decoration:none;font-size:1rem;padding:4px 12px;border:1px solid var(--line);border-radius:999px}
.sub{color:var(--m);margin:12px auto 0;font-size:.95rem;max-width:34ch}
.bar{height:3px;width:56px;border-radius:3px;background:var(--r);margin:22px auto 24px}
.list{display:flex;flex-direction:column;gap:16px}
.card{position:relative;overflow:hidden;background:var(--card);background:linear-gradient(165deg,color-mix(in srgb,var(--b) 20%,#141414) 0%,#141414 62%);border:1px solid var(--line);border-color:color-mix(in srgb,var(--b) 38%,#2a2a2a);border-radius:20px;padding:18px}
.card:before{content:"";position:absolute;left:0;right:0;top:0;height:4px;background:var(--b)}
.hd{display:flex;align-items:center;gap:14px}
.logo{width:60px;height:60px;border-radius:15px;flex-shrink:0;display:block;box-shadow:0 0 0 1px rgba(255,255,255,.1),0 6px 18px rgba(0,0,0,.45)}
.nm{min-width:0}
h3{font-size:1.4rem;font-weight:800;letter-spacing:-.01em;line-height:1.15}
.tag{display:inline-block;margin-top:4px;font-size:.68rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--b);color:color-mix(in srgb,var(--b) 70%,#fff);white-space:nowrap}
.blurb{color:#e5e5e5;margin-top:12px;font-size:.95rem}
.go{display:flex;align-items:center;justify-content:center;gap:8px;min-height:58px;margin-top:14px;border-radius:14px;background:var(--b);color:var(--bt);font-weight:800;font-size:1.12rem;text-decoration:none;-webkit-tap-highlight-color:transparent;transition:transform .1s}
.go:active{transform:scale(.98)}
.code{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:10px;background:rgba(0,0,0,.35);border:1px dashed color-mix(in srgb,var(--b) 55%,transparent);border-radius:12px;padding:8px 8px 8px 14px}
.code span{color:var(--m);font-size:.9rem;min-width:0;overflow-wrap:anywhere}
.code b{color:#fff;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:1.05rem;letter-spacing:.04em}
.code button{flex-shrink:0;min-height:44px;padding:0 14px;border:1px solid var(--b);border-radius:10px;background:transparent;color:#fff;font-weight:800;font-size:.92rem;cursor:pointer}
.code button.ok{background:var(--b);color:var(--bt)}
h2.sec{font-size:1.3rem;font-weight:900;margin:36px 0 12px;letter-spacing:-.01em}
h2.sec span{color:var(--r)}
.socs{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.soc{display:flex;flex-direction:column;justify-content:center;min-height:62px;padding:10px 14px;border-radius:14px;border:1px solid var(--line);background:#141414;text-decoration:none;color:#fff}
.soc:first-child{grid-column:1/-1;background:var(--r);border-color:var(--r)}
.soc b{font-size:1rem}.soc span{color:var(--m);font-size:.9rem}
.soc:first-child span{color:#ffe1df}
footer{text-align:center;color:var(--m);font-size:.8rem;margin-top:30px}
'''.strip()
t = open('template.html').read()
script = '<script>' + t.split('<script>',1)[1]
title = 'Free Money · Playoffs + Rivalry Weekend · @DFSJOEYOG'
desc = 'MLB playoffs. Rivalry weekend. The apps I use: SmackTok, Kalshi, Polymarket, DraftKings, Courtside.'
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#0a0a0a">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<style>
{css}
</style>
</head>
<body>
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
{script}'''
open('free/index.html','w').write(page)
print('ok')

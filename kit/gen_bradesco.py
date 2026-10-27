import sys
SELO='<svg width="34" height="34" viewBox="0 0 24 24" style="vertical-align:-6px"><circle cx="12" cy="12" r="11" fill="#1d9bf0"/><path d="M7 12.5l3.2 3.2L17 9" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
BASE='''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:"P";font-weight:300;src:url("fonts/node_modules/@fontsource/poppins/files/poppins-latin-300-normal.woff2")}
@font-face{font-family:"P";font-weight:500;src:url("fonts/node_modules/@fontsource/poppins/files/poppins-latin-500-normal.woff2")}
@font-face{font-family:"P";font-weight:600;src:url("fonts/node_modules/@fontsource/poppins/files/poppins-latin-600-normal.woff2")}
@font-face{font-family:"P";font-weight:700;src:url("fonts/sistema/Poppins-Bold.ttf")}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{position:relative;font-family:"P",sans-serif;color:#fff;background:radial-gradient(900px 700px at 100% 0%,rgba(30,140,80,.35),transparent 70%),radial-gradient(800px 600px at 0% 100%,rgba(255,180,0,.12),transparent 70%),#162526}
.cab{position:absolute;left:54px;top:60px;display:flex;align-items:center;gap:18px}
.cab img{width:84px;height:84px;border-radius:50%}
.cab .n{font-weight:600;font-size:30px}.cab .a{font-weight:300;font-size:24px;color:rgba(255,255,255,.75)}
h1{position:absolute;left:54px;right:54px;top:200px;font-weight:700;font-size:68px;line-height:1.08;letter-spacing:-1px}
h1 em{font-style:normal;color:#FFB400}
.fn{position:absolute;left:54px;right:54px;bottom:50px;font-weight:300;font-size:20px;color:rgba(255,255,255,.65)}
.pg{position:absolute;right:54px;top:84px;font-weight:500;font-size:24px;color:rgba(255,255,255,.6)}
@@CSS@@
</style></head><body>
<div class="cab"><img src="assets/avatar_infobolsa.png"><div><div class="n">InfoBolsa Investimentos @@SELO@@</div><div class="a">@infobolsainvest</div></div></div>
<div class="pg">@@PG@@</div>
@@BODY@@
<div class="fn">Fontes: Agência Senado, Agência Brasil e Exame. Projeção de 05/10/2026.</div>
</body></html>'''
def page(css,body,pg): return BASE.replace('@@CSS@@',css).replace('@@SELO@@',SELO).replace('@@PG@@',pg).replace('@@BODY@@',body)

# Slide 2 do carrossel do Bradesco (27/10/2026): print do comunicado aos parceiros
out=sys.argv[1]
B=BASE.replace('Fontes: Agência Senado, Agência Brasil e Exame. Projeção de 05/10/2026.','Comunicado do Bradesco aos parceiros imobiliários, de 26/10/2026.')
css='''.pr{position:absolute;left:50%;top:172px;transform:translateX(-50%);height:1058px;border-radius:18px;box-shadow:0 20px 60px rgba(0,0,0,.5)}'''
body='<img class="pr" src="assets/prints/bradesco-comunicado-2026-10-26.png">'
open(out,'w').write(B.replace('@@CSS@@',css).replace('@@SELO@@',SELO).replace('@@PG@@','2/2').replace('@@BODY@@',body))

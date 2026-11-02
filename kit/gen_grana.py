import os
FS="fonts/node_modules/@fontsource/"
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:"P";font-weight:300;src:url("{FS}poppins/files/poppins-latin-300-normal.woff2")}}
@font-face{{font-family:"P";font-weight:500;src:url("{FS}poppins/files/poppins-latin-500-normal.woff2")}}
@font-face{{font-family:"P";font-weight:600;src:url("{FS}poppins/files/poppins-latin-600-normal.woff2")}}
@font-face{{font-family:"P";font-weight:700;src:url("fonts/sistema/Poppins-Bold.ttf")}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:"P";color:#fff;background:radial-gradient(120% 80% at 70% 0%,#17324f 0%,#0b1626 55%,#070d18 100%)}}
.lg{{position:absolute;left:80px;top:70px;height:70px}}
.pill{{position:absolute;right:80px;top:78px;background:#fff;color:#0b1626;border-radius:40px;padding:10px 26px;font-weight:600;font-size:24px}}
h1{{position:absolute;left:80px;right:80px;top:190px;font-weight:300;font-size:64px;line-height:1.12;letter-spacing:-1px}}
h1 b{{font-weight:700;color:#1edc6e}}
.card{{position:absolute;left:80px;right:80px;height:150px;border-radius:26px;background:#fff;color:#0b1626;display:flex;align-items:center;gap:26px;padding:0 34px}}
.ck{{width:70px;height:70px;border-radius:50%;background:#1edc6e;display:flex;align-items:center;justify-content:center;flex:none}}
.card b{{display:block;font-weight:700;font-size:35px;line-height:1.15;color:#12306b}}
.card span{{font-size:25px;color:#3b4a63}}
.pr{{position:absolute;left:80px;right:80px;top:880px;height:215px;border-radius:30px;background:linear-gradient(100deg,#0d8f6a,#1edc6e);color:#06231a;padding:30px 44px}}
.pr small{{font-size:26px;font-weight:600;letter-spacing:1px;text-transform:uppercase}}
.pr .v{{display:flex;align-items:baseline;gap:22px;margin-top:6px}}
.pr .de{{font-size:38px;font-weight:500;text-decoration:line-through;opacity:.7}}
.pr .por{{font-size:104px;font-weight:700;line-height:1}}
.off{{position:absolute;right:44px;top:34px;background:#06231a;color:#1edc6e;border-radius:40px;padding:10px 26px;font-weight:700;font-size:34px}}
.ft{{position:absolute;left:80px;right:80px;top:1130px;display:flex;justify-content:space-between;align-items:center;font-size:34px;font-weight:600}}
.ft i{{font-style:normal;background:#fff;color:#0b1626;border-radius:40px;padding:10px 28px;font-size:28px;font-weight:600}}
.rd{{position:absolute;left:80px;right:80px;bottom:44px;font-size:19px;color:#8fa1ba;line-height:1.4}}
</style></head><body>
<img class="lg" src="assets/logo_grana.png"><div class="pill">App parceiro da B3</div>
<h1>Você vai declarar o IR da bolsa <b>de qualquer jeito.</b> Por que pagar R$ 120 a mais?</h1>
<div class="card" style="top:530px"><div class="ck"><svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></div><div><b>Declaração automática do IR da bolsa</b><span>Você importa na Receita e pronto</span></div></div>
<div class="card" style="top:700px"><div class="ck"><svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></div><div><b>Otimizador de IR</b><span>Tudo no plano completo Mais Grana</span></div></div>
<div class="pr"><small>Mais Grana anual</small><div class="off">R$ 120 off</div><div class="v"><span class="de">de R$ 359</span><span class="por">R$ 239</span></div></div>
<div class="ft"><span>Black do Grana</span><i>link na bio</i></div>
<div class="rd">Plano Mais Grana anual com R$ 120 de desconto em relação ao valor cheio de R$ 359. Conteúdo publicitário em parceria com o Grana Capital.</div>
</body></html>'''
open('tg.html','w').write(html)
os.system('python3 render.py tg.html ../pronto/grana/black-1.png')

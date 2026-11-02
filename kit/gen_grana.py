import os
FS="fonts/node_modules/@fontsource/"
CSS=f'''@font-face{{font-family:"P";font-weight:300;src:url("{FS}poppins/files/poppins-latin-300-normal.woff2")}}
@font-face{{font-family:"P";font-weight:500;src:url("{FS}poppins/files/poppins-latin-500-normal.woff2")}}
@font-face{{font-family:"P";font-weight:600;src:url("{FS}poppins/files/poppins-latin-600-normal.woff2")}}
@font-face{{font-family:"P";font-weight:700;src:url("fonts/sistema/Poppins-Bold.ttf")}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:"P";color:#162526;background:linear-gradient(160deg,#ffffff 0%,#f3f8f5 55%,#e2f0e8 100%)}}
.lg{{position:absolute;left:80px;top:64px;height:84px}}
.pill{{position:absolute;right:80px;top:84px;background:#162526;color:#fff;border-radius:40px;padding:10px 26px;font-weight:500;font-size:23px}}
h1{{position:absolute;left:80px;right:80px;top:200px;font-weight:600;font-size:64px;line-height:1.12;letter-spacing:-1px}}
h1 em{{font-style:normal;color:#0f7a43}}
.card{{position:absolute;left:80px;right:80px;border-radius:26px;background:#fff;border:1.5px solid #cfe3d6;box-shadow:0 10px 30px rgba(22,37,38,.07);display:flex;align-items:center;gap:26px;padding:0 34px}}
.ck{{width:64px;height:64px;border-radius:50%;background:#0f7a43;display:flex;align-items:center;justify-content:center;flex:none}}
.card b{{display:block;font-weight:600;font-size:34px;line-height:1.15}}
.card span{{font-size:25px;color:#4d5f5a}}
.dk{{position:absolute;left:80px;right:80px;border-radius:30px;background:#162526;color:#fff}}
.y{{color:#FFB400}}
.ft{{position:absolute;left:80px;right:80px;display:flex;justify-content:space-between;align-items:center;font-size:34px;font-weight:600}}
.ft i{{font-style:normal;background:#0f7a43;color:#fff;border-radius:40px;padding:10px 28px;font-size:28px;font-weight:600}}
.rd{{position:absolute;left:80px;right:80px;bottom:44px;font-size:19px;color:#6b7c76;line-height:1.4}}'''
CK='<div class="ck"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></div>'
TOP='<img class="lg" src="assets/logo_grana.png"><div class="pill">App parceiro da B3</div>'
RD='<div class="rd">Plano Mais Grana anual com R$ 120 de desconto em relação ao valor cheio de R$ 359. Conteúdo publicitário em parceria com o Grana Capital.</div>'
def pg(body,n):
    open('tg.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{TOP}{body}{RD}</body></html>')
    os.system(f'python3 render.py tg.html ../pronto/grana/black-{n}.png')
# A
pg(f'''<h1>Você vai declarar o IR da bolsa <em>de qualquer jeito.</em> Por que pagar R$ 120 a mais?</h1>
<div class="card" style="top:530px;height:150px">{CK}<div><b>Declaração automática do IR da bolsa</b><span>Você importa na Receita e pronto</span></div></div>
<div class="card" style="top:700px;height:150px">{CK}<div><b>Otimizador de IR</b><span>Tudo no plano completo Mais Grana</span></div></div>
<div class="dk" style="top:880px;height:215px;padding:30px 44px"><div style="font-size:25px;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:#9fd9b8">Mais Grana anual</div>
<div style="position:absolute;right:44px;top:32px;background:#FFB400;color:#162526;border-radius:40px;padding:10px 26px;font-weight:700;font-size:34px">R$ 120 off</div>
<div style="display:flex;align-items:baseline;gap:22px;margin-top:10px"><span style="font-size:38px;text-decoration:line-through;opacity:.6">de R$ 359</span><span style="font-size:104px;font-weight:700;line-height:1">R$ 239</span></div></div>
<div class="ft" style="top:1130px"><span>Black do Grana</span><i>link na bio</i></div>''','1')
# B
pg(f'''<h1>Se você investe na bolsa, essa é a <em>Black que vale a pena.</em></h1>
<div class="dk" style="top:470px;height:390px;text-align:center;padding-top:38px"><div style="font-size:30px;font-weight:500;letter-spacing:1px;color:#9fd9b8">MAIS GRANA ANUAL</div>
<div class="y" style="font-size:150px;font-weight:700;line-height:1.05;margin-top:6px">R$ 120</div><div style="font-size:52px;font-weight:600">a menos</div><div style="font-size:28px;margin-top:10px;opacity:.75">de R$ 359 por R$ 239</div></div>
<div class="card" style="top:885px;height:115px">{CK}<div><b>Declaração automática do IR da bolsa</b></div></div>
<div class="card" style="top:1015px;height:115px">{CK}<div><b>Otimizador de IR</b></div></div>
<div class="ft" style="top:1160px;font-size:30px"><span>Black do Grana</span><i style="font-size:26px">link na bio</i></div>''','2')
# C
pg(f'''<h1>Assinar depois sai <em>R$ 120 mais caro.</em> Simples assim.</h1>
<div style="position:absolute;left:80px;right:80px;top:450px;height:330px;display:flex;gap:30px">
<div class="card" style="position:static;flex:1;flex-direction:column;justify-content:center;gap:6px;text-align:center;padding:0;background:#fff"><span style="font-size:28px;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:#6b7c76">Depois</span><b style="font-size:84px;font-weight:700;text-decoration:line-through;color:#9aa8a3;text-decoration-thickness:6px">R$ 359</b><span>valor cheio por ano</span></div>
<div class="dk" style="position:static;flex:1;display:flex;flex-direction:column;justify-content:center;text-align:center;gap:6px"><span style="font-size:28px;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:#FFB400">Agora</span><b style="font-size:96px;font-weight:700;line-height:1">R$ 239</b><span style="font-size:25px;opacity:.8">Mais Grana anual</span></div></div>
<div class="card" style="top:820px;height:130px">{CK}<div><b>Declaração automática do IR da bolsa</b></div></div>
<div class="card" style="top:970px;height:130px">{CK}<div><b>Otimizador de IR</b></div></div>
<div class="ft" style="top:1150px"><span>Black do Grana</span><i>link na bio</i></div>''','3')

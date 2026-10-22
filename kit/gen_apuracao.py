import sys,json
# uso: python3 gen_apuracao.py out.html pct fl_pct lu_pct fl_votos lu_votos "linha1" "linha2" "parcial"
o,pct,fp,lp,fv,lv,l1,l2,par=sys.argv[1:10]
w=float(pct.replace(',','.'))
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:"P";font-weight:300;src:url("fonts/node_modules/@fontsource/poppins/files/poppins-latin-300-normal.woff2")}}
@font-face{{font-family:"P";font-weight:500;src:url("fonts/node_modules/@fontsource/poppins/files/poppins-latin-500-normal.woff2")}}
@font-face{{font-family:"P";font-weight:600;src:url("fonts/node_modules/@fontsource/poppins/files/poppins-latin-600-normal.woff2")}}
@font-face{{font-family:"P";font-weight:700;src:url("fonts/sistema/Poppins-Bold.ttf")}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{position:relative;font-family:"P",sans-serif;background:#162526;color:#fff}}
.f{{position:absolute;top:0;height:620px;background-size:cover;width:540px}}
.fa{{left:0;background-image:url(assets/flavio.jpg);background-position:50% 12%}}
.fb{{right:0;background-image:url(assets/lula.jpg);background-position:50% 8%}}
.sh{{position:absolute;left:0;right:0;top:0;height:620px;background:linear-gradient(180deg,rgba(22,37,38,0) 45%,rgba(22,37,38,1) 100%)}}
.mid{{position:absolute;left:539px;top:0;width:2px;height:620px;background:#162526}}
.nm{{position:absolute;top:500px;width:540px;text-align:center;font-weight:600;font-size:34px;letter-spacing:.5px;text-transform:uppercase}}
.nm small{{display:inline-block;margin-left:12px;font-size:19px;font-weight:500;border:1.5px solid rgba(255,255,255,.7);border-radius:6px;padding:2px 9px;vertical-align:4px}}
.na{{left:0}}.nb{{right:0}}
.pc{{position:absolute;top:548px;width:540px;text-align:center;font-weight:700;font-size:122px;color:#FFB400;letter-spacing:-2px;line-height:1.1}}
.vt{{position:absolute;top:688px;width:540px;text-align:center;font-weight:400;font-size:26px;color:#e8f0ea}}
.pa{{left:0}}.pb{{right:0}}
.urg{{position:absolute;left:44px;top:790px;display:flex;align-items:center;gap:22px}}
.urg b{{background:#e5383b;font-weight:700;font-size:30px;padding:8px 22px;border-radius:10px;letter-spacing:1px}}
.urg span{{font-weight:500;font-size:24px;letter-spacing:1px;text-transform:uppercase;color:#e8f0ea}}
.big{{position:absolute;left:44px;top:850px;font-weight:600;font-size:78px;letter-spacing:-1px}}
.big em{{font-style:normal;color:#FFB400;font-weight:700}}
.bar{{position:absolute;left:44px;right:44px;top:975px;height:14px;border-radius:7px;background:rgba(255,255,255,.14)}}
.bar i{{display:block;height:14px;border-radius:7px;background:#FFB400;width:{w}%}}
.tx{{position:absolute;left:44px;right:44px;top:1018px;font-weight:300;font-size:32px;line-height:1.4;color:#e8f0ea}}
.tx b{{font-weight:600;color:#fff}}
.ft{{position:absolute;left:44px;right:44px;top:1210px;border-top:1px solid rgba(255,255,255,.18);padding-top:26px;display:flex;align-items:center;gap:18px}}
.ft img{{width:84px;height:84px;border-radius:50%;object-fit:cover;object-position:50% 55%}}
.ft .n{{font-weight:600;font-size:28px}}.ft .h{{font-weight:300;font-size:22px;color:rgba(255,255,255,.75)}}
.ft .fo{{margin-left:auto;text-align:right;font-weight:300;font-size:17px;line-height:1.4;color:rgba(255,255,255,.65)}}
</style></head><body>
<div class="f fa"></div><div class="f fb"></div><div class="sh"></div><div class="mid"></div>
<div class="nm na">Flávio Bolsonaro<small>PL</small></div><div class="nm nb">Lula<small>PT</small></div>
<div class="pc pa">{fp}%</div><div class="pc pb">{lp}%</div>
<div class="vt pa">{fv} votos</div><div class="vt pb">{lv} votos</div>
<div class="urg"><b>URGENTE</b><span>Presidente · 2º turno · Resultado parcial</span></div>
<div class="big"><em>{pct}%</em> das urnas apuradas</div>
<div class="bar"><i></i></div>
<div class="tx">{l1}<br>{l2}</div>
<div class="ft"><img src="assets/foto.png"><div><div class="n">Douglas Medeiros</div><div class="h">@infobolsainvestimentos</div></div><div class="fo">Fonte: TSE<br>{par}<br>Fotos: Agência Senado e Ricardo Stuckert/PR</div></div>
</body></html>'''
open(o,'w').write(html)

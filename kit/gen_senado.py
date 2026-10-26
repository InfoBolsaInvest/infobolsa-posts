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

slide=sys.argv[1]; out=sys.argv[2]
if slide=='2':
    d=[("PL",28),("PT",9),("MDB",8),("União",6),("PP",6),("Republicanos",5),("PSD",5),("PSB",4),("Outros",10)]
    rows=''.join(f'<div class="r"><div class="l">{n}</div><div class="b"><i style="width:{v/28*100}%;background:{"#FFB400" if n=="PL" else "rgba(255,255,255,.85)"}"></i></div><div class="v" style="color:{"#FFB400" if n=="PL" else "#fff"}">{v}</div></div>' for n,v in d)
    css='.r{display:flex;align-items:center;gap:20px;height:78px}.l{width:260px;font-weight:500;font-size:34px}.b{flex:1;height:44px;border-radius:12px;background:rgba(255,255,255,.1)}.b i{display:block;height:44px;border-radius:12px}.v{width:70px;font-weight:700;font-size:42px;text-align:right}.tb{position:absolute;left:54px;right:54px;top:470px}.sub{position:absolute;left:54px;right:54px;top:392px;font-weight:300;font-size:30px;color:#e8f0ea}'
    body='<h1>Quem tem mais cadeiras<br>no Senado em <em>2027</em></h1><div class="sub">Total de <b>81</b> senadores. Maioria absoluta: <b>41</b>.</div><div class="tb">'+rows+'</div>'
    open(out,'w').write(page(css,body,'2/6'))
if slide=='3':
    css='.big{position:absolute;left:54px;right:54px;top:420px;display:flex;gap:24px}.cx{flex:1;border-radius:28px;background:rgba(255,255,255,.08);padding:34px 30px;height:300px}.cx .nu{font-weight:700;font-size:130px;line-height:1;color:#FFB400}.cx .tx{font-weight:300;font-size:30px;margin-top:14px;color:#e8f0ea}.li{position:absolute;left:54px;right:54px;top:780px}.li div{font-weight:300;font-size:36px;line-height:1.35;padding:20px 0;border-top:1.5px solid rgba(255,255,255,.18)}.li b{font-weight:700;color:#FFB400}'
    body='<h1>A eleição renovou<br><em>54 das 81</em> cadeiras</h1><div class="big"><div class="cx"><div class="nu">54</div><div class="tx">vagas em disputa</div></div><div class="cx"><div class="nu" style="color:#fff">27</div><div class="tx">cadeiras que não estavam em jogo</div></div></div><div class="li"><div>O <b>PL</b> elegeu <b>19</b> senadores (35,2% das vagas) e soma <b>28</b></div><div>O <b>MDB</b> elegeu <b>7</b> vagas</div><div>O <b>PT</b> elegeu <b>6</b> e soma <b>9</b></div></div>'
    open(out,'w').write(page(css,body,'3/6'))
if slide=='4':
    it=[("Leis e reformas","Vota projetos de lei, reformas e mudanças em impostos."),("Supremo Tribunal Federal","Aprova ou rejeita os nomes indicados para o STF."),("Banco Central","Aprova o presidente e os diretores do Banco Central."),("Impeachment","Julga o presidente da República em caso de processo.")]
    rows=''.join(f'<div class="it"><div class="k">{i+1}</div><div><div class="t">{a}</div><div class="d">{b}</div></div></div>' for i,(a,b) in enumerate(it))
    css='.ls{position:absolute;left:54px;right:54px;top:430px}.it{display:flex;gap:28px;align-items:flex-start;padding:30px 0;border-top:1.5px solid rgba(255,255,255,.18)}.k{width:76px;height:76px;border-radius:50%;background:#FFB400;color:#162526;font-weight:700;font-size:44px;display:flex;align-items:center;justify-content:center;flex:none}.t{font-weight:600;font-size:42px}.d{font-weight:300;font-size:31px;line-height:1.3;color:#e8f0ea;margin-top:6px}'
    body='<h1>O que o Senado<br><em>decide</em> no seu dia a dia</h1><div class="ls">'+rows+'</div>'
    open(out,'w').write(page(css,body,'4/6'))
if slide=='5':
    it=[("41","maioria absoluta","Vale para leis complementares."),("49","três quintos","Necessário para aprovar mudança na Constituição (PEC)."),("54","dois terços","Necessário para condenar no julgamento de impeachment.")]
    rows=''.join(f'<div class="it"><div class="nu">{a}</div><div><div class="t">{b}</div><div class="d">{c}</div></div></div>' for a,b,c in it)
    css='.ls{position:absolute;left:54px;right:54px;top:430px}.it{display:flex;gap:34px;align-items:center;padding:30px 0;border-top:1.5px solid rgba(255,255,255,.18)}.nu{width:190px;font-weight:700;font-size:118px;line-height:1;color:#FFB400;flex:none}.t{font-weight:600;font-size:42px}.d{font-weight:300;font-size:31px;line-height:1.3;color:#e8f0ea;margin-top:6px}.ob{position:absolute;left:54px;right:54px;top:1090px;border-radius:24px;background:rgba(255,180,0,.14);padding:26px 34px;font-weight:300;font-size:32px;line-height:1.35}.ob b{font-weight:700;color:#FFB400}'
    body='<h1>Quantos votos<br><em>contam</em> no Senado</h1><div class="ls">'+rows+'</div><div class="ob">O PL terá <b>28</b> dos 81 votos e o PT, <b>9</b>. Para chegar a esses números, qualquer lado precisa de aliados.</div>'
    open(out,'w').write(page(css,body,'5/6'))
if slide=='6':
    css='.c{position:absolute;left:54px;right:54px;top:360px;text-align:center}.c .q{font-weight:300;font-size:44px;color:#e8f0ea}.c .m{font-weight:700;font-size:86px;line-height:1.08;margin:22px 0 60px}.c .m em{font-style:normal;color:#FFB400}.bt{display:inline-flex;gap:20px;align-items:center;background:#FFB400;color:#162526;font-weight:700;font-size:44px;padding:26px 56px;border-radius:999px}.sm{margin-top:70px;font-weight:300;font-size:34px;color:#e8f0ea;line-height:1.4}'
    body='<div class="c"><div class="q">Quer entender como a política mexe com o seu dinheiro?</div><div class="m">Me segue para <em>não perder</em> as próximas notícias</div><div class="bt">+ Seguir @infobolsainvest</div><div class="sm">Notícias que importam para quem investe, todo dia às 12h.</div></div>'
    open(out,'w').write(page(css,body,'6/6').replace('<h1>',''))

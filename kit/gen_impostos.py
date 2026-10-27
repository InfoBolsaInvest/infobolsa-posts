import sys,re
src=open('gen_senado.py').read()
BASE=re.search(r"BASE='''(.*?)'''",src,re.S).group(1)
SELO=re.search(r"SELO='(.*?)'\n",src).group(1)
css='''
h1{top:185px;font-size:66px}
.bl{position:absolute;left:54px;right:54px;border-radius:30px;background:rgba(255,255,255,.07);display:flex;align-items:center;padding:0 40px;gap:30px}
.b1{top:370px;height:300px}.b2{top:760px;height:440px}
.lf{width:430px}
.chip{display:inline-block;background:#FFB400;color:#162526;font-weight:700;font-size:30px;padding:6px 22px;border-radius:12px;letter-spacing:1px}
.lf .t{font-weight:600;font-size:40px;line-height:1.15;margin-top:18px}
.lf .d{font-weight:300;font-size:27px;line-height:1.3;color:#e8f0ea;margin-top:12px}
.ln{width:70px;flex:none;align-self:stretch;position:relative}
.rt{flex:1;display:flex;flex-direction:column;gap:16px}
.tg{display:flex;align-items:center;justify-content:space-between;gap:14px;border-radius:18px;background:rgba(22,37,38,.9);border:2px solid rgba(255,180,0,.55);padding:12px 24px}
.tg b{font-weight:700;font-size:38px;color:#FFB400;white-space:nowrap}.tg span{font-weight:300;font-size:22px;color:#e8f0ea;text-align:right;line-height:1.15}
.mid{position:absolute;left:0;right:0;top:672px;text-align:center;font-weight:600;font-size:30px;color:#e8f0ea}
.mid svg{display:block;margin:0 auto 0;height:36px;width:36px}
.rd{position:absolute;left:54px;right:54px;top:1222px;text-align:center;font-weight:600;font-size:32px}
.rd em{font-style:normal;color:#FFB400}
'''
def tags(l): return ''.join(f'<div class="tg"><b>{a}</b><span>{b}</span></div>' for a,b in l)
def lines(n,h):
    # conector em chave ligando a caixa as etiquetas
    return f'<svg width="70" height="{h}" viewBox="0 0 70 {h}"><path d="M0 {h/2} H30 M30 {h*0.18} V{h*0.82} M30 {h*0.18} H70 M30 {h*0.82} H70" stroke="#FFB400" stroke-width="4" fill="none" stroke-linecap="round"/></svg>'
body=f'''<h1>Seu dinheiro paga imposto<br><em>duas vezes</em></h1>
<div class="bl b1"><div class="lf"><span class="chip">AO GANHAR</span><div class="t">Descontado do seu salário</div><div class="d">Já sai antes de o dinheiro cair na sua conta.</div></div><div class="ln">{lines(2,200)}</div><div class="rt">{tags([("IR","Imposto de Renda"),("INSS","Previdência")])}</div></div>
<div class="mid"><svg width="44" height="44" viewBox="0 0 44 44"><path d="M22 4v32M10 24l12 12 12-12" stroke="#FFB400" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>O que sobra vai para as compras</div>
<div class="bl b2"><div class="lf"><span class="chip">AO GASTAR</span><div class="t">Embutido no preço</div><div class="d">Você paga sem ver na nota: já vem dentro do preço do que compra.</div></div><div class="ln">{lines(4,340)}</div><div class="rt">{tags([("ICMS","Estadual"),("PIS/Cofins","Federal"),("IPI","Federal, indústria"),("ISS","Municipal, serviços")])}</div></div>
<div class="rd">Por isso o salário compra <em>menos do que parece</em></div>'''
html=BASE.replace('@@CSS@@',css).replace('@@SELO@@',SELO).replace('@@PG@@','').replace('@@BODY@@',body)
html=re.sub(r'<div class="fn">.*?</div>','<div class="fn" style="bottom:28px;text-align:center">As alíquotas variam por produto, estado e município.</div>',html)
open(sys.argv[1],'w').write(html)

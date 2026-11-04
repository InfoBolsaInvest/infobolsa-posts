import os
from decimal import Decimal as D, ROUND_HALF_UP
from gen_inst import pasta, pagina
from base import brl
cdi=D('0.1365'); ir=D('0.825'); base=D(10000)
def liq(p): return base*cdi*(p/D(100))*ir
linhas=[("POUPANÇA",D('616.78'))]+[(f"CDB <b>{p}%</b> CDI",liq(D(p)).quantize(D('0.01'),rounding=ROUND_HALF_UP)) for p in (100,101,102,103,104,105,110)]
rows=''
for i,(n,v) in enumerate(linhas):
    m=((1+v/base)**(D(1)/D(12))-1)*100
    rows+=f'<div class="cr{" p" if i==0 else ""}"><span>{n}</span><em>{brl(m.quantize(D("0.01"),rounding=ROUND_HALF_UP))}% ao mês</em><b>R$ {brl(v)}</b></div>'
css='''<style>.cr{display:flex;align-items:center;justify-content:space-between;height:78px;border-bottom:1px solid var(--linha);padding:0 8px}
.cr:last-child{border-bottom:0}.cr span{font-size:30px;color:var(--sub)}.cr span b{font-weight:700;color:var(--fg)}
.cr em{font-style:normal;font-size:27px;font-weight:500;color:var(--acc);margin-left:auto;margin-right:34px;width:230px;text-align:right;white-space:nowrap}.cr>b{font-size:42px;font-weight:700;color:var(--fg);white-space:nowrap}.cr.p span{font-weight:500}
.cr:nth-child(8)>b{color:var(--acc)}.ne{margin-top:14px;text-align:center;font-size:22px;color:var(--mute)}</style>'''
miolo=css+f'<div style="position:absolute;left:34px;right:34px;top:84px">{rows}</div>'
corpo=pasta(470,740,"Valores líquidos, após IR",miolo,"verde")
html=pagina("verde",'Selic mantida em <span>13,75%</span>','Quanto rendem <b style="font-weight:700">R$ 10.000,00</b> em 12 meses?',corpo,["Rendimento mensal médio já descontado o IR. Simulação com CDI constante de 13,65% ao ano e IR de 17,50% (prazo acima de 360 dias). O rendimento real pode variar.","Não é uma recomendação de compra ou venda."],tsize=76)
open('tc.html','w').write(html)
os.makedirs('../pronto/2026-11-04-cdb',exist_ok=True)
os.system('python3 render.py tc.html ../pronto/2026-11-04-cdb/1.png')
print(linhas)

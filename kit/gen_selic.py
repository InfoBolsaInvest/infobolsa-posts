import os
from gen_inst import pasta, pagina
css='''<style>.sr{display:flex;align-items:center;justify-content:space-between;height:112px;border-bottom:1px solid var(--linha);padding:0 6px}
.sr span{font-size:27px;color:var(--sub);line-height:1.2}.sr span small{display:block;font-size:19px;color:var(--mute)}
.sr b{font-size:50px;font-weight:700;color:var(--fg);white-space:nowrap}.sr b.g{color:var(--acc)}
.qq{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:22px}
.qq div{border-radius:18px;background:#eef6f1;padding:18px 20px;font-size:23px;line-height:1.35;color:var(--sub)}
.qq div b{display:block;font-size:26px;font-weight:600;color:var(--fg);margin-bottom:4px}
.qq div.y{background:#fff7e0}</style>'''
miolo=css+'''<div style="position:absolute;left:34px;right:34px;top:80px">
<div class="sr"><span>Selic hoje<small>Após o corte de 0,25 ponto em setembro</small></span><b>13,75%</b></div>
<div class="sr"><span>Chance de manter a Selic<small>Opções de Copom da B3, em 02/11</small></span><b class="g">68,80%</b></div>
<div class="sr"><span>Selic no fim de 2026<small>Mediana do Boletim Focus, em 26/10</small></span><b>13,25%</b></div>
<div class="qq"><div><b>Esperam manter</b>Itaú, HSBC, C6 e BTG</div><div class="y"><b>Esperam corte de 0,25</b>Inter, ASA e Daycoval</div></div></div>'''
corpo=pasta(470,610,"O que o mercado espera",miolo,"verde")
html=pagina("verde","Hoje tem <span>Copom</span>: a Selic vai cair?","A decisão sai hoje, depois do fechamento do mercado 👇",corpo,["Probabilidades implícitas nos preços das opções de Copom da B3, não são uma previsão oficial. Fonte: B3 e Boletim Focus do Banco Central.","Não é uma recomendação de compra ou venda."],tsize=66)
open('ts.html','w').write(html)
os.system('python3 render.py ts.html ../pronto/2026-11-04-selic/1.png')

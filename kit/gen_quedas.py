import sys,re
src=open('gen_senado.py').read()
BASE=re.search(r"BASE='''(.*?)'''",src,re.S).group(1)
SELO=re.search(r"SELO='(.*?)'\n",src).group(1)
D=[("VAMO3","Vamos","-54,60"),("MGLU3","Magalu","-53,98"),("CEAB3","C&A","-46,17"),("CSAN3","Cosan","-45,77"),("CYRE3","Cyrela","-43,77"),("MRVE3","MRV","-42,53"),("ASAI3","Assaí","-39,64"),("RENT3","Localiza","-39,03"),("B3SA3","B3","-37,42"),("SMFT3","Smart Fit","-33,99")]
css='''
h1{top:185px;font-size:66px}
.sb{position:absolute;left:54px;right:54px;top:395px;font-weight:300;font-size:30px;color:#e8f0ea}
.gr{position:absolute;left:54px;right:54px;top:470px;display:grid;grid-template-columns:1fr 1fr;grid-auto-flow:column;grid-template-rows:repeat(5,1fr);gap:16px 20px}
.cd{height:132px;border-radius:24px;background:rgba(255,255,255,.07);display:flex;align-items:center;padding:0 26px;gap:18px}
.rk{font-weight:700;font-size:22px;color:#FFB400;width:34px}
.tk{flex:1}.tk b{display:block;font-weight:700;font-size:38px;line-height:1}.tk span{font-weight:300;font-size:24px;color:#e8f0ea}
.pc{font-weight:700;font-size:40px;color:#ff5a5a;white-space:nowrap}
'''
cards=''.join(f'<div class="cd"><div class="rk">{i+1}</div><div class="tk"><b>{t}</b><span>{e}</span></div><div class="pc">{v}%</div></div>' for i,(t,e,v) in enumerate(D))
body=f'''<h1>Ações que <em>mais caíram</em><br>após as eleições</h1>
<div class="sb">As 10 maiores quedas da Bolsa após o 2º turno</div>
<div class="gr">{cards}</div>'''
html=BASE.replace('@@CSS@@',css).replace('@@SELO@@',SELO).replace('@@PG@@','').replace('@@BODY@@',body)
html=re.sub(r'<div class="fn">.*?</div>','<div class="fn" style="bottom:28px;text-align:center">Variação às 12h27 de 26/10/2026. Fonte: Status Invest. Não é recomendação de investimento.</div>',html)
open(sys.argv[1],'w').write(html)

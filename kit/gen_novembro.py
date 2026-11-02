import sys, os
from gen_inst import pasta, pagina
RAW="""AIEC11 0,92 09/11|ARRI11 0,05 09/11|BCIA11 0,86 30/11|BCRI11 0,80 13/11|BRCO11 0,91 16/11|CYCR11 0,10 12/11|GARE11 0,08 09/11|GRUL11 0,08 12/11|HGBS11 0,17 16/11|HGBL11 0,07 16/11|HGCR11 1,00 16/11|HGLG11 1,17 16/11|HABT11 0,92 12/11|HGRE11 0,85 16/11|HGRU11 0,95 16/11|HSML11 0,75 09/11|HTMX11 1,20 09/11|ICRI11 1,05 12/11|JSAF11 0,08 16/11|JSRE11 0,50 16/11|KIVO11 0,92 16/11|HFOF11 0,06 16/11|ITRI11 0,75 12/11|KFOF11 0,80 16/11|KNCR11 1,10 13/11|KNHF11 1,00 12/11|KNHY11 0,86 13/11|KNIP11 0,71 13/11|KNRI11 1,10 16/11|KNSC11 0,08 13/11|KNUQ11 1,06 12/11|KORE11 0,60 16/11|LIFE11 0,11 09/11|LVBI11 0,80 09/11|MANA11 0,11 24/11|MXRF11 0,095 16/11|MFII11 0,30 16/11|OUJP11 1,50 16/11|PMIS11 0,09 16/11|PORD11 0,09 09/11|PMLL11 1,00 16/11|JPPA11 1,20 16/11|RCRB11 1,30 13/11|RBHY11 0,90 16/11|RBVA11 0,09 13/11|RZTR11 0,87 09/11|SEED11 1,39 16/11|TRBL11 0,44 16/11|TEPP11 0,06 16/11|TGAR11 0,46 16/11|TRXF11 0,93 16/11|TVRI11 1,05 16/11|URPR11 0,30 16/11|VCJR11 0,82 13/11|VGRI11 0,07 09/11|VGHF11 0,05 09/11|VILG11 0,82 16/11|VINO11 0,04 16/11|VISC11 0,84 16/11|VCRI11 0,09 16/11|VRTA11 0,85 13/11|VRTM11 0,09 13/11|XPCI11 0,82 16/11|XPLG11 0,82 16/11|XPSF11 0,07 16/11|WHGR11 0,10 16/11|GTWR11 0,90 16/11|VSHO11 1,50 10/11|PVBI11 0,37 09/11|HSAF11 0,95 09/11|HSLG11 0,65 16/11|ZAVI11 0,11 13/11"""
L=sorted([x.split() for x in RAW.split("|")])
assert len(L)==len(set(l[0] for l in L)), "duplicado"
print(len(L))
cuts=[(0,24),(24,48),(48,72)]
css="""<style>.nv{position:absolute;left:28px;right:28px;top:82px;display:grid;grid-template-columns:1fr 1fr;column-gap:22px}
.nr{height:56px;display:flex;align-items:center;gap:12px;border-bottom:1px solid var(--linha)}
.nr b{background:#162526;color:#fff;font-weight:600;font-size:21px;letter-spacing:.5px;padding:6px 12px;border-radius:9px;min-width:114px;text-align:center}
.nr span{font-size:23px;font-weight:500;color:var(--fg);flex:1;white-space:nowrap}
.nr i{font-style:normal;font-size:21px;color:var(--acc);font-weight:600}
.nc{display:flex;flex-direction:column}</style>"""
for k,(a,b) in enumerate(cuts,1):
    part=L[a:b]; half=(len(part)+1)//2
    def col(rows): return '<div class="nc">'+''.join(f'<div class="nr"><b>{t}</b><span>R$ {v}</span><i>{d}</i></div>' for t,v,d in rows)+'</div>'
    h=82+12*56+30
    miolo=css+f'<div class="nv">{col(part[:half])}{col(part[half:])}</div>'
    corpo=pasta(400,h,f"Valor por cota e data de pagamento ({k}/3)",miolo,"verde")
    html=pagina("verde","<span>Dividendos</span> de novembro","FIIs que já anunciaram quanto vão pagar 👇",corpo,["Valores por cota, arredondados, com pagamento em novembro/2026. Confira o comunicado de cada fundo.","Rendimentos passados não garantem rendimentos futuros. Não é recomendação de compra ou venda."],tsize=72)
    open(f"t{k}.html","w").write(html)
    os.system(f"python3 render.py t{k}.html ../pronto/2026-11-02-novembro/{k}.png")

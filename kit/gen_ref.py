import os, math
from gen_inst import pasta, pagina
OUT="../pronto/2026-11-02-ref"
def render(html,n):
    open("t.html","w").write(html); os.system(f"python3 render.py t.html {OUT}/{n}.png")

# ---- 2: inquilinos TRXF11 (donut)
D=[("Mercado Livre",14.91),("Multilocatário logístico",14.16),("Lojistas de shoppings",10.85),("Assaí",6.86),("Grupo Mateus",6.56),("Einstein",6.44),("Pão de Açúcar",4.26),("Multilocatário corporativo",3.95),("DHL",3.71),("Shopee",3.11),("Outros",25.19)]
assert abs(sum(v for _,v in D)-100)<0.01
COR=["#0b3d2e","#0f7a43","#2e9e66","#5cbf8a","#9bd8b5","#FFB400","#ffd166","#162526","#4a6a62","#8fa59d","#d3ddd8"]
cx,cy,R,r=444,225,190,104
a=-90;svg=""
for (n,v),c in zip(D,COR):
    s=v*3.6;a0,a1=math.radians(a),math.radians(a+s);a+=s
    p=lambda R_,t:(cx+R_*math.cos(t),cy+R_*math.sin(t))
    x0,y0=p(R,a0);x1,y1=p(R,a1);x2,y2=p(r,a1);x3,y3=p(r,a0);lg=1 if s>180 else 0
    svg+=f'<path d="M{x0:.1f} {y0:.1f} A{R} {R} 0 {lg} 1 {x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f} A{r} {r} 0 {lg} 0 {x3:.1f} {y3:.1f}Z" fill="{c}" stroke="#fff" stroke-width="3"/>'
    if v>=6:
        m=(a0+a1)/2;tx,ty=p((R+r)/2,m)
        col="#162526" if c in("#FFB400","#9bd8b5","#ffd166","#5cbf8a") else "#fff"
        svg+=f'<text x="{tx:.1f}" y="{ty+7:.1f}" text-anchor="middle" font-size="{21 if v>=10 else 17}" font-weight="600" fill="{col}" font-family="P">{str(v).replace(".",",")}%</text>'
svg+=f'<text x="{cx}" y="{cy-4}" text-anchor="middle" font-size="26" fill="#162526" font-weight="600" font-family="P">TRXF11</text><text x="{cx}" y="{cy+26}" text-anchor="middle" font-size="19" fill="#5b6b66" font-family="P">receita de aluguel</text>'
leg="".join(f'<div class="lg"><i style="background:{c}"></i><span>{n}</span><b>{f"{v:.2f}".replace(".",",")}%</b></div>' for (n,v),c in zip(D,COR))
css='<style>.lg{display:flex;align-items:center;gap:12px;height:42px;font-size:21px;border-bottom:1px solid var(--linha)}.lg i{width:20px;height:20px;border-radius:6px;flex:none}.lg span{flex:1;color:var(--fg)}.lg b{font-weight:600;color:var(--fg)}.lgs{position:absolute;left:34px;right:34px;top:500px;display:grid;grid-template-columns:1fr 1fr;column-gap:34px}</style>'
miolo=css+f'<svg style="position:absolute;left:0;top:70px" width="888" height="500">{svg}</svg><div class="lgs" style="top:500px">{leg}</div>'
miolo=miolo.replace('width="888" height="500"','width="888" height="500" viewBox="0 0 888 500"')
corpo=pasta(415,790,"Receita de aluguel por inquilino",miolo,"verde")
render(pagina("verde","Os principais <span>inquilinos</span> do FII TRXF11","Quem paga o aluguel que vira provento 👇",corpo,["Fonte: relatório gerencial de setembro/2026 do TRXF11. Menores inquilinos em Outros.","Não é recomendação de compra ou venda."],tsize=66),2)

# ---- 3: mais lucrativas
L=[("PETR4","Petrobras","133,3"),("ITUB4","Itaú","48,9"),("BBDC4","Bradesco","26,6"),("BPAC11","BTG Pactual","19,1"),("BBAS3","Banco do Brasil","16,8")]
css='''<style>.pd{position:absolute;left:0;right:0;top:70px;height:470px}
.pc{position:absolute;bottom:0;width:260px;border-radius:20px 20px 0 0;background:linear-gradient(180deg,#e2f0e8,#cfe6d8);border:1.5px solid var(--borda);border-bottom:0;text-align:center}
.pc img{width:104px;height:104px;border-radius:20px;position:absolute;left:78px;top:-56px;box-shadow:0 8px 20px rgba(22,37,38,.18)}
.pc .rk{position:absolute;top:62px;left:0;right:0;font-size:60px;font-weight:700;color:#0f7a43}
.pc .nm{position:absolute;left:0;right:0;font-size:27px;font-weight:600;color:var(--fg)}
.pc .vl{position:absolute;left:0;right:0;font-size:36px;font-weight:700;color:var(--fg)}
.pc.o1{background:linear-gradient(180deg,#FFB400,#ffd166);border-color:#e6a200}.pc.o1 .rk{color:#162526}
.rw{position:absolute;left:34px;right:34px;height:96px;border-radius:20px;background:#fff;border:1.5px solid var(--borda);display:flex;align-items:center;gap:20px;padding:0 24px}
.rw i{font-style:normal;font-size:38px;font-weight:700;color:#0f7a43;width:48px}.rw img{width:64px;height:64px;border-radius:14px}.rw span{flex:1;font-size:32px;font-weight:600}.rw b{font-size:36px;font-weight:700}</style>'''
def col(i,x,h,o=""):
    t,n,v=L[i]
    return f'<div class="pc {o}" style="left:{x}px;height:{h}px"><img src="assets/logos_b3/{t}.png"><div class="rk">{i+1}º</div><div class="nm" style="top:{h-150}px">{n}</div><div class="vl" style="top:{h-100}px">R$ {v} bi</div></div>'
pod=f'<div class="pd">{col(1,50,340)}{col(0,314,430,"o1")}{col(2,578,310)}</div>'
rows="".join(f'<div class="rw" style="top:{590+j*108}px"><i>{j+4}º</i><img src="assets/logos_b3/{L[j+3][0]}.png"><span>{L[j+3][1]}</span><b>R$ {L[j+3][2]} bi</b></div>' for j in range(2))
corpo=pasta(415,810,"Lucro líquido, últimos 12 meses",css+pod+rows,"verde")
render(pagina("verde","As 5 empresas <span>mais lucrativas</span> do Brasil","Quanto elas ganharam nos últimos 12 meses 👇",corpo,["Lucro recorrente dos 4 trimestres até o 2T26 (3T26 ainda não divulgado).","Não é recomendação de compra ou venda."],tsize=66),3)

# ---- 4: renda passiva
R=[("1 ano","R$ 12.542","R$ 100"),("2 anos","R$ 26.343","R$ 211"),("3 anos","R$ 41.529","R$ 332"),("5 anos","R$ 76.624","R$ 613"),("7 anos","R$ 119.115","R$ 953"),("10 anos","R$ 200.217","R$ 1.602")]
css='''<style>.rp{position:absolute;left:34px;right:34px;top:84px}.rp .h,.rp .l{display:grid;grid-template-columns:1fr 1.3fr 1.1fr;align-items:center}
.rp .h{height:48px;font-size:19px;letter-spacing:1.5px;text-transform:uppercase;color:var(--mute);border-bottom:1px solid var(--linha)}
.rp .l{height:84px;font-size:32px;border-bottom:1px solid var(--linha)}.rp .l b{font-weight:600;color:var(--acc)}.rp .l:last-child{background:#fff7e0;border-radius:14px;padding:0 12px;margin:0 -12px}
.fm{position:absolute;left:34px;right:34px;top:660px;text-align:center;font-size:27px;line-height:1.4;color:var(--sub)}.fm b{color:var(--fg);font-weight:600}</style>'''
body=css+'<div class="rp"><div class="h"><span>Tempo</span><span>Patrimônio</span><span>Renda por mês</span></div>'+"".join(f'<div class="l"><span>{a}</span><span>{b}</span><b>{c}</b></div>' for a,b,c in R)+'</div><div class="fm">Comece pequeno. <b>Consistência e tempo</b> fazem a diferença.</div>'
corpo=pasta(400,780,"Investindo R$ 1.000 por mês",body,"verde")
render(pagina("verde","Renda passiva não começa em <span>R$ 10 mil</span> por mês","Veja o que aportes mensais podem virar 👇",corpo,["Simulação: aporte de R$ 1.000 por mês, proventos de 0,8% ao mês reinvestidos, sem considerar impostos nem variação de preço.","Resultados passados não garantem resultados futuros. Não é recomendação de compra ou venda."],tsize=62),4)

import os, json
from decimal import Decimal as D
from gen_inst import pasta, pagina

OUT = "../pronto/2026-11-02-tres"
os.makedirs(OUT, exist_ok=True)
def brl(v, c=2):
    s = f"{v:,.{c}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")
def render(html, n):
    open("tz.html", "w").write(html)
    os.system(f"python3 render.py tz.html {OUT}/{n}.png"); os.remove("tz.html")

# StatusInvest, fechamento de 30/10/2026 (B3 fechada em 02/11): cotação, proventos com data COM nos 12 meses
A = {"BBSE3": ("41.32", "4.5901"), "SANB11": ("23.94", "2.1724"), "VALE3": ("62.02", "5.6125"), "CPFE3": ("41.90", "3.7359"),
     "ITSA4": ("12.45", "1.1317"), "TAEE11": ("39.59", "3.0065"), "PETR4": ("52.71", "3.6667"), "ITUB4": ("38.69", "3.1177"),
     "ABEV3": ("14.60", "1.2505"), "CMIG4": ("10.07", "0.7878"), "CXSE3": ("21.38", "1.3500"), "BBDC4": ("13.86", "1.6076")}
tk = lambda t: f'<span style="font-weight:800;font-size:42px;letter-spacing:.5px;color:#162526">{t}</span>'

# ---------- 2: R$ 100 mil em ações
rows = []
for t in ["BBSE3", "SANB11", "VALE3", "CPFE3", "ITSA4", "TAEE11", "PETR4", "ITUB4"]:
    p, v = map(D, A[t]); ano = D(100000) / p * v
    rows.append((ano, t))
rows.sort(reverse=True)
lg2 = lambda t: (f'<span style="display:flex;align-items:center;gap:16px"><img src="assets/logos_b3/{t}.png" style="width:52px;height:52px;border-radius:12px;object-fit:cover">'
                 f'<span style="font-weight:800;font-size:40px;letter-spacing:.5px;color:#162526">{t}</span></span>')
linhas = [[lg2(t), "R$ " + brl(a / 12), "R$ " + brl(a)] for a, t in rows]
c = {"titulo": "Quanto rendem <span>R$ 100 mil</span> em ações que pagam dividendos?", "tsize": 52, "sub": "Simulação com a cotação de 30/10/2026 👇",
     "aba": "Rendimento de R$ 100 mil", "colunas": ["Ação", "Média por mês", "Em 12 meses"], "cols": "1.1fr 1fr 1fr", "lh": 74, "top": 440,
     "destaque": 1, "linhas": linhas,
     "rodape": ["Cotações de 30/10/2026 e proventos com data COM nos últimos 12 meses. Fonte: Status Invest.", "Valores brutos. Dividendos passados não garantem dividendos futuros. Não é recomendação de compra ou venda."]}
json.dump(c, open(f"{OUT}/2.json", "w"), ensure_ascii=False, indent=1)
os.system(f"python3 gen_inst.py tab {OUT}/2.json tz.html verde && python3 render.py tz.html {OUT}/2.png; rm -f tz.html")

# ---------- 3: quanto precisa pra ganhar R$ 1.621 por mês
rows = []
for t in ["BBSE3", "ABEV3", "ITSA4", "PETR4", "TAEE11", "ITUB4", "CMIG4", "CXSE3", "BBDC4"]:
    p, v = map(D, A[t]); rows.append((D(1621) * 12 / v * p, t, p, v))
rows.sort()
lg = lambda t: (f'<span style="display:flex;align-items:center;gap:16px"><img src="assets/logos_b3/{t}.png" style="width:46px;height:46px;border-radius:11px;object-fit:cover">'
                f'<span style="font-weight:800;font-size:34px;letter-spacing:.4px;color:#162526">{t}</span></span>')
linhas = [[lg(t), "R$ " + brl(v), "R$ " + brl(p), "R$ " + brl(inv)] for inv, t, p, v in rows]
c = {"titulo": "Quanto você precisa pra ganhar <span>R$ 1.621</span> por mês?", "tsize": 66, "sub": "Veja quanto investir em cada ação pra receber isso 👇",
     "aba": "Salário mínimo em dividendos", "colunas": ["Ação", "Prov. 12M", "Preço", "Precisa investir"], "cols": "1.5fr .9fr .9fr 1.35fr", "lh": 66, "top": 440,
     "destaque": 3, "linhas": linhas,
     "rodape": ["Com base nos proventos dos últimos 12 meses. Cotações de 30/10/2026. Fonte: Status Invest.", "Não é uma recomendação de compra ou venda."]}
json.dump(c, open(f"{OUT}/3.json", "w"), ensure_ascii=False, indent=1)
os.system(f"python3 gen_inst.py tab {OUT}/3.json tz.html verde && python3 render.py tz.html {OUT}/3.png; rm -f tz.html")

# ---------- 1: carteira que paga todo mês
G = [("FIIs de tijolo", "Renda previsível", "Galpões, shoppings e lojas", "#e6f3ec", "#0f7a43", ["HGLG11", "XPML11", "BTLG11"]),
     ("FIIs de papel", "Segue os juros", "CRIs ligados ao CDI e à inflação", "#eaf4f0", "#0f7a43", ["MXRF11", "KNCR11", "CPTS11"]),
     ("Ações", "Crescimento", "Crescem e dividem o lucro", "#fff7e0", "#b87900", ["WEGE3", "ITUB4", "VALE3"]),
     ("Lá fora", "Proteção", "Dólar e mercado global na carteira", "#eef0f2", "#162526", ["IVVB11", "NASD11", "GOLD11"])]
css = '''<style>.g4{position:absolute;left:96px;right:96px;top:470px;display:grid;grid-template-columns:1fr 1fr;gap:28px}
.cd{border-radius:28px;padding:28px 28px 24px;border:1.5px solid #d6e5dc;height:340px;position:relative}
.cd .t{font-size:19px;letter-spacing:1.6px;text-transform:uppercase;color:#5d726d}
.cd .n{position:absolute;right:26px;top:24px;width:46px;height:46px;border-radius:50%;color:#fff;font-weight:700;font-size:26px;display:flex;align-items:center;justify-content:center}
.cd h3{margin:6px 0 2px;font-size:40px;font-weight:700;line-height:1.1}.cd p{margin:0 0 12px;font-size:21px;color:#3f5552;line-height:1.25;height:28px}
.cd .r{display:flex;align-items:center;gap:14px;background:#fff;border-radius:16px;height:56px;padding:0 14px;margin-top:8px;box-shadow:0 1px 4px rgba(22,37,38,.07)}
.cd .r img,.cd .r .ni{width:44px;height:44px;border-radius:10px;object-fit:cover}.cd .r b{font-size:30px;font-weight:800;letter-spacing:.4px;color:#162526}
.ni{background:#0b1d33;color:#fff;font-weight:800;font-size:26px;display:flex;align-items:center;justify-content:center}</style>'''
cards = ""
for i, (tg, tt, sb, bg, cor, ts) in enumerate(G, 1):
    rs = "".join(f'<div class="r">' + (f'<img src="assets/logos_b3/{t}.png">' if os.path.exists(f"assets/logos_b3/{t}.png") else '<div class="ni">N</div>') + f'<b>{t}</b></div>' for t in ts)
    cards += f'<div class="cd" style="background:{bg}"><div class="t">{tg}</div><div class="n" style="background:{cor}">{i}</div><h3 style="color:{cor}">{tt}</h3><p>{sb}</p>{rs}</div>'
render(pagina("verde", "Carteira que paga todo mês: <span>as 4 partes</span> que não podem faltar", "Um exemplo em cada parte 👇", css + f'<div class="g4">{cards}</div>',
              ["Exemplos por categoria, sem ordem de preferência.", "Não é uma recomendação de compra ou venda."], tsize=56), 1)

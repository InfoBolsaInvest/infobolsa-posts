import os, json
from decimal import Decimal as D
from gen_inst import pasta, pagina

OUT = "../pronto/2026-11-02-tres2"
os.makedirs(OUT, exist_ok=True)
def brl(v, c=2):
    s = f"{v:,.{c}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")
def render(html, n):
    open("tz.html", "w").write(html)
    os.system(f"python3 render.py tz.html {OUT}/{n}.png"); os.remove("tz.html")
def logo(t, w, r):
    if os.path.exists(f"assets/logos_b3/{t}.png"):
        return f'<img src="assets/logos_b3/{t}.png" style="width:{w}px;height:{w}px;border-radius:{r}px;object-fit:cover;flex:none">'
    return (f'<span style="width:{w}px;height:{w}px;border-radius:{r}px;background:#162526;color:#fff;font-weight:800;font-size:{int(w*.4)}px;'
            f'display:flex;align-items:center;justify-content:center;flex:none">{t[:2]}</span>')

# ---------- 1: dividendos recorrentes (Status Invest: dividendos/JCP em todos os anos de 2016 a 2025, checado ativo a ativo)
E1 = ["GGBR4", "TAEE11", "BBAS3", "BBDC4", "CMIG4", "SBSP3", "CSMG3", "ITUB4", "SAPR4", "BRSR6", "VALE3", "KLBN4", "EGIE3", "WEGE3", "TIMS3"]
css = '''<style>.g5{position:absolute;left:34px;right:34px;top:84px;display:grid;grid-template-columns:repeat(5,1fr);row-gap:26px}
.g5 div{display:flex;flex-direction:column;align-items:center;gap:12px}.g5 b{font-size:27px;font-weight:800;letter-spacing:.3px;color:#162526}</style>'''
cel = "".join(f'<div>{logo(t, 118, 26)}<b>{t}</b></div>' for t in E1)
corpo = pasta(440, 700, "Dividendos todos os anos", css + f'<div class="g5">{cel}</div>', "verde")
render(pagina("verde", "Essas empresas pagam <span>dividendos recorrentes</span> há mais de 10 anos...", "", corpo,
              ["Com base no histórico de proventos do Status Invest, de 2016 a 2025.", "Proventos passados não garantem proventos futuros. Não é recomendação de compra ou venda."], tsize=56), 1)

# ---------- 2: FIIs abaixo de R$ 10 (Status Invest, 30/10/2026)
F2 = [("CPTS11", "7,00", "15,43", "392.504", "Papel"), ("GARE11", "8,20", "12,15", "553.693", "Logística"), ("SNEL11", "7,62", "15,75", "119.274", "Energia limpa"),
      ("TEPP11", "6,91", "16,74", "45.664", "Escritório"), ("KNSC11", "8,74", "12,81", "268.171", "Papel"), ("MANA11", "8,94", "15,38", "37.908", "Híbrido"),
      ("VGIR11", "8,90", "16,97", "273.654", "Papel"), ("RBVA11", "8,12", "13,30", "92.794", "Varejo"), ("MXRF11", "8,88", "13,40", "1.509.087", "Papel"),
      ("GGRC11", "8,48", "14,15", "411.230", "Logística"), ("CPSH11", "9,04", "15,15", "38.251", "Shopping"), ("ALZR11", "9,70", "10,37", "206.111", "Híbrido")]
def cot(s):
    n = int(s.replace(".", ""))
    return f"{n/1_000_000:.2f} mi".replace(".", ",") if n >= 1_000_000 else f"{n//1000} mil"
css = '''<style>.g3{position:absolute;left:96px;right:96px;top:430px;display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.fc{background:#fff;border:1.5px solid #d6e5dc;border-radius:22px;padding:14px 14px 12px;height:236px;box-shadow:0 1px 6px rgba(22,37,38,.06)}
.fc .h{display:flex;align-items:center;gap:9px}.fc .h b{font-size:27px;font-weight:800;letter-spacing:.2px;color:#162526}
.fc .p{margin:10px 0 8px;height:54px;border-radius:14px;background:#e6f3ec;color:#0f7a43;font-weight:800;font-size:36px;display:flex;align-items:center;justify-content:center}
.fc .l{font-size:18px;color:#3f5552;line-height:1.45;white-space:nowrap}.fc .l span{color:#7b8f8a}</style>'''
cards = "".join(f'<div class="fc"><div class="h">{logo(t, 40, 10)}<b>{t}</b></div><div class="p">R$ {p}</div>'
                f'<div class="l"><span>Setor:</span> {s}</div><div class="l"><span>DY 12M:</span> {d}%</div><div class="l"><span>Cotistas:</span> {cot(c)}</div></div>'
                for t, p, d, c, s in F2)
render(pagina("verde", "Alguns fundos imobiliários por <span>menos de R$ 10</span>", "Cotações de 30/10/2026 👇", css + f'<div class="g3">{cards}</div>',
              ["Dividend yield dos últimos 12 meses e número de cotistas. Fonte: Status Invest.", "Rendimentos passados não garantem rendimentos futuros. Não é recomendação de compra ou venda."], tsize=56), 2)

# ---------- 3: quanto investir em cada FII para R$ 1.621 por mês
F3 = [("VGIA11", "0.12", "8.50"), ("SNAG11", "0.12", "9.58"), ("SNEL11", "0.10", "7.62"), ("VGIR11", "0.13", "8.90"), ("KNSC11", "0.08", "8.74"),
      ("HSML11", "0.75", "79.80"), ("VGHF11", "0.05", "4.80"), ("TRXF11", "0.93", "66.45"), ("MXRF11", "0.095", "8.88")]
rows = sorted((D(1621) / D(r) * D(p), t, D(r), D(p)) for t, r, p in F3)
lg = lambda t: (f'<span style="display:flex;align-items:center;gap:16px">{logo(t, 46, 11)}'
                f'<span style="font-weight:800;font-size:34px;letter-spacing:.4px;color:#162526">{t}</span></span>')
linhas = [[lg(t), "R$ " + brl(r, 3 if r == D("0.095") else 2), "R$ " + brl(p), "R$ " + brl(inv)] for inv, t, r, p in rows]
c = {"titulo": "Quanto investir em cada FII para ganhar <span>R$ 1.621</span> por mês?", "tsize": 62, "sub": "",
     "aba": "Salário mínimo em rendimentos", "colunas": ["FII", "Últ. rend.", "Preço", "Precisa investir"], "cols": "1.5fr .9fr .9fr 1.35fr", "lh": 66, "top": 440,
     "destaque": 3, "linhas": linhas,
     "rodape": ["Último rendimento anunciado de cada fundo e cotações de 30/10/2026. Fonte: Status Invest.", "Rendimentos passados não garantem rendimentos futuros. Não é recomendação de compra ou venda."]}
json.dump(c, open(f"{OUT}/3.json", "w"), ensure_ascii=False, indent=1)
os.system(f"python3 gen_inst.py tab {OUT}/3.json tz.html verde && python3 render.py tz.html {OUT}/3.png; rm -f tz.html")

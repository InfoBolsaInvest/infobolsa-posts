#!/usr/bin/env python3
"""4 posts de 25/11/2026 (galpões, Focus, classificando, salário mínimo) no padrão InfoBolsa."""
import json, math, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ".")
from gen_inst import CSS, FS, SELO, SCRIPT, curva

BASE = """
body{background:linear-gradient(172deg,#ffffff 0%,#ffffff 58%,#eef6f1 100%)!important}
.luz{position:absolute;inset:0;background:radial-gradient(ellipse 760px 620px at 100% 100%,rgba(15,122,67,.07),transparent 70%)}
.cab{top:70px}
.t{position:absolute;left:84px;right:84px;top:245px;font-weight:700;font-size:var(--ts,60px);line-height:1.15;letter-spacing:-1px;color:#162526}
.t .n{font-weight:400}.t .g{color:#0f7a43}
.t:after{content:'';display:block;width:110px;height:7px;border-radius:4px;background:#FFB400;margin-top:24px}
.sb{position:absolute;left:84px;right:84px;font-size:32px;color:#3f5552}
"""


def pag(corpo, ts=60, extra=""):
    h = (f'<div class="cab"><div class="ft"><img src="assets/foto.png" alt=""></div>'
         f'<div><div class="nm">Douglas Medeiros {SELO}</div><div class="ar">@infobolsainvestimentos</div></div></div>')
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS.replace("FS/", FS)}{BASE}{extra}</style></head>'
            f'<body style="--fg:#162526;--sub:#3f5552;--foto:#162526;--ts:{ts}px"><div class="luz"></div>{curva("branco")}{h}{corpo}{SCRIPT}</body></html>')


def br(v, d=2):
    return f"{v:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


# 1. Galpões com mais cotistas (pódio)
G = [("HGLG11", "Pátria Log", 608345), ("BTLG11", "BTG Logística", 505908), ("GGRC11", "GGR Covepi", 411230),
     ("XPLG11", "XP Log", 347304), ("VILG11", "Vinci Logística", 149265)]
CSS1 = """
.pd{position:absolute;left:70px;right:70px;top:490px;display:grid;grid-template-columns:1fr 1fr;gap:40px;grid-auto-rows:220px}
.pc{background:#fff;border:1.5px solid #e3ece7;border-radius:30px;box-shadow:0 12px 30px rgba(22,37,38,.06);display:flex;align-items:center;gap:24px;padding:24px 28px;position:relative}
.pc.um{grid-column:1/3;justify-content:center;padding:30px}
.pc{padding:24px 24px 24px 30px;gap:22px}.pc.um{gap:30px}
.pc img{width:84px;height:84px;border-radius:24px;object-fit:contain}
.pc.um img{width:140px;height:140px}
.pc .tk{font-weight:700;font-size:40px;color:#162526;line-height:1}
.pc.um .tk{font-size:58px}
.pc .nm2{font-size:24px;color:#7b8f8a;margin-top:6px}
.pc .q{font-weight:700;font-size:34px;color:#0f7a43;margin-top:12px}
.pc.um .q{font-size:46px}
.pc .q small{font-size:24px;font-weight:500;color:#3f5552}
.md{position:absolute;left:-12px;top:-12px;width:54px;height:54px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:26px;color:#fff;box-shadow:0 6px 14px rgba(0,0,0,.15)}
"""
cores = ["#FFB400", "#9aa5a8", "#c07a3c", "#0f7a43", "#0f7a43"]
cards = ""
for i, (t, n, q) in enumerate(G):
    cards += (f'<div class="pc{" um" if i == 0 else ""}"><div class="md" style="background:{cores[i]}">{i + 1}º</div>'
              f'<img src="assets/logos_b3/{t}.png"><div><div class="tk">{t}</div><div class="nm2">{n}</div>'
              f'<div class="q num">{br(q / 1000, 0)} mil <small>cotistas</small></div></div></div>')
open("q1.html", "w").write(pag('<div class="t">🚨 Os 5 FIIs de galpões com <span class="g">mais cotistas</span> 👇</div>'
                               f'<div class="pd">{cards}</div>', 58, CSS1))

# 2. Focus
F = [("IPCA", ["5,15%", "5,12%", "4,00%", "4,00%"]), ("PIB", ["1,70%", "1,00%", "1,71%", "2,00%"]),
     ("Dólar", ["R$ 5,55", "R$ 5,50", "R$ 5,50", "R$ 5,55"]), ("Selic", ["13,75%", "13,00%", "11,00%", "10,50%"])]
CSS2 = """
.fs{position:absolute;left:84px;right:84px;top:445px;font-size:32px;color:#3f5552}
.fo{position:absolute;left:60px;right:60px;top:540px;background:#fff;border:1.5px solid #e3ece7;border-radius:30px;overflow:hidden;box-shadow:0 12px 30px rgba(22,37,38,.06)}
.fo .r{display:grid;grid-template-columns:1.15fr 1fr 1fr 1fr 1fr;align-items:center;height:150px;border-top:1.5px solid #e3ece7;text-align:center}
.fo .r:first-child{height:90px;border-top:none;background:#162526;color:#FFB400;font-weight:700;font-size:28px;letter-spacing:1px}
.fo .r:first-child div:first-child{color:#fff}
.fo .r:nth-child(odd):not(:first-child){background:#f6faf7}
.fo .r div:first-child{text-align:left;padding-left:32px;font-weight:700;font-size:40px;color:#162526}
.fo .v{font-weight:700;font-size:40px;color:#162526}
.fo .v small{font-size:22px;color:#7b8f8a;font-weight:500;margin-right:4px}
"""
rows = '<div class="r"><div>Indicador</div><div>2026</div><div>2027</div><div>2028</div><div>2029</div></div>'
for k, vs in F:
    rows += f'<div class="r"><div>{k}</div>' + "".join(
        f'<div class="v num">{"<small>R$</small>" + v[3:] if v.startswith("R$") else v}</div>' for v in vs) + "</div>"
open("q2.html", "w").write(pag('<div class="t">O que o mercado projeta para a <span class="g">economia brasileira?</span></div>'
                               '<div class="fs">Boletim Focus de 23/11/2026 👇</div>'
                               f'<div class="fo">{rows}</div>', 60, CSS2))

# 3. Classificando os investimentos
C = [("Reserva de emergência", ["Poupança", "CDB liquidez diária", "Tesouro Selic"]),
     ("Crescer o patrimônio", ["Previdência cara", "Tesouro IPCA+", "Ações"]),
     ("Receber renda mensal", ["Imóvel para alugar", "Ações", "FIIs"])]
CSS3 = """
.cl{position:absolute;left:60px;right:60px;top:480px;display:flex;flex-direction:column;gap:36px}
.bl{background:#fff;border:1.5px solid #e3ece7;border-radius:30px;padding:22px 26px 24px;box-shadow:0 12px 30px rgba(22,37,38,.06)}
.bl h3{margin:0 0 18px;font-weight:700;font-size:34px;color:#162526;text-align:center}
.bl .g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px}
.cbx{border-radius:20px;overflow:hidden;border:1.5px solid #e3ece7;text-align:center}
.cbx .cbl{font-weight:700;font-size:24px;letter-spacing:2px;color:#fff;padding:8px 0}
.cbx .cbn{font-weight:700;font-size:29px;color:#162526;padding:12px 10px;min-height:82px;display:flex;align-items:center;justify-content:center;line-height:1.15}
"""
lbs = [("RUIM", "#c0392b"), ("BOM", "#d99a00"), ("ÓTIMO", "#0f7a43")]
bl = ""
for t, its in C:
    bl += f'<div class="bl"><h3>{t}</h3><div class="g3">' + "".join(
        f'<div class="cbx"><div class="cbl" style="background:{c}">{l}</div><div class="cbn">{x}</div></div>'
        for (l, c), x in zip(lbs, its)) + "</div></div>"
open("q3.html", "w").write(pag('<div class="t">Classificando os <span class="g">investimentos</span> 👇</div>'
                               f'<div class="cl">{bl}</div>', 64, CSS3))

# 4. Salário mínimo com FIIs
SAL = 1621
S = [("VGIA11", .12, 7.61), ("SNAG11", .12, 9.40), ("SNEL11", .10, 7.26), ("VGIR11", .119, 8.24), ("MCHF11", .07, 9.10),
     ("HSML11", .75, 78.73), ("VGHF11", .05, 3.92), ("TRXF11", .93, 55.70), ("MXRF11", .095, 8.50)]
L = []
for t, r, p in S:
    q = math.ceil(SAL / r)
    L.append((t, r, p, q * p))
L.sort(key=lambda x: x[3])
CSS4 = """
.sm{position:absolute;left:60px;right:60px;top:510px;background:#fff;border:1.5px solid #e3ece7;border-radius:30px;overflow:hidden;box-shadow:0 12px 30px rgba(22,37,38,.06)}
.sm .r{display:grid;grid-template-columns:1fr .9fr .9fr 1.5fr;align-items:center;height:76px;border-top:1.5px solid #e3ece7;text-align:center;font-size:30px;color:#3f5552}
.sm .r:first-child{height:70px;border-top:none;background:#162526;color:#fff;font-weight:700;font-size:24px}
.sm .r:first-child div:last-child{color:#FFB400}
.sm .r:nth-child(odd):not(:first-child){background:#f6faf7}
.sm .r div:first-child{font-weight:700;color:#162526;font-size:32px}
.sm .r:first-child div:first-child{color:#fff;font-size:24px}
.sm .r div:last-child{font-weight:700;color:#0f7a43}
.sm .r:first-child div:last-child{color:#FFB400}
"""
rows = '<div class="r"><div>FII</div><div>Últ. rend.</div><div>Preço</div><div>Investimento necessário</div></div>'
for t, r, p, v in L:
    rows += (f'<div class="r"><div>{t}</div><div class="num">R$ {br(r, 3 if round(r, 2) != r else 2)}</div>'
             f'<div class="num">R$ {br(p)}</div><div class="num">R$ {br(v)}</div></div>')
open("q4.html", "w").write(pag('<div class="t">Quanto investir para receber <span class="g" style="white-space:nowrap">1 salário</span> <span class="g">mínimo</span> por mês?</div>'
                               '<div class="sb" style="top:440px">R$ 1.621,00 por mês, com cada FII 👇</div>'
                               f'<div class="sm">{rows}</div>', 58, CSS4))
json.dump([[t, r, p, round(v, 2)] for t, r, p, v in L], open("/tmp/claude-0/-home-claude/bb41cf14-75e1-5f31-b4e9-ee9e21090f51/scratchpad/sal.json", "w"))
print([(t, br(v)) for t, r, p, v in L])

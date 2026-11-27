#!/usr/bin/env python3
"""Carrossel 27/11/2026: FIIs sobem com Trabuco na Fazenda (mapa de calor, motivos, segmentos)."""
import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ".")
from gen_inst import CSS, FS, SELO, SCRIPT, curva

BASE = """
body{background:linear-gradient(172deg,#ffffff 0%,#ffffff 58%,#eef6f1 100%)!important}
.luz{position:absolute;inset:0;background:radial-gradient(ellipse 760px 620px at 100% 100%,rgba(15,122,67,.07),transparent 70%)}
.cab{top:70px}
.t{position:absolute;left:84px;right:84px;top:245px;font-weight:400;font-size:var(--ts,60px);line-height:1.15;letter-spacing:-1px;color:#162526}
.t b{font-weight:700}
.t:after{content:'';display:block;width:110px;height:7px;border-radius:4px;background:#FFB400;margin-top:24px}
.sb{position:absolute;left:84px;right:84px;font-size:30px;color:#3f5552}
"""


def pag(corpo, ts=60, extra=""):
    h = (f'<div class="cab"><div class="ft"><img src="assets/foto.png" alt=""></div>'
         f'<div><div class="nm">Douglas Medeiros {SELO}</div><div class="ar">@infobolsainvestimentos</div></div></div>')
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS.replace("FS/", FS)}{BASE}{extra}</style></head>'
            f'<body style="--fg:#162526;--sub:#3f5552;--foto:#162526;--ts:{ts}px"><div class="luz"></div>{curva("branco")}{h}{corpo}{SCRIPT}</body></html>')


V = {"KNRI11": 1.90, "HGLG11": 1.65, "XPML11": 3.61, "BTLG11": 1.90, "MXRF11": 2.76, "KNCR11": 0.06, "VISC11": 3.29,
     "HGRU11": 2.42, "XPLG11": 1.54, "PVBI11": 5.44, "HSML11": 2.61, "TGAR11": 4.50, "KNIP11": 0.82, "CPTS11": 2.81,
     "RECR11": 1.09, "VGHF11": 2.26, "TRXF11": 5.00, "LVBI11": 2.07, "BRCR11": 3.36, "HGRE11": 2.33, "JSRE11": 2.91,
     "ALZR11": 2.82, "GGRC11": 3.00, "KNSC11": 0.96, "HGCR11": 1.35, "VGIR11": 1.43, "MCCI11": 0.64,
     "SNME11": 0.95, "RZTR11": 5.56, "VILG11": 1.92, "KNHF11": 1.42, "PCIP11": 1.66, "HFOF11": 1.92}
pc = lambda v: ("+" if v > 0 else "") + f"{v:.2f}".replace(".", ",") + "%"


def cor(v):
    # verde mais escuro para alta maior
    if v >= 4: return "#0b5e33"
    if v >= 3: return "#0f7a43"
    if v >= 2: return "#1f9457"
    if v >= 1: return "#3fae72"
    return "#7cc89c"


L = sorted(V.items(), key=lambda x: -x[1])
big, small = L[:6], L[6:30]

# 1. Mapa de calor
CSS1 = """
.hm{position:absolute;left:84px;right:84px;top:520px}
.hb{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:10px}
.hs{display:grid;grid-template-columns:repeat(6,1fr);gap:10px}
.tl{border-radius:16px;color:#fff;display:flex;flex-direction:column;justify-content:center;padding:0 18px}
.hb .tl{height:120px}
.hb .tl b{font-size:36px;font-weight:700}
.hb .tl span{font-size:30px;font-weight:600;opacity:.95}
.hs .tl{height:92px;padding:0 10px;align-items:center;text-align:center}
.hs .tl b{font-size:22px;font-weight:700}
.hs .tl span{font-size:21px;font-weight:600;opacity:.95}
.lg{display:flex;align-items:center;gap:14px;margin-top:22px;font-size:22px;color:#7b8f8a}
.lg i{display:block;width:44px;height:16px;border-radius:5px}
"""
tile = lambda t, v: f'<div class="tl" style="background:{cor(v)}"><b>{t}</b><span class="num">{pc(v)}</span></div>'
leg = "".join(f'<i style="background:{cor(x)}"></i>' for x in (0.5, 1.5, 2.5, 3.5, 4.5))
html = pag('<div class="t">Dia de festa nos <b>fundos imobiliários</b> 🟩</div>'
           '<div class="sb" style="top:430px">Variação de hoje (27/11) dos maiores FIIs, às 12h20 👇</div>'
           f'<div class="hm"><div class="hb">{"".join(tile(t, v) for t, v in big)}</div>'
           f'<div class="hs">{"".join(tile(t, v) for t, v in small)}</div>'
           f'<div class="lg">menos {leg} mais alta</div></div>', 62, CSS1)
open("h1.html", "w").write(html)

# 2. Motivos
CSS2 = """
.mv{position:absolute;left:84px;right:84px;top:440px;border-top:3px solid #cdd9d3}
.mv .r{display:flex;gap:30px;padding:22px 0;border-bottom:3px solid #cdd9d3;align-items:flex-start}
.mv .n{flex:none;width:64px;height:64px;border-radius:50%;background:#162526;color:#FFB400;font-weight:700;font-size:32px;display:flex;align-items:center;justify-content:center}
.mv h3{margin:4px 0 8px;font-size:38px;font-weight:700;color:#162526}
.mv p{margin:0;font-size:27px;line-height:1.35;color:#3f5552}
.mv .dd{display:flex;align-items:baseline;gap:18px;margin-top:10px;font-weight:700}
.mv .dd s{font-size:36px;color:#9aaba6}
.mv .dd em{font-style:normal;font-size:48px;color:#0f7a43}
.bx{position:absolute;left:84px;right:84px;bottom:70px;background:#162526;border-radius:28px;padding:26px 34px;color:#fff;font-size:27px;line-height:1.4}
.bx b{color:#FFB400}
"""
html = pag('<div class="t">Por que os FIIs <b>subiram tanto hoje?</b></div>'
           '<div class="mv">'
           '<div class="r"><div class="n">1</div><div><h3>Trabuco na Fazenda</h3><p>Ontem à noite o Planalto confirmou Luiz Carlos Trabuco, presidente do conselho do Bradesco, como ministro da Fazenda a partir de 2027.</p></div></div>'
           '<div class="r"><div class="n">2</div><div><h3>Mais confiança nas contas</h3><p>O mercado vê nele um nome que pode arrumar as contas públicas. Menos risco, menos juro cobrado.</p></div></div>'
           '<div class="r"><div class="n">3</div><div><h3>Juros longos despencaram</h3><p>Taxa do DI para janeiro de 2035, na abertura:</p>'
           '<div class="dd num"><s>14,51%</s><span style="color:#7b8f8a;font-size:34px">→</span><em>13,88%</em></div></div></div>'
           '</div>'
           '<div class="bx"><b>E o que isso tem a ver com FII?</b> O juro longo é o maior concorrente dos fundos imobiliários. Quando ele cai, o dividendo do FII fica mais atraente e a cota sobe.</div>', 60, CSS2)
open("h2.html", "w").write(html)

# 3. Por segmento
S = [("🏢", "Lajes corporativas", ["PVBI11", "BRCR11", "JSRE11"]), ("🛍️", "Shoppings", ["XPML11", "VISC11", "HSML11"]),
     ("📦", "Logística", ["GGRC11", "LVBI11", "VILG11"]), ("📄", "Papel (CRI)", ["CPTS11", "MXRF11", "HGCR11"])]
CSS3 = """
.sg{position:absolute;left:84px;right:84px;top:410px;border-top:3px solid #cdd9d3}
.sg .r{display:grid;grid-template-columns:1.25fr 1fr 1fr 1fr;align-items:center;height:165px;border-bottom:3px solid #cdd9d3;column-gap:14px}
.sg .nm2{font-weight:700;font-size:32px;color:#162526;line-height:1.15}
.sg .nm2 i{font-style:normal;display:block;font-size:38px;margin-bottom:4px}
.sg .c{text-align:center;background:#e3f3e9;border-radius:18px;padding:14px 0}
.sg .c b{display:block;font-size:27px;color:#162526}
.sg .c span{font-size:29px;font-weight:700;color:#0f7a43}
.ob{position:absolute;left:84px;right:84px;top:1110px;font-size:29px;line-height:1.4;color:#3f5552}
.ob b{color:#162526}
"""
rows = "".join(f'<div class="r"><div class="nm2"><i>{ic}</i>{n}</div>' + "".join(
    f'<div class="c"><b>{t}</b><span class="num">{pc(V[t])}</span></div>' for t in ts) + "</div>" for ic, n, ts in S)
html = pag('<div class="t">Subiu de tudo: <b>tijolo e papel</b></div>'
           f'<div class="sg">{rows}</div>'
           '<div class="ob">Quem mais sofreu com os juros altos foi quem mais subiu hoje: <b>lajes corporativas e shoppings</b>. '
           'Os FIIs de papel, que ganham com juro alto, subiram menos.</div>', 62, CSS3)
open("h3.html", "w").write(html)

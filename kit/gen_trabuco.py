#!/usr/bin/env python3
"""Carrossel 27/11/2026: efeito Trabuco (Ibovespa, ações, FIIs e quem é Trabuco)."""
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


pc = lambda v: ("+" if v > 0 else "") + f"{v:.2f}".replace(".", ",") + "%"

# 1. Placar
CSS1 = """
.pl{position:absolute;left:84px;right:84px;top:470px;border-top:3px solid #cdd9d3}
.pl .r{display:flex;align-items:center;justify-content:space-between;height:240px;border-bottom:3px solid #cdd9d3}
.pl .k{font-size:28px;color:#7b8f8a;font-weight:600;letter-spacing:1px}
.pl .k b{display:block;font-size:46px;color:#162526;letter-spacing:0;margin-top:4px}
.pl .k small{display:block;font-size:26px;font-weight:400;margin-top:6px}
.pl .v{font-weight:700;font-size:92px;letter-spacing:-2px;text-align:right;line-height:1}
.pl .v small{display:block;font-size:30px;letter-spacing:0;font-weight:500;color:#7b8f8a;margin-top:8px}
.up{color:#0f7a43}.dn{color:#c0392b}
"""
R = [("ONTEM (26/11)", "Ibovespa", "maior alta desde o 1º turno", "+6,07%", "176.800 pontos", "up"),
     ("HOJE (27/11)", "Ibovespa", "na máxima do dia", "+3,86%", "183.623 pontos", "up"),
     ("HOJE (27/11)", "Dólar", "na mínima do dia", "−4,60%", "R$ 5,48", "dn")]
rows = "".join(f'<div class="r"><div class="k">{a}<b>{b}</b><small>{c}</small></div><div class="v num {cl}">{v}<small>{s}</small></div></div>'
               for a, b, c, v, s, cl in R)
open("t1.html", "w").write(pag('<div class="t"><b>A bolsa disparou</b> e o dólar despencou 🚀</div>'
                               f'<div class="pl">{rows}</div>', 64, CSS1))

# 2 e 3. Barras
CSS2 = """
.bs{position:absolute;left:84px;right:84px;top:400px;display:flex;flex-direction:column;gap:22px}
.bs .r{display:flex;align-items:center;gap:22px;height:86px}
.bs .lq{flex:none;width:86px;height:86px;border-radius:18px;overflow:hidden;display:flex;align-items:center;justify-content:center;background:#162526;color:#fff;font-weight:700;font-size:19px}
.bs .lq img{width:100%;height:100%;object-fit:cover}
.bs .tk{flex:none;width:150px;font-weight:700;font-size:32px;color:#162526}
.bs .tr{flex:1;height:58px;background:#edf3ef;border-radius:14px;position:relative}
.bs .br{height:100%;border-radius:14px;background:linear-gradient(90deg,#3fae72,#0f7a43);display:flex;align-items:center;justify-content:flex-end;padding-right:16px;color:#fff;font-weight:700;font-size:28px;box-sizing:border-box;min-width:130px}
.nt{position:absolute;left:84px;right:84px;bottom:70px;font-size:24px;color:#7b8f8a}
"""


def barras(itens, logo):
    mx = max(v for _, v in itens)
    out = ""
    for t, v in itens:
        lq = f'<img src="assets/logos_b3/{t}.png">' if logo else t[:4]
        out += (f'<div class="r"><div class="lq">{lq}</div><div class="tk">{t}</div>'
                f'<div class="tr"><div class="br num" style="width:{v / mx * 100:.1f}%">{pc(v)}</div></div></div>')
    return out


A = [("HAPV3", 12.15), ("MRVE3", 10.69), ("VAMO3", 10.36), ("MGLU3", 10.26), ("COGN3", 7.10), ("YDUQ3", 6.79),
     ("B3SA3", 6.50), ("CYRE3", 6.05)]
open("t2.html", "w").write(pag('<div class="t"><b>Ações</b> que mais sobem hoje</div>'
                               f'<div class="bs">{barras(A, True)}</div>'
                               , 64, CSS2))
F = [("RZTR11", 5.73), ("PVBI11", 4.89), ("TRXF11", 4.64), ("XPML11", 3.61), ("TGAR11", 3.61), ("VISC11", 3.24),
     ("BRCR11", 3.10), ("GGRC11", 3.00)]
open("t3.html", "w").write(pag('<div class="t"><b>FIIs</b> que mais sobem hoje</div>'
                               f'<div class="bs">{barras(F, False)}</div>'
                               , 64, CSS2))

# 4. Trabuco
CSS4 = """
.cv{position:absolute;left:84px;right:84px;top:440px;display:flex;gap:34px}
.cv .tl{flex:1;position:relative;padding-left:44px}
.cv .tl:before{content:'';position:absolute;left:12px;top:16px;bottom:16px;width:4px;background:#d9e7de;border-radius:2px}
.cv .e{position:relative;margin-bottom:28px}
.cv .e:before{content:'';position:absolute;left:-45px;top:10px;width:30px;height:30px;border-radius:50%;background:#fff;border:5px solid #0f7a43;box-sizing:border-box}
.cv .e.f:before{background:#FFB400;border-color:#FFB400}
.cv .e b{display:block;font-size:40px;color:#162526}
.cv .e span{font-size:31px;color:#3f5552;line-height:1.3}
.pq{position:absolute;left:84px;right:84px;bottom:70px;background:#162526;border-radius:28px;padding:28px 34px;color:#fff}
.pq h4{margin:0 0 12px;color:#FFB400;font-size:28px;font-weight:700}
.pq p{margin:0;font-size:29px;line-height:1.4}
"""
E = [("17 anos", "Entra no Bradesco como escriturário"), ("2009 a 2018", "Presidente do Bradesco"),
     ("2018", "Presidente do conselho do banco"), ("26/11/2026", "Aceita ser ministro da Fazenda de Lula a partir de 2027")]
tl = "".join(f'<div class="e{" f" if i == 3 else ""}"><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate(E))
open("t4.html", "w").write(pag('<div class="t">O motivo: <b>Luiz Carlos Trabuco</b> na Fazenda</div>'
                               f'<div class="cv"><div class="tl">{tl}</div></div>'
                               '<div class="pq"><h4>Por que o mercado gostou?</h4><p>É um nome que o mercado conhece e confia. '
                               'A aposta é em contas públicas mais em ordem, o que derruba os juros futuros. '
                               'Juro menor ajuda as empresas, principalmente varejo, construtoras e educação, e deixa os FIIs mais atraentes.</p></div>', 60, CSS4))

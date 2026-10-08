#!/usr/bin/env python3
"""Post 'Veja quanto rende 100 MIL REAIS investidos em cada FII' (modelo branco)."""
import json, sys
from decimal import Decimal
from base import pagina, brl

CSS = """
.titulo{top:%(titulo_top)spx;font-size:%(titulo_size)spx;line-height:%(titulo_lh)spx}
.emo{font-family:"Noto Color Emoji";font-size:.8em;margin-left:.12em}
.tabela{position:absolute;left:76px;top:%(tab_top)spx;width:928px}
.cab,.lin{display:grid;grid-template-columns:%(cols)s;align-items:center;text-align:center}
.cab{font-family:"Aileron";font-weight:400;font-size:%(cab_size)spx;color:#4f4f4f;height:%(cab_h)spx;text-transform:uppercase}
.lin{height:%(lin_h)spx;border-bottom:2.5px solid #161616}
.lin:last-child{border-bottom:none}
.tk{font-family:"Poppins";font-weight:800;font-size:%(tk_size)spx;color:#161616;line-height:1}
.vl{font-family:"Poppins";font-weight:300;font-size:%(vl_size)spx;color:#1c1c1c;line-height:1}
.rod{font-size:%(rod_size)spx}
.rod.data{font-style:italic;font-size:%(data_size)spx}
"""
DEF = dict(titulo_top=330, titulo_size=52, titulo_lh=60, tab_top=506, cols="272px 312px 344px",
           cab_size=20.5, cab_h=46, lin_h=88.8, tk_size=46, vl_size=41, rod_size=23.5, data_size=25,
           data_top=1183, rod_top=1232)


def build(cfg):
    p = dict(DEF); p.update(cfg.get("ajustes", {}))
    total = Decimal(cfg["valor"])
    linhas = []
    for tk, rend, preco in cfg["fundos"]:
        mes = total / Decimal(preco) * Decimal(rend)
        linhas.append((mes, tk, Decimal(rend), Decimal(preco)))
    linhas.sort(reverse=True)
    html = "".join(
        f'<div class="lin"><span class="tk">{tk}</span><span class="vl">R$ {brl(mes)}</span><span class="vl">R$ {brl(mes * 12)}</span></div>'
        for mes, tk, rend, preco in linhas)
    rod = f'<div class="rod data" style="top:{p["data_top"]}px">{cfg["data"]}</div>' + "".join(
        f'<div class="rod" style="top:{p["rod_top"] + i * 32}px">{t}</div>' for i, t in enumerate(cfg["rodape"]))
    c = cfg["colunas"]
    corpo = f"""<div class="titulo">{cfg['titulo']}</div>
<div class="tabela"><div class="cab"><span>{c[0]}</span><span>{c[1]}</span><span>{c[2]}</span></div>{html}</div>
{rod}"""
    return pagina(CSS % p, corpo), linhas


if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    html, linhas = build(cfg)
    open(sys.argv[2], "w").write(html)
    for mes, tk, rend, preco in linhas:
        print(tk, rend, preco, brl(mes), brl(mes * 12))

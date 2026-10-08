#!/usr/bin/env python3
"""Post 'Quanto preciso investir em cada FII para receber um salário mínimo todo mês?' (modelo branco)."""
import json, sys
from decimal import Decimal
from base import pagina, brl

CSS = """
.titulo{top:%(titulo_top)spx;font-size:52px;line-height:59px}
.tabela{position:absolute;left:95px;top:%(tab_top)spx;width:890px}
.cab,.lin{display:grid;grid-template-columns:173px 236px 160px 321px;text-align:center}
.cab{font-family:"Poppins";font-weight:600;font-size:27.5px;line-height:36px;height:%(cab_h)spx}
.lin{font-family:"Aileron";font-weight:400;font-size:%(lin_size)spx;line-height:%(lin_h)spx;height:%(lin_h)spx;color:#262626;border-bottom:2.5px solid #161616}
.lin:last-child{border-bottom:none}
.lin span{display:block;transform:translateY(%(lin_dy)spx)}
.lin .dest{font-weight:700}
.rod{font-size:%(rod_size)spx}
"""
DEF = dict(titulo_top=326, tab_top=565, cab_h=44, lin_h=64, lin_size=33.7, lin_dy=1, rod_size=25, rod_top=1228)


def build(cfg):
    p = dict(DEF)
    p.update(cfg.get("ajustes", {}))
    sal = Decimal(cfg["salario"])
    linhas = []
    for tk, rend, preco in cfg["fundos"]:
        rend, preco = Decimal(rend), Decimal(preco)
        linhas.append((sal / rend * preco, tk, rend, preco))
    if cfg.get("ordenar", True):
        linhas.sort()
    html = []
    for inv, tk, rend, preco in linhas:
        html.append(
            f'<div class="lin"><span>{tk}</span><span>R$ {brl(rend)}</span><span>R$ {brl(preco)}</span>'
            f'<span class="dest">R$ {brl(inv)}</span></div>'
        )
    rod = "".join(f'<div class="rod" style="top:{p["rod_top"] + i * 34}px">{t}</div>' for i, t in enumerate(cfg["rodape"]))
    corpo = f"""<div class="titulo">{cfg['titulo']}</div>
<div class="tabela"><div class="cab">{"".join(f"<span>{c}</span>" for c in cfg.get("cabecalho", ["FII", "Últ. Rend.", "Preço", "Invest. Necessário"]))}</div>{''.join(html)}</div>
{rod}"""
    return pagina(CSS % p, corpo), linhas


if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    html, linhas = build(cfg)
    open(sys.argv[2], "w").write(html)
    for inv, tk, rend, preco in linhas:
        print(tk, rend, preco, brl(inv))

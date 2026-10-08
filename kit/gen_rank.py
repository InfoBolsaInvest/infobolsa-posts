#!/usr/bin/env python3
"""Post de ranking 'Investimentos que mais renderam' (modelo branco)."""
import json, sys
from decimal import Decimal
from base import pagina, brl

CSS = """
.titulo{top:%(titulo_top)spx;font-size:54px;line-height:62px}
.sub{position:absolute;left:102px;top:%(sub_top)spx;font-size:%(sub_size)spx;line-height:52px;font-weight:400;white-space:nowrap}
.tabela{position:absolute;left:95px;top:%(tab_top)spx;width:890px}
.cab,.lin{display:grid;grid-template-columns:74px 1fr 250px;align-items:center}
.cab{font-family:"Poppins";font-weight:600;font-size:28px;line-height:36px;height:%(cab_h)spx}
.cab .n{grid-column:1 / span 2;padding-left:14px}
.cab .v{text-align:right;padding-right:22px}
.lin{height:%(lin_h)spx;border-bottom:2.5px solid #161616;font-family:"Aileron";font-weight:400;font-size:%(lin_size)spx;color:#262626}
.lin:last-child{border-bottom:none}
.ic{display:flex;align-items:center;justify-content:center;font-family:"Noto Color Emoji";font-size:%(ic_size)spx;line-height:1;padding-left:10px}
.ic svg{width:%(ic_svg)spx;height:%(ic_svg)spx}
.nm{padding-left:6px;white-space:nowrap}
.nm small{font-size:.78em;font-weight:300;color:#4a4a4a;margin-left:.3em}
.vl{text-align:right;padding-right:22px;font-weight:700;font-size:%(val_size)spx;white-space:nowrap}
.pos{color:#12924a}
.neg{color:#d63333}
.rod{font-size:%(rod_size)spx}
"""
DEF = dict(titulo_top=334, sub_top=462, sub_size=40, tab_top=546, cab_h=46, lin_h=76, lin_size=35, val_size=37,
           ic_size=38, ic_svg=42, rod_size=24.5, rod_top=1228)

BTC = ('<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="23" fill="#f7931a"/>'
       '<text x="24.5" y="34.5" text-anchor="middle" font-family="DejaVu Sans" font-weight="700" font-size="30" fill="#fff">₿</text></svg>')


def pct(v):
    v = Decimal(v)
    s = brl(abs(v))
    return ("+" if v > 0 else "-" if v < 0 else "") + s + "%"


def build(cfg):
    p = dict(DEF)
    p.update(cfg.get("ajustes", {}))
    itens = sorted(cfg["itens"], key=lambda x: -Decimal(x[3]))
    linhas = []
    for icone, nome, detalhe, valor in itens:
        ic = BTC if icone == "btc" else icone
        det = f"<small>{detalhe}</small>" if detalhe else ""
        cls = "pos" if Decimal(valor) > 0 else "neg"
        linhas.append(
            f'<div class="lin"><span class="ic">{ic}</span><span class="nm">{nome}{det}</span>'
            f'<span class="vl {cls}">{pct(valor)}</span></div>'
        )
    rod = "".join(f'<div class="rod" style="top:{p["rod_top"] + i * 33}px">{t}</div>' for i, t in enumerate(cfg["rodape"]))
    corpo = f"""<div class="titulo">{cfg['titulo']}</div>
<div class="sub">{cfg['sub']}</div>
<div class="tabela"><div class="cab"><span class="n">{cfg['colunas'][0]}</span><span class="v">{cfg['colunas'][1]}</span></div>{''.join(linhas)}</div>
{rod}"""
    return pagina(CSS % p, corpo), itens


if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    html, itens = build(cfg)
    open(sys.argv[2], "w").write(html)
    for i in itens:
        print(i[1], pct(i[3]))

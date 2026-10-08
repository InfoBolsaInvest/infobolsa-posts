#!/usr/bin/env python3
"""Gera o HTML do post no modelo 'socio de grandes empresas' (fundo branco)."""
import json, sys
from base import BASE_CSS, CABECALHO, SCRIPT as SCRIPT_BASE

TP = "fonts/node_modules/@typopro/web-aileron/TypoPRO-Aileron-"
CSS = """
.titulo{position:absolute;left:102px;font-size:54px;line-height:62px;font-weight:400;white-space:nowrap}
.titulo b{font-weight:700}
.linha{position:absolute;left:103px;height:109px}
.quadro{position:absolute;left:0;top:0;width:109px;height:109px;border:2px solid #1a1a1a;border-radius:18px;background:#fcfdff;overflow:hidden}
.quadro img{display:block;width:105px;height:105px}
.ticker{position:absolute;left:125px;top:%(ticker_top)spx;font-family:"Aileron";font-weight:200;font-size:%(ticker_size)spx;line-height:34px;color:%(ticker_color)s;white-space:nowrap}
.preco{position:absolute;left:%(preco_left)spx;top:%(preco_top)spx;font-family:"League Spartan";font-weight:700;font-size:%(preco_size)spx;line-height:60px;color:#2f2f2f;white-space:nowrap}
.chave{position:absolute;left:%(chave_left)spx;width:70px;height:589.5px}
.total{position:absolute;left:%(total_left)spx;width:424px;text-align:center;font-family:"League Spartan";font-weight:700;font-size:%(total_size)spx;line-height:96px;color:#2f2f2f;white-space:nowrap}
.apoio{position:absolute;left:%(apoio_left)spx;width:440px;text-align:center;font-family:"Aileron";font-weight:400;font-size:%(apoio_size)spx;line-height:%(apoio_lh)spx;color:#303030}
.apoio b{font-weight:700}
.cotacoes{position:absolute;left:0;width:1080px;text-align:center;font-family:"Aileron";font-weight:300;font-size:%(cot_size)spx;line-height:36px;color:%(cot_color)s}
"""

DEFAULTS = dict(
    tp=TP, ticker_top=7.5, ticker_size=28.5, ticker_color="#3a3a3a",
    preco_left=126, preco_top=38, preco_size=54.5,
    chave_left=480, total_left=560, total_size=88,
    apoio_left=552, apoio_size=32.6, apoio_lh=36.8,
    cot_size=28, cot_color="#3d3d3d",
    # deslocamentos verticais relativos ao topo do primeiro quadro (T0)
    passo=127.6, chave_dy=13, total_dy=210, apoio_dy=316, cot_dy=726,
)



def build(cfg):
    p = dict(DEFAULTS)
    p.update(cfg.get("ajustes", {}))
    t0 = cfg["t0"]
    css = BASE_CSS + CSS % p
    rows = []
    for i, (logo, ticker, preco) in enumerate(cfg["linhas"]):
        top = round(t0 + i * p["passo"])
        rows.append(
            f'<div class="linha" style="top:{top}px"><div class="quadro"><img src="{logo if '/' in logo else f'assets/logo_{logo}.png'}" alt=""></div>'
            f'<div class="ticker">{ticker}</div><div class="preco">R$ {preco}</div></div>'
        )
    html = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><style>{css}</style></head><body>
{CABECALHO}
<div class="titulo" style="top:{cfg['titulo_top']}px">{cfg['titulo']}</div>
{''.join(rows)}
<img class="chave" style="top:{t0 + p['chave_dy']}px" src="assets/chave.png" alt="">
<div class="total" style="top:{t0 + p['total_dy']}px">R$ {cfg['total']}</div>
<div class="apoio" style="top:{t0 + p['apoio_dy']}px">{cfg['apoio']}</div>
<div class="cotacoes" style="top:{t0 + p['cot_dy']}px">Cotações do dia {cfg['data']}</div>
{SCRIPT_BASE}
</body></html>"""
    return html


if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    open(sys.argv[2], "w").write(build(cfg))

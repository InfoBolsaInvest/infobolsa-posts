#!/usr/bin/env python3
"""Gera o HTML do post 'Hoje é a data de pagamento' no modelo de fundo branco."""
import json, sys
from decimal import Decimal, ROUND_HALF_UP
from base import BASE_CSS, CABECALHO, SCRIPT as SCRIPT_BASE

TP = "fonts/node_modules/@typopro/web-aileron/TypoPRO-Aileron-"
FS = "fonts/node_modules/@fontsource/"


def brl(v, casas=2):
    """Formata Decimal no padrão brasileiro: 50600 -> 50.600,00"""
    q = Decimal(1).scaleb(-casas)
    v = Decimal(v).quantize(q, rounding=ROUND_HALF_UP)
    inteiro, _, frac = f"{v:.{casas}f}".partition(".")
    neg = inteiro.startswith("-")
    inteiro = inteiro.lstrip("-")
    grupos = []
    while len(inteiro) > 3:
        grupos.insert(0, inteiro[-3:])
        inteiro = inteiro[:-3]
    grupos.insert(0, inteiro)
    s = ".".join(grupos)
    if casas:
        s += "," + frac
    return ("-" if neg else "") + s


def milhar(n):
    return brl(Decimal(n), 0)


CSS = """
.titulo{position:absolute;left:102px;top:%(titulo_top)spx;font-size:54px;line-height:62px;font-weight:400;white-space:nowrap}
.titulo b{font-weight:700}
.sub{position:absolute;left:102px;top:%(sub_top)spx;font-size:%(sub_size)spx;line-height:52px;font-weight:400;white-space:nowrap}

.quadro{position:absolute;left:103px;top:%(bloco_top)spx;width:%(quadro)spx;height:%(quadro)spx;border:2px solid #1a1a1a;border-radius:32px;background:#fcfdff;overflow:hidden;display:flex;align-items:center;justify-content:center}
.quadro svg{width:62%%;height:62%%}
.quadro img{width:%(logo_w)s%%;height:auto}
.info{position:absolute;left:%(info_left)spx;top:%(bloco_top)spx}
.tk{font-family:"League Spartan";font-weight:700;font-size:%(tk_size)spx;line-height:%(tk_lh)spx;color:#2f2f2f;white-space:nowrap;margin-top:%(tk_mt)spx}
.itens{margin-top:%(itens_mt)spx}
.item{display:flex;align-items:center;height:%(item_h)spx;font-family:"Aileron";font-weight:400;font-size:%(item_size)spx;color:#303030;white-space:nowrap}
.item b{font-weight:700;margin-left:.28em}
.item svg{width:25px;height:25px;margin-right:13px;flex:none}

.tabela{position:absolute;left:95px;top:%(tab_top)spx;width:890px}
.cab,.lin{display:grid;grid-template-columns:%(cols)s;text-align:center}
.cab{font-family:"Poppins";font-weight:600;font-size:28px;line-height:36px;height:%(cab_h)spx}
.lin{font-family:"Aileron";font-weight:400;font-size:%(lin_size)spx;line-height:%(lin_h)spx;height:%(lin_h)spx;color:#262626;border-bottom:2.5px solid #161616;letter-spacing:.012em}
.lin:last-child{border-bottom:none}
.lin span{display:block;transform:translateY(%(lin_dy)spx)}
.lin .dest{font-weight:700}

.rod{position:absolute;left:0;width:1080px;text-align:center;font-family:"Aileron";font-weight:300;font-size:%(rod_size)spx;line-height:34px;color:#3d3d3d}
"""

DEFAULTS = dict(
    tp=TP, fs=FS, titulo_top=334, sub_top=398, sub_size=42,
    bloco_top=492, quadro=205, info_left=342,
    tk_size=62, tk_lh=62, tk_mt=4, itens_mt=2, item_h=37, item_size=28,
    tab_top=744, cab_h=50, lin_h=60, lin_size=34, lin_dy=3,
    cols="1fr 1fr 1fr", rod_size=25, rod_top=1232, logo_w=62,
)

CHECK = """<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="12" fill="#2fb457"/><path fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" d="M6.8 12.4l3.5 3.4 7-7.4"/></svg>"""


def predios(cor="#23456b"):
    """Ícone de prédios para fundos imobiliários."""
    jan = []
    for r in range(5):
        for c in range(3):
            jan.append(f'<rect x="{24 + c * 11}" y="{21 + r * 11.5}" width="6.4" height="6.4" rx="1" fill="#fcfdff"/>')
    for r in range(3):
        for c in range(2):
            jan.append(f'<rect x="{65.5 + c * 9.5}" y="{47 + r * 11.5}" width="5.6" height="5.6" rx="1" fill="#fcfdff"/>')
    return (
        f'<svg viewBox="0 0 100 100" aria-hidden="true">'
        f'<rect x="17" y="13" width="41" height="73" rx="3" fill="{cor}"/>'
        f'<rect x="60.5" y="39" width="24" height="47" rx="3" fill="{cor}"/>'
        f'{"".join(jan)}'
        f'<rect x="33.5" y="77" width="8" height="9" rx="1" fill="#fcfdff"/>'
        f'<rect x="9" y="86" width="82" height="4.5" rx="2.2" fill="{cor}"/>'
        f"</svg>"
    )


def build(cfg):
    p = dict(DEFAULTS)
    p.update(cfg.get("ajustes", {}))
    css = BASE_CSS + CSS % p
    valor = Decimal(cfg["valor_por_cota"])
    cot = Decimal(cfg["cotacao"])
    linhas = []
    for q in cfg["quantidades"]:
        linhas.append(
            f'<div class="lin"><span>{milhar(q)}</span><span class="dest">R$ {brl(valor * q)}</span><span>R$ {brl(cot * q)}</span></div>'
        )
    itens = "".join(f'<div class="item">{CHECK}{rot}<b>{val}</b></div>' for rot, val in cfg["itens"])
    quadro = f'<img src="{cfg["logo"]}" alt="">' if cfg.get("logo") else predios()
    rod = "".join(
        f'<div class="rod" style="top:{p["rod_top"] + i * 34}px">{t}</div>' for i, t in enumerate(cfg["rodape"])
    )
    cab = "".join(f"<span>{c}</span>" for c in cfg["colunas"])
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><style>{css}</style></head><body>
{CABECALHO}
<div class="titulo">{cfg['titulo']}</div>
<div class="sub">{cfg['sub']}</div>
<div class="quadro">{quadro}</div>
<div class="info"><div class="tk">{cfg['ticker']}</div><div class="itens">{itens}</div></div>
<div class="tabela"><div class="cab">{cab}</div>{''.join(linhas)}</div>
{rod}
{SCRIPT_BASE}
</body></html>"""


if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    open(sys.argv[2], "w").write(build(cfg))

#!/usr/bin/env python3
"""Post 'Os primeiros R$ 100 mil são os mais difíceis': tempo para juntar cada R$ 100 mil (modelo branco)."""
import json, sys
from decimal import Decimal
from base import pagina, brl

CSS = """
.titulo{top:%(titulo_top)spx;font-size:%(titulo_size)spx;line-height:%(titulo_lh)spx}
.sub{position:absolute;left:102px;top:%(sub_top)spx;font-family:"Aileron";font-weight:400;font-size:%(sub_size)spx;line-height:%(sub_lh)spx;color:#262626;white-space:nowrap}
.sub b{font-weight:700}
.barras{position:absolute;left:103px;top:%(bar_top)spx;width:882px}
.b{display:flex;align-items:center;height:%(lin_h)spx}
.rot{width:%(rot_w)spx;font-family:"Poppins";font-weight:600;font-size:%(rot_size)spx;color:#161616;white-space:nowrap}
.rot small{font-weight:400;font-size:.82em;color:#3a3a3a}
.bar{height:%(bar_h)spx;border:2px solid #161616;border-radius:7px;background:%(cor)s;flex:none}
.b.um .bar{background:%(cor1)s}
.tmp{margin-left:14px;font-family:"Aileron";font-weight:700;font-size:%(tmp_size)spx;color:#161616;white-space:nowrap}
.fim{position:absolute;left:0;width:1080px;top:%(fim_top)spx;text-align:center;font-family:"Aileron";font-weight:400;font-size:%(fim_size)spx;line-height:38px;color:#1c1c1c}
.fim b{font-weight:700}
.rod{font-size:%(rod_size)spx}
"""
DEF = dict(titulo_top=330, titulo_size=54, titulo_lh=62, sub_top=474, sub_size=31, sub_lh=40,
           bar_top=578, lin_h=54.5, rot_w=250, rot_size=27.5, bar_h=34, bar_max=330, tmp_size=27.5,
           cor="#ffc629", cor1="#ff8a3c", fim_top=1140, fim_size=29.5, rod_size=22.5, rod_top=1236)


def meses_txt(m):
    a, r = divmod(m, 12)
    pa = f"{a} ano" + ("s" if a > 1 else "") if a else ""
    pr = f"{r} " + ("meses" if r != 1 else "mês") if r else ""
    return " e ".join(x for x in (pa, pr) if x)


def simular(aporte, taxa, alvo, n):
    """Mês em que o saldo passa de cada múltiplo de 'alvo' (aporte no fim de cada mês)."""
    saldo, mes, marcos = Decimal(0), 0, []
    while len(marcos) < n:
        mes += 1
        saldo = saldo * (1 + taxa) + aporte
        if saldo >= alvo * (len(marcos) + 1):
            marcos.append(mes)
    return marcos


def build(cfg):
    p = dict(DEF); p.update(cfg.get("ajustes", {}))
    aporte, taxa, alvo, n = Decimal(cfg["aporte"]), Decimal(cfg["taxa_mes"]) / 100, Decimal(cfg["alvo"]), cfg["marcos"]
    marcos = simular(aporte, taxa, alvo, n)
    passos = [marcos[0]] + [marcos[i] - marcos[i - 1] for i in range(1, n)]
    mx = max(passos)
    linhas = ""
    for i, m in enumerate(passos):
        w = max(18, round(p["bar_max"] * m / mx))
        linhas += (f'<div class="b{" um" if i == 0 else ""}"><div class="rot">{i + 1}º <small>R$ 100 mil</small></div>'
                   f'<div class="bar" style="width:{w}px"></div><div class="tmp">{meses_txt(m)}</div></div>')
    total = marcos[-1]
    fim = cfg["fim"].format(total=meses_txt(total), aportes=brl(aporte * total, 0), final=brl(alvo * n, 0))
    rod = "".join(f'<div class="rod" style="top:{p["rod_top"] + i * 31}px">{t}</div>' for i, t in enumerate(cfg["rodape"]))
    corpo = f"""<div class="titulo">{cfg['titulo']}</div>
<div class="sub">{cfg['sub']}</div>
<div class="barras">{linhas}</div>
<div class="fim">{fim}</div>
{rod}"""
    return pagina(CSS % p, corpo), marcos, passos


if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    html, marcos, passos = build(cfg)
    open(sys.argv[2], "w").write(html)
    print("marcos (mês acumulado):", marcos)
    print("passos:", passos, [meses_txt(m) for m in passos], "total", meses_txt(marcos[-1]))

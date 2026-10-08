#!/usr/bin/env python3
"""Post comparativo entre duas empresas (ex.: Banco do Brasil x Nubank), modelo branco."""
import json, sys
from base import pagina

CSS = """
.titulo{top:%(titulo_top)spx;font-size:%(titulo_size)spx;line-height:62px}
.sub{position:absolute;left:102px;top:%(sub_top)spx;font-size:%(sub_size)spx;line-height:50px;font-weight:400;white-space:nowrap}
.vs{position:absolute;left:95px;top:%(tab_top)spx;width:890px}
.row{display:grid;grid-template-columns:%(cols)s;align-items:center}
.head{height:%(head_h)spx}
.emp{display:flex;flex-direction:column;align-items:center;gap:%(emp_gap)spx}
.quad{width:%(quad)spx;height:%(quad)spx;border-radius:24px;display:flex;align-items:center;justify-content:center;overflow:hidden;border:2px solid #1a1a1a}
.quad img{display:block}
.nm{font-family:"Poppins";font-weight:700;font-size:%(nm_size)spx;line-height:34px;color:#161616;white-space:nowrap}
.lin{height:%(lin_h)spx;border-top:2.5px solid #161616}
.lab{font-family:"Aileron";font-weight:700;font-size:%(lab_size)spx;line-height:1.16;color:#161616;padding-left:4px}
.lab small{display:block;font-weight:400;font-size:%(lab_small)spx;color:#4f4f4f;margin-top:3px}
.cel{justify-self:center;width:%(cel_w)spx;height:%(cel_h)spx;border-radius:12px;background:#ececec;display:flex;align-items:center;justify-content:center;font-family:"Aileron";font-weight:700;font-size:%(val_size)spx;color:#161616;white-space:nowrap}
.cel.pos{color:#12924a}
.cel.neg{color:#d63333}
.vl{position:absolute;top:0;height:%(vl_h)spx;width:2.5px;background:#161616}
.rod{font-size:%(rod_size)spx}
"""
DEF = dict(titulo_top=334, titulo_size=54, sub_top=398, sub_size=39, tab_top=486, cols="282px 304px 304px",
           head_h=196, emp_gap=12, quad=118, nm_size=27, lin_h=103, lab_size=27.5, lab_small=20.5,
           cel_w=268, cel_h=74, val_size=37, rod_size=23, rod_top=1228)


def build(cfg):
    p = dict(DEF); p.update(cfg.get("ajustes", {}))
    n = len(cfg["linhas"])
    p["vl_h"] = p["head_h"] + n * p["lin_h"]
    a, b = cfg["empresas"]
    def emp(e):
        return (f'<div class="emp"><div class="quad" style="background:{e.get("fundo", "#fcfdff")}">'
                f'<img src="{e["logo"]}" style="width:{e.get("logo_w", 70)}%" alt=""></div><div class="nm">{e["nome"]}</div></div>')
    linhas = ""
    for rot, det, va, vb, *cls in cfg["linhas"]:
        ca, cb = (cls + ["", ""])[:2]
        small = f"<small>{det}</small>" if det else ""
        linhas += (f'<div class="row lin"><div class="lab">{rot}{small}</div>'
                   f'<div class="cel {ca}">{va}</div><div class="cel {cb}">{vb}</div></div>')
    cols = [float(c.replace("px", "")) for c in p["cols"].split()]
    vls = f'<div class="vl" style="left:{cols[0]}px"></div><div class="vl" style="left:{cols[0] + cols[1]}px"></div>'
    rod = "".join(f'<div class="rod" style="top:{p["rod_top"] + i * 31}px">{t}</div>' for i, t in enumerate(cfg["rodape"]))
    corpo = f"""<div class="titulo">{cfg['titulo']}</div>
<div class="sub">{cfg['sub']}</div>
<div class="vs">{vls}<div class="row head"><div></div>{emp(a)}{emp(b)}</div>{linhas}</div>
{rod}"""
    return pagina(CSS % p, corpo)


if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    open(sys.argv[2], "w").write(build(cfg))

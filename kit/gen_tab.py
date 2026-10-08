#!/usr/bin/env python3
"""Tabela genérica no modelo branco (estilo do post '100 mil em FIIs').
cfg: titulo, sub (opcional), colunas [..], linhas [[c1, c2, ...]] (strings já formatadas; c1 pode ter <small>),
destaque (índice da coluna em negrito, opcional), fim (frase abaixo da tabela, opcional), data (itálico, opcional), rodape [..]."""
import json, sys
from base import pagina

CSS = """
.titulo{top:%(titulo_top)spx;font-size:%(titulo_size)spx;line-height:%(titulo_lh)spx}
.titulo .emo,.fim .emo{font-family:"Noto Color Emoji";font-size:.8em;margin-left:.12em}
.sub{position:absolute;left:102px;top:%(sub_top)spx;font-family:"Aileron";font-weight:400;font-size:%(sub_size)spx;line-height:%(sub_lh)spx;color:#262626;white-space:nowrap}
.sub b{font-weight:700}
.tabela{position:absolute;left:76px;top:%(tab_top)spx;width:928px}
.cab,.lin{display:grid;grid-template-columns:%(cols)s;align-items:center;text-align:center}
.cab{font-family:"Aileron";font-weight:400;font-size:%(cab_size)spx;line-height:24px;color:#4f4f4f;min-height:%(cab_h)spx;text-transform:uppercase}
.lin{height:%(lin_h)spx;border-bottom:2.5px solid #161616}
.lin:last-child{border-bottom:none}
.lin>span{white-space:nowrap}
.tk{font-family:"Poppins";font-weight:800;font-size:%(tk_size)spx;color:#161616;line-height:1.05}
.tk small{display:block;font-family:"Aileron";font-weight:400;font-size:%(tk_small)spx;color:#4a4a4a;margin-top:4px;letter-spacing:0}
.vl{font-family:"Poppins";font-weight:300;font-size:%(vl_size)spx;color:#1c1c1c;line-height:1.05}
.vl small{display:block;font-family:"Aileron";font-size:%(tk_small)spx;color:#4a4a4a;margin-top:4px}
.vl.b{font-weight:700}
.pos{color:#12924a}.neg{color:#d63333}
.fim{position:absolute;left:0;width:1080px;top:%(fim_top)spx;text-align:center;font-family:"Aileron";font-weight:400;font-size:%(fim_size)spx;line-height:38px;color:#1c1c1c}
.fim b{font-weight:700}
.rod{font-size:%(rod_size)spx}
.rod.data{font-style:italic;font-size:%(data_size)spx}
"""
DEF = dict(titulo_top=330, titulo_size=52, titulo_lh=60, sub_top=468, sub_size=31, sub_lh=40, tab_top=506,
           cols="272px 312px 344px", cab_size=20.5, cab_h=46, lin_h=88.8, tk_size=44, tk_small=20, vl_size=39,
           fim_top=1120, fim_size=29, rod_size=23.5, data_size=25, data_top=1183, rod_top=1232)


def build(cfg):
    p = dict(DEF); p.update(cfg.get("ajustes", {}))
    dest = cfg.get("destaque")
    linhas = ""
    for row in cfg["linhas"]:
        cel = [f'<span class="tk">{row[0]}</span>']
        for j, v in enumerate(row[1:], 1):
            cls = "vl b" if j == dest else "vl"
            cel.append(f'<span class="{cls}">{v}</span>')
        linhas += f'<div class="lin">{"".join(cel)}</div>'
    cab = "".join(f"<span>{c}</span>" for c in cfg["colunas"])
    extra = ""
    if cfg.get("sub"):
        extra += f'<div class="sub">{cfg["sub"]}</div>'
    if cfg.get("fim"):
        extra += f'<div class="fim">{cfg["fim"]}</div>'
    if cfg.get("data"):
        extra += f'<div class="rod data" style="top:{p["data_top"]}px">{cfg["data"]}</div>'
    rod = "".join(f'<div class="rod" style="top:{p["rod_top"] + i * 32}px">{t}</div>' for i, t in enumerate(cfg["rodape"]))
    corpo = f"""<div class="titulo">{cfg['titulo']}</div>{extra}
<div class="tabela"><div class="cab">{cab}</div>{linhas}</div>
{rod}"""
    return pagina(CSS % p, corpo)


if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    open(sys.argv[2], "w").write(build(cfg))

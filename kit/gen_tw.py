#!/usr/bin/env python3
"""Post estilo Twitter (fundo branco liso, só cabeçalho + título + conteúdo).
Uso: python3 gen_tw.py grade config.json saida.html
grade: titulo, itens [{logo, fundo, valor, det, emoji}], cols"""
import json, sys
from gen_inst import CSS, FS, SELO, SCRIPT, curva

EXTRA = """
body{background:linear-gradient(172deg,#ffffff 0%,#ffffff 58%,#eef6f1 100%)!important}
.luz{position:absolute;inset:0;background:radial-gradient(ellipse 760px 620px at 100% 100%,rgba(15,122,67,.07),transparent 70%)}
.tw-t:after{content:'';display:block;width:110px;height:7px;border-radius:4px;background:#FFB400;margin-top:22px}
.cab{top:70px}
.tw-t{position:absolute;left:96px;right:96px;top:260px;font-weight:700;font-size:var(--ts,76px);line-height:1.08;letter-spacing:-1.5px;color:#162526}
.gr{position:absolute;left:70px;right:70px;display:grid;row-gap:26px;column-gap:26px}
.it{display:flex;flex-direction:column;align-items:center;text-align:center;background:#fff;border:1.5px solid #e3ece7;border-radius:30px;padding:24px 10px 22px;box-shadow:0 10px 26px rgba(22,37,38,.05)}
.lq{width:128px;height:128px;border-radius:30px;display:flex;align-items:center;justify-content:center;overflow:hidden;margin-bottom:14px}
.lq img{width:68%;height:68%;object-fit:contain}
.lq.em{font-size:112px;line-height:1}
.it .v{font-weight:700;font-size:50px;letter-spacing:-1px;color:#162526;line-height:1.1}
.it .d{font-size:25px;color:#3f5552;line-height:1.3;margin-top:4px}
"""

def grade(c):
    it = ""
    for x in c["itens"]:
        lq = (f'<div class="lq em">{x["emoji"]}</div>' if x.get("emoji")
              else f'<div class="lq" style="background:{x["fundo"]}"><img src="{x["logo"]}"></div>')
        it += f'<div class="it">{lq}<div class="v num">{x["valor"]}</div><div class="d">{x.get("det", "")}</div></div>'
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS.replace('FS/', FS)}{EXTRA}</style></head>
<body style="--fg:#162526;--sub:#3f5552;--foto:#162526;--ts:{c.get("tsize", 76)}px"><div class="luz"></div>{curva("branco")}
<div class="cab"><div class="ft"><img src="assets/foto.png" alt=""></div>
<div><div class="nm">Douglas Medeiros {SELO}</div><div class="ar">@infobolsainvestimentos</div></div></div>
<div class="tw-t">{c["titulo"]}</div>
<div class="gr" style="top:{c.get("top", 420)}px;grid-template-columns:repeat({c.get("cols", 3)},1fr)">{it}</div>
<div style="position:absolute;left:96px;right:96px;bottom:52px;text-align:center;font-size:22px;line-height:1.45;color:#7b8f8a">{c.get("nota", "")}</div>
{SCRIPT}</body></html>"""

CSS_VS = """
.vh{position:absolute;left:96px;right:96px;display:grid;grid-template-columns:1fr 1.1fr 1fr;align-items:center;text-align:center}
.vh .lg{width:150px;height:150px;border-radius:34px;overflow:hidden;margin:0 auto}
.vh .lg img{width:100%;height:100%;object-fit:contain}
.vh .vs{font-weight:700;font-size:64px;color:#0f7a43;font-style:italic}
.vr{position:absolute;left:96px;right:96px;display:flex;flex-direction:column}
.vr .ln{display:grid;grid-template-columns:1fr 1.1fr 1fr;align-items:center;text-align:center;height:var(--lh,116px);border-bottom:2px solid #d9e7de}
.vr .ln:nth-child(odd){background:#f3f8f5;border-radius:22px}
.vr .ln:last-child{border-bottom:none}
.vr .x{font-weight:700;font-size:46px;color:#162526}
.vr .l{font-weight:600;font-size:28px;color:#3f5552;line-height:1.2}
.rk{position:absolute;left:96px;right:96px;display:flex;flex-direction:column}
.rw{display:flex;align-items:center;gap:28px;height:var(--rh,150px);border-bottom:2px solid #d9e7de;padding:0 26px}
.rw:nth-child(odd){background:#f3f8f5;border-radius:22px}
.rw:last-child{border-bottom:none}
.rw .ps{font-weight:700;font-size:30px;color:#0f7a43;width:66px;height:66px;border-radius:50%;background:#e2f0e8;display:flex;align-items:center;justify-content:center;flex:none}
.rw:first-child .ps{background:#FFB400;color:#162526}
.rw .lq{width:104px;height:104px;border-radius:24px;overflow:hidden;flex:none}
.rw .lq img{width:100%;height:100%;object-fit:contain}
.rw .tk{flex:1;font-weight:700;font-size:46px;line-height:1.1;color:#162526;display:flex;flex-direction:column;align-items:flex-start}
.rw .tk small{display:block;font-size:24px;font-weight:400;color:#7b8f8a;margin-top:4px}
.rw .v{font-weight:700;font-size:44px;color:#0f7a43;white-space:nowrap}
"""


def _pag(c, corpo):
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS.replace('FS/', FS)}{EXTRA}{CSS_VS}</style></head>
<body style="--fg:#162526;--sub:#3f5552;--foto:#162526;--ts:{c.get("tsize", 76)}px"><div class="luz"></div>{curva("branco")}
<div class="cab"><div class="ft"><img src="assets/foto.png" alt=""></div>
<div><div class="nm">Douglas Medeiros {SELO}</div><div class="ar">@infobolsainvestimentos</div></div></div>
<div class="tw-t">{c["titulo"]}</div>{corpo}{SCRIPT}</body></html>"""


def vs(c):
    a, b = c["empresas"]
    lg = lambda e: f'<div class="lg" style="background:{e.get("fundo", "#fff")}"><img src="{e["logo"]}"></div>'
    top = c.get("top", 400)
    h = f'<div class="vh" style="top:{top}px">{lg(a)}<div class="vs">VS</div>{lg(b)}</div>'
    rows = "".join(f'<div class="ln"><div class="x num">{x}</div><div class="l">{l}</div><div class="x num">{y}</div></div>' for l, x, y in c["linhas"])
    return _pag(c, h + f'<div class="vr" style="top:{top + 180}px;--lh:{c.get("lh", 116)}px">{rows}</div>')


def ranking(c):
    rows = "".join(f'<div class="rw"><div class="ps">{x["pos"]}º</div><div class="lq"><img src="{x["logo"]}"></div>'
                   f'<div class="tk">{x["tk"]}<small>{x.get("det", "")}</small></div><div class="v num">{x["valor"]}</div></div>' for x in c["itens"])
    return _pag(c, f'<div class="rk" style="top:{c.get("top", 430)}px;--rh:{c.get("rh", 150)}px">{rows}</div>')


if __name__ == "__main__":
    tipo, cfg, out = sys.argv[1:4]
    c = json.load(open(cfg))
    open(out, "w").write({"grade": grade, "vs": vs, "ranking": ranking}[tipo](c))

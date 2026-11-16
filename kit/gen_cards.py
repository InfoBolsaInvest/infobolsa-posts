#!/usr/bin/env python3
"""Posts em cards. Uso: python3 gen_cards.py grade|ranking config.json saida.html
grade: cfg titulo, sub, itens [{logo, fundo, nome, valor, det, destaque}], cols, top, rodape
ranking: cfg titulo, sub, itens [{pos, logo, fundo, tk, det, valor}], top, rodape"""
import json, sys
from gen_inst import pagina

CSS = """<style>
.gd{position:absolute;left:96px;right:96px;display:grid;gap:22px}
.cd{background:#fff;border:1.5px solid var(--borda);border-radius:26px;box-shadow:0 12px 30px rgba(22,37,38,.06);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:26px 14px;text-align:center}
.cd.dst{border:3px solid var(--dot)}
.cd .lq{width:110px;height:110px;border-radius:26px;display:flex;align-items:center;justify-content:center;overflow:hidden;margin-bottom:16px}
.cd .lq img{width:70%;height:70%;object-fit:contain}
.cd .lq.full img{width:100%;height:100%}
.cd .nm{font-size:24px;font-weight:500;color:var(--sub)}
.cd .vl{font-size:50px;font-weight:700;letter-spacing:-1px;line-height:1.15;margin-top:4px}
.cd .dt{font-size:22px;color:var(--mute);margin-top:2px}
.rk{position:absolute;left:96px;right:96px;display:flex;flex-direction:column;gap:18px}
.rw{display:flex;align-items:center;gap:26px;background:#fff;border:1.5px solid var(--borda);border-radius:24px;padding:0 34px;height:var(--rh,128px);box-shadow:0 10px 26px rgba(22,37,38,.05)}
.rw .ps{width:58px;height:58px;border-radius:50%;background:var(--chip);color:var(--acc);font-weight:700;font-size:28px;display:flex;align-items:center;justify-content:center;flex:none}
.rw.p1 .ps{background:#FFB400;color:#162526}
.rw .lq{width:96px;height:96px;border-radius:20px;overflow:hidden;flex:none}
.rw .lq img{width:100%;height:100%;object-fit:contain}
.rw .tk{flex:1;font-size:42px;font-weight:700;line-height:1.1;display:flex;flex-direction:column;align-items:flex-start}
.rw .tk small{display:block;font-size:23px;margin-top:4px;font-weight:400;color:var(--mute)}
.rw .vl{font-size:44px;font-weight:700;color:var(--acc);white-space:nowrap}
</style>"""

def grade(c):
    cols = c.get("cols", 3)
    it = ""
    for x in c["itens"]:
        full = " full" if x.get("full") else ""
        it += (f'<div class="cd{" dst" if x.get("destaque") else ""}"><div class="lq{full}" style="background:{x.get("fundo", "#fff")}"><img src="{x["logo"]}"></div>'
               f'<div class="nm">{x["nome"]}</div><div class="vl num">{x["valor"]}</div><div class="dt">{x.get("det", "")}</div></div>')
    corpo = CSS + f'<div class="gd" style="top:{c.get("top", 440)}px;grid-template-columns:repeat({cols},1fr);grid-auto-rows:{c.get("ch", 330)}px">{it}</div>'
    if c.get("fim"):
        corpo += f'<div style="position:absolute;left:96px;right:96px;top:{c["fim_top"]}px;text-align:center;font-size:26px;line-height:1.35;color:var(--sub)">{c["fim"]}</div>'
    return pagina("verde", c["titulo"], c.get("sub", ""), corpo, c["rodape"], tsize=c.get("tsize", 72))

def ranking(c):
    it = ""
    for x in c["itens"]:
        it += (f'<div class="rw{" p1" if x["pos"] == 1 else ""}"><div class="ps">{x["pos"]}º</div><div class="lq" style="background:{x.get("fundo", "#fff")}"><img src="{x["logo"]}"></div>'
               f'<div class="tk">{x["tk"]}<small>{x.get("det", "")}</small></div><div class="vl num">{x["valor"]}</div></div>')
    corpo = CSS + f'<div class="rk" style="top:{c.get("top", 440)}px;--rh:{c.get("rh", 128)}px">{it}</div>'
    return pagina("verde", c["titulo"], c.get("sub", ""), corpo, c["rodape"], tsize=c.get("tsize", 72))

if __name__ == "__main__":
    tipo, cfg, out = sys.argv[1:4]
    c = json.load(open(cfg))
    open(out, "w").write({"grade": grade, "ranking": ranking}[tipo](c))

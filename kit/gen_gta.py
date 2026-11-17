#!/usr/bin/env python3
"""Carrossel 'antes x depois' (ex.: GTA V 2013 x GTA VI 2026), uma ação por slide.
Uso: python3 gen_gta.py config.json prefixo  -> prefixo-1.html (capa), prefixo-2.html...
cfg: capa_titulo, capa_sub, rot_a, ano_a, rot_b, ano_b, itens [{tk,nome,logo,a,b,var}], nota"""
import json, sys
from gen_inst import CSS, FS, SELO, SCRIPT

EX = """
body{background:#fff!important}
.q{position:absolute;display:flex;flex-direction:column;justify-content:center}
.esq{left:0;width:540px;padding:0 50px;align-items:center;text-align:center}
.esq img{width:380px;height:300px;object-fit:contain;filter:drop-shadow(0 8px 18px rgba(0,0,0,.15))}
.esq .r{font-weight:700;font-size:96px;line-height:1;letter-spacing:-2px}
.esq .a{font-weight:600;font-size:44px;margin-top:14px;opacity:.85}
.esq .s{font-size:24px;margin-top:10px;opacity:.7}
.cima.esq{top:var(--t0,0px);height:var(--hh,675px);background:#fff;color:#162526}
.baixo.esq{top:calc(var(--t0,0px) + var(--hh,675px));height:var(--hh,675px);background:#fff;color:#162526}
.dir{left:540px;width:540px;padding:0 50px;align-items:flex-start}
.cima.dir{top:var(--t0,0px);height:var(--hh,675px);background:#f4f7f5}
.baixo.dir{top:calc(var(--t0,0px) + var(--hh,675px));height:var(--hh,675px);background:#f4f7f5}
.dir .lg{display:flex;align-items:center;gap:22px}
.dir .lg img{width:96px;height:96px;border-radius:26px;object-fit:contain}
.dir .tk{font-weight:700;font-size:46px;color:#162526;line-height:1}
.dir .nm{font-size:26px;color:#7b8f8a;margin-top:6px}
.dir .p{font-weight:700;font-size:100px;letter-spacing:-3px;color:#162526;margin-top:30px;line-height:1}
.dir .p small{font-size:56px;letter-spacing:0;margin-right:8px;font-weight:600}
.dir .v{margin-top:24px;font-weight:700;font-size:40px;padding:10px 24px;border-radius:40px}
.up{background:#e2f0e8;color:#0f7a43}.dn{background:#f8e1de;color:#c0392b}
.div{position:absolute;left:0;right:0;top:calc(var(--t0,0px) + var(--hh,675px) - 3px);height:6px;background:#FFB400}
.rod{position:absolute;left:auto;right:40px;top:auto;bottom:26px;font-size:22px;color:#7b8f8a}
.cap{position:absolute;inset:0;background:linear-gradient(172deg,#fff 0%,#fff 58%,#eef6f1 100%)}
.cap .t{position:absolute;left:96px;right:96px;top:300px;font-weight:700;font-size:88px;line-height:1.05;letter-spacing:-2px;color:#162526}
.cap .t span{color:#0f7a43}
.cap .t:after{content:'';display:block;width:120px;height:8px;border-radius:4px;background:#FFB400;margin-top:30px}
.cap .s{position:absolute;left:96px;right:96px;top:760px;font-size:36px;line-height:1.35;color:#3f5552}
.cap .arr{position:absolute;right:96px;bottom:90px;font-weight:600;font-size:30px;color:#0f7a43}
"""

TOPO = """<style>.tt{position:absolute;left:0;right:0;top:0;height:230px;background:#162526;display:flex;align-items:center;padding:0 60px;color:#fff;font-weight:700;font-size:62px;line-height:1.08;letter-spacing:-1.5px}.tt span{color:#FFB400}
.esq img{width:340px!important;height:250px!important}</style>"""


def pag(body):
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS.replace('FS/', FS)}{EX}</style></head>
<body style="--fg:#162526;--sub:#3f5552;--foto:#162526">{body}{SCRIPT}</body></html>"""

def capa(c):
    return pag(f"""<div class="cap"><div class="cab"><div class="ft"><img src="assets/foto.png" alt=""></div>
<div><div class="nm">Douglas Medeiros {SELO}</div><div class="ar">@infobolsainvestimentos</div></div></div>
<div class="t">{c["capa_titulo"]}</div><div class="s">{c["capa_sub"]}</div><div class="arr">Arrasta pro lado →</div></div>""")

def slide(c, x, topo=False):
    lg = f'<div class="lg"><img src="{x["logo"]}"><div><div class="tk">{x["tk"]}</div><div class="nm">{x["nome"]}</div></div></div>'
    cls = "dn" if x["var"].startswith("-") else "up"
    pr = lambda v: f'<div class="p num"><small>R$</small>{v}</div>'
    pre = (TOPO + f'<div class="tt"><div>{c["titulo"]}</div></div>') if topo else ""
    st = '<style>body{--t0:230px;--hh:560px}</style>' if topo else ""
    return pag(st + pre + f"""<div class="q cima esq"><img src="{c["logo_a"]}"><div class="a">{c["ano_a"]}</div></div>
<div class="q cima dir">{lg}{pr(x["a"])}</div>
<div class="q baixo esq"><img src="{c["logo_b"]}"><div class="a">{c["ano_b"]}</div></div>
<div class="q baixo dir">{lg}{pr(x["b"])}<div class="v num {cls}">{x["var"]}</div></div>
<div class="div"></div><div class="rod">@infobolsainvestimentos</div>""")

if __name__ == "__main__":
    cfg, pre = sys.argv[1:3]
    c = json.load(open(cfg))
    for i, x in enumerate(c["itens"], 1):
        open(f"{pre}-{i}.html", "w").write(slide(c, x, topo=(i == 1)))

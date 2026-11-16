#!/usr/bin/env python3
"""Post estilo Twitter (fundo branco liso, só cabeçalho + título + conteúdo).
Uso: python3 gen_tw.py grade config.json saida.html
grade: titulo, itens [{logo, fundo, valor, det, emoji}], cols"""
import json, sys
from gen_inst import CSS, FS, SELO, SCRIPT

EXTRA = """
body{background:#ffffff!important}
.cab{top:70px}
.tw-t{position:absolute;left:96px;right:96px;top:260px;font-weight:700;font-size:var(--ts,76px);line-height:1.08;letter-spacing:-1.5px;color:#162526}
.gr{position:absolute;left:70px;right:70px;display:grid;row-gap:60px}
.it{display:flex;flex-direction:column;align-items:center;text-align:center}
.lq{width:170px;height:170px;border-radius:38px;display:flex;align-items:center;justify-content:center;overflow:hidden;margin-bottom:22px}
.lq img{width:68%;height:68%;object-fit:contain}
.lq.em{font-size:150px;line-height:1}
.it .v{font-weight:700;font-size:54px;letter-spacing:-1px;color:#162526;line-height:1.1}
.it .d{font-size:28px;color:#3f5552;line-height:1.3;margin-top:4px}
"""

def grade(c):
    it = ""
    for x in c["itens"]:
        lq = (f'<div class="lq em">{x["emoji"]}</div>' if x.get("emoji")
              else f'<div class="lq" style="background:{x["fundo"]}"><img src="{x["logo"]}"></div>')
        it += f'<div class="it">{lq}<div class="v num">{x["valor"]}</div><div class="d">{x.get("det", "")}</div></div>'
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS.replace('FS/', FS)}{EXTRA}</style></head>
<body style="--fg:#162526;--sub:#3f5552;--foto:#162526;--ts:{c.get("tsize", 76)}px">
<div class="cab"><div class="ft"><img src="assets/foto.png" alt=""></div>
<div><div class="nm">Douglas Medeiros {SELO}</div><div class="ar">@infobolsainvestimentos</div></div></div>
<div class="tw-t">{c["titulo"]}</div>
<div class="gr" style="top:{c.get("top", 420)}px;grid-template-columns:repeat({c.get("cols", 3)},1fr)">{it}</div>
{SCRIPT}</body></html>"""

if __name__ == "__main__":
    tipo, cfg, out = sys.argv[1:4]
    c = json.load(open(cfg))
    open(out, "w").write({"grade": grade}[tipo](c))

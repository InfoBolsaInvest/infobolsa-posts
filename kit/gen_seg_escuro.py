#!/usr/bin/env python3
"""Post escuro 'N segmentos' (foto de fundo, uma linha por segmento com foto e logo do fundo). Uso: python3 gen_seg_escuro.py config.json saida.html
cfg: fundo, titulo1, titulo2 (amarelo), sub, linhas [[segmento, pilula, foto, logo, ticker, dy, logo_fundo?]], fecho, rodape [linhas]"""
import json, sys
from gen_escuro import CSS as _C, SELO, SCRIPT, cor_logo

CSS = """
@font-face{font-family:"Anton";src:url("fonts/node_modules/@fontsource/anton/files/anton-latin-400-normal.woff2")}
@font-face{font-family:"Poppins";font-weight:400;src:url("fonts/sistema/Poppins-Regular.ttf")}
@font-face{font-family:"Poppins";font-weight:500;src:url("fonts/node_modules/@fontsource/poppins/files/poppins-latin-500-normal.woff2")}
@font-face{font-family:"Poppins";font-weight:600;src:url("fonts/node_modules/@fontsource/poppins/files/poppins-latin-600-normal.woff2")}
@font-face{font-family:"Poppins";font-weight:700;src:url("fonts/sistema/Poppins-Bold.ttf")}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden;background:#05070b}
body{position:relative;font-family:"Poppins",sans-serif;color:#fff;-webkit-font-smoothing:antialiased}
.bg{position:absolute;inset:0;background-size:cover;background-position:50% 40%}
.sombra{position:absolute;inset:0;background:linear-gradient(180deg,rgba(4,10,9,.88) 0%,rgba(4,10,9,.80) 45%,rgba(4,10,9,.93) 100%)}
.luz{position:absolute;inset:0;background:radial-gradient(ellipse 700px 600px at 100% 0%,rgba(15,122,67,.35),transparent 70%)}
.cab{position:absolute;top:50px;left:0;width:1080px;display:flex;justify-content:center;align-items:center;gap:18px}
.cab .ft{width:78px;height:78px;border-radius:50%;overflow:hidden;border:3px solid #fff;flex:none}
.cab .ft img{width:100%;height:100%;object-fit:cover}
.cab .nm{font-weight:700;font-size:29px;line-height:34px;display:flex;align-items:center;gap:8px}
.cab .nm svg{width:26px;height:26px}
.cab .ar{font-size:22px;line-height:28px;opacity:.9}
.t1{position:absolute;left:0;width:1080px;top:150px;text-align:center;font-family:"Anton";font-size:128px;line-height:1.02;letter-spacing:1px}
.t2{position:absolute;left:0;width:1080px;top:282px;text-align:center;font-family:"Anton";font-size:128px;line-height:1.02;letter-spacing:1px;color:#FFB400}
.sub{position:absolute;left:0;width:1080px;top:424px;text-align:center;font-size:27px;letter-spacing:7px;color:#e6efe9;font-weight:400}
.lin{position:absolute;left:70px;right:70px;top:490px;display:flex;flex-direction:column;gap:12px}
.r{height:134px;display:flex;align-items:center;background:rgba(8,16,14,.82);border:1.5px solid rgba(255,255,255,.16);border-left:7px solid #FFB400;border-radius:18px;overflow:hidden}
.r .ph{width:226px;height:100%;background-size:cover;background-position:center;flex:none}
.r .tx{flex:1;padding:0 26px}
.r .tx b{display:block;font-weight:600;font-size:38px;line-height:1.1}
.r .tx i{display:inline-block;font-style:normal;font-size:21px;letter-spacing:1px;color:#FFB400;border:1.5px solid rgba(255,180,0,.7);border-radius:30px;padding:2px 18px;margin-top:9px}
.r .dv{width:1.5px;height:84px;background:rgba(255,255,255,.2);flex:none}
.r .tk{width:262px;display:flex;align-items:center;gap:16px;padding-left:22px;flex:none}
.r .lg{width:78px;height:78px;border-radius:16px;overflow:hidden;flex:none;display:flex;align-items:center;justify-content:center}
.r .lg img{width:100%;height:100%;object-fit:cover}
.r .tk b{display:block;font-weight:700;font-size:29px;color:#FFB400;letter-spacing:1px}
.r .tk small{display:block;font-size:19px;color:#dfe9e3;margin-top:2px}.r .tk small em{font-style:normal;font-weight:700;color:#fff}
.fecho{position:absolute;left:0;width:1080px;bottom:104px;text-align:center;font-size:24px;letter-spacing:7px;color:#e6efe9}
.fecho em{font-style:normal;color:#FFB400;font-weight:600}
.rod{position:absolute;left:0;width:1080px;bottom:34px;text-align:center;font-size:19px;line-height:1.5;color:rgba(255,255,255,.62)}
"""

def build(c):
    ln = ""
    for seg, pil, foto, logo, tk, dy, *x in c["linhas"]:
        fundo, cheio = cor_logo(logo)
        if x: fundo = x[0]
        ln += (f'<div class="r"><div class="ph" style="background-image:url(\'{foto}\')"></div>'
               f'<div class="tx"><b>{seg}</b><i>{pil}</i></div><div class="dv"></div>'
               f'<div class="tk"><div class="lg" style="background:{fundo}"><img src="{logo}" alt=""></div>'
               f'<div><b>{tk}</b><small>DY 12m <em>{dy}</em></small></div></div></div>')
    rod = "<br>".join(c["rodape"])
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="bg" style="background-image:url('{c['fundo']}')"></div><div class="sombra"></div><div class="luz"></div>
<div class="cab"><div class="ft"><img src="assets/foto.png" alt=""></div><div><div class="nm">Douglas Medeiros {SELO}</div><div class="ar">@infobolsainvestimentos</div></div></div>
<div class="t1">{c['titulo1']}</div><div class="t2">{c['titulo2']}</div><div class="sub">{c['sub']}</div>
<div class="lin">{ln}</div><div class="fecho">{c['fecho']}</div><div class="rod">{rod}</div>{SCRIPT}</body></html>"""

if __name__ == "__main__":
    open(sys.argv[2], "w").write(build(json.load(open(sys.argv[1]))))

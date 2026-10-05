#!/usr/bin/env python3
"""Base comum do modelo de fundo branco (cabeçalho com foto, nome, selo e arroba).
Medidas do cabeçalho conferidas com as páginas "Precisa ser rico para investir" do arquivo do Canva."""
from decimal import Decimal, ROUND_HALF_UP

TP = "fonts/node_modules/@typopro/web-aileron/TypoPRO-Aileron-"
FS = "fonts/node_modules/@fontsource/"

BASE_CSS = f"""
@font-face{{font-family:"Poppins";font-weight:400;src:url("fonts/sistema/Poppins-Regular.ttf")}}
@font-face{{font-family:"Poppins";font-weight:300;src:url("{FS}poppins/files/poppins-latin-300-normal.woff2")}}
@font-face{{font-family:"Poppins";font-weight:500;src:url("{FS}poppins/files/poppins-latin-500-normal.woff2")}}
@font-face{{font-family:"Poppins";font-weight:800;src:url("{FS}poppins/files/poppins-latin-800-normal.woff2")}}
@font-face{{font-family:"Aileron";font-weight:300;font-style:italic;src:url("{TP}LightItalic.ttf")}}
@font-face{{font-family:"Poppins";font-weight:600;src:url("{FS}poppins/files/poppins-latin-600-normal.woff2")}}
@font-face{{font-family:"Poppins";font-weight:700;src:url("fonts/sistema/Poppins-Bold.ttf")}}
@font-face{{font-family:"Aileron";font-weight:200;src:url("{TP}Thin.ttf")}}
@font-face{{font-family:"Aileron";font-weight:300;src:url("{TP}Light.ttf")}}
@font-face{{font-family:"Aileron";font-weight:400;src:url("{TP}Regular.ttf")}}
@font-face{{font-family:"Aileron";font-weight:600;src:url("{TP}SemiBold.ttf")}}
@font-face{{font-family:"Aileron";font-weight:700;src:url("{TP}Bold.ttf")}}
@font-face{{font-family:"League Spartan";font-weight:700;src:url("{FS}league-spartan/files/league-spartan-latin-700-normal.woff2")}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;background:#fff;overflow:hidden}}
body{{position:relative;font-family:"Poppins",sans-serif;color:#161616;-webkit-font-smoothing:antialiased;text-rendering:geometricPrecision}}
.foto{{position:absolute;left:103.0px;top:100.7px;width:185.6px;height:185.6px;border-radius:50%;overflow:hidden}}
.foto img{{position:absolute;left:50%;top:50%;width:190.4px;height:190.4px;transform:translate(-50%,-50%)}}
.nome{{position:absolute;left:312.8px;top:136.4px;font-weight:700;font-size:56.2px;line-height:68.3px;white-space:nowrap}}
.arroba{{position:absolute;left:312.9px;top:197.9px;font-weight:400;font-size:35.9px;line-height:50.5px;white-space:nowrap}}
.selo{{position:absolute;left:844.1px;top:127.6px;width:40.1px;height:40.1px}}
.titulo{{position:absolute;left:102px;font-weight:400;white-space:nowrap}}
.titulo b{{font-weight:700}}
.rod{{position:absolute;left:0;width:1080px;text-align:center;font-family:"Aileron";font-weight:300;line-height:34px;color:#3d3d3d}}
"""

CABECALHO = """<div class="foto"><img src="assets/foto.png" alt=""></div>
<div class="nome">Douglas Medeiros</div>
<div class="arroba">@infobolsainvestimentos</div>
<svg class="selo" viewBox="0 0 40 40" aria-hidden="true"><path id="selo-contorno" fill="#2799ff" d=""/><path fill="none" stroke="#fff" stroke-width="3.7" stroke-linecap="round" stroke-linejoin="round" d="M12.4 20.7l5.1 4.9 10-10.6"/></svg>"""

SCRIPT = """<script>(function(){var p=[],N=360;for(var i=0;i<N;i++){var t=2*Math.PI*i/N,r=17.3+1.25*Math.cos(12*t);p.push((20+r*Math.sin(t)).toFixed(2)+' '+(20-r*Math.cos(t)).toFixed(2));}document.getElementById('selo-contorno').setAttribute('d','M'+p.join(' L')+'Z');})();</script>"""


def pagina(css, corpo):
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><style>{BASE_CSS}{css}</style></head><body>
{CABECALHO}
{corpo}
{SCRIPT}
</body></html>"""


def brl(v, casas=2):
    """Decimal no padrão brasileiro: 50600 -> 50.600,00"""
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

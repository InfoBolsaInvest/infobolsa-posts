#!/usr/bin/env python3
"""Post escuro de notícia (foto de fundo, manchete grande), inspirado no estilo Nord.
cfg:
  fundo: caminho da foto; foco: background-position (ex.: "50% 30%"); zoom: background-size (ex.: "cover")
  tag: etiqueta azul opcional (ex.: "MERCADO")
  modo: "manchete" (titulo grande + sub) ou "numero" (rotulo + numero gigante + sub)
  titulo: manchete (aceita <em>palavra</em> para destacar em azul)
  rotulo, numero: usados no modo "numero"
  sub: texto de apoio (aceita <em>)
  fonte: linha pequena no rodapé (opcional)
  logo: caminho do logo da empresa citada (opcional, aparece num quadrado acima da etiqueta)
  logo_fundo: cor do quadrado do logo (padrão branco)
  ajustes: {titulo_size, numero_size, sub_size, bloco_bottom, escuro}
"""
import json, os, sys

FS = "fonts/node_modules/@fontsource/"
CSS = f"""
@font-face{{font-family:"Anton";src:url("{FS}anton/files/anton-latin-400-normal.woff2")}}
@font-face{{font-family:"Poppins";font-weight:400;src:url("fonts/sistema/Poppins-Regular.ttf")}}
@font-face{{font-family:"Poppins";font-weight:500;src:url("{FS}poppins/files/poppins-latin-500-normal.woff2")}}
@font-face{{font-family:"Poppins";font-weight:600;src:url("{FS}poppins/files/poppins-latin-600-normal.woff2")}}
@font-face{{font-family:"Poppins";font-weight:700;src:url("fonts/sistema/Poppins-Bold.ttf")}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:#05070b}}
body{{position:relative;font-family:"Poppins",sans-serif;color:#fff;-webkit-font-smoothing:antialiased}}
.bg{{position:absolute;inset:0;background-size:%(zoom)s;background-position:%(foco)s;background-repeat:no-repeat}}
.sombra{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(3,5,9,.55) 0%%,rgba(3,5,9,.12) 22%%,rgba(6,16,14,.10) 38%%,rgba(8,26,20,%(escuro)s) 62%%,rgba(9,38,26,.97) 100%%)}}
.verde{{position:absolute;inset:0;background:radial-gradient(ellipse 1100px 560px at 50%% 105%%,rgba(0,128,58,.55),transparent 70%%)}}
.faixa{{position:absolute;left:0;right:0;bottom:0;height:10px;background:linear-gradient(90deg,#00803A,#3fd98a)}}
.cab{{position:absolute;top:56px;left:0;width:1080px;display:flex;justify-content:center;align-items:center;gap:18px}}
.cab .ft{{width:86px;height:86px;border-radius:50%%;overflow:hidden;border:3px solid #3fd98a;flex:none}}
.cab .ft img{{width:100%%;height:100%%;object-fit:cover}}
.cab .nm{{font-weight:700;font-size:31px;line-height:36px;display:flex;align-items:center;gap:8px;text-shadow:0 2px 10px rgba(0,0,0,.45)}}
.cab .nm svg{{width:28px;height:28px}}
.cab .ar{{font-weight:400;font-size:23px;line-height:30px;opacity:.92;text-shadow:0 2px 10px rgba(0,0,0,.45)}}
.bloco{{position:absolute;left:72px;right:72px;bottom:%(bloco_bottom)spx}}
.tag{{display:inline-block;background:#00803A;color:#fff;font-weight:700;font-size:26px;letter-spacing:2px;padding:8px 26px;border-radius:8px;margin-bottom:26px;text-transform:uppercase}}
.lg{{width:118px;height:118px;border-radius:24px;display:flex;align-items:center;justify-content:center;margin-bottom:26px;box-shadow:0 8px 30px rgba(0,0,0,.45);overflow:hidden}}
.lg img{{width:86%%;height:86%%;object-fit:contain}}
.titulo{{font-family:"Anton";font-size:%(titulo_size)spx;line-height:1.08;letter-spacing:.5px;text-transform:none}}
.rotulo{{font-weight:700;font-size:%(rotulo_size)spx;line-height:1.1}}
.numero{{font-family:"Anton";font-size:%(numero_size)spx;line-height:1;color:#FFB400;margin:6px 0 10px -4px;letter-spacing:1px}}
em{{font-style:normal;color:#FFB400}}
.sub{{font-weight:400;font-size:%(sub_size)spx;line-height:1.32;margin-top:22px;color:#eef3f8}}
.sub b,.sub em{{font-weight:700}}
.fonte{{position:absolute;left:0;width:1080px;bottom:34px;text-align:center;font-size:20px;color:rgba(255,255,255,.62)}}
"""
DEF = dict(foco="50% 50%", zoom="cover", escuro=".78", titulo_size=104, rotulo_size=62, numero_size=250,
           sub_size=38, bloco_bottom=120)

SELO = """<svg viewBox="0 0 40 40" aria-hidden="true"><path id="selo" fill="#2799ff" d=""/><path fill="none" stroke="#fff" stroke-width="3.7" stroke-linecap="round" stroke-linejoin="round" d="M12.4 20.7l5.1 4.9 10-10.6"/></svg>"""
SCRIPT = """<script>(function(){var p=[],N=360;for(var i=0;i<N;i++){var t=2*Math.PI*i/N,r=17.3+1.25*Math.cos(12*t);p.push((20+r*Math.sin(t)).toFixed(2)+' '+(20-r*Math.cos(t)).toFixed(2));}document.getElementById('selo').setAttribute('d','M'+p.join(' L')+'Z');})();</script>"""


def build(cfg):
    p = dict(DEF); p.update(cfg.get("ajustes", {}))
    for k in ("foco", "zoom"):
        if cfg.get(k): p[k] = cfg[k]
    tag = f'<div class="tag">{cfg["tag"]}</div><br>' if cfg.get("tag") else ""
    if cfg.get("modo") == "numero":
        miolo = f'<div class="rotulo">{cfg["rotulo"]}</div><div class="numero">{cfg["numero"]}</div>'
    else:
        miolo = f'<div class="titulo">{cfg["titulo"]}</div>'
    if cfg.get("logo"):
        tag = f'<div class="lg" style="background:{cfg.get("logo_fundo", "#fff")}"><img src="{cfg["logo"]}" alt=""></div>' + tag
    sub = f'<div class="sub">{cfg["sub"]}</div>' if cfg.get("sub") else ""
    fonte = cfg.get("fonte", "")
    cr = os.path.join(os.path.dirname(cfg["fundo"]), "creditos.json")
    if os.path.exists(cr):
        cred = json.load(open(cr)).get(os.path.basename(cfg["fundo"]), {}).get("credito")
        if cred:
            fonte = f"{fonte}. {cred}" if fonte else cred
    fonte = f'<div class="fonte">{fonte}</div>' if fonte else ""
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS % p}</style></head><body>
<div class="bg" style="background-image:url('{cfg['fundo']}')"></div><div class="sombra"></div><div class="verde"></div><div class="faixa"></div>
<div class="cab"><div class="ft"><img src="assets/foto.png" alt=""></div>
<div><div class="nm">Douglas Medeiros {SELO}</div><div class="ar">@infobolsainvestimentos</div></div></div>
<div class="bloco">{tag}{miolo}{sub}</div>
{fonte}
{SCRIPT}
</body></html>"""


if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    open(sys.argv[2], "w").write(build(cfg))

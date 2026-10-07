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
@font-face{{font-family:"Poppins";font-weight:300;src:url("{FS}poppins/files/poppins-latin-300-normal.woff2")}}
@font-face{{font-family:"Poppins";font-weight:400;src:url("fonts/sistema/Poppins-Regular.ttf")}}
@font-face{{font-family:"Poppins";font-weight:500;src:url("{FS}poppins/files/poppins-latin-500-normal.woff2")}}
@font-face{{font-family:"Poppins";font-weight:600;src:url("{FS}poppins/files/poppins-latin-600-normal.woff2")}}
@font-face{{font-family:"Poppins";font-weight:700;src:url("fonts/sistema/Poppins-Bold.ttf")}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:#162526}}
body{{position:relative;font-family:"Poppins",sans-serif;font-weight:300;color:#fff;-webkit-font-smoothing:antialiased}}
.bg{{position:absolute;inset:0;background-size:%(zoom)s;background-position:%(foco)s;background-repeat:no-repeat}}
.tinta{{position:absolute;inset:0;background:#162526;mix-blend-mode:color;opacity:.35}}
.sombra{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,21,22,.72) 0%%,rgba(22,37,38,.18) 20%%,rgba(22,37,38,.12) 36%%,rgba(18,40,34,%(escuro)s) 60%%,rgba(13,30,26,.97) 100%%)}}
.luz{{position:absolute;inset:0;background:radial-gradient(ellipse 760px 620px at 100%% 100%%,rgba(0,128,58,.38),transparent 70%%)}}
.cab{{position:absolute;top:70px;left:96px;display:flex;align-items:center;gap:18px}}
.cab .ft{{width:88px;height:88px;border-radius:50%%;overflow:hidden;border:2px solid rgba(255,255,255,.85);flex:none}}
.cab .ft img{{width:100%%;height:100%%;object-fit:cover}}
.cab .nm{{font-weight:600;font-size:31px;line-height:36px;display:flex;align-items:center;gap:8px;text-shadow:0 2px 10px rgba(0,0,0,.35)}}
.cab .nm svg{{width:28px;height:28px}}
.cab .ar{{font-weight:300;font-size:24px;line-height:31px;opacity:.8;text-shadow:0 2px 10px rgba(0,0,0,.35)}}
.bloco{{position:absolute;left:96px;right:80px;bottom:%(bloco_bottom)spx}}
.tag{{display:inline-block;border:1.5px solid #ffb400;color:#ffb400;background:rgba(22,37,38,.55);font-weight:500;font-size:22px;letter-spacing:4px;padding:8px 22px;border-radius:30px;margin-bottom:28px;text-transform:uppercase}}
.lg{{width:110px;height:110px;border-radius:50%%;border:2px solid rgba(255,255,255,.85);display:flex;align-items:center;justify-content:center;margin-bottom:26px;overflow:hidden}}
.lg img{{width:72%%;height:72%%;object-fit:contain}}
.titulo{{font-weight:500;font-size:%(titulo_size)spx;line-height:1.06;letter-spacing:-1.5px}}
.rotulo{{font-weight:400;font-size:%(rotulo_size)spx;line-height:1.1;letter-spacing:-.5px}}
.numero{{font-weight:500;font-size:%(numero_size)spx;line-height:1;color:#ffb400;margin:6px 0 10px -6px;letter-spacing:-4px}}
em{{font-style:normal;color:#ffb400}}
.sub{{font-weight:300;font-size:%(sub_size)spx;line-height:1.35;margin-top:24px;color:rgba(255,255,255,.88)}}
.sub b,.sub em{{font-weight:500}}
.fonte{{position:absolute;left:96px;right:80px;bottom:40px;font-size:19px;line-height:1.4;color:rgba(255,255,255,.6)}}
"""
DEF = dict(foco="50% 50%", zoom="cover", escuro=".78", titulo_size=88, rotulo_size=56, numero_size=210,
           sub_size=34, bloco_bottom=130)

SELO = """<svg viewBox="0 0 40 40" aria-hidden="true"><path id="selo" fill="#2799ff" d=""/><path fill="none" stroke="#fff" stroke-width="3.7" stroke-linecap="round" stroke-linejoin="round" d="M12.4 20.7l5.1 4.9 10-10.6"/></svg>"""
SCRIPT = """<script>(function(){var p=[],N=360;for(var i=0;i<N;i++){var t=2*Math.PI*i/N,r=17.3+1.25*Math.cos(12*t);p.push((20+r*Math.sin(t)).toFixed(2)+' '+(20-r*Math.cos(t)).toFixed(2));}document.getElementById('selo').setAttribute('d','M'+p.join(' L')+'Z');})();</script>"""


def build(cfg):
    p = dict(DEF); p.update(cfg.get("ajustes", {}))
    p["numero_size"] = min(int(p["numero_size"]), 220)
    p["titulo_size"] = min(int(p["titulo_size"]), 92)
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
<div class="bg" style="background-image:url('{cfg['fundo']}')"></div><div class="tinta"></div><div class="sombra"></div><div class="luz"></div>
<div class="cab"><div class="ft"><img src="assets/foto.png" alt=""></div>
<div><div class="nm">Douglas Medeiros {SELO}</div><div class="ar">@infobolsainvestimentos</div></div></div>
<div class="bloco">{tag}{miolo}{sub}</div>
{fonte}
{SCRIPT}
</body></html>"""


if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    open(sys.argv[2], "w").write(build(cfg))

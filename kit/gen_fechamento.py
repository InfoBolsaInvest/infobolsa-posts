#!/usr/bin/env python3
"""Post diario "Fechamento de mercado" (tema escuro, visual limpo, 1080x1350).
Uso: python3 gen_fechamento.py configs/fechamento/2026-10-02.json post.html && python3 render.py post.html post.png
cfg:
  data: "AAAA-MM-DD"
  ibov: {pontos: "192.114", var: 2.63}
  extras: [{rotulo, valor (opcional), var}]   (ate 2, linha discreta embaixo do Ibovespa)
  altas / baixas: [[ticker, nome, var], ...]   (ate 5 cada; var com sinal)
  nota_altas / nota_baixas: texto no lugar das linhas que faltarem
  fonte: linha do rodape
  layout: "lado" (padrao), "pilha", "pilha3" ou "lado3" (ou 3o argumento na linha de comando)
Logos: assets/logos_b3/TICKER.png (acervo github.com/thefintz/icones-b3). Sem logo, mostra as letras do ticker.
"""
import json, sys, os, datetime

FS = "fonts/node_modules/@fontsource/"
DIAS = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro",
         "outubro", "novembro", "dezembro"]
AZUL, VERDE, VERM = "#3aa2ff", "#4ee39b", "#ff6b7a"


def pct(v, sinal=True):
    s = f"{abs(v):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return (("+" if v > 0 else "-" if v < 0 else "") if sinal else "") + s + "%"


ICO_UP = '<svg viewBox="0 0 24 24"><path d="M4 16l6-6 4 4 6-7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M15 7h5v5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICO_DN = '<svg viewBox="0 0 24 24"><path d="M4 8l6 6 4-4 6 7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M15 17h5v-5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICO_IBOV = '<svg viewBox="0 0 24 24"><path d="M3 20h18" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><path d="M6 17V11M10 17V7M14 17V10M18 17V5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>'

CSS = f"""
@font-face{{font-family:"P";font-weight:300;src:url("{FS}poppins/files/poppins-latin-300-normal.woff2")}}
@font-face{{font-family:"P";font-weight:400;src:url("fonts/sistema/Poppins-Regular.ttf")}}
@font-face{{font-family:"P";font-weight:500;src:url("{FS}poppins/files/poppins-latin-500-normal.woff2")}}
@font-face{{font-family:"P";font-weight:600;src:url("{FS}poppins/files/poppins-latin-600-normal.woff2")}}
@font-face{{font-family:"P";font-weight:700;src:url("fonts/sistema/Poppins-Bold.ttf")}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{position:relative;font-family:"P",sans-serif;font-weight:300;color:#fff;-webkit-font-smoothing:antialiased;
 background:linear-gradient(155deg,#030722 0%,#050c33 38%,#0a2a86 78%,#0d4bd0 100%)}}
.luz{{position:absolute;inset:0;background:radial-gradient(ellipse 760px 620px at 100% 100%,rgba(40,120,255,.35),transparent 70%)}}
.curva{{position:absolute;inset:0}}
.cab{{position:absolute;top:70px;left:96px;display:flex;align-items:center;gap:18px}}
.cab .ft{{width:88px;height:88px;border-radius:50%;overflow:hidden;border:2px solid rgba(255,255,255,.85);flex:none}}
.cab .ft img{{width:100%;height:100%;object-fit:cover}}
.cab .nm{{font-weight:600;font-size:31px;line-height:36px;display:flex;align-items:center;gap:8px}}
.cab .nm svg{{width:28px;height:28px}}
.cab .ar{{font-weight:300;font-size:24px;line-height:31px;opacity:.75}}
.tit{{position:absolute;top:196px;left:96px}}
.tit h1{{font-weight:400;font-size:98px;line-height:1.02;letter-spacing:-1px}}
.tit h1 span{{color:{AZUL}}}
.tit p{{font-size:30px;line-height:1.35;margin-top:18px;color:rgba(255,255,255,.82)}}
.trilho{{position:absolute;left:150px;top:500px;bottom:130px;width:1px;background:linear-gradient(180deg,rgba(255,255,255,.28),rgba(255,255,255,.06))}}
.no{{position:absolute;left:96px;width:108px;height:108px;border-radius:50%;border:1.5px solid rgba(255,255,255,.30);
 background:#071447;display:flex;align-items:center;justify-content:center;color:#fff}}
.no svg{{width:46px;height:46px}}
.ibov{{position:absolute;top:520px;left:236px;right:96px}}
.ibov .lb{{font-size:24px;letter-spacing:4px;text-transform:uppercase;color:rgba(255,255,255,.65)}}
.ibov .pt{{display:flex;align-items:baseline;gap:22px;margin-top:2px}}
.ibov .pt b{{font-weight:400;font-size:84px;line-height:1.05;letter-spacing:-1px}}
.ibov .pt i{{font-style:normal;font-weight:400;font-size:44px}}
.ibov .ex{{display:flex;gap:44px;margin-top:6px;font-size:23px;color:rgba(255,255,255,.7)}}
.ibov .ex b{{font-weight:500;color:#fff}}
.pasta{{position:absolute}}
.psvg{{position:absolute;inset:0}}
.aba{{position:absolute;top:0;left:30px;height:56px;display:flex;align-items:center;gap:12px;font-weight:400;font-size:26px;letter-spacing:.5px}}
.aba em{{font-style:normal;width:10px;height:10px;border-radius:50%}}
.grid{{position:absolute;top:66px;left:30px;right:30px;display:grid;grid-template-columns:1fr 1fr;column-gap:44px}}
.grid>div>.it:last-child{{border-bottom:none}}
.it{{display:flex;align-items:center;gap:16px;height:60px;border-bottom:1px solid rgba(255,255,255,.10)}}
.lg{{width:46px;height:46px;border-radius:50%;overflow:hidden;flex:none;background:#fff;display:flex;align-items:center;justify-content:center;
 font-weight:600;font-size:14px;color:#0b1a36;box-shadow:0 0 0 1.5px rgba(255,255,255,.35)}}
.lg img{{width:100%;height:100%;object-fit:cover}}
.it .tk{{flex:1;font-weight:400;font-size:28px;letter-spacing:.5px}}
.it .vr{{font-weight:400;font-size:28px}}
.nota{{height:120px;display:flex;align-items:center;font-size:21px;line-height:1.4;color:rgba(255,255,255,.6)}}
.rod{{position:absolute;left:96px;bottom:40px;font-size:19px;line-height:1.5;color:rgba(255,255,255,.55)}}
"""

SELO = """<svg viewBox="0 0 40 40" aria-hidden="true"><path id="selo" fill="#2799ff" d=""/><path fill="none" stroke="#fff" stroke-width="3.7" stroke-linecap="round" stroke-linejoin="round" d="M12.4 20.7l5.1 4.9 10-10.6"/></svg>"""
SCRIPT = """<script>(function(){var p=[],N=360;for(var i=0;i<N;i++){var t=2*Math.PI*i/N,r=17.3+1.25*Math.cos(12*t);p.push((20+r*Math.sin(t)).toFixed(2)+' '+(20-r*Math.cos(t)).toFixed(2));}document.getElementById('selo').setAttribute('d','M'+p.join(' L')+'Z');})();</script>"""
CURVA = """<svg class="curva" viewBox="0 0 1080 1350" width="1080" height="1350"><path d="M850 1350 C 950 1265, 1010 1280, 1080 1185" fill="none" stroke="rgba(120,180,255,.35)" stroke-width="1.5"/><path d="M900 1350 C 960 1300, 1020 1300, 1080 1240" fill="none" stroke="rgba(120,180,255,.18)" stroke-width="1.2"/></svg>"""


def logo(tk):
    for nome in (tk, tk[:4] + "3", tk[:4] + "4", tk[:4]):
        p = f"assets/logos_b3/{nome}.png"
        if os.path.exists(p):
            return f'<div class="lg"><img src="{p}" alt=""></div>'
    return f'<div class="lg">{tk[:4]}</div>'


def pasta_svg(w, h, cor, tw=330, th=56, r=20, tint=False):
    d = (f"M0 {r} Q0 0 {r} 0 H{tw-34} Q{tw-16} 0 {tw-8} 14 L{tw+8} {th-12} Q{tw+15} {th} {tw+34} {th} "
         f"H{w-r} Q{w} {th} {w} {th+r} V{h-r} Q{w} {h} {w-r} {h} H{r} Q0 {h} 0 {h-r} Z")
    c, o1, o2 = (cor, ".16", ".04") if tint else ("#fff", ".10", ".04")
    gid = "g" + cor[1:] + str(w) + ("t" if tint else "")
    return (f'<svg class="psvg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{c}" stop-opacity="{o1}"/><stop offset="1" stop-color="{c}" stop-opacity="{o2}"/></linearGradient></defs>'
            f'<path d="{d}" fill="url(#{gid})" stroke="rgba(255,255,255,.16)" stroke-width="1.5"/>'
            f'<path d="M{r} 1.5 H{tw-36}" stroke="{cor}" stroke-width="3" stroke-linecap="round" opacity=".9"/></svg>')


def it_html(tk, v, cor):
    return f'<div class="it">{logo(tk)}<div class="tk">{tk}</div><div class="vr" style="color:{cor}">{pct(v)}</div></div>'


def pasta(x, top, w, h, titulo, cor, miolo, tw=330, tint=False):
    return (f'<div class="pasta" style="left:{x}px;top:{top}px;width:{w}px;height:{h}px">{pasta_svg(w, h, cor, tw, tint=tint)}'
            f'<div class="aba"><em style="background:{cor}"></em>{titulo}</div>{miolo}</div>')


def lista_2col(lista, cor, nota):
    lst = lista[:5]
    col = lambda L: "".join(it_html(tk, v, cor) for tk, _n, v in L)
    nt = f'<div class="nota">{nota}</div>' if (3 < len(lista) < 5 and nota) else ""
    return f'<div class="grid"><div>{col(lst[:3])}</div><div>{col(lst[3:])}{nt}</div></div>'


def lista_1col(lista, cor, nota, alt):
    h = "".join(it_html(tk, v, cor) for tk, _n, v in lista[:5])
    if len(lista) < 5 and nota:
        h += f'<div class="nota" style="height:{alt*(5-len(lista))}px">{nota}</div>'
    return f'<div class="grid g1" style="--alt:{alt}px">{h}</div>'


def ibov_txt(cfg, iv):
    exs = ""
    for e in cfg.get("extras", [])[:2]:
        val = (e["valor"] + " " if e.get("valor") else "") + pct(e["var"])
        exs += f'<span>{e["rotulo"]} <b>{val}</b></span>'
    return (f'<div class="pt"><b>{cfg["ibov"]["pontos"]} pts</b><i style="color:{VERDE if iv >= 0 else VERM}">{pct(iv)}</i></div>'
            f'<div class="ex">{exs}</div>')


EXTRA_CSS = """
.g1{position:absolute;top:66px;left:26px;right:26px;display:block}
.g1 .it{height:var(--alt)}
.g1 .it:last-child{border-bottom:none}
.g1 .tk{font-size:27px}.g1 .vr{font-size:27px}
.ibp{position:absolute;top:66px;left:34px;right:34px}
.ibp .pt{display:flex;align-items:baseline;gap:22px}
.ibp .pt b{font-weight:400;font-size:80px;line-height:1.05;letter-spacing:-1px}
.ibp .pt i{font-style:normal;font-weight:400;font-size:42px}
.ibp .ex{display:flex;gap:44px;margin-top:8px;font-size:23px;color:rgba(255,255,255,.7)}
.ibp .ex b{font-weight:500;color:#fff}
"""


def build(cfg, layout=None):
    layout = layout or cfg.get("layout", "lado")
    d = datetime.date.fromisoformat(cfg["data"])
    iv = cfg["ibov"]["var"]
    data_txt = f'{DIAS[d.weekday()]}, {d.day} de {MESES[d.month-1]} de {d.year}'
    A, B = cfg["altas"], cfg["baixas"]
    na, nb = cfg.get("nota_altas"), cfg.get("nota_baixas")
    H2 = 56 + 14 + 3 * 60 + 18
    if layout == "pilha":  # trilho + Ibovespa solto + pastas empilhadas
        corpo = (f'<div class="trilho"></div><div class="no" style="top:514px">{ICO_IBOV}</div>'
                 f'<div class="ibov"><div class="lb">Ibovespa</div>{ibov_txt(cfg, iv)}</div>'
                 f'<div class="no" style="top:686px;color:{VERDE}">{ICO_UP}</div>'
                 + pasta(236, 712, 748, H2, "Maiores altas", VERDE, lista_2col(A, VERDE, na))
                 + f'<div class="no" style="top:964px;color:{VERM}">{ICO_DN}</div>'
                 + pasta(236, 990, 748, H2, "Maiores baixas", VERM, lista_2col(B, VERM, nb)))
    elif layout == "lado":  # Ibovespa solto + pastas lado a lado
        hp = 56 + 14 + 5 * 74 + 16
        corpo = (f'<div class="no" style="top:514px">{ICO_IBOV}</div>'
                 f'<div class="ibov"><div class="lb">Ibovespa</div>{ibov_txt(cfg, iv)}</div>'
                 + pasta(96, 742, 432, hp, "Maiores altas", VERDE, lista_1col(A, VERDE, na, 74), tw=270)
                 + pasta(552, 742, 432, hp, "Maiores baixas", VERM, lista_1col(B, VERM, nb, 74), tw=270))
    elif layout == "pilha3":  # tres pastas empilhadas, largura total
        corpo = (pasta(96, 484, 888, 214, "Ibovespa", AZUL, f'<div class="ibp">{ibov_txt(cfg, iv)}</div>', tw=280)
                 + pasta(96, 714, 888, H2, "Maiores altas", VERDE, lista_2col(A, VERDE, na))
                 + pasta(96, 990, 888, H2, "Maiores baixas", VERM, lista_2col(B, VERM, nb)))
    elif layout == "lado3":  # pasta do Ibovespa + altas e baixas lado a lado, com cor
        hp = 56 + 14 + 5 * 70 + 16
        corpo = (pasta(96, 496, 888, 222, "Ibovespa", AZUL, f'<div class="ibp">{ibov_txt(cfg, iv)}</div>', tw=280, tint=True)
                 + pasta(96, 742, 432, hp, "Maiores altas", VERDE, lista_1col(A, VERDE, na, 70), tw=270, tint=True)
                 + pasta(552, 742, 432, hp, "Maiores baixas", VERM, lista_1col(B, VERM, nb, 70), tw=270, tint=True))
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}{EXTRA_CSS}</style></head><body>
<div class="luz"></div>{CURVA}
<div class="cab"><div class="ft"><img src="assets/foto.png" alt=""></div>
<div><div class="nm">Douglas Medeiros {SELO}</div><div class="ar">@infobolsainvestimentos</div></div></div>
<div class="tit"><h1><span>Fechamento</span><br>de mercado</h1><p>{data_txt}</p></div>
{corpo}
<div class="rod">{cfg.get("fonte", "Fonte: B3")}. Não é uma recomendação de compra ou venda.</div>
{SCRIPT}
</body></html>"""


if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    open(sys.argv[2], "w").write(build(cfg, sys.argv[3] if len(sys.argv) > 3 else None))

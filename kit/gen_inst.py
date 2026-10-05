#!/usr/bin/env python3
"""Posts no estilo institucional (mesma linha do Fechamento de mercado), 1080x1350.
Uso: python3 gen_inst.py TIPO config.json saida.html [tema]
TIPO: pag (dividendos / data de pagamento), vs (comparativo), fii (quanto investir para receber X por mes)
tema: azul (degradê azul), claro (fundo branco), preto (quase preto). Padrao: azul.
Le os mesmos json usados por gen_pag.py, gen_vs.py e gen_fii.py.
"""
import json, sys, re
from decimal import Decimal as D
from base import brl

FS = "fonts/node_modules/@fontsource/"
TEMAS = {
    "azul": dict(bg="linear-gradient(155deg,#030722 0%,#050c33 38%,#0a2a86 78%,#0d4bd0 100%)",
                 luz="rgba(40,120,255,.35)", fg="#ffffff", sub="rgba(255,255,255,.80)", mute="rgba(255,255,255,.55)",
                 acc="#3aa2ff", card1="rgba(255,255,255,.10)", card2="rgba(255,255,255,.04)", borda="rgba(255,255,255,.16)",
                 linha="rgba(255,255,255,.10)", chip="rgba(255,255,255,.07)", curva="rgba(120,180,255,.35)", foto="rgba(255,255,255,.85)"),
    "preto": dict(bg="linear-gradient(170deg,#07090f 0%,#0a0e18 60%,#0b1430 100%)",
                  luz="rgba(40,110,255,.20)", fg="#ffffff", sub="rgba(255,255,255,.78)", mute="rgba(255,255,255,.50)",
                  acc="#3aa2ff", card1="rgba(255,255,255,.07)", card2="rgba(255,255,255,.025)", borda="rgba(255,255,255,.13)",
                  linha="rgba(255,255,255,.09)", chip="rgba(255,255,255,.06)", curva="rgba(90,150,255,.30)", foto="rgba(255,255,255,.85)"),
    "claro": dict(bg="linear-gradient(160deg,#ffffff 0%,#f4f7fc 55%,#e7eefb 100%)",
                  luz="rgba(29,111,224,.10)", fg="#0a1633", sub="#3d4a66", mute="#7a869e",
                  acc="#1d6fe0", card1="#ffffff", card2="#f7f9fd", borda="#d9e1ef",
                  linha="#e6ebf4", chip="#eef3fb", curva="rgba(29,111,224,.30)", foto="#0a1633"),
}

CSS = """
@font-face{font-family:"P";font-weight:300;src:url("FS/poppins/files/poppins-latin-300-normal.woff2")}
@font-face{font-family:"P";font-weight:400;src:url("fonts/sistema/Poppins-Regular.ttf")}
@font-face{font-family:"P";font-weight:500;src:url("FS/poppins/files/poppins-latin-500-normal.woff2")}
@font-face{font-family:"P";font-weight:600;src:url("FS/poppins/files/poppins-latin-600-normal.woff2")}
@font-face{font-family:"P";font-weight:700;src:url("fonts/sistema/Poppins-Bold.ttf")}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{position:relative;font-family:"P",sans-serif;font-weight:300;color:var(--fg);-webkit-font-smoothing:antialiased;background:var(--bg)}
.luz{position:absolute;inset:0;background:radial-gradient(ellipse 760px 620px at 100% 100%,var(--luz),transparent 70%)}
.curva{position:absolute;inset:0}
.cab{position:absolute;top:70px;left:96px;display:flex;align-items:center;gap:18px}
.cab .ft{width:88px;height:88px;border-radius:50%;overflow:hidden;border:2px solid var(--foto);flex:none}
.cab .ft img{width:100%;height:100%;object-fit:cover}
.cab .nm{font-weight:600;font-size:31px;line-height:36px;display:flex;align-items:center;gap:8px}
.cab .nm svg{width:28px;height:28px}
.cab .ar{font-size:24px;line-height:31px;color:var(--sub)}
.tit{position:absolute;top:196px;left:96px;right:96px}
.tit h1{font-weight:400;font-size:var(--tsize,92px);line-height:1.04;letter-spacing:-1px}
.tit h1 span{color:var(--acc)}
.tit p{font-size:30px;line-height:1.35;margin-top:16px;color:var(--sub)}
.pasta{position:absolute;left:96px;width:888px}
.psvg{position:absolute;inset:0}
.aba{position:absolute;top:0;left:30px;height:56px;display:flex;align-items:center;gap:12px;font-weight:400;font-size:26px;letter-spacing:.5px}
.aba em{font-style:normal;width:10px;height:10px;border-radius:50%;background:var(--acc)}
.rod{position:absolute;left:96px;right:96px;bottom:44px;font-size:19px;line-height:1.5;color:var(--mute)}
.num{font-variant-numeric:tabular-nums}
/* tabela */
.tb{position:absolute;top:70px;left:34px;right:34px}
.tb .hd,.tb .ln{display:grid;grid-template-columns:var(--cols);align-items:center;column-gap:16px}
.tb .hd{height:44px;font-size:19px;font-weight:500;letter-spacing:1.5px;text-transform:uppercase;color:var(--mute);border-bottom:1px solid var(--linha)}
.tb .ln{height:var(--lh,62px);font-size:27px;border-bottom:1px solid var(--linha)}
.tb .ln:last-child{border-bottom:none}
.tb .r{text-align:right}
.tb b{font-weight:600}
.tb .ac{color:var(--acc);font-weight:600}
.tk{display:flex;align-items:center;gap:14px;font-weight:500}
.mono{width:42px;height:42px;border-radius:50%;background:var(--chip);border:1px solid var(--borda);display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600;color:var(--acc);letter-spacing:.3px}
/* bloco do ativo */
.ativo{position:absolute;left:96px;right:96px;display:flex;align-items:center;gap:28px}
.ativo .lg{width:112px;height:112px;border-radius:50%;overflow:hidden;flex:none;display:flex;align-items:center;justify-content:center;border:1.5px solid var(--borda)}
.ativo .lg img{width:100%;height:100%;object-fit:contain}
.ativo .tic{font-weight:400;font-size:58px;line-height:1;letter-spacing:.5px}
.ativo .tic small{display:block;font-size:20px;letter-spacing:3px;text-transform:uppercase;color:var(--mute);margin-bottom:8px}
.chips{display:flex;gap:14px;margin-left:auto}
.chip{background:var(--chip);border:1px solid var(--borda);border-radius:18px;padding:14px 20px;min-width:150px}
.chip .r{font-size:17px;color:var(--mute);letter-spacing:.5px}
.chip .v{font-size:27px;font-weight:500;margin-top:2px}
/* comparativo */
.vs .hd{height:150px;border-bottom:1px solid var(--linha)}
.emp{display:flex;flex-direction:column;align-items:center;gap:10px;font-size:23px;font-weight:500}
.emp .lg{width:86px;height:86px;border-radius:50%;overflow:hidden;display:flex;align-items:center;justify-content:center;border:1.5px solid var(--borda)}
.emp .lg img{object-fit:contain}
.vs .ln{height:var(--lh,92px)}
.vs .lb{font-size:26px;font-weight:500;line-height:1.2}
.vs .lb small{display:block;font-size:18px;font-weight:300;color:var(--mute)}
.vs .vl{text-align:center;font-size:32px;font-weight:500}
"""

SELO = """<svg viewBox="0 0 40 40" aria-hidden="true"><path id="selo" fill="#2799ff" d=""/><path fill="none" stroke="#fff" stroke-width="3.7" stroke-linecap="round" stroke-linejoin="round" d="M12.4 20.7l5.1 4.9 10-10.6"/></svg>"""
SCRIPT = """<script>(function(){var p=[],N=360;for(var i=0;i<N;i++){var t=2*Math.PI*i/N,r=17.3+1.25*Math.cos(12*t);p.push((20+r*Math.sin(t)).toFixed(2)+' '+(20-r*Math.cos(t)).toFixed(2));}document.getElementById('selo').setAttribute('d','M'+p.join(' L')+'Z');})();</script>"""


def curva(t):
    c = TEMAS[t]["curva"]
    return (f'<svg class="curva" viewBox="0 0 1080 1350" width="1080" height="1350"><path d="M850 1350 C 950 1265, 1010 1280, 1080 1185" fill="none" stroke="{c}" stroke-width="1.5"/>'
            f'<path d="M900 1350 C 960 1300, 1020 1300, 1080 1240" fill="none" stroke="{c}" stroke-width="1.2" opacity=".55"/></svg>')


def pasta(top, h, titulo, miolo, tema, tw=330, th=56, r=20, w=888):
    T = TEMAS[tema]
    d = (f"M0 {r} Q0 0 {r} 0 H{tw-34} Q{tw-16} 0 {tw-8} 14 L{tw+8} {th-12} Q{tw+15} {th} {tw+34} {th} "
         f"H{w-r} Q{w} {th} {w} {th+r} V{h-r} Q{w} {h} {w-r} {h} H{r} Q0 {h} 0 {h-r} Z")
    svg = (f'<svg class="psvg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs><linearGradient id="gp{top}" x1="0" y1="0" x2="0" y2="1">'
           f'<stop offset="0" stop-color="{T["card1"]}"/><stop offset="1" stop-color="{T["card2"]}"/></linearGradient></defs>'
           f'<path d="{d}" fill="url(#gp{top})" stroke="{T["borda"]}" stroke-width="1.5"/>'
           f'<path d="M{r} 1.5 H{tw-36}" stroke="{T["acc"]}" stroke-width="3" stroke-linecap="round"/></svg>')
    return f'<div class="pasta" style="top:{top}px;height:{h}px">{svg}<div class="aba"><em></em>{titulo}</div>{miolo}</div>'


def limpa(s):
    return re.sub(r"</?b>", "", s)


def pagina(tema, titulo, sub, corpo, rodape, tsize=92):
    T = TEMAS[tema]
    vars_ = ";".join(f"--{k}:{v}" for k, v in T.items())
    rod = "<br>".join(rodape)
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS.replace('FS/', FS)}</style></head>
<body style="{vars_};--tsize:{tsize}px"><div class="luz"></div>{curva(tema)}
<div class="cab"><div class="ft"><img src="assets/foto.png" alt=""></div>
<div><div class="nm">Douglas Medeiros {SELO}</div><div class="ar">@infobolsainvestimentos</div></div></div>
<div class="tit"><h1>{titulo}</h1><p>{sub}</p></div>
{corpo}
<div class="rod">{rod}</div>{SCRIPT}</body></html>"""


def build_pag(c, tema):
    nome = limpa(c["titulo"]).replace("Dividendos do ", "").replace("Dividendos da ", "")
    pre = "do" if " do " in limpa(c["titulo"]) else "da"
    titulo = f'<span>Dividendos</span><br>{pre} {nome}'
    vpc, cot = D(c["valor_por_cota"]), D(c["cotacao"])
    it = {k.rstrip(":"): v for k, v in c["itens"]}
    dy = next((v for k, v in it.items() if "yield" in k.lower()), "")
    cot_k = next((k for k in it if k.lower().startswith("cota")), "Cotação")
    chips = (f'<div class="chip"><div class="r">Por ação (12 meses)</div><div class="v num">R$ {brl(vpc, 4)}</div></div>'
             f'<div class="chip"><div class="r">Dividend yield</div><div class="v num">{dy}</div></div>'
             f'<div class="chip"><div class="r">{cot_k}</div><div class="v num">R$ {brl(cot)}</div></div>')
    lg = c.get("logo", "")
    ativo = (f'<div class="ativo" style="top:446px"><div class="lg" style="background:#fff"><img src="{lg}" style="width:100%;height:100%;object-fit:cover"></div>'
             f'<div class="tic"><small>{it.get("Tipo", "")}</small>{c["ticker"]}</div></div>'
             f'<div class="ativo" style="top:584px">{chips.replace("class=\"chip\"", "class=\"chip\" style=\"flex:1\"")}</div>')
    linhas = "".join(f'<div class="ln num"><div>{brl(D(q), 0)} ações</div><div class="r ac">R$ {brl(D(q) * vpc)}</div><div class="r">R$ {brl(D(q) * cot)}</div></div>'
                     for q in c["quantidades"])
    n = len(c["quantidades"])
    lh = 56
    h = 70 + 44 + n * lh + 18
    tab = (f'<div class="tb" style="--cols:1fr 1.15fr 1.15fr;--lh:{lh}px"><div class="hd"><div>Se você tivesse</div><div class="r">Teria recebido</div><div class="r">Valor hoje</div></div>{linhas}</div>')
    corpo = ativo + pasta(700, h, "Proventos em 12 meses", tab, tema)
    return pagina(tema, titulo, "Quanto você teria recebido em 12 meses", corpo, c["rodape"], tsize=88)


def build_vs(c, tema):
    a, b = c["empresas"]
    titulo = f'{a["nome"]} <span>x</span> {b["nome"]}'
    def emp(e):
        return (f'<div class="emp"><div class="lg" style="background:{e.get("fundo", "#fff")}"><img src="{e["logo"]}" style="width:{int(e.get("logo_w", 80) * 0.62)}px"></div>{e["nome"]}</div>')
    linhas = "".join(f'<div class="ln"><div class="lb">{l}<small>{d}</small></div><div class="vl num">{x}</div><div class="vl num">{y}</div></div>'
                     for l, d, x, y in c["linhas"])
    n = len(c["linhas"])
    lh = 86
    tab = (f'<div class="tb vs" style="--cols:1.25fr 1fr 1fr;--lh:{lh}px;top:62px"><div class="hd"><div></div>{emp(a)}{emp(b)}</div>{linhas}</div>')
    h = 62 + 150 + n * lh + 20
    corpo = pasta(440, h, "Comparativo", tab, tema)
    return pagina(tema, titulo, limpa(c.get("sub", "")), corpo, c["rodape"], tsize=86)


def build_fii(c, tema):
    alvo = D(c["salario"])
    fundos = [(t, D(r), D(p)) for t, r, p in c["fundos"]]
    rows = [(t, r, p, (alvo / r) * p) for t, r, p in fundos]
    if c.get("ordenar"):
        rows.sort(key=lambda x: x[3])
    titulo = f'Quanto investir em cada<br>FII para <span>receber<br>R$ {brl(alvo)} por mês</span>'
    linhas = "".join(f'<div class="ln num"><div class="tk">{t}</div><div class="r">R$ {brl(r)}</div>'
                     f'<div class="r">R$ {brl(p)}</div><div class="r ac">R$ {brl(v)}</div></div>' for t, r, p, v in rows)
    lh = 64
    h = 70 + 44 + len(rows) * lh + 18
    tab = (f'<div class="tb" style="--cols:1.25fr .9fr .95fr 1.35fr;--lh:{lh}px"><div class="hd"><div>Fundo</div><div class="r">Últ. rend.</div><div class="r">Preço</div><div class="r">Investimento</div></div>{linhas}</div>')
    corpo = pasta(1250 - 40 - h - 10, h, "Investimento necessário", tab, tema)
    return pagina(tema, titulo, "", corpo, c["rodape"], tsize=72)


if __name__ == "__main__":
    tipo, cfgp, out = sys.argv[1:4]
    tema = sys.argv[4] if len(sys.argv) > 4 else "azul"
    c = json.load(open(cfgp))
    html = {"pag": build_pag, "vs": build_vs, "fii": build_fii}[tipo](c, tema)
    open(out, "w").write(html)

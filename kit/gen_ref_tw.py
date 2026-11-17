import json, os, sys
os.chdir("/home/claude/infobolsa-posts/kit")
sys.path.insert(0, ".")
from gen_inst import CSS, FS, SELO, SCRIPT, curva

BASE = """
body{background:linear-gradient(172deg,#ffffff 0%,#ffffff 58%,#eef6f1 100%)!important}
.luz{position:absolute;inset:0;background:radial-gradient(ellipse 760px 620px at 100% 100%,rgba(15,122,67,.07),transparent 70%)}
.cab{top:70px}
.t{position:absolute;left:84px;right:84px;top:250px;font-weight:700;font-size:var(--ts,62px);line-height:1.15;letter-spacing:-1px;color:#162526}
.t .n{font-weight:400}
.t:after{content:'';display:block;width:110px;height:7px;border-radius:4px;background:#FFB400;margin-top:20px}
.l2{position:absolute;left:84px;right:84px;display:grid;grid-template-columns:1fr 1fr;row-gap:50px;column-gap:40px;font-size:48px;color:#162526}
.l2 b{font-weight:600}
.tot{position:absolute;left:84px;font-weight:700;font-size:92px;color:#162526;letter-spacing:-1px}
.tot span{color:#0f7a43}
.fn{position:absolute;left:84px;right:84px;font-size:24px;line-height:1.45;color:#7b8f8a}
.br{position:absolute;left:70px;right:60px;display:flex;flex-direction:column;gap:22px}
.row{display:flex;align-items:center;gap:20px;height:96px}
.row img{width:96px;height:96px;border-radius:14px;object-fit:contain;flex:none}
.bar{height:96px;border-radius:12px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:34px;white-space:nowrap;flex:none}
.val{font-weight:700;font-size:34px;color:#162526;white-space:nowrap}
.secs{position:absolute;left:84px;right:84px;display:flex;flex-direction:column;gap:34px}
.sec h2{margin:0 0 8px;font-weight:700;font-size:54px;color:#162526;letter-spacing:-1px}
.sec ul{margin:0;padding:0;list-style:none}
.sec li{font-size:42px;color:#162526;line-height:1.5;padding-left:46px;position:relative}
.sec li:before{content:'';position:absolute;left:8px;top:30px;width:14px;height:14px;border-radius:50%;background:var(--c)}
.sec li small{font-size:32px;color:#3f5552}
"""


def pag(corpo, ts=62, cab=True):
    h = (f'<div class="cab"><div class="ft2"><img src="assets/foto.png" alt=""></div>'
         f'<div><div class="nm">Douglas Medeiros {SELO}</div><div class="ar">@infobolsainvestimentos</div></div></div>') if cab else ""
    h = h.replace('class="ft2"', 'class="ft"')
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS.replace("FS/", FS)}{BASE}</style></head>'
            f'<body style="--fg:#162526;--sub:#3f5552;--foto:#162526;--ts:{ts}px"><div class="luz"></div>{curva("branco")}{h}{corpo}{SCRIPT}</body></html>')


P = "../pronto/2026-11-17-"
# 1. FIIs
c = json.load(open(P + "semdinheiro/config.json"))
it = "".join(f"<div><b>{t}:</b> R$ {p}</div>" for t, p in c["itens"])
html = pag(f'<div class="t">"Eu não tenho dinheiro para<br>investir"</div>'
           f'<div class="l2" style="top:500px">{it}</div>'
           f'<div class="tot" style="top:1075px">Total: <span class="num">R$ {c["total"]}</span></div>'
           f'<div class="fn" style="top:1225px">Fonte: StatusInvest, cotações de 17/11/2026.<br>Este conteúdo não é uma recomendação de compra.</div>', 64)
open("r1.html", "w").write(html)
# 2. Bancos
c = json.load(open(P + "bancos/config.json"))
mx = max(x["v"] for x in c["itens"])
nomes = {"Itaú": "Itaú", "Banco do Brasil": "Banco do Brasil"}
rows = ""
for x in c["itens"]:
    w = max(36, int(600 * x["v"] / mx))
    txt = x["txt"].replace(" bi", " bilhões").replace(" mi", " milhões").replace("R$ 1,27 bilhões", "R$ 1,27 bilhão")
    if w > 380:
        rows += f'<div class="row"><img src="{x["logo"]}" style="background:{x.get("fundo", "transparent")}"><div class="bar" style="width:{w}px;background:{x["cor"]}">{x["nome"]} - {txt}</div></div>'
    elif w > 200:
        rows += f'<div class="row"><img src="{x["logo"]}" style="background:{x.get("fundo", "transparent")}"><div class="bar" style="width:{w}px;background:{x["cor"]}">{x["nome"]}</div><div class="val num">{txt}</div></div>'
    else:
        rows += f'<div class="row"><img src="{x["logo"]}" style="background:{x.get("fundo", "transparent")}"><div class="bar" style="width:{w}px;background:{x["cor"]}"></div><div class="val num">{x["nome"]} - {txt}</div></div>'
html = pag(f'<div class="t" style="font-size:52px">🚨 Quanto cada banco lucrou <span class="n">no 3º trimestre (valor em R$):</span> 👇💰🏦</div>'
           f'<div class="br" style="top:455px">{rows}</div>', 52)
open("r2.html", "w").write(html.replace(" - ", ": "))
# 3. Investimento
sec = lambda t, c, its, top=0: f'<div class="sec" style="--c:{c}"><h2>{t}</h2><ul>' + "".join(f"<li>{i}</li>" for i in its) + "</ul></div>"
html = pag('<div class="t" style="font-size:76px">ENTENDA DE UMA VEZ:</div><div class="secs" style="top:410px">'
           + sec("É INVESTIMENTO:", "#0f7a43", ["Tesouro Direto", "CDB, LCI e LCA", "Ações", "Fundos Imobiliários"], 390)
           + sec("NÃO É INVESTIMENTO:", "#c0392b", ["Consórcio", "Loteria e apostas", "Título de capitalização"], 760)
           + sec("DEPENDE:", "#d99a00", ["Poupança <small>(rende pouco)</small>", "Previdência Privada <small>(olhe as taxas)</small>"], 1065) + "</div>", 76)
open("r3.html", "w").write(html)

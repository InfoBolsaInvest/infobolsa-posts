#!/usr/bin/env python3
"""Post estilo Twitter (fundo branco liso, só cabeçalho + título + conteúdo).
Uso: python3 gen_tw.py grade config.json saida.html
grade: titulo, itens [{logo, fundo, valor, det, emoji}], cols"""
import json, sys
from gen_inst import CSS, FS, SELO, SCRIPT, curva

EXTRA = """
body{background:linear-gradient(172deg,#ffffff 0%,#ffffff 58%,#eef6f1 100%)!important}
.luz{position:absolute;inset:0;background:radial-gradient(ellipse 760px 620px at 100% 100%,rgba(15,122,67,.07),transparent 70%)}
.tw-t:after{content:'';display:block;width:110px;height:7px;border-radius:4px;background:#FFB400;margin-top:22px}
.cab{top:70px}
.tw-t{position:absolute;left:96px;right:96px;top:260px;font-weight:700;font-size:var(--ts,76px);line-height:1.08;letter-spacing:-1.5px;color:#162526}
.gr{position:absolute;left:70px;right:70px;display:grid;row-gap:26px;column-gap:26px}
.it{display:flex;flex-direction:column;align-items:center;text-align:center;background:#fff;border:1.5px solid #e3ece7;border-radius:30px;padding:24px 10px 22px;box-shadow:0 10px 26px rgba(22,37,38,.05)}
.lq{width:128px;height:128px;border-radius:30px;display:flex;align-items:center;justify-content:center;overflow:hidden;margin-bottom:14px}
.lq img{width:68%;height:68%;object-fit:contain}
.lq.em{font-size:112px;line-height:1}
.it .v{font-weight:700;font-size:50px;letter-spacing:-1px;color:#162526;line-height:1.1}
.it .d{font-size:25px;color:#3f5552;line-height:1.3;margin-top:4px}
"""

def grade(c):
    it = ""
    for x in c["itens"]:
        lq = (f'<div class="lq em">{x["emoji"]}</div>' if x.get("emoji")
              else f'<div class="lq" style="background:{x["fundo"]}"><img src="{x["logo"]}"></div>')
        it += f'<div class="it">{lq}<div class="v num">{x["valor"]}</div><div class="d">{x.get("det", "")}</div></div>'
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS.replace('FS/', FS)}{EXTRA}</style></head>
<body style="--fg:#162526;--sub:#3f5552;--foto:#162526;--ts:{c.get("tsize", 76)}px"><div class="luz"></div>{curva("branco")}
<div class="cab"><div class="ft"><img src="assets/foto.png" alt=""></div>
<div><div class="nm">Douglas Medeiros {SELO}</div><div class="ar">@infobolsainvestimentos</div></div></div>
<div class="tw-t">{c["titulo"]}</div>
<div class="gr" style="top:{c.get("top", 420)}px;grid-template-columns:repeat({c.get("cols", 3)},1fr)">{it}</div>
<div style="position:absolute;left:96px;right:96px;bottom:52px;text-align:center;font-size:22px;line-height:1.45;color:#7b8f8a">{c.get("nota", "")}</div>
{SCRIPT}</body></html>"""

CSS_VS = """
.vh{position:absolute;left:96px;right:96px;display:grid;grid-template-columns:1fr 1.1fr 1fr;align-items:center;text-align:center}
.vh .lg{width:150px;height:150px;border-radius:34px;overflow:hidden;margin:0 auto}
.vh .lg img{width:100%;height:100%;object-fit:contain}
.vh .vs{font-weight:700;font-size:64px;color:#0f7a43;font-style:italic}
.vr{position:absolute;left:96px;right:96px;display:flex;flex-direction:column}
.vr .ln{display:grid;grid-template-columns:1fr 1.1fr 1fr;align-items:center;text-align:center;height:var(--lh,116px);border-bottom:2px solid #d9e7de}
.vr .ln:nth-child(odd){background:#f3f8f5;border-radius:22px}
.vr .ln:last-child{border-bottom:none}
.vr .x{font-weight:700;font-size:46px;color:#162526}
.vr .l{font-weight:600;font-size:28px;color:#3f5552;line-height:1.2}
.rk{position:absolute;left:96px;right:96px;display:flex;flex-direction:column}
.rw{display:flex;align-items:center;gap:28px;height:var(--rh,150px);border-bottom:2px solid #d9e7de;padding:0 26px}
.rw:nth-child(odd){background:#f3f8f5;border-radius:22px}
.rw:last-child{border-bottom:none}
.rw .ps{font-weight:700;font-size:30px;color:#0f7a43;width:66px;height:66px;border-radius:50%;background:#e2f0e8;display:flex;align-items:center;justify-content:center;flex:none}
.rw:first-child .ps{background:#FFB400;color:#162526}
.rw .lq{width:104px;height:104px;border-radius:24px;overflow:hidden;flex:none}
.rw .lq img{width:100%;height:100%;object-fit:contain}
.rw .tk{flex:1;font-weight:700;font-size:46px;line-height:1.1;color:#162526;display:flex;flex-direction:column;align-items:flex-start}
.rw .tk small{display:block;font-size:24px;font-weight:400;color:#7b8f8a;margin-top:4px}
.rw .v{font-weight:700;font-size:44px;color:#0f7a43;white-space:nowrap}
"""


def _pag(c, corpo):
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS.replace('FS/', FS)}{EXTRA}{CSS_VS}</style></head>
<body style="--fg:#162526;--sub:#3f5552;--foto:#162526;--ts:{c.get("tsize", 76)}px"><div class="luz"></div>{curva("branco")}
<div class="cab"><div class="ft"><img src="assets/foto.png" alt=""></div>
<div><div class="nm">Douglas Medeiros {SELO}</div><div class="ar">@infobolsainvestimentos</div></div></div>
<div class="tw-t">{c["titulo"]}</div>{corpo}{SCRIPT}</body></html>"""


def vs(c):
    a, b = c["empresas"]
    lg = lambda e: f'<div class="lg" style="background:{e.get("fundo", "#fff")}"><img src="{e["logo"]}"></div>'
    top = c.get("top", 400)
    h = f'<div class="vh" style="top:{top}px">{lg(a)}<div class="vs">VS</div>{lg(b)}</div>'
    rows = "".join(f'<div class="ln"><div class="x num">{x}</div><div class="l">{l}</div><div class="x num">{y}</div></div>' for l, x, y in c["linhas"])
    return _pag(c, h + f'<div class="vr" style="top:{top + 180}px;--lh:{c.get("lh", 116)}px">{rows}</div>')


def ranking(c):
    rows = "".join(f'<div class="rw"><div class="ps">{x["pos"]}º</div><div class="lq"><img src="{x["logo"]}"></div>'
                   f'<div class="tk">{x["tk"]}<small>{x.get("det", "")}</small></div><div class="v num">{x["valor"]}</div></div>' for x in c["itens"])
    return _pag(c, f'<div class="rk" style="top:{c.get("top", 430)}px;--rh:{c.get("rh", 150)}px">{rows}</div>')


CSS_TB = """
.tb{position:absolute;left:70px;right:70px}
.tb .hd,.tb .ln{display:grid;grid-template-columns:1.25fr 1fr 1fr 1fr;align-items:center}
.tb .hd{height:84px;font-size:22px;letter-spacing:0;font-weight:600;color:#7b8f8a;text-align:center}
.tb .hd div:first-child{text-align:left;padding-left:26px}
.tb .hd b{display:block;font-size:30px;color:#162526;margin-bottom:2px}
.tb .ln{height:var(--lh,100px);border-bottom:2px solid #d9e7de;text-align:center}
.tb .ln:last-child{border-bottom:none}
.tb .ln:nth-child(even){background:#f3f8f5;border-radius:20px}
.tb .tk{display:flex;align-items:center;gap:16px;padding-left:20px;font-weight:700;font-size:34px;color:#162526}
.tb .tk img{width:66px;height:66px;border-radius:16px;object-fit:contain}
.tb .p{font-weight:600;font-size:36px;color:#3f5552}
.tb .p.n{font-weight:700;color:#162526}
.tb .v{font-weight:700;font-size:36px}
.tb .up{color:#0f7a43}.tb .dn{color:#c0392b}
"""


def tabela(c):
    hd = "".join(f"<div>{h}</div>" for h in c["cab"])
    rows = "".join(f'<div class="ln"><div class="tk"><img src="{x["logo"]}">{x["tk"]}</div><div class="p num">{x["a"]}</div>'
                   f'<div class="p n num">{x["b"]}</div><div class="v num {"up" if not x["var"].startswith("-") else "dn"}">{x["var"]}</div></div>' for x in c["itens"])
    corpo = f'<style>{CSS_TB}</style><div class="tb" style="top:{c.get("top", 420)}px;--lh:{c.get("lh", 100)}px"><div class="hd">{hd}</div>{rows}</div>'
    corpo += f'<div style="position:absolute;left:96px;right:96px;bottom:48px;text-align:center;font-size:22px;line-height:1.45;color:#7b8f8a">{c.get("nota", "")}</div>'
    return _pag(c, corpo)


CSS_GTA = """
.gw{position:absolute;left:70px;right:70px;display:flex;flex-direction:column;gap:44px}
.gw .sep{position:absolute;left:0;right:0;top:calc(var(--ch,390px) + 21px);height:3px;border-radius:2px;background:#cfd8d4}
.gc{display:grid;grid-template-columns:1fr 1fr;height:var(--ch,390px);background:#fff;border:1.5px solid #e3ece7;border-radius:32px;box-shadow:0 12px 30px rgba(22,37,38,.06);overflow:hidden}
.gc .l{display:flex;flex-direction:column;align-items:center;justify-content:center;border-right:3px solid #cfd8d4}
.gc .l img{width:300px;height:220px;object-fit:contain}
.gc .l .y{font-weight:700;font-size:40px;color:#162526;margin-top:12px}
.gc .r{display:flex;flex-direction:column;justify-content:center;padding:0 44px;background:#f6faf7}
.gc .lg{display:flex;align-items:center;gap:18px}
.gc .lg img{width:84px;height:84px;border-radius:20px;object-fit:contain}
.gc .tk{font-weight:700;font-size:40px;color:#162526;line-height:1}
.gc .nm{font-size:22px;color:#7b8f8a;margin-top:4px}
.gc .p{font-weight:700;font-size:86px;letter-spacing:-2px;color:#162526;margin-top:20px;line-height:1}
.gc .p small{font-size:44px;letter-spacing:0;margin-right:6px;font-weight:600}
.gc .v{align-self:flex-start;margin-top:16px;font-weight:700;font-size:32px;padding:8px 20px;border-radius:30px}
.gc .pk{margin-top:14px;font-size:24px;color:#7b8f8a;line-height:1.3}.gc .pk b{color:#c0392b}
.gc .up{background:#e2f0e8;color:#0f7a43}.gc .dn{background:#f8e1de;color:#c0392b}
"""


def gta(c, x, titulo):
    lg = f'<div class="lg"><img src="{x["logo"]}"><div><div class="tk">{x["tk"]}</div><div class="nm">{x["nome"]}</div></div></div>'
    cls = "dn" if x["var"].startswith("-") else "up"
    card = lambda glogo, ano, pr, extra: (f'<div class="gc"><div class="l"><img src="{glogo}"><div class="y">{ano}</div></div>'
                                         f'<div class="r">{lg}<div class="p num"><small>R$</small>{pr}</div>{extra}</div></div>')
    corpo = (f'<style>{CSS_GTA}</style><div class="gw" style="top:{c.get("top", 420) + (55 if x.get("pico") else 0)}px;--ch:{c.get("ch", 390) - (15 if x.get("pico") else 0)}px">'
             + card(c["logo_a"], c["ano_a"], x["a"], "")
             + '<div class="sep"></div>'
             + card(c["logo_b"], c["ano_b"], x["b"], f'<div class="v num {cls}">{x["var"]}</div>') + "</div>")
    return _pag({**c, "titulo": titulo}, corpo)


CSS_X = """
.l2{position:absolute;left:96px;right:96px;display:grid;grid-template-columns:1fr 1fr;column-gap:40px}
.l2 .li{display:flex;justify-content:space-between;align-items:center;height:var(--lh,86px);border-bottom:2px solid #e3ece7;font-size:38px;color:#162526}
.l2 .li b{font-weight:700}
.l2 .li span{font-weight:500;color:#3f5552}
.tot{position:absolute;left:96px;right:96px;display:flex;align-items:center;justify-content:space-between;background:#162526;border-radius:28px;padding:0 44px;height:130px;color:#fff;font-weight:700;font-size:54px}
.tot span{color:#FFB400}
.br{position:absolute;left:70px;right:70px;display:flex;flex-direction:column;gap:12px}
.br .row{display:flex;align-items:center;gap:20px;height:var(--lh,98px)}
.br .row img{width:84px;height:84px;border-radius:20px;object-fit:contain;flex:none}
.br .bar{height:84px;border-radius:18px;display:flex;align-items:center;padding:0 22px;color:#fff;font-weight:700;font-size:28px;white-space:nowrap;flex:none}
.br .val{font-weight:700;font-size:34px;color:#162526;white-space:nowrap}
.cols{position:absolute;left:70px;right:70px;display:flex;flex-direction:column;gap:20px}
.cx{border-radius:30px;padding:22px 40px;background:#fff;border:1.5px solid #e3ece7;box-shadow:0 12px 30px rgba(22,37,38,.06)}
.cx h3{margin:0 0 14px;font-size:36px;font-weight:700;display:flex;align-items:center;gap:14px}
.cx h3 i{font-style:normal;width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:28px}
.cx .gr2{display:grid;grid-template-columns:1fr 1fr;gap:6px 30px}
.cx .gr2 div{font-size:32px;color:#162526;padding:6px 0}
.cx p{margin:4px 0;font-size:28px;color:#3f5552;line-height:1.35}
.cx p b{color:#162526}
"""


def lista2(c):
    it = "".join(f'<div class="li"><b>{t}</b><span class="num">R$ {p}</span></div>' for t, p in c["itens"])
    corpo = (f'<style>{CSS_X}</style><div class="l2" style="top:{c.get("top", 430)}px;--lh:{c.get("lh", 86)}px">{it}</div>'
             f'<div class="tot" style="top:{c["tot_top"]}px"><div>Total</div><span class="num">R$ {c["total"]}</span></div>'
             f'<div style="position:absolute;left:96px;right:96px;bottom:48px;text-align:center;font-size:22px;color:#7b8f8a">{c.get("nota", "")}</div>')
    return _pag(c, corpo)


def barras(c):
    mx = max(x["v"] for x in c["itens"])
    rows = ""
    for x in c["itens"]:
        dentro = x["v"] / mx > .35
        rows += (f'<div class="row"><img src="{x["logo"]}" style="background:{x.get("fundo", "transparent")}"><div class="bar" style="width:{max(14, int(560 * x["v"] / mx))}px;background:{x["cor"]}">{x["nome"] if dentro else ""}</div>'
                 f'<div class="val num">{"" if dentro else x["nome"] + " "}{x["txt"]}</div></div>')
    corpo = (f'<style>{CSS_X}</style><div class="br" style="top:{c.get("top", 430)}px;--lh:{c.get("lh", 98)}px">{rows}</div>'
             f'<div style="position:absolute;left:96px;right:96px;bottom:48px;text-align:center;font-size:22px;line-height:1.45;color:#7b8f8a">{c.get("nota", "")}</div>')
    return _pag(c, corpo)


def colunas(c):
    bx = ""
    for b in c["caixas"]:
        if b.get("grade"):
            miolo = '<div class="gr2">' + "".join(f"<div>{i}</div>" for i in b["itens"]) + "</div>"
        else:
            miolo = "".join(f"<p>{i}</p>" for i in b["itens"])
        bx += f'<div class="cx" style="border-left:10px solid {b["cor"]}"><h3 style="color:{b["cor"]}"><i style="background:{b["cor"]}">{b["ic"]}</i>{b["t"]}</h3>{miolo}</div>'
    return _pag(c, f'<style>{CSS_X}</style><div class="cols" style="top:{c.get("top", 400)}px">{bx}</div>')


if __name__ == "__main__":
    tipo, cfg, out = sys.argv[1:4]
    if tipo == "gta":
        c = json.load(open(cfg))
        for i, x in enumerate(c["itens"], 1):
            cor = "#c0392b" if x["var"].startswith("-") else "#0f7a43"
            t = c["titulo"] if i == 1 else f'{x["nome"]}: <span style="color:{cor}">{x["var"]}</span>'
            if x.get("pico"):
                t += f'<div style="font-size:30px;font-weight:500;letter-spacing:0;color:#3f5552;margin-top:12px;line-height:1.3">{x["pico"]}</div>'
            open(f"{out}-{i}.html", "w").write(gta(c, x, t))
        sys.exit()
    c = json.load(open(cfg))
    open(out, "w").write({"grade": grade, "vs": vs, "ranking": ranking, "tabela": tabela, "lista2": lista2, "barras": barras, "colunas": colunas}[tipo](c))

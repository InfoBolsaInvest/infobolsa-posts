#!/usr/bin/env python3
"""Carrossel de texto estilo Twitter no padrão InfoBolsa (fundo branco com verde, cabeçalho do Douglas).
Uso: python3 gen_texto.py config.json prefixo   -> prefixo-1.html, prefixo-2.html...
slide: {capa: true, tag, titulo, sub}  ou  {titulo, p: [texto|{"m": texto marcado}], cmp: {a_t, a: [...], b_t, b: [...]}}"""
import json, sys
from gen_inst import CSS, FS, SELO, SCRIPT, curva

EX = """
body{background:linear-gradient(172deg,#ffffff 0%,#ffffff 58%,#eef6f1 100%)!important}
.luz{position:absolute;inset:0;background:radial-gradient(ellipse 760px 620px at 100% 100%,rgba(15,122,67,.07),transparent 70%)}
.cab{top:70px}
.cx{position:absolute;left:84px;right:84px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;padding-top:150px}
.h{font-weight:700;font-size:56px;line-height:1.12;letter-spacing:-1px;color:#162526}
.h:after{content:'';display:block;width:110px;height:7px;border-radius:4px;background:#FFB400;margin:22px 0 10px}
.p{font-size:40px;line-height:1.35;color:#2b3d3c;margin-top:30px}
.p b{color:#162526}
mark{background:#FFB400;color:#162526;padding:0 8px;border-radius:6px;font-weight:700}
.tag{display:inline-block;background:#162526;color:#FFB400;font-weight:700;font-size:28px;letter-spacing:2px;padding:10px 22px;border-radius:12px;margin-bottom:34px;align-self:flex-start}
.cap .h{font-size:92px;line-height:1.04;letter-spacing:-2px}
.cap .h span{color:#0f7a43}
.cap .s{font-size:40px;color:#3f5552;margin-top:20px}
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:34px}
.cmp .c{border-radius:26px;padding:28px 30px}
.cmp .a{background:#f1f5f3;border:1.5px solid #dfe8e3}
.cmp .b{background:#162526;color:#fff}
.cmp .t{font-weight:700;font-size:32px;letter-spacing:1px;margin-bottom:12px}
.cmp .b .t{color:#FFB400}
.cmp .i{font-size:30px;line-height:1.3;padding:12px 0;border-top:1.5px solid rgba(128,128,128,.25)}
.cmp .i b{font-weight:700}
.st{display:flex;flex-direction:column;gap:20px;margin-top:30px}
.st .k{display:flex;align-items:center;gap:30px;background:#fff;border:1.5px solid #e3ece7;border-radius:26px;padding:24px 32px;box-shadow:0 10px 26px rgba(22,37,38,.05)}
.st .v{font-weight:700;font-size:58px;color:#0f7a43;min-width:300px;letter-spacing:-1px}
.st .d{font-size:30px;color:#2b3d3c;line-height:1.3}
.tbl{margin-top:30px;border-radius:26px;overflow:hidden;border:1.5px solid #e3ece7;background:#fff}
.tbl .r{display:grid;grid-template-columns:1.2fr 1fr 1fr;align-items:center;min-height:96px;border-top:1.5px solid #e3ece7;font-size:32px;text-align:center}
.tbl .r:first-child{border-top:none;background:#162526;color:#fff;font-weight:700;font-size:28px;min-height:76px}
.tbl .r:first-child div:last-child{color:#FFB400}
.tbl .r div:first-child{text-align:left;padding-left:28px;font-weight:600}
.tbl .r .pl{font-weight:700;color:#c0392b}
.ck{display:flex;flex-direction:column;gap:20px;margin-top:30px}
.ck .k{display:flex;gap:24px;align-items:flex-start;background:#fff;border:1.5px solid #e3ece7;border-radius:26px;padding:26px 30px}
.ck .ic{width:60px;height:60px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:32px}
.ck .t{font-weight:700;font-size:36px;color:#162526}
.ck .d{font-size:29px;color:#3f5552;line-height:1.3;margin-top:4px}
.tl{margin-top:34px;position:relative;padding-left:56px}
.tl:before{content:'';position:absolute;left:17px;top:14px;bottom:14px;width:4px;background:#d9e7de}
.tl .e{position:relative;margin-bottom:28px;font-size:34px;color:#2b3d3c}
.tl .e b{color:#162526}
.tl .e:before{content:'';position:absolute;left:-52px;top:8px;width:30px;height:30px;border-radius:50%;background:#fff;border:5px solid #d9e7de;box-sizing:border-box}
.tl .e.ok:before{background:#0f7a43;border-color:#0f7a43}
.n{position:absolute;right:84px;bottom:46px;font-size:24px;color:#7b8f8a}
"""


def pg(body, i, n):
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS.replace("FS/", FS)}{EX}</style></head>'
            f'<body style="--fg:#162526;--sub:#3f5552;--foto:#162526"><div class="luz"></div>{curva("branco")}'
            f'<div class="cab"><div class="ft"><img src="assets/foto.png" alt=""></div>'
            f'<div><div class="nm">Douglas Medeiros {SELO}</div><div class="ar">@infobolsainvestimentos</div></div></div>'
            f'{body}<div class="n">{i}/{n}</div>{SCRIPT}</body></html>')


def par(x):
    return f'<div class="p">{x}</div>' if isinstance(x, str) else f'<div class="p"><mark>{x["m"]}</mark></div>'


def slide(s):
    if s.get("capa"):
        return (f'<div class="cx cap"><div class="tag">{s["tag"]}</div><div class="h">{s["titulo"]}</div>'
                f'<div class="s">{s.get("sub", "")}</div></div>')
    cmp = ""
    if s.get("cmp"):
        c = s["cmp"]
        col = lambda k, t, its: f'<div class="c {k}"><div class="t">{t}</div>' + "".join(f'<div class="i">{x}</div>' for x in its) + "</div>"
        cmp = f'<div class="cmp">{col("a", c["a_t"], c["a"])}{col("b", c["b_t"], c["b"])}</div>'
    ex = ""
    if s.get("stats"):
        ex = '<div class="st">' + "".join(f'<div class="k"><div class="v num">{v}</div><div class="d">{d}</div></div>' for v, d in s["stats"]) + "</div>"
    if s.get("tab"):
        ex = '<div class="tbl">' + "".join('<div class="r">' + "".join(f'<div class="{"pl" if j == 2 and i and r[1] != r[2] else ""} num">{c}</div>' for j, c in enumerate(r)) + "</div>" for i, r in enumerate(s["tab"])) + "</div>"
    if s.get("check"):
        ex = '<div class="ck">' + "".join(f'<div class="k"><div class="ic" style="background:{c}">{ic}</div><div><div class="t">{t}</div><div class="d">{d}</div></div></div>' for ic, c, t, d in s["check"]) + "</div>"
    if s.get("tl"):
        ex = '<div class="tl">' + "".join(f'<div class="e {"ok" if ok else ""}">{t}</div>' for ok, t in s["tl"]) + "</div>"
    pre = "".join(par(x) for x in s.get("p0", []))
    return f'<div class="cx"><div class="h">{s["titulo"]}</div>{pre}{cmp}{ex}{"".join(par(x) for x in s.get("p", []))}</div>'


if __name__ == "__main__":
    cfg, pre = sys.argv[1:3]
    c = json.load(open(cfg))
    n = len(c["slides"]) + (1 if c.get("extra") else 0)
    for i, s in enumerate(c["slides"], 1):
        open(f"{pre}-{i}.html", "w").write(pg(slide(s), i, n))

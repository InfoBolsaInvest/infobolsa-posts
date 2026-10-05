#!/usr/bin/env python3
"""Gera os fundos desenhados (sem foto) usados no post escuro de notícia.
Uso: python3 gen_fundos.py  (cria assets/fundos/desenho-*.jpg)"""
import math, os, random, subprocess
from PIL import Image

W, H = 1080, 1350
BASE = """<!doctype html><html><head><meta charset="utf-8"><style>
*{margin:0;padding:0}html,body{width:1080px;height:1350px;overflow:hidden;background:#04070d}
.g{position:absolute;inset:0;background:radial-gradient(ellipse 70%% 45%% at %(gx)s%% 30%%,%(cor)s 0%%,rgba(4,7,13,0) 70%%)}
svg{position:absolute;inset:0}
</style></head><body><div class="g"></div><svg width="1080" height="1350" viewBox="0 0 1080 1350">%(svg)s</svg></body></html>"""


def grade():
    s = ""
    for x in range(0, W + 1, 90):
        s += f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="#ffffff" stroke-opacity=".045"/>'
    for y in range(0, H + 1, 90):
        s += f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#ffffff" stroke-opacity=".045"/>'
    return s


def velas(sobe, seed):
    random.seed(seed)
    s, v, n = grade(), 0.0, 22
    pts, larg = [], W / n
    for i in range(n):
        d = random.uniform(-1, 1) + (0.55 if sobe else -0.55)
        a, f = v, v + d
        hi, lo = max(a, f) + random.uniform(.1, .6), min(a, f) - random.uniform(.1, .6)
        pts.append((a, f, hi, lo)); v = f
    vals = [x for p in pts for x in p]
    mn, mx = min(vals), max(vals)
    Y = lambda t: 820 - (t - mn) / (mx - mn) * 640
    linha = []
    for i, (a, f, hi, lo) in enumerate(pts):
        cx = larg * i + larg / 2
        cor = "#2fd27a" if f >= a else "#ff4d5e"
        s += f'<line x1="{cx:.1f}" y1="{Y(hi):.1f}" x2="{cx:.1f}" y2="{Y(lo):.1f}" stroke="{cor}" stroke-width="3" opacity=".75"/>'
        y1, y2 = sorted((Y(a), Y(f)))
        s += f'<rect x="{cx-larg*.32:.1f}" y="{y1:.1f}" width="{larg*.64:.1f}" height="{max(y2-y1,4):.1f}" rx="3" fill="{cor}" opacity=".8"/>'
        linha.append(f"{cx:.1f},{Y(f):.1f}")
    s += f'<polyline points="{" ".join(linha)}" fill="none" stroke="#35b0ff" stroke-width="5" opacity=".9"/>'
    return s


def predios():
    random.seed(7)
    s, x = grade(), -20
    while x < W:
        w = random.randint(70, 150); h = random.randint(260, 760)
        s += f'<rect x="{x}" y="{900-h}" width="{w}" height="{h+450}" fill="#0d1a2e" stroke="#35b0ff" stroke-opacity=".35" stroke-width="2"/>'
        for jy in range(900 - h + 24, 900, 46):
            for jx in range(x + 14, x + w - 20, 30):
                if random.random() < .45:
                    s += f'<rect x="{jx}" y="{jy}" width="14" height="22" fill="#ffd36b" opacity="{random.uniform(.35,.85):.2f}"/>'
        x += w + random.randint(6, 22)
    return s


def simbolo(txt, tam, y, cor="#35b0ff"):
    return grade() + (f'<text x="540" y="{y}" text-anchor="middle" font-family="DejaVu Sans" font-weight="700" '
                      f'font-size="{tam}" fill="{cor}" opacity=".22">{txt}</text>'
                      f'<text x="540" y="{y}" text-anchor="middle" font-family="DejaVu Sans" font-weight="700" '
                      f'font-size="{tam}" fill="none" stroke="{cor}" stroke-width="4" opacity=".75">{txt}</text>')


def governo():
    s = grade()
    # cúpulas e torres (silhueta inspirada no Congresso)
    s += '<rect x="0" y="760" width="1080" height="600" fill="#0b1626"/>'
    s += '<rect x="80" y="730" width="920" height="40" fill="#13253f" stroke="#35b0ff" stroke-opacity=".5"/>'
    s += '<path d="M180 730 A150 70 0 0 1 480 730 Z" fill="#13253f" stroke="#35b0ff" stroke-width="3" opacity=".9"/>'
    s += '<path d="M600 640 A150 90 0 0 0 900 640 L900 730 L600 730 Z" fill="#13253f" stroke="#35b0ff" stroke-width="3" opacity=".9"/>'
    s += '<rect x="500" y="250" width="34" height="480" fill="#13253f" stroke="#35b0ff" stroke-width="3"/>'
    s += '<rect x="556" y="250" width="34" height="480" fill="#13253f" stroke="#35b0ff" stroke-width="3"/>'
    s += '<rect x="534" y="430" width="22" height="26" fill="#13253f" stroke="#35b0ff" stroke-width="2"/>'
    for y in range(275, 720, 30):
        s += f'<line x1="505" y1="{y}" x2="529" y2="{y}" stroke="#ffd36b" opacity=".5"/><line x1="561" y1="{y}" x2="585" y2="{y}" stroke="#ffd36b" opacity=".5"/>'
    return s


def banco():
    s = grade()
    s += '<path d="M240 420 L540 220 L840 420 Z" fill="#13253f" stroke="#35b0ff" stroke-width="4"/>'
    for i in range(6):
        x = 280 + i * 104
        s += f'<rect x="{x}" y="450" width="56" height="330" fill="#13253f" stroke="#35b0ff" stroke-width="3"/>'
    s += '<rect x="220" y="790" width="640" height="40" fill="#13253f" stroke="#35b0ff" stroke-width="3"/>'
    s += '<rect x="250" y="425" width="580" height="22" fill="#13253f" stroke="#35b0ff" stroke-width="3"/>'
    return s


def petroleo():
    s = grade()
    s += '<path d="M540 170 C 540 170 330 470 330 610 A210 210 0 0 0 750 610 C 750 470 540 170 540 170 Z" fill="#0d1a2e" stroke="#35b0ff" stroke-width="5"/>'
    s += '<path d="M440 600 A110 110 0 0 0 520 720" fill="none" stroke="#ffffff" stroke-opacity=".5" stroke-width="10" stroke-linecap="round"/>'
    return s


def agro():
    s = grade()
    s += '<rect x="0" y="760" width="1080" height="600" fill="#0b1626"/>'
    for i in range(-6, 14):
        s += f'<line x1="540" y1="700" x2="{i*90}" y2="1350" stroke="#2fd27a" stroke-opacity=".35" stroke-width="3"/>'
    s += '<circle cx="540" cy="520" r="160" fill="#ffd36b" opacity=".18"/><circle cx="540" cy="520" r="160" fill="none" stroke="#ffd36b" stroke-width="4" opacity=".7"/>'
    s += '<line x1="0" y1="700" x2="1080" y2="700" stroke="#35b0ff" stroke-width="3" opacity=".6"/>'
    return s


FUNDOS = {
    "alta": (velas(True, 3), "rgba(39,153,255,.45)", 50),
    "queda": (velas(False, 5), "rgba(255,77,94,.30)", 50),
    "imoveis-fii": (predios(), "rgba(39,153,255,.40)", 50),
    "dolar": (simbolo("$", 620, 700, "#2fd27a"), "rgba(47,210,122,.30)", 50),
    "juros-selic": (simbolo("%", 560, 680), "rgba(39,153,255,.45)", 50),
    "governo-brasilia": (governo(), "rgba(39,153,255,.40)", 50),
    "bancos": (banco(), "rgba(39,153,255,.40)", 50),
    "petroleo": (petroleo(), "rgba(39,153,255,.35)", 50),
    "agro": (agro(), "rgba(255,211,107,.25)", 50),
    "inflacao": (simbolo("IPCA", 300, 600, "#ffb84d"), "rgba(255,184,77,.28)", 50),
}

if __name__ == "__main__":
    os.makedirs("assets/fundos", exist_ok=True)
    for nome, (svg, cor, gx) in FUNDOS.items():
        open("tmp_f.html", "w").write(BASE % dict(svg=svg, cor=cor, gx=gx))
        subprocess.run(["python3", "render.py", "tmp_f.html", "tmp_f.png"], check=True)
        Image.open("tmp_f.png").convert("RGB").save(f"assets/fundos/desenho-{nome}.jpg", quality=90)
        print(nome)
    for f in ("tmp_f.html", "tmp_f.png"): os.remove(f)

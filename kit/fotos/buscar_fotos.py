#!/usr/bin/env python3
"""Busca fotos livres no Wikimedia Commons para os fundos dos posts.
Lê kit/fotos/buscar.json ({tema: busca}), baixa até 6 candidatas por tema em kit/fotos/candidatas/
e gera folhas de contato (kit/fotos/candidatas/_folha-*.jpg) para escolher."""
import json, os, re, io, urllib.parse, urllib.request
from PIL import Image, ImageDraw

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "candidatas")
UA = {"User-Agent": "InfoBolsaPosts/1.0 (github.com/InfoBolsaInvest/infobolsa-posts)"}


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()


def limpa(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()


os.makedirs(OUT, exist_ok=True)
temas = json.load(open(os.path.join(BASE, "buscar.json")))
meta = {}
mp = os.path.join(OUT, "_creditos.json")
if os.path.exists(mp):
    meta = json.load(open(mp))
for tema, busca in temas.items():
    q = urllib.parse.urlencode({"action": "query", "format": "json", "generator": "search", "gsrnamespace": 6,
                                "gsrlimit": 25, "gsrsearch": busca + " filetype:bitmap", "prop": "imageinfo",
                                "iiprop": "url|size|mime|extmetadata", "iiurlwidth": 1600})
    j = json.loads(get("https://commons.wikimedia.org/w/api.php?" + q))
    pages = sorted(j.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 0))
    n = 0
    for p in pages:
        ii = (p.get("imageinfo") or [{}])[0]
        if ii.get("mime") != "image/jpeg" or ii.get("width", 0) < 1200 or ii.get("height", 0) < 800:
            continue
        m = ii.get("extmetadata", {})
        lic = limpa(m.get("LicenseShortName", {}).get("value"))
        if not re.search(r"CC0|Public domain|CC BY", lic, re.I):
            continue
        nome = f"{tema}-{n + 1}.jpg"
        try:
            im = Image.open(io.BytesIO(get(ii["thumburl"]))).convert("RGB")
        except Exception as e:
            print("erro", tema, e); continue
        im.thumbnail((1600, 1600))
        im.save(os.path.join(OUT, nome), quality=90)
        meta[nome] = {"tema": tema, "arquivo": p["title"], "autor": limpa(m.get("Artist", {}).get("value")),
                      "licenca": lic, "pagina": ii.get("descriptionurl")}
        n += 1
        if n >= 6:
            break
    print(tema, n)
json.dump(meta, open(mp, "w"), ensure_ascii=False, indent=1)

# folhas de contato: 4 temas por folha, 6 fotos por linha
temas_ok = [t for t in temas if any(v["tema"] == t for v in meta.values())]
for f in range(0, len(temas_ok), 4):
    grupo = temas_ok[f:f + 4]
    W, H = 6 * 320, len(grupo) * 250
    folha = Image.new("RGB", (W, H), (20, 20, 20))
    d = ImageDraw.Draw(folha)
    for r, t in enumerate(grupo):
        for c in range(6):
            nome = f"{t}-{c + 1}.jpg"
            pth = os.path.join(OUT, nome)
            if not os.path.exists(pth):
                continue
            im = Image.open(pth); im.thumbnail((316, 220))
            folha.paste(im, (c * 320 + 2, r * 250 + 28))
            d.rectangle([c * 320 + 2, r * 250 + 2, c * 320 + 200, r * 250 + 24], fill=(0, 0, 0))
            d.text((c * 320 + 6, r * 250 + 6), nome, fill=(255, 255, 0))
    folha.save(os.path.join(OUT, f"_folha-{f // 4 + 1:02d}.jpg"), quality=85)

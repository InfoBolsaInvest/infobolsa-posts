#!/usr/bin/env python3
"""Gera e renderiza um carrossel "historia" inteiro.
Uso (dentro de kit/): python3 carrossel.py config.json ../sugestoes/AAAA-MM-DD-HHh [tema]
Cria ../sugestoes/AAAA-MM-DD-HHh-1.png, -2.png ... (último = slide "segue") e apaga os html temporários."""
import sys, os, subprocess
cfg, saida = sys.argv[1], sys.argv[2]
tema = sys.argv[3] if len(sys.argv) > 3 else "verde"
arqs = subprocess.check_output([sys.executable, "gen_inst.py", "historia", cfg, "hist_tmp.html", tema], text=True).split()
for i, a in enumerate(arqs, 1):
    subprocess.check_call([sys.executable, "render.py", a, f"{saida}-{i}.png"])
    os.remove(a)
    print(f"{saida}-{i}.png")

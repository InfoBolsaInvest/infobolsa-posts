#!/usr/bin/env python3
"""Posts de segunda 12/10 e terça 13/10/2026 (modelo branco). Rodar de dentro da pasta modelos."""
import json, os, subprocess, sys
from decimal import Decimal as D
sys.path.insert(0, ".")
from base import brl

OUT = "saida/png"; CFG = "configs/semana-12-a-18-10"
os.makedirs(OUT, exist_ok=True)
NAO_REC = "Não é uma recomendação de compra ou venda de ativos"
HIP = "Rentabilidade hipotética, não é garantia de retorno"

def r2(v): return brl(D(v))
def pct(v, casas=2): return brl(D(str(v).replace(",", ".")), casas) + "%"

# StatusInvest, 05/10/2026: (cotação, proventos 12m, DY 12m, P/L, P/VP, ROE, valor de mercado)
A = {
 "ITUB4": ("49.98", "3.1354", "6.27", "11,77", "2,53", "21,50%", "575075368974"),
 "BBAS3": ("26.62", "0.6904", "2.60", "9,89", "0,82", "8,27%", "152669418826"),
 "BBDC4": ("21.98", "1.2596", "5.73"),
 "BBSE3": ("41.02", "4.5901", "11.20"), "PETR4": ("56.09", "3.6667", "6.56"), "ITSA4": ("16.24", "1.1317", "6.96"),
 "TAEE11": ("44.40", "3.0065", "6.78"), "CMIG4": ("12.13", "0.7878", "6.50"), "VALE3": ("70.67", "5.6125", "7.95"),
 "SANB11": ("28.55", "2.3072", "8.08"), "CPFE3": ("50.80", "3.7359", "7.36"), "ISAE4": ("29.50", "1.8506", "6.27"),
 "CPLE3": ("17.65", "1.0626", "6.01"), "EQTL3": ("48.26", "1.9002", "3.95"), "EGIE3": ("32.62", "1.1200", "3.44"),
 "ALUP11": ("36.44", "1.0800", "2.97"),
}
DATA = "05/10/26"

posts = []
def add(dia, hora, slug, ger, cfg): posts.append((dia, hora, slug, ger, cfg))

# ================================================= SEGUNDA 12/10
seg = "1. segunda-feira 12-10"
acoes100 = ["BBSE3", "SANB11", "VALE3", "CPFE3", "ITSA4", "TAEE11", "PETR4", "ITUB4"]
add(seg, "10h", "100-mil-em-acoes-de-dividendos", "gen_rend100.py", {
 "titulo": "Quanto rendem <b>R$ 100 mil</b> em<br>ações que pagam dividendos? <span class=\"emo\">👇</span>",
 "valor": "100000", "colunas": ["Ação", "Média por mês", "Em 12 meses"],
 "fundos": [[t, str(D(A[t][1]) / 12), A[t][0]] for t in acoes100],
 "data": f"Cotações de {DATA} e proventos dos últimos 12 meses",
 "rodape": ["Valores brutos. Dividendos passados não garantem dividendos futuros", NAO_REC],
 "ajustes": {"lin_h": 78, "tk_size": 44, "vl_size": 40}})

add(seg, "18h", "dividendos-bradesco", "gen_pag.py", {
 "titulo": "<b>Dividendos do Bradesco</b>", "sub": "Quanto teria recebido se tivesse...", "ticker": "BBDC4",
 "logo": "assets/logo_bradesco_wiki.svg",
 "itens": [["Proventos por ação em 12 meses:", "R$ 1,2596"], ["Tipo:", "JCP mensal e complementar"],
           ["Dividend yield:", "5,73%"], ["Cotação em 05/10:", "R$ 21,98"]],
 "valor_por_cota": "1.2596", "cotacao": "21.98", "quantidades": [100, 300, 500, 1000, 3000, 5000, 10000],
 "colunas": ["Qtd de ações", "Proventos em 12 meses", "Valor hoje"],
 "rodape": ["Proventos brutos com data COM nos últimos 12 meses", NAO_REC],
 "ajustes": {"quadro": 212, "itens_mt": 4, "item_h": 37.5, "cols": "0.82fr 1.2fr 0.98fr", "logo_w": 92}})

res = [[f"R$ {brl(c, 0)}", f"R$ {brl(c * 6, 0)}", f"R$ {brl(c * 12, 0)}"] for c in (2000, 3000, 5000, 8000, 10000, 15000)]
add(seg, "20h", "reserva-de-emergencia", "gen_tab.py", {
 "titulo": "De quanto precisa ser a sua<br><b>reserva de emergência?</b> <span class=\"emo\">🛟</span>",
 "colunas": ["Custo de vida por mês", "6 meses<br>(carteira assinada)", "12 meses<br>(autônomo)"], "linhas": res, "destaque": 1,
 "fim": "O lugar dela é onde dá para resgatar no mesmo dia,<br><b>como Tesouro Selic ou CDB com liquidez diária</b>",
 "data": "Regra comum: 6 meses para CLT e 12 meses para autônomo",
 "rodape": [NAO_REC],
 "ajustes": {"cols": "320px 304px 304px", "tk_size": 38, "vl_size": 36, "lin_h": 88, "cab_h": 56, "tab_top": 492, "fim_top": 1080, "fim_size": 27, "data_top": 1170, "rod_top": 1218}})

# ================================================= TERÇA 13/10
ter = "2. terça-feira 13-10"
a, b = A["ITUB4"], A["BBAS3"]
def bi(v): return brl(D(v) / D(1_000_000_000), 0)
add(ter, "07h", "itau-x-banco-do-brasil", "gen_vs.py", {
 "titulo": "<b>Itaú x Banco do Brasil</b>", "sub": "Os números dos dois bancos hoje",
 "empresas": [{"nome": "Itaú", "logo": "assets/logo_itau_wiki.svg", "fundo": "#ffffff", "logo_w": 92},
              {"nome": "Banco do Brasil", "logo": "assets/logo_bb.svg", "fundo": "#fcfc30", "logo_w": 62}],
 "linhas": [["Cotação", "em 05/10/2026", f"R$ {r2(a[0])}", f"R$ {r2(b[0])}"],
            ["Dividend yield", "últimos 12 meses", pct(a[2]), pct(b[2])],
            ["P/L", "preço sobre lucro", a[3], b[3]],
            ["P/VP", "preço sobre valor patrimonial", a[4], b[4]],
            ["ROE", "retorno sobre o patrimônio", a[5], b[5]],
            ["Valor de mercado", "", f"R$ {bi(a[6])} bi", f"R$ {bi(b[6])} bi"]],
 "rodape": ["Dados do StatusInvest. Ações ITUB4 e BBAS3", NAO_REC],
 "ajustes": {"tab_top": 478, "head_h": 182, "lin_h": 88, "cel_h": 66, "rod_top": 1236}})

def patrimonio(aporte, meses, taxa=D("0.008")):
    s = D(0)
    for _ in range(meses): s = s * (1 + taxa) + aporte
    return s
cedo = []
for idade in (20, 25, 30, 35, 40, 45, 50):
    m = (60 - idade) * 12
    cedo.append([f"{idade} anos", f"R$ {brl(500 * m, 0)}", f"R$ {brl(patrimonio(D(500), m), 0)}"])
p25, p35 = patrimonio(D(500), 420), patrimonio(D(500), 300)
add(ter, "12h", "comecar-cedo-500-por-mes", "gen_tab.py", {
 "titulo": "Investindo <b>R$ 500 por mês</b> até<br>os 60 anos, quanto você teria? <span class=\"emo\">⏳</span>",
 "colunas": ["Começou com", "Saiu do seu bolso", "Aos 60 anos teria"], "linhas": cedo, "destaque": 2,
 "fim": f"Quem começa aos 25 chega aos 60 com<br><b>{brl(p25 / p35, 1)} vezes mais</b> do que quem começa aos 35",
 "data": "Simulação com rendimento de 0,80% ao mês, sem descontar a inflação",
 "rodape": [HIP],
 "ajustes": {"cols": "270px 320px 338px", "tk_size": 38, "vl_size": 36, "lin_h": 72, "tab_top": 492, "fim_top": 1066, "fim_size": 27, "data_top": 1168, "rod_top": 1220}})

ele = sorted(["CPFE3", "TAEE11", "CMIG4", "ISAE4", "CPLE3", "EQTL3", "EGIE3", "ALUP11"], key=lambda t: -D(A[t][2]))
add(ter, "18h", "eletricas-que-pagam-dividendos", "gen_tab.py", {
 "titulo": "Empresas de energia e quanto<br><b>pagaram de dividendos</b> <span class=\"emo\">⚡</span>",
 "colunas": ["Ação", "Cotação", "Dividend yield 12 meses", "100 ações pagaram"],
 "linhas": [[t, f"R$ {r2(A[t][0])}", pct(A[t][2]), f"R$ {brl(D(A[t][1]) * 100)}"] for t in ele], "destaque": 2,
 "data": f"Dados do StatusInvest em {DATA}. Proventos brutos dos últimos 12 meses",
 "rodape": ["Dividendos passados não garantem dividendos futuros", NAO_REC],
 "ajustes": {"cols": "236px 222px 232px 238px", "tk_size": 36, "vl_size": 33, "lin_h": 74, "cab_size": 18.5, "cab_h": 56, "tab_top": 492, "data_top": 1150, "rod_top": 1200, "data_size": 22}})

def meses_ate(aporte, alvo, taxa=D("0.01")):
    s, m = D(0), 0
    while s < alvo:
        m += 1; s = s * (1 + taxa) + aporte
    return m, s
def tempo(m):
    a_, r = divmod(m, 12)
    pa = f"{a_} ano" + ("s" if a_ > 1 else "") if a_ else ""
    pr = f"{r} " + ("meses" if r != 1 else "mês") if r else ""
    return " e ".join(x for x in (pa, pr) if x)
cem = []
for ap in (300, 500, 800, 1000, 1500, 2000, 3000):
    m, s = meses_ate(D(ap), D(100_000))
    cem.append([f"R$ {brl(ap, 0)}", tempo(m), f"R$ {brl(ap * m, 0)}"])
add(ter, "20h", "quanto-tempo-para-juntar-100-mil", "gen_tab.py", {
 "titulo": "Quanto tempo leva para<br>juntar <b>R$ 100 mil?</b> <span class=\"emo\">💰</span>",
 "colunas": ["Investindo por mês", "Tempo até R$ 100 mil", "Saiu do seu bolso"], "linhas": cem, "destaque": 1,
 "fim": "O que falta para os R$ 100 mil <b>vem dos juros</b>",
 "data": "Simulação com rendimento de 1,00% ao mês",
 "rodape": [HIP],
 "ajustes": {"cols": "300px 340px 288px", "tk_size": 38, "vl_size": 33, "lin_h": 78, "tab_top": 492, "fim_top": 1098, "data_top": 1160, "rod_top": 1210}})

# ------------------------------------------------ render
so = sys.argv[1:]
for dia, hora, slug, ger, cfg in posts:
    if so and slug not in so: continue
    fc = f"{CFG}/{slug}.json"; json.dump(cfg, open(fc, "w"), ensure_ascii=False, indent=1)
    subprocess.run(["python3", ger, fc, f"tmp_{slug}.html"], check=True, capture_output=True)
    subprocess.run(["python3", "render.py", f"tmp_{slug}.html", f"{OUT}/{hora} {slug}.png"], check=True)
    os.remove(f"tmp_{slug}.html")
json.dump([[d, h, s] for d, h, s, _, _ in posts], open(f"{CFG}/indice.json", "w"), ensure_ascii=False, indent=1)
print(len(posts), "posts")

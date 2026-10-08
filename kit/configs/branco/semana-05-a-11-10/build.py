#!/usr/bin/env python3
"""Gera os 24 posts de quarta 07/10 a domingo 11/10/2026 (modelo branco). Rodar em /home/claude/post."""
import json, os, subprocess, sys
from decimal import Decimal as D, ROUND_HALF_UP
sys.path.insert(0, ".")
from base import brl

OUT = "semana2/png"; CFG = "semana2/cfg"
os.makedirs(OUT, exist_ok=True); os.makedirs(CFG, exist_ok=True)
DATA = "02/10/26"
NAO_REC = "Não é uma recomendação de compra ou venda de ativos"

def r2(v): return brl(D(v))
def pct(v, casas=2): return brl(D(str(v).replace(",", ".")), casas) + "%"
def mi(v): return brl(D(v) / D(1_000_000_000), 0)

posts = []   # (dia, hora, slug, gerador, cfg)
def add(dia, hora, slug, ger, cfg): posts.append((dia, hora, slug, ger, cfg))

# ------------------------------------------------ dados (StatusInvest, fechamento de 02/10/26)
A = {  # ticker: (cotação, proventos 12m, DY 12m, P/L, P/VP, ROE, valor de mercado, valorização 12m)
 "PETR4": ("51.17", "3.6667", "7.17", "4,94", "1,37", "27,73%", "700076616412", "80,49"),
 "VALE3": ("72.10", "5.6125", "7.78", "30,87", "1,63", "5,27%", "320063418984", "29,96"),
 "ITUB4": ("44.83", "3.1354", "6.99", "10,56", "2,27", "21,50%", "517311114653", "31,47"),
 "BBDC4": ("19.23", "1.2596", "6.55", "8,28", "1,12", "13,56%", "190955101424", "20,19"),
 "ITSA4": ("14.67", "1.1317", "7.71"), "TAEE11": ("42.85", "3.0065", "7.02"), "BBSE3": ("40.45", "4.5901", "11.35"),
 "CMIG4": ("11.41", "0.7878", "6.90"), "ABEV3": ("15.84", "1.2505", "7.89"), "CXSE3": ("20.41", "1.3500", "6.61"),
 "SANB11": ("28.09", "2.3072", "8.21"), "CPFE3": ("48.09", "3.7359", "7.77"), "CMIN3": ("4.97", "0.3858", "7.76"),
 "TIMS3": ("18.55", "1.4721", "7.94"), "BLAU3": ("10.82", "0.9027", "8.34"), "KLBN11": ("18.62", "1.1727", "6.30"),
}
F = {  # FII: (cotação, último rendimento, pago em 12m, DY 12m, P/VP)
 "MXRF11": ("9.09", "0.10", "1.1950", "13.15", "0,98"), "HGLG11": ("147.90", "1.17", "13.41", "9.07", "0,89"),
 "KNRI11": ("157.91", "1.10", "13.21", "8.37", "0,97"), "XPML11": ("101.90", "0.92", "11.04", "10.83", "0,93"),
 "VISC11": ("105.51", "0.84", "9.99", "9.47", "0,91"), "BTLG11": ("100.00", "0.81", "9.62", "9.62", "0,93"),
 "KNCR11": ("105.50", "1.13", "13.92", "13.19", "1,03"), "CPTS11": ("7.56", "0.09", "1.08", "14.29", "0,87"),
 "HSML11": ("83.00", "0.75", "8.66", "10.43", "0,83"), "KNSC11": ("9.11", "0.08", "1.13", "12.40", "1,04"),
 "GARE11": ("8.39", "0.083", "0.996", "11.87", "0,93"), "GGRC11": ("8.91", "0.10", "1.20", "13.47", "0,82"),
 "RBVA11": ("8.67", "0.09", "1.08", "12.46", "0,81"), "SNEL11": ("7.96", "0.10", "1.20", "15.08", "0,99"),
 "VGIR11": ("9.65", "0.13", "1.51", "15.65", "0,98"), "LVBI11": ("96.84", "0.80", "9.10", "9.40", "0,80"),
 "PVBI11": ("65.50", "0.37", "4.99", "7.62", "0,63"), "XPLG11": ("93.81", "0.82", None, None, None),
 "HGRU11": ("114.40", "0.95", None, None, None), "BRCO11": ("109.87", "0.91", None, None, None),
}
CDI, SELIC, POUP_MES = D("13.65"), D("13.75"), D("0.6624")

# ================================================= QUARTA 07/10
add("3. quarta-feira 07-10", "07h", "dividendos-itausa", "gen_pag.py", {
 "titulo": "<b>Dividendos da Itaúsa</b>", "sub": "Quanto teria recebido se tivesse...", "ticker": "ITSA4", "logo": "assets/logo_txt_itausa.svg",
 "itens": [["Proventos por ação em 12 meses:", "R$ 1,1317"], ["Tipo:", "Dividendos e JCP"],
           ["Dividend yield:", "7,71%"], ["Cotação em 02/10:", "R$ 14,67"]],
 "valor_por_cota": "1.1317", "cotacao": "14.67", "quantidades": [100, 300, 500, 1000, 3000, 5000, 10000],
 "colunas": ["Qtd de ações", "Proventos em 12 meses", "Valor hoje"],
 "rodape": ["Proventos brutos com data COM nos últimos 12 meses", NAO_REC],
 "ajustes": {"quadro": 212, "itens_mt": 4, "item_h": 37.5, "cols": "0.82fr 1.2fr 0.98fr", "logo_w": 92}})

# renda fixa: R$ 100 mil por 1 ano, valores líquidos
ir = D("0.175")
rf = [("Poupança", "isenta de IR", D(100000) * ((1 + POUP_MES / 100) ** 12 - 1)),
      ("Tesouro Selic", "13,75% ao ano", D(100000) * SELIC / 100 * (1 - ir) - D(100000) * D("0.002")),
      ("CDB 100% do CDI", "13,65% ao ano", D(100000) * CDI / 100 * (1 - ir)),
      ("LCI e LCA 90% do CDI", "isentas de IR", D(100000) * CDI * D("0.9") / 100),
      ("CDB 110% do CDI", "15,02% ao ano", D(100000) * CDI * D("1.1") / 100 * (1 - ir))]
rf.sort(key=lambda x: x[2])
add("3. quarta-feira 07-10", "12h", "100-mil-renda-fixa", "gen_tab.py", {
 "titulo": "Quanto rende <b>R$ 100 mil</b><br>na renda fixa em 1 ano? <span class=\"emo\">👇</span>",
 "colunas": ["Investimento", "Por mês (média)", "Em 1 ano"],
 "linhas": [[f"{n}<small>{s}</small>", f"R$ {r2(v / 12)}", f"R$ {r2(v)}"] for n, s, v in rf], "destaque": 2,
 "data": "Valores líquidos, com Selic de 13,75% e CDI de 13,65% ao ano",
 "rodape": ["IR de 17,5% (1 ano) e taxa de custódia de 0,20% no Tesouro. Simulação", "Rentabilidade passada ou projetada não é garantia de retorno"],
 "ajustes": {"cols": "380px 264px 284px", "tk_size": 31, "vl_size": 37, "tab_top": 500, "lin_h": 106, "data_top": 1112, "rod_top": 1170, "rod_size": 22.5}})

def vs_bancos():
    a, b = A["ITUB4"], A["BBDC4"]
    return {"titulo": "<b>Itaú x Bradesco</b>", "sub": "Os números dos dois gigantes hoje",
     "empresas": [{"nome": "Itaú", "logo": "assets/logo_itau_wiki.svg", "fundo": "#ffffff", "logo_w": 92},
                  {"nome": "Bradesco", "logo": "assets/logo_bradesco_branco.svg", "fundo": "#e5173f", "logo_w": 90}],
     "linhas": [["Cotação", "em 02/10/2026", f"R$ {r2(a[0])}", f"R$ {r2(b[0])}"],
                ["Dividend yield", "últimos 12 meses", pct(a[2]), pct(b[2])],
                ["P/L", "preço sobre lucro", a[3], b[3]],
                ["P/VP", "preço sobre valor patrimonial", a[4], b[4]],
                ["ROE", "retorno sobre o patrimônio", a[5], b[5]],
                ["Valor de mercado", "", f"R$ {mi(a[6])} bi", f"R$ {mi(b[6])} bi"]],
     "rodape": ["Dados do StatusInvest. Ações ITUB4 e BBDC4", NAO_REC],
     "ajustes": {"tab_top": 478, "head_h": 182, "lin_h": 88, "cel_h": 66, "rod_top": 1236}}
add("3. quarta-feira 07-10", "18h", "itau-x-bradesco", "gen_vs.py", vs_bancos())

f10 = ["MXRF11", "VGIR11", "KNSC11", "GGRC11", "RBVA11", "GARE11", "SNEL11", "CPTS11"]
f10.sort(key=lambda t: -D(F[t][0]))
add("3. quarta-feira 07-10", "20h", "fiis-abaixo-de-10-reais", "gen_tab.py", {
 "titulo": "FIIs com cota <b>abaixo de R$ 10</b><br>que pagam todo mês <span class=\"emo\">👇</span>",
 "colunas": ["Fundo", "Cotação", "Último rendimento", "100 cotas rendem"],
 "linhas": [[t, f"R$ {r2(F[t][0])}", f"R$ {brl(D(F[t][1]), 3 if len(F[t][1].split('.')[1]) > 2 else 2)}", f"R$ {r2(D(F[t][1]) * 100)}"] for t in f10],
 "destaque": 3, "data": "Cotações de 02/10/26 e último rendimento anunciado",
 "rodape": ["Os rendimentos mudam todo mês", NAO_REC],
 "ajustes": {"cols": "222px 216px 250px 240px", "tk_size": 38, "vl_size": 34, "lin_h": 74, "cab_size": 19, "tab_top": 500}})

# ================================================= QUINTA 08/10
add("4. quinta-feira 08-10", "07h", "data-de-pagamento-tots3", "gen_pag.py", {
 "titulo": "Hoje é a <b>data de pagamento</b>", "sub": "Quanto teria recebido se tivesse...", "ticker": "TOTS3", "logo": "assets/logo_txt_totvs.svg",
 "itens": [["JCP por ação (bruto):", "R$ 0,15"], ["Valor líquido, após o IR:", "R$ 0,1275"],
           ["Data COM:", "23/09/2026"], ["DY deste pagamento:", "0,42%"]],
 "valor_por_cota": "0.1275", "cotacao": "35.55", "quantidades": [100, 300, 500, 1000, 3000, 5000, 10000],
 "colunas": ["Qtd de ações", "Valor líquido", "Valor investido"],
 "rodape": ["Valor investido pela cotação da data COM (R$ 35,55)", NAO_REC],
 "ajustes": {"quadro": 212, "itens_mt": 4, "item_h": 37.5, "logo_w": 92}})

sm = [(t, D(A[t][1]), A[t][0]) for t in ["BBSE3", "ITSA4", "PETR4", "TAEE11", "CMIG4", "BBDC4", "ITUB4", "ABEV3", "CXSE3"]]
add("4. quinta-feira 08-10", "10h", "salario-minimo-em-acoes", "gen_fii.py", {
 "salario": str(1621 * 12), "ordenar": True,
 "titulo": "Quanto preciso investir em cada<br>ação para <b>receber um salário<br>mínimo por mês? (R$ 1.621,00)</b>",
 "cabecalho": ["Ação", "Prov. 12 meses", "Preço", "Invest. Necessário"],
 "fundos": [[t, str(r.quantize(D("0.0001"))), p] for t, r, p in sm],
 "rodape": ["Com base nos proventos dos últimos 12 meses. Cotações de 02/10/26", NAO_REC],
 "ajustes": {"rod_top": 1218, "rod_size": 23}})

def meses_ate(aporte, alvo, taxa=D("0.01")):
    s, m = D(0), 0
    while s < alvo:
        m += 1; s = s * (1 + taxa) + aporte
    return m
def tempo(m):
    a, r = divmod(m, 12)
    pa = f"{a} ano" + ("s" if a > 1 else "") if a else ""
    pr = f"{r} " + ("meses" if r != 1 else "mês") if r else ""
    return " e ".join(x for x in (pa, pr) if x)
mil = []
for ap in (300, 500, 1000, 2000, 3000, 5000):
    m = meses_ate(D(ap), D(1_000_000)); mil.append([f"R$ {brl(ap, 0)}", tempo(m), f"R$ {brl(ap * m, 0)}"])
add("4. quinta-feira 08-10", "12h", "tempo-ate-1-milhao", "gen_tab.py", {
 "titulo": "Quanto tempo leva para<br>juntar <b>R$ 1 milhão?</b>",
 "colunas": ["Investindo por mês", "Tempo até R$ 1 milhão", "Saiu do seu bolso"], "linhas": mil, "destaque": 1,
 "data": "Simulação com rendimento de 1,00% ao mês",
 "rodape": ["Rentabilidade hipotética, não é garantia de retorno"],
 "ajustes": {"cols": "300px 340px 288px", "tk_size": 38, "vl_size": 33, "lin_h": 92, "tab_top": 492, "data_top": 1150, "rod_top": 1206}})

c100 = sorted(["ITSA4", "BBDC4", "ITUB4", "PETR4", "BBSE3", "TAEE11", "VALE3", "CMIG4"], key=lambda t: -D(A[t][1]))
add("4. quinta-feira 08-10", "18h", "dividendos-de-100-acoes", "gen_tab.py", {
 "titulo": "Quanto <b>100 ações</b> de cada empresa<br>pagaram em 12 meses? <span class=\"emo\">💰</span>",
 "colunas": ["Ação", "100 ações custam", "Proventos em 12 meses"],
 "linhas": [[t, f"R$ {brl(D(A[t][0]) * 100)}", f"R$ {brl(D(A[t][1]) * 100)}"] for t in c100], "destaque": 2,
 "data": "Cotações de 02/10/26 e proventos brutos dos últimos 12 meses",
 "rodape": [NAO_REC],
 "ajustes": {"cols": "250px 320px 358px", "tk_size": 40, "vl_size": 36, "lin_h": 76, "tab_top": 498, "rod_top": 1234}})

fi = [(t, F[t][1], F[t][0]) for t in ["HGLG11", "KNRI11", "XPML11", "VISC11", "BTLG11", "KNCR11", "MXRF11", "HSML11", "CPTS11"]]
add("4. quinta-feira 08-10", "20h", "1000-por-mes-em-fiis", "gen_fii.py", {
 "salario": "1000", "ordenar": True,
 "titulo": "Quanto preciso investir em cada<br>FII para <b>receber R$ 1.000,00<br>todo mês?</b>",
 "fundos": [[t, r, p] for t, r, p in fi],
 "rodape": ["Cotações de 02/10/26 e último rendimento de cada fundo", NAO_REC],
 "ajustes": {"rod_top": 1218, "rod_size": 23}})

# ================================================= SEXTA 09/10
add("5. sexta-feira 09-10", "07h", "data-de-pagamento-jhsf3", "gen_pag.py", {
 "titulo": "Hoje é a <b>data de pagamento</b>", "sub": "Quanto teria recebido se tivesse...", "ticker": "JHSF3", "logo": "assets/logo_txt_jhsf.svg",
 "itens": [["Dividendo por ação:", "R$ 0,0692"], ["Imposto de renda:", "isento"],
           ["Data COM:", "30/09/2026"], ["DY deste pagamento:", "0,59%"]],
 "valor_por_cota": "0.0691563395", "cotacao": "11.73", "quantidades": [100, 300, 500, 1000, 3000, 5000, 10000],
 "colunas": ["Qtd de ações", "Dividendos", "Valor investido"],
 "rodape": ["Valor investido pela cotação da data COM (R$ 11,73)", NAO_REC],
 "ajustes": {"quadro": 212, "itens_mt": 4, "item_h": 37.5, "logo_w": 92}})

def patrimonio(aporte, meses, taxa=D("0.01")):
    s = D(0)
    for _ in range(meses): s = s * (1 + taxa) + aporte
    return s
jc = []
for anos in (5, 10, 15, 20, 25, 30):
    s = patrimonio(D(500), anos * 12)
    jc.append([f"{anos} anos", f"R$ {brl(500 * anos * 12, 0)}", f"R$ {brl(s, 0)}"])
add("5. sexta-feira 09-10", "10h", "500-por-mes-juros-compostos", "gen_tab.py", {
 "titulo": "Investindo <b>R$ 500 por mês</b>,<br>quanto você teria? <span class=\"emo\">📈</span>",
 "colunas": ["Tempo", "Saiu do seu bolso", "Você teria"], "linhas": jc, "destaque": 2,
 "fim": f"Em 30 anos, <b>R$ {brl(patrimonio(D(500), 360) - 180000, 0)} vieram dos juros</b>",
 "data": "Simulação com rendimento de 1,00% ao mês",
 "rodape": ["Rentabilidade hipotética, não é garantia de retorno"],
 "ajustes": {"cols": "250px 320px 358px", "tk_size": 40, "vl_size": 37, "lin_h": 90, "tab_top": 492, "fim_top": 1088, "data_top": 1150, "rod_top": 1206}})

gig = sorted(["BBSE3", "SANB11", "ABEV3", "VALE3", "CPFE3", "ITSA4", "PETR4", "ITUB4"], key=lambda t: -D(A[t][2]))
add("5. sexta-feira 09-10", "12h", "gigantes-que-mais-pagam-dividendos", "gen_tab.py", {
 "titulo": "As gigantes da bolsa que<br><b>mais pagaram dividendos</b>",
 "sub": "Empresas com valor de mercado acima de R$ 50 bilhões",
 "colunas": ["Ação", "Cotação", "Dividend yield 12 meses"],
 "linhas": [[t, f"R$ {r2(A[t][0])}", pct(A[t][2])] for t in gig], "destaque": 2,
 "data": "Dados do StatusInvest em 02/10/26",
 "rodape": ["Dividendos passados não garantem dividendos futuros", NAO_REC],
 "ajustes": {"cols": "260px 300px 368px", "tk_size": 40, "vl_size": 37, "lin_h": 68, "tab_top": 524, "sub_top": 466, "sub_size": 28, "data_top": 1160, "rod_top": 1206}})

add("5. sexta-feira 09-10", "18h", "dividendos-taesa", "gen_pag.py", {
 "titulo": "<b>Dividendos da Taesa</b>", "sub": "Quanto teria recebido se tivesse...", "ticker": "TAEE11",
 "logo": "assets/logo_taee.png",
 "itens": [["Proventos por unit em 12 meses:", "R$ 3,0065"], ["Tipo:", "Dividendos e JCP"],
           ["Dividend yield:", "7,02%"], ["Cotação em 02/10:", "R$ 42,85"]],
 "valor_por_cota": "3.0065", "cotacao": "42.85", "quantidades": [10, 30, 50, 100, 300, 500, 1000],
 "colunas": ["Qtd de units", "Proventos em 12 meses", "Valor hoje"],
 "rodape": ["Proventos brutos com data COM nos últimos 12 meses", NAO_REC],
 "ajustes": {"quadro": 212, "itens_mt": 4, "item_h": 37.5, "cols": "0.82fr 1.2fr 0.98fr", "logo_w": 92}})

pop = ["HGLG11", "KNRI11", "XPML11", "VISC11", "BTLG11", "KNCR11", "HSML11", "MXRF11"]
add("5. sexta-feira 09-10", "20h", "fiis-mais-populares-12-meses", "gen_tab.py", {
 "titulo": "Quanto os FIIs mais famosos<br><b>pagaram em 12 meses</b> <span class=\"emo\">🏢</span>",
 "colunas": ["Fundo", "Cotação", "Pago por cota em 12 meses", "Dividend yield"],
 "linhas": [[t, f"R$ {r2(F[t][0])}", f"R$ {r2(F[t][2])}", pct(F[t][3])] for t in pop], "destaque": 3,
 "data": "Dados do StatusInvest em 02/10/26",
 "rodape": ["Rendimentos passados não garantem rendimentos futuros", NAO_REC],
 "ajustes": {"cols": "226px 230px 262px 210px", "tk_size": 37, "vl_size": 33, "lin_h": 74, "cab_size": 18.5, "tab_top": 498, "data_top": 1150, "rod_top": 1200}})

# ================================================= SÁBADO 10/10
ts = D(10000) * SELIC / 100 * (1 - ir); pp = D(10000) * ((1 + POUP_MES / 100) ** 12 - 1)
add("6. sábado 10-10", "07h", "tesouro-selic-x-poupanca", "gen_vs.py", {
 "titulo": "<b>Tesouro Selic x Poupança</b>", "sub": "Onde deixar a sua reserva?",
 "empresas": [{"nome": "Tesouro Selic", "logo": "assets/logo_tesouro.svg", "fundo": "#eef3fb", "logo_w": 78},
              {"nome": "Poupança", "logo": "assets/logo_poupanca.svg", "fundo": "#fdeef3", "logo_w": 78}],
 "linhas": [["Rendimento", "ao ano, antes do IR", "13,75%", "8,24%"],
            ["Imposto de renda", "", "22,5% a 15%", "Isenta"],
            ["R$ 10 mil em 1 ano", "lucro líquido", f"R$ {brl(ts, 0)}", f"R$ {brl(pp, 0)}", "pos", ""],
            ["Garantia", "", "Tesouro Nacional", "FGC"],
            ["Resgate", "", "Todo dia útil", "Qualquer dia"]],
 "rodape": ["Selic de 13,75% ao ano e poupança de 0,66% ao mês (out/26). Simulação", "IR de 17,5% para 1 ano. Até R$ 10 mil, o Tesouro Selic não cobra custódia"],
 "ajustes": {"rod_top": 1218, "rod_size": 22, "val_size": 33}})

viver = []
for renda in (3000, 5000, 10000, 20000):
    viver.append([f"R$ {brl(renda, 0)}", f"R$ {brl(D(renda) / D('0.008'), 0)}", f"R$ {brl(D(renda) / D('0.01'), 0)}"])
add("6. sábado 10-10", "10h", "quanto-precisa-para-viver-de-renda", "gen_tab.py", {
 "titulo": "Quanto você precisa ter<br>investido para <b>viver de renda?</b>",
 "colunas": ["Renda por mês", "Rendendo 0,80% ao mês", "Rendendo 1,00% ao mês"], "linhas": viver,
 "fim": "Para manter o poder de compra, o ideal é<br><b>reinvestir uma parte para cobrir a inflação</b>",
 "data": "Simulação. Rendimentos líquidos e hipotéticos",
 "rodape": ["Rentabilidade hipotética, não é garantia de retorno"],
 "ajustes": {"cols": "268px 330px 330px", "tk_size": 36, "vl_size": 36, "lin_h": 104, "tab_top": 500, "fim_top": 1012, "data_top": 1150, "rod_top": 1206}})

bar = sorted(["ITSA4", "BBDC4", "CMIG4", "CMIN3", "TIMS3", "BLAU3", "KLBN11", "ABEV3"], key=lambda t: -D(A[t][2]))
add("6. sábado 10-10", "12h", "acoes-abaixo-de-20-reais", "gen_tab.py", {
 "titulo": "Ações <b>abaixo de R$ 20</b> que<br>pagam dividendos <span class=\"emo\">👇</span>",
 "colunas": ["Ação", "Cotação", "Dividend yield 12 meses"],
 "linhas": [[t, f"R$ {r2(A[t][0])}", pct(A[t][2])] for t in bar], "destaque": 2,
 "data": "Dados do StatusInvest em 02/10/26",
 "rodape": ["Dividendos passados não garantem dividendos futuros", NAO_REC],
 "ajustes": {"cols": "260px 300px 368px", "tk_size": 40, "vl_size": 37, "lin_h": 76, "tab_top": 498, "data_top": 1150, "rod_top": 1200}})

add("6. sábado 10-10", "18h", "dividendos-cemig", "gen_pag.py", {
 "titulo": "<b>Dividendos da Cemig</b>", "sub": "Quanto teria recebido se tivesse...", "ticker": "CMIG4",
 "logo": "assets/logo_cmig.png",
 "itens": [["Proventos por ação em 12 meses:", "R$ 0,7878"], ["Tipo:", "Dividendos e JCP"],
           ["Dividend yield:", "6,90%"], ["Cotação em 02/10:", "R$ 11,41"]],
 "valor_por_cota": "0.7878", "cotacao": "11.41", "quantidades": [100, 300, 500, 1000, 3000, 5000, 10000],
 "colunas": ["Qtd de ações", "Proventos em 12 meses", "Valor hoje"],
 "rodape": ["Proventos brutos com data COM nos últimos 12 meses", NAO_REC],
 "ajustes": {"quadro": 212, "itens_mt": 4, "item_h": 37.5, "cols": "0.82fr 1.2fr 0.98fr", "logo_w": 92}})

p_, v_ = A["PETR4"], A["VALE3"]
add("6. sábado 10-10", "20h", "petrobras-x-vale", "gen_vs.py", {
 "titulo": "<b>Petrobras x Vale</b>", "sub": "As duas gigantes da bolsa hoje",
 "empresas": [{"nome": "Petrobras", "logo": "assets/logo_petrobras.svg", "fundo": "#ffffff", "logo_w": 70},
              {"nome": "Vale", "logo": "assets/logo_vale.svg", "fundo": "#ffffff", "logo_w": 84}],
 "linhas": [["Cotação", "em 02/10/2026", f"R$ {r2(p_[0])}", f"R$ {r2(v_[0])}"],
            ["Dividend yield", "últimos 12 meses", pct(p_[2]), pct(v_[2])],
            ["P/L", "preço sobre lucro", p_[3], v_[3]],
            ["ROE", "retorno sobre o patrimônio", p_[5], v_[5]],
            ["Valorização", "últimos 12 meses", "+" + pct(p_[7]), "+" + pct(v_[7]), "pos", "pos"],
            ["Valor de mercado", "", f"R$ {mi(p_[6])} bi", f"R$ {mi(v_[6])} bi"]],
 "rodape": ["Dados do StatusInvest. Ações PETR4 e VALE3", NAO_REC],
 "ajustes": {"tab_top": 478, "head_h": 182, "lin_h": 88, "cel_h": 66, "rod_top": 1236}})

# ================================================= DOMINGO 11/10
def aporte_para(alvo, meses, taxa=D("0.01")):
    fator = ((1 + taxa) ** meses - 1) / taxa
    return alvo / fator
ap = []
for anos in (10, 15, 20, 25, 30):
    a = aporte_para(D(1_000_000), anos * 12)
    ap.append([f"{anos} anos", f"R$ {brl(a, 2)}", f"R$ {brl(a * anos * 12, 0)}"])
add("7. domingo 11-10", "07h", "quanto-investir-para-1-milhao", "gen_tab.py", {
 "titulo": "Quanto investir por mês para<br>ter <b>R$ 1 milhão?</b> <span class=\"emo\">🎯</span>",
 "colunas": ["Em quanto tempo", "Investindo por mês", "Saiu do seu bolso"], "linhas": ap, "destaque": 1,
 "fim": "Quanto antes começar, <b>menos sai do seu bolso</b>",
 "data": "Simulação com rendimento de 1,00% ao mês",
 "rodape": ["Rentabilidade hipotética, não é garantia de retorno"],
 "ajustes": {"cols": "280px 330px 318px", "tk_size": 38, "vl_size": 36, "lin_h": 100, "tab_top": 496, "fim_top": 1090, "data_top": 1150, "rod_top": 1206}})

add("7. domingo 11-10", "10h", "dividendos-itau", "gen_pag.py", {
 "titulo": "<b>Dividendos do Itaú</b>", "sub": "Quanto teria recebido se tivesse...", "ticker": "ITUB4",
 "logo": "assets/logo_itau_wiki.svg",
 "itens": [["Proventos por ação em 12 meses:", "R$ 3,1354"], ["Tipo:", "Dividendos e JCP"],
           ["Dividend yield:", "6,99%"], ["Cotação em 02/10:", "R$ 44,83"]],
 "valor_por_cota": "3.1354", "cotacao": "44.83", "quantidades": [10, 30, 50, 100, 300, 500, 1000],
 "colunas": ["Qtd de ações", "Proventos em 12 meses", "Valor hoje"],
 "rodape": ["Proventos brutos com data COM nos últimos 12 meses", NAO_REC],
 "ajustes": {"quadro": 212, "itens_mt": 4, "item_h": 37.5, "cols": "0.82fr 1.2fr 0.98fr", "logo_w": 100}})

p5 = {"PETR4": ("8.59", "51.17"), "BBSE3": ("12.27", "40.45"), "ITUB4": ("16.68", "44.83"), "ITSA4": ("6.11", "14.67"),
      "BBAS3": ("10.65", "23.72"), "TAEE11": ("23.21", "42.85"), "WEGE3": ("33.75", "51.45"), "BBDC4": ("13.86", "19.23")}
lin5 = sorted(([t, D(1000) * D(b) / D(a)] for t, (a, b) in p5.items()), key=lambda x: -x[1])
lin5 = [[t, f"R$ {brl(v, 0)}", ("+" if v >= 1000 else "") + pct((v / 1000 - 1) * 100)] for t, v in lin5]
cdi5 = D("1000") * D("1.8126058")
lin5.append(["CDI<small>referência</small>", f"R$ {brl(cdi5, 0)}", "+" + pct((cdi5 / 1000 - 1) * 100)])
add("7. domingo 11-10", "12h", "1000-reais-ha-5-anos", "gen_tab.py", {
 "titulo": "Quanto valeriam hoje <b>R$ 1.000</b><br>investidos há 5 anos? <span class=\"emo\">⏳</span>",
 "colunas": ["Investimento", "Valeria hoje", "Variação"], "linhas": lin5, "destaque": 1,
 "data": "De 05/10/2021 a 02/10/2026",
 "rodape": ["Cotações ajustadas por proventos (StatusInvest) e CDI acumulado (Banco Central)", "Rentabilidade passada não é garantia de retorno futuro"],
 "ajustes": {"cols": "292px 336px 300px", "tk_size": 37, "vl_size": 34, "lin_h": 67, "tab_top": 494, "data_top": 1170, "rod_top": 1218, "rod_size": 22}})

tij = sorted(["HGLG11", "XPML11", "VISC11", "BTLG11", "HSML11", "LVBI11", "KNRI11", "PVBI11"], key=lambda t: D(F[t][4].replace(",", ".")))
add("7. domingo 11-10", "18h", "fiis-de-tijolo-p-vp-abaixo-de-1", "gen_tab.py", {
 "titulo": "FIIs de tijolo negociados<br><b>abaixo do valor patrimonial</b>",
 "colunas": ["Fundo", "Cotação", "P/VP", "Dividend yield"],
 "linhas": [[t, f"R$ {r2(F[t][0])}", F[t][4], pct(F[t][3])] for t in tij], "destaque": 2,
 "fim": "P/VP abaixo de 1 não quer dizer que o fundo está barato.<br><b>Vale olhar vacância, inadimplência e a qualidade dos imóveis</b>",
 "data": "Dados do StatusInvest em 02/10/26",
 "rodape": [NAO_REC],
 "ajustes": {"cols": "232px 250px 196px 250px", "tk_size": 37, "vl_size": 34, "lin_h": 66, "tab_top": 496, "fim_top": 1074, "fim_size": 25, "data_top": 1162, "rod_top": 1214}})

ag = [("KNCR11", "14/10"), ("MXRF11", "15/10"), ("HGLG11", "15/10"), ("KNRI11", "15/10"), ("VISC11", "15/10"),
      ("XPLG11", "15/10"), ("HGRU11", "15/10"), ("BRCO11", "15/10")]
add("7. domingo 11-10", "20h", "agenda-fiis-semana", "gen_tab.py", {
 "titulo": "FIIs que <b>pagam nesta semana</b> <span class=\"emo\">🗓️</span>",
 "sub": "Rendimentos de 12 a 16 de outubro",
 "colunas": ["Fundo", "Pagamento", "Valor por cota", "Rendimento no mês"],
 "linhas": [[t, d, f"R$ {r2(F[t][1])}", pct(D(F[t][1]) / D(F[t][0]) * 100)] for t, d in ag], "destaque": 2,
 "data": "Rendimento no mês sobre a cotação de 02/10/26",
 "rodape": ["Recebe quem tinha as cotas na data COM, em 30/09", NAO_REC],
 "ajustes": {"cols": "232px 220px 246px 230px", "tk_size": 37, "vl_size": 33, "lin_h": 72, "cab_size": 18.5, "tab_top": 520, "sub_top": 412, "data_top": 1150, "rod_top": 1200}})

# ------------------------------------------------ render
so = sys.argv[1:]
for dia, hora, slug, ger, cfg in posts:
    if so and slug not in so: continue
    fc = f"{CFG}/{slug}.json"; json.dump(cfg, open(fc, "w"), ensure_ascii=False, indent=1)
    subprocess.run(["python3", ger, fc, f"s2_{slug}.html"], check=True, capture_output=True)
    subprocess.run(["python3", "render.py", f"s2_{slug}.html", f"{OUT}/{slug}.png"], check=True)
json.dump([[d, h, s] for d, h, s, _, _ in posts], open("semana2/indice.json", "w"), ensure_ascii=False, indent=1)
print(len(posts), "posts")

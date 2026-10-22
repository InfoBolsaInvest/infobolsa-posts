"""Slides do 2º turno 2026 no estilo do post do 1º turno (cards claros, números grandes), tema verde InfoBolsa.
Uso: python3 gen_eleicao.py N saida.html  (N = 1..5)"""
import sys
from gen_inst import pagina

VERM, AZUL = "#e5383b", "#2f6fe0"
FOTO = {"lula": ("assets/lula.jpg", "50% 14%"), "flavio": ("assets/flavio.jpg", "50% 14%"), "jair": ("assets/jair.jpg", "50% 18%")}
CSS = """<style>
.av{border-radius:50%;background-size:cover;flex:none;border:5px solid var(--c)}
.cd{position:absolute;left:96px;width:888px;background:#fff;border:1.5px solid var(--borda);border-radius:24px;box-shadow:0 8px 30px rgba(22,37,38,.06)}
.yr{display:inline-block;background:#162526;color:#fff;font-weight:600;font-size:22px;padding:4px 16px;border-radius:8px}
.pr{position:absolute;display:flex;align-items:center;gap:22px}
.pr .t{font-size:24px;line-height:1.15;color:var(--sub)}
.pr .n{font-weight:700;font-size:66px;line-height:1;letter-spacing:-2px}
.x{position:absolute;font-size:34px;color:var(--mute);font-weight:300}
.ch{position:absolute;left:96px;width:888px;background:#eef4f0;border-radius:18px;padding:20px 28px;font-size:25px;line-height:1.3;color:var(--sub)}
.ch b{color:var(--fg);font-weight:600}
.ch small{display:block;font-size:20px;color:var(--mute);margin-top:4px}
.cta{position:absolute;left:0;right:0;text-align:center;font-weight:600;font-size:30px}
.tbl{position:absolute;left:96px;width:888px;border-top:3px solid #162526}
.tbl .r{display:grid;grid-template-columns:1.25fr 1fr 1fr;column-gap:14px;align-items:center;border-bottom:1.5px solid #cfdcd3;padding:13px 0}
.tbl .h{font-weight:700;font-size:38px;text-align:center}
.tbl .l b{display:block;font-weight:600;font-size:24px}.tbl .l small{font-size:18px;color:var(--mute)}
.tbl .v{background:#e8efea;border-radius:14px;text-align:center;font-weight:600;font-size:32px;padding:11px 6px;line-height:1.15}
.tbl .v small{display:block;font-weight:400;font-size:16px;color:var(--mute)}
</style>"""

def av(k, size, cor, x=None, y=None, extra=""):
    img, pos = FOTO[k]
    pos_css = f"left:{x}px;top:{y}px;position:absolute;" if x is not None else ""
    return f'<div class="av" style="--c:{cor};width:{size}px;height:{size}px;background-image:url({img});background-position:{pos};{pos_css}{extra}"></div>'

def s1():
    def par(y, ano, a, b):
        (ka, na, pa, ca), (kb, nb, pb, cb) = a, b
        return (f'<div class="cd" style="top:{y}px;height:262px"></div>'
                f'<div style="position:absolute;left:128px;top:{y+22}px" class="yr">{ano}</div>'
                f'<div class="pr" style="left:128px;top:{y+80}px">{av(ka,128,ca)}<div><div class="t">{na}</div><div class="n" style="color:{ca}">{pa}</div></div></div>'
                f'<div class="x" style="left:526px;top:{y+120}px">x</div>'
                f'<div class="pr" style="right:128px;top:{y+80}px"><div style="text-align:right"><div class="t">{nb}</div><div class="n" style="color:{cb}">{pb}</div></div>{av(kb,128,cb)}</div>')
    corpo = (CSS + par(410, "2022", ("lula", "Lula", "48,43%", VERM), ("jair", "Jair Bolsonaro", "43,20%", AZUL))
             + par(710, "2026", ("flavio", "Flávio Bolsonaro", "47,03%", AZUL), ("lula", "Lula", "45,16%", VERM))
             + '<div class="cta" style="top:1030px">Arrasta pro lado e compara 👉</div>')
    return pagina("verde", "O que <span>mudou</span> e o que<br><span>continuou igual</span>", "1º turno para presidente, percentual de votos válidos", corpo,
                  ["Fonte: TSE, resultado final do 1º turno de 2026 (04/10) e de 2022.", "Fotos: Agência Senado, Ricardo Stuckert/PR e Alan Santos/PR"], tsize=66)

def s2():
    def y(v): return 540 + (49.5 - v) / 7.5 * 470
    xs = (300, 780)
    pts = [("lula", 48.43, "48,43%", "Lula", VERM, 0), ("jair", 43.20, "43,20%", "Jair Bolsonaro", AZUL, 0),
           ("flavio", 47.03, "47,03%", "Flávio Bolsonaro", AZUL, 1), ("lula", 45.16, "45,16%", "Lula", VERM, 1)]
    svg = (f'<svg style="position:absolute;left:0;top:0" width="1080" height="1350">'
           f'<line x1="{xs[0]}" y1="{y(48.43)}" x2="{xs[1]}" y2="{y(45.16)}" stroke="{VERM}" stroke-width="7"/>'
           f'<line x1="{xs[0]}" y1="{y(43.20)}" x2="{xs[1]}" y2="{y(47.03)}" stroke="{AZUL}" stroke-width="7"/>'
           f'<line x1="130" y1="{y(50)}" x2="950" y2="{y(50)}" stroke="#9aaca4" stroke-width="2" stroke-dasharray="6 7"/></svg>')
    labs = ""
    for k, v, t, nome, cor, col in pts:
        cx = xs[col]; cy = y(v)
        labs += av(k, 80, cor, cx - 40, cy - 40)
        if col == 0:
            labs += f'<div style="position:absolute;right:{1080-cx+54}px;top:{cy-34}px;text-align:right;color:{cor}"><div style="font-weight:700;font-size:44px;line-height:1">{t}</div><div style="font-size:19px;color:var(--sub)">{nome}</div></div>'
        else:
            labs += f'<div style="position:absolute;left:{cx+54}px;top:{cy-34}px;color:{cor}"><div style="font-weight:700;font-size:44px;line-height:1">{t}</div><div style="font-size:19px;color:var(--sub)">{nome}</div></div>'
    anos = f'<div style="position:absolute;left:{xs[0]-60}px;top:432px;width:120px;text-align:center;font-weight:700;font-size:34px">2022</div><div style="position:absolute;left:{xs[1]-60}px;top:432px;width:120px;text-align:center;font-weight:700;font-size:34px">2026</div>'
    meta = f'<div style="position:absolute;left:130px;top:{y(50)+8}px;font-size:18px;color:var(--mute);line-height:1.2">Acima de 50%:<br>vitória no 1º turno</div>'
    ch = (f'<div class="ch" style="top:1010px;padding:14px 26px"><span class="yr" style="font-size:19px">2022</span> <b>Lula</b> na frente por <b>5,23 pontos</b><small>6,19 milhões de votos a mais que o segundo colocado</small></div>'
          f'<div class="ch" style="top:1118px;padding:14px 26px"><span class="yr" style="font-size:19px">2026</span> <b>Flávio Bolsonaro</b> na frente por <b>1,87 pontos</b><small>2,22 milhões de votos a mais que o segundo colocado</small></div>')
    return pagina("verde", "A liderança <span>mudou de lado</span>", "Votos válidos no 1º turno para presidente", CSS + svg + labs + anos + meta + ch,
                  ["Fonte: TSE. Fotos: Agência Senado, Ricardo Stuckert/PR e Alan Santos/PR"], tsize=62)

def s3():
    def lin(t, s, a, b):
        return f'<div class="r"><div class="l"><b>{t}</b><small>{s}</small></div><div class="v">{a}</div><div class="v">{b}</div></div>'
    tb = (f'<div class="tbl" style="top:410px"><div class="r" style="border-bottom:3px solid #162526"><div></div><div class="h">2022</div><div class="h">2026</div></div>'
          + lin("Os dois primeiros", "soma dos percentuais", "91,63%", "92,19%")
          + lin("Terceiro colocado", "percentual dos votos válidos", "<small>Simone Tebet</small>4,16%", "<small>Augusto Cury</small>2,89%")
          + lin("Abstenção", "eleitores que não votaram", "20,95%", "21,08%")
          + lin("Brancos e nulos", "sobre o total de votos", "4,41%", "4,77%")
          + lin("Como terminou", "o 1º turno", "2º turno", "2º turno") + '</div>')
    fim = '<div style="position:absolute;left:96px;right:96px;top:1090px;text-align:center;font-size:27px;line-height:1.35;color:var(--sub)">Nos dois anos, <b style="color:var(--fg);font-weight:600">mais de 9 em cada 10 votos válidos</b><br>foram para os dois primeiros colocados</div>'
    return pagina("verde", "O que <span>continuou igual</span>", "A disputa segue concentrada em dois nomes", CSS + tb + fim,
                  ["Fonte: TSE, resultado final do 1º turno de 2026 (04/10) e de 2022."], tsize=62)

def s4():
    def card(x, ano, ib, ibt, dl, dlt):
        return (f'<div class="cd" style="left:{x}px;width:430px;top:440px;height:470px"></div>'
                f'<div class="yr" style="position:absolute;left:{x+28}px;top:466px">{ano}</div>'
                f'<div style="position:absolute;left:{x+28}px;top:530px;font-size:21px;color:var(--mute)">Ibovespa no dia seguinte ao 1º turno</div>'
                f'<div style="position:absolute;left:{x+28}px;top:560px;font-weight:700;font-size:78px;letter-spacing:-2px;color:#0f7a43">{ib}</div>'
                f'<div style="position:absolute;left:{x+28}px;top:668px;font-size:20px;color:var(--sub)">{ibt}</div>'
                f'<div style="position:absolute;left:{x+28}px;top:730px;font-size:21px;color:var(--mute)">Dólar no mesmo dia</div>'
                f'<div style="position:absolute;left:{x+28}px;top:760px;font-weight:700;font-size:78px;letter-spacing:-2px;color:#d4343a">{dl}</div>'
                f'<div style="position:absolute;left:{x+28}px;top:868px;font-size:20px;color:var(--sub)">{dlt}</div>')
    corpo = (CSS + card(96, "2022", "+5,54%", "de 110.037 para 116.134 pontos", "-3,82%", "de R$ 5,4066 para R$ 5,2002")
             + card(554, "2026", "+7,70%", "de 192.115 para 206.912 pontos", "-4,12%", "de R$ 5,22 para cerca de R$ 5,00")
             + '<div style="position:absolute;left:96px;right:96px;top:960px;text-align:center;font-size:27px;line-height:1.4;color:var(--sub)">Nos dois anos, a primeira reação do mercado saiu na<br>segunda-feira seguinte ao 1º turno. <b style="color:var(--fg);font-weight:600">O que aconteceu antes<br>não indica o que vai acontecer agora.</b></div>')
    return pagina("verde", "Como a <span>bolsa reagiu</span>", "Ibovespa e dólar depois do 1º turno, 2022 e 2026", corpo,
                  ["Não é uma recomendação de compra ou venda de ativos.", "Fontes: B3 e Banco Central (dólar PTAX de venda em 2022), via StatusInvest, Bora Investir e Jornal do Comércio."], tsize=62)

def s5():
    def barra(y, rot, sub, w, cor, txt, pont=False):
        b = (f'<div style="position:absolute;left:340px;top:{y+6}px;width:{w}px;height:46px;border-radius:8px;background:{cor}"></div>' if not pont else
             f'<div style="position:absolute;left:340px;top:{y+6}px;width:120px;height:46px;border-radius:8px;border:3px dashed #9aaca4"></div>')
        t = f'<div style="position:absolute;left:{340+(w if not pont else 120)+16}px;top:{y+10}px;font-size:25px;line-height:1.1;color:var(--fg)">{txt}</div>'
        return f'<div style="position:absolute;left:128px;top:{y}px;font-size:23px;line-height:1.15;font-weight:500">{rot}</div>' + b + t
    av2 = (f'<div style="position:absolute;left:0;right:0;top:370px;display:flex;justify-content:center;gap:90px;align-items:center">'
           f'<div style="text-align:center">{av("flavio",150,AZUL).replace("position:absolute;","")}<div style="font-weight:600;font-size:26px;margin-top:10px">Flávio Bolsonaro</div><div style="font-size:19px;color:var(--mute)">47,03% no 1º turno</div></div>'
           f'<div style="font-size:36px;color:var(--mute)">x</div>'
           f'<div style="text-align:center">{av("lula",150,VERM)}<div style="font-weight:600;font-size:26px;margin-top:10px">Lula</div><div style="font-size:19px;color:var(--mute)">45,16% no 1º turno</div></div></div>')
    cd = '<div class="cd" style="top:740px;height:410px"></div><div style="position:absolute;left:128px;top:764px;font-size:22px;color:var(--sub)">A vantagem de quem liderou, em pontos percentuais (p.p.)</div>'
    bs = (barra(830, "1º turno<br>de 2022", "", 350, VERM, "<b>5,23 p.p.</b> para Lula")
          + barra(910, "2º turno<br>de 2022", "", 121, VERM, "<b>1,80 p.p.</b> para Lula")
          + barra(990, "1º turno<br>de 2026", "", 125, AZUL, "<b>1,87 p.p.</b> para Flávio")
          + barra(1070, "2º turno<br>de 2026", "", 0, "", "<span style='color:var(--mute)'>sai hoje à noite</span>", pont=True))
    cta = '<div class="cta" style="top:1185px;font-size:28px">👉 Salva pra comparar com o resultado de hoje</div>'
    return pagina("verde", "E agora? <span>2º turno</span><br>hoje, 25 de outubro", "", CSS + av2 + cd + bs + cta,
                  ["Fonte: TSE. Fotos: Agência Senado, Ricardo Stuckert/PR e Alan Santos/PR"], tsize=62).replace('top:196px','top:196px')

if __name__ == "__main__":
    open(sys.argv[2], "w").write({"1": s1, "2": s2, "3": s3, "4": s4, "5": s5}[sys.argv[1]]())

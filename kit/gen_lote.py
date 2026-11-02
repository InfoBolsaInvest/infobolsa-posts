import json, math, os, subprocess
from base import brl
R=lambda v,c=2:"R$ "+brl(v,c)
P=lambda v:brl(v,2)+"%"
def i_m(a): return (1+a)**(1/12)-1
def fv(pmt,anos,a=.10):
    i=i_m(a);n=anos*12;return pmt*((1+i)**n-1)/i
def pmt_p(meta,anos,a=.10):
    i=i_m(a);n=anos*12;return meta*i/((1+i)**n-1)
def anosmeses(x):
    m=round(x*12);a,mm=divmod(m,12)
    s=f"{a} anos" if a!=1 else "1 ano"
    if mm: s+=f" e {mm} {'meses' if mm>1 else 'mês'}"
    return s
SIM="Simulação com rendimento de 10,00% ao ano, constante, sem imposto e sem inflação."
HIP="Rentabilidade hipotética, não é garantia de retorno."
NR="Não é uma recomendação de compra ou venda."
posts=[]
def add(slug,cfg,leg): posts.append((slug,cfg,leg))
BASE=dict(tsize=76,top=445)

# 1 sobra pouco
rows=[[f"<b>{R(m,2)}</b>",brl(fv(m,10),2),brl(fv(m,20),2),brl(fv(m,30),2)] for m in (100,200,300,500,1000)]
add("01-sobra-pouco",dict(titulo="“Não sobra nada<br>pra <span>investir</span>”",sub="Olha o que <b>R$ 100 por mês</b> viram com o tempo 👇",aba="Guardando todo mês",colunas=["Guardando por mês","Em 10 anos (R$)","Em 20 anos (R$)","Em 30 anos (R$)"],cols="1.1fr 1fr 1fr 1.1fr",lh=88,destaque=3,linhas=rows,fim="Não precisa ser rico. <b>Precisa começar.</b>",rodape=[SIM,HIP,NR],tsize=80,top=450),
f"“Não sobra nada pra investir” é a frase que mais escuto 💬\n\nMas olha a conta: guardando só {R(100,2)} por mês, em 30 anos você junta {R(fv(100,30),2)}. Com {R(500,2)} por mês, são {R(fv(500,30),2)}. O segredo não é o valor, é a constância.\n\nComeça pequeno, mas começa. Aumenta o valor quando der.\n\nManda pra aquele amigo que vive dizendo que não sobra nada. E me segue se você tá começando agora.\n\n👉 Quanto você consegue guardar por mês? Comenta aqui!\n\n{SIM}\n{HIP}\n{NR}\n\n#investimentos #educacaofinanceira #comecaraninvestir #jurosCompostos #rendapassiva")

# 2 juntar 100 mil
rows=[]
for a in (5,10,15,20):
    p=pmt_p(100000,a);tot=p*a*12
    rows.append([f"<b>{a} anos</b>",R(p,2),R(tot,2),R(100000-tot,2)])
add("02-100-mil",dict(titulo="Como juntar<br><span>R$ 100 mil</span>",sub="Quanto guardar por mês em cada prazo 👇",aba="Meta de R$ 100.000,00",colunas=["Prazo","Guardar por mês","Sai do seu bolso","Os juros fazem"],cols="0.8fr 1.1fr 1.1fr 1.1fr",lh=96,destaque=3,linhas=rows,fim="Quanto mais tempo, <b>mais o juro trabalha por você.</b>",rodape=[SIM,HIP,NR],tsize=84,top=450),
f"Como juntar R$ 100 mil? 💰\n\nEm 20 anos, guardando {R(pmt_p(100000,20),2)} por mês, o dinheiro que sai do seu bolso é {R(pmt_p(100000,20)*240,2)}. O resto, {R(100000-pmt_p(100000,20)*240,2)}, são juros trabalhando por você. Em 5 anos o esforço é bem maior: {R(pmt_p(100000,5),2)} por mês.\n\nO tempo é o melhor aliado de quem investe.\n\nManda pra quem tem o sonho dos 100 mil. E me segue pra aprender a chegar lá.\n\n👉 Em quanto tempo você quer juntar os seus R$ 100 mil? Comenta aqui!\n\n{SIM}\n{HIP}\n{NR}\n\n#investimentos #100mil #educacaofinanceira #jurosCompostos #dinheiro")

# 3 renda por mes
rows=[[f"<b>{R(r,2)}</b> por mês",R(r/.008,2),R(r*12,2)] for r in (1000,2000,3000,5000,10000)]
add("03-renda-mensal",dict(titulo="Quanto preciso ter pra<br>receber <span>R$ 1.000</span> por mês?",sub="Renda passiva, de acordo com o seu sonho 👇",aba="Patrimônio necessário",colunas=["Renda que você quer","Você precisa ter","Recebe por ano"],cols="1.1fr 1.1fr 1fr",lh=88,destaque=1,linhas=rows,fim="Ninguém começa com isso. <b>Dá pra montar aos poucos.</b>",rodape=["Considera rendimento de 0,80% ao mês (cerca de 10,03% ao ano). Rendimentos passados não garantem rendimentos futuros.",HIP,NR],tsize=70,top=450),
f"Quanto você precisa ter pra receber R$ 1.000 por mês? 🏢\n\nA conta é simples: com um rendimento de 0,80% ao mês, são {R(1000/.008,2)} pra receber R$ 1.000,00 por mês. Pra R$ 3.000,00 por mês, {R(3000/.008,2)}. Parece muito? Ninguém monta isso de uma vez: vai comprando aos poucos, mês a mês.\n\nÉ assim que funciona a renda passiva com fundos imobiliários, por exemplo.\n\nManda pra quem sonha em viver de renda. E me segue se você quer montar a sua.\n\n👉 Quanto você queria receber por mês? Comenta aqui!\n\nSimulação com rendimento de 0,80% ao mês, constante. Rendimentos passados não garantem rendimentos futuros.\n{HIP}\n{NR}\n\n#rendapassiva #fundosimobiliarios #FIIs #dividendos #investimentos")

# 4 colchao x investido
rows=[[f"<b>{a} anos</b>",R(1000,2),R(1000*1.1**a,2),R(1000*1.1**a-1000,2)] for a in (10,20,30,40)]
add("04-colchao",dict(titulo="R$ 1.000 <span>parados</span><br>x R$ 1.000 investidos",sub="O mesmo dinheiro, dois destinos 👇",aba="Depois de quanto tempo",colunas=["Passou","Debaixo do colchão","Investido","Diferença"],cols="0.7fr 1.15fr 1.1fr 1.1fr",lh=96,destaque=2,linhas=rows,fim="Dinheiro parado <b>nunca vai dobrar sozinho.</b>",rodape=[SIM+" Sem aportes.",HIP,NR],tsize=70,top=450),
f"R$ 1.000 parados ou R$ 1.000 investidos: onde você quer que o seu dinheiro esteja? 🤔\n\nDebaixo do colchão, em 30 anos você continua com R$ 1.000,00 (e comprando bem menos). Investido, o mesmo valor vira {R(1000*1.1**30,2)}. A diferença é o tempo trabalhando a seu favor.\n\nManda pra aquele amigo que guarda dinheiro em casa. E me segue pra aprender a fazer ele render.\n\n👉 Hoje seu dinheiro está parado ou rendendo? Comenta aqui!\n\n{SIM} Sem aportes.\n{HIP}\n{NR}\n\n#investimentos #jurosCompostos #educacaofinanceira #dinheiroparado #comecaraninvestir")

# 5 inflacao
rows=[[f"<b>{a} anos</b>",R(1000/(1.045**a),2),R(1000-1000/(1.045**a),2)] for a in (5,10,15,20)]
add("05-poder-compra",dict(titulo="O que R$ 1.000 <span>parados</span><br>compram no futuro",sub="Com preço subindo, o dinheiro parado compra menos 👇",aba="Poder de compra",colunas=["Daqui a","R$ 1.000 compram só","Você perde"],cols="0.8fr 1.4fr 1fr",lh=96,destaque=2,linhas=rows,fim="Parado, o dinheiro <b>perde valor sem você ver.</b>",rodape=["Simulação com inflação de 4,50% ao ano, constante. A inflação real muda a cada ano.",NR],tsize=70,top=450),
f"Dinheiro parado perde valor sem você perceber 📉\n\nCom a inflação em 4,50% ao ano (só uma simulação), R$ 1.000,00 guardados hoje compram o equivalente a {R(1000/1.045**10,2)} daqui a 10 anos. Em 20 anos, só {R(1000/1.045**20,2)}. A nota continua lá, mas ela compra cada vez menos.\n\nPor isso investir é proteger o que você já tem.\n\nManda pra quem guarda dinheiro em casa. E me segue pra aprender a proteger o seu.\n\n👉 Você já sentiu o dinheiro render menos no mercado? Comenta aqui!\n\nSimulação com inflação de 4,50% ao ano, constante. A inflação real muda a cada ano.\n{NR}\n\n#inflacao #investimentos #educacaofinanceira #dinheiroparado #financaspessoais")

# 6 comecar cedo
rows=[]
for idade in (25,30,35,40,45):
    a=65-idade;rows.append([f"Começa aos <b>{idade}</b>",f"{a} anos",brl(500*a*12,2),brl(fv(500,a),2)])
add("06-comecar-cedo",dict(titulo="Quanto custa<br><span>esperar</span> pra começar?",sub="Guardando <b>R$ 500 por mês</b> até os 65 anos 👇",aba="Começar cedo",colunas=["Quando começa","Investe por","Do seu bolso (R$)","Aos 65 anos (R$)"],cols="1.1fr 0.9fr 1.1fr 1.15fr",lh=88,destaque=3,linhas=rows,fim="Cada ano de espera <b>custa caro.</b>",rodape=[SIM,HIP,NR],tsize=76,top=450),
f"Quanto custa esperar pra começar a investir? ⏳\n\nGuardando R$ 500,00 por mês até os 65 anos, quem começa aos 25 chega com {R(fv(500,40),2)}. Quem começa aos 35, com {R(fv(500,30),2)}. Aos 45, {R(fv(500,20),2)}. Esperar 10 anos custa mais da metade do resultado.\n\nO melhor dia pra começar foi há 10 anos. O segundo melhor é hoje.\n\nManda pra alguém que vive adiando. E me segue se você vai começar agora.\n\n👉 Com quantos anos você começou a investir? Comenta aqui!\n\n{SIM}\n{HIP}\n{NR}\n\n#investimentos #comecaraninvestir #jurosCompostos #educacaofinanceira #aposentadoria")

# 7 IR renda fixa
rows=[["Até 180 dias","22,50%",R(1000*(1-.225),2)],["De 181 a 360 dias","20,00%",R(1000*(1-.20),2)],["De 361 a 720 dias","17,50%",R(1000*(1-.175),2)],["Acima de 720 dias","15,00%",R(1000*(1-.15),2)]]
add("07-imposto-renda-fixa",dict(titulo="Quanto de <span>imposto</span><br>na renda fixa?",sub="Quanto mais tempo, menos imposto 👇",aba="Tabela do Imposto de Renda",colunas=["Quanto tempo investiu","Imposto sobre o lucro","De R$ 1.000 de lucro, fica"],cols="1.2fr 1fr 1.2fr",lh=96,destaque=2,linhas=rows,fim="LCI e LCA são <b>isentas</b> de imposto para pessoa física.",rodape=["Vale para CDB e Tesouro Direto. Não considera IOF (nos primeiros 30 dias) nem taxa de custódia.",NR],tsize=76,top=450),
f"Quanto de imposto você paga na renda fixa? 🧾\n\nDepende do tempo: até 180 dias o Imposto de Renda é de 22,50% sobre o lucro. Acima de 720 dias, cai pra 15,00%. Ou seja, deixar o dinheiro mais tempo rendendo faz você ficar com mais. Já LCI e LCA são isentas pra pessoa física.\n\nManda pra quem investe em CDB ou Tesouro Direto. E me segue pra aprender a pagar menos imposto.\n\n👉 Você sabia dessa tabela? Comenta aqui!\n\nO imposto é cobrado só sobre o lucro, na hora do resgate.\n{NR}\n\n#rendafixa #impostoderenda #CDB #tesourodireto #educacaofinanceira")

# 8 qual e qual
rows=[["<b>Renda fixa</b><small>CDB, Tesouro Direto</small>","Você empresta dinheiro e recebe de volta com juros","Menor risco"],
["<b>Fundos imobiliários</b><small>FIIs</small>","Você vira dono de pedacinhos de imóveis e recebe aluguel todo mês","Risco médio"],
["<b>Ações</b><small>Pedaço de empresas</small>","Você vira sócio de uma empresa e ganha com lucro e valorização","Maior risco"]]
add("08-quem-e-quem",dict(titulo="Renda fixa, FII e ações:<br><span>qual é qual</span>?",sub="Em português simples, pra quem tá começando 👇",aba="Os três jeitos de investir",colunas=["Tipo","O que você é","Risco"],cols="1.15fr 1.7fr .8fr",lh=150,linhas=rows,fim="Um não substitui o outro. <b>Eles se completam.</b>",rodape=["O risco varia de acordo com o ativo escolhido.",NR],tsize=76,top=470),
f"Renda fixa, FII e ações: qual é qual? 🤔\n\nNa renda fixa você empresta dinheiro e recebe de volta com juros. Nos fundos imobiliários você vira dono de pedacinhos de imóveis e recebe aluguel todo mês. Nas ações você vira sócio de uma empresa e ganha com o lucro dela e com a valorização.\n\nCada um tem um papel, e o risco muda de um pro outro. Quanto maior o risco, maior pode ser o retorno, mas também a oscilação.\n\nManda pra quem ainda confunde tudo isso. E me segue pra aprender do zero.\n\n👉 Qual desses você já tem? Comenta aqui!\n\n{NR}\n\n#rendafixa #fundosimobiliarios #acoes #investimentos #educacaofinanceira")

# 9 dividendo
rows=[["<b>1. Data com</b>","Último dia pra ter a ação e <b>ter direito</b> ao dividendo"],["<b>2. Data ex</b>","Quem compra a partir daqui <b>não recebe</b> esse pagamento"],["<b>3. Data de pagamento</b>","O dinheiro <b>cai na sua conta</b>, direto na corretora"]]
add("09-como-funciona-dividendo",dict(titulo="Como funciona<br>o <span>dividendo</span>",sub="Os 3 dias que você precisa conhecer 👇",aba="Passo a passo",colunas=["Data","O que significa"],cols="1fr 2fr",lh=150,linhas=rows,fim="Quem tinha a ação na data com, <b>recebe.</b>",rodape=["Cada empresa divulga as suas datas. Confira sempre no comunicado ou no site de relações com investidores.",NR],tsize=80,top=470),
f"Como funciona o dividendo? 💸\n\nDividendo é a parte do lucro que a empresa divide com os sócios. Pra receber, você precisa ter a ação até a data com. Quem compra depois, na data ex, não recebe esse pagamento. Alguns dias depois, na data de pagamento, o dinheiro cai na sua conta, na corretora.\n\nManda pra quem quer receber dividendos mas nunca entendeu direito. E me segue pra aprender mais.\n\n👉 Qual foi o primeiro dividendo que você recebeu? Comenta aqui!\n\nCada empresa divulga as suas datas. Confira sempre no comunicado oficial.\n{NR}\n\n#dividendos #acoes #rendapassiva #investimentos #educacaofinanceira")

# 10 mitos
rows=[["<b>“Bolsa é coisa de rico”</b>","Dá pra começar com poucos reais, com uma cota só"],["<b>“Bolsa é cassino”</b>","Quem investe pensando em anos não está apostando"],["<b>“Preciso entender de tudo”</b>","Dá pra começar com o básico e aprender no caminho"],["<b>“Se cair, perdi tudo”</b>","Só perde quem vende. Mas risco existe: diversifique"],["<b>“Tenho que acertar o melhor dia”</b>","Investir todo mês costuma funcionar melhor"]]
add("10-mitos",dict(titulo="5 <span>mitos</span><br>sobre a bolsa",sub="E o que é verdade em cada um 👇",aba="Mito e verdade",colunas=["O que dizem","A verdade"],cols="1fr 1.35fr",lh=116,linhas=rows,fim="Informação <b>desmonta o medo.</b>",rodape=["Investimentos em renda variável têm risco de perda.",NR],tsize=84,top=430),
f"5 mitos sobre a bolsa que impedem muita gente de começar 🚫\n\n“Bolsa é coisa de rico”, “bolsa é cassino”, “preciso entender de tudo”, “se cair, perdi tudo”, “tenho que acertar o melhor dia”. Nenhum deles é bem assim. Dá pra começar com pouco, estudando aos poucos e investindo todo mês. Risco existe, e por isso a diversificação importa.\n\nManda pra quem ainda acredita em algum desses. E me segue pra perder o medo da bolsa.\n\n👉 Qual desses mitos você já acreditou? Comenta aqui!\n\nInvestimentos em renda variável têm risco de perda.\n{NR}\n\n#bolsadevalores #mitos #investimentos #educacaofinanceira #comecaraninvestir")

# 11 reserva
rows=[[f"<b>{R(g,2)}</b> por mês",R(g*6,2),R(g*12,2)] for g in (2000,3000,5000,8000)]
add("11-reserva",dict(titulo="Quanto você precisa<br>na <span>reserva de emergência</span>",sub="Antes de investir em qualquer coisa 👇",aba="Quanto guardar",colunas=["Seu gasto mensal","Reserva de 6 meses","Reserva de 12 meses"],cols="1.1fr 1.1fr 1.1fr",lh=96,destaque=1,linhas=rows,fim="Primeiro a reserva. <b>Depois os investimentos.</b>",rodape=["6 meses para quem tem renda fixa (CLT). 12 meses para quem tem renda variável (autônomo, comissão). Deixe em investimento seguro e com liquidez diária, como Tesouro Selic.",NR],tsize=64,top=450),
f"Quanto você precisa na reserva de emergência? 🛟\n\nA regra é guardar de 6 a 12 meses do seu gasto mensal. Quem tem renda fixa (CLT) costuma ficar com 6 meses. Quem tem renda variável (autônomo, comissão), com 12. Se você gasta R$ 3.000,00 por mês, são R$ 18.000,00 a R$ 36.000,00.\n\nDeixe num investimento seguro e com liquidez diária, como o Tesouro Selic. É dinheiro pra imprevisto, não pra render o máximo.\n\nManda pra quem ainda não tem reserva. E me segue pra montar a sua.\n\n👉 Você já tem sua reserva de emergência? Comenta aqui!\n\n{NR}\n\n#reservadeemergencia #tesourodireto #educacaofinanceira #investimentos #financaspessoais")

# 12 50/30/20
rows=[[f"<b>{R(s,2)}</b>",R(s*.5,2),R(s*.3,2),R(s*.2,2)] for s in (2000,3000,5000,8000)]
add("12-50-30-20",dict(titulo="Ganha <span>R$ 3.000</span>?<br>Quanto dá pra investir",sub="A regra 50-30-20 aplicada ao seu salário 👇",aba="Dividindo o salário",colunas=["Salário","50% contas","30% desejos","20% investir"],cols="0.9fr 1fr 1fr 1fr",lh=96,destaque=3,linhas=rows,fim="Guardar <b>20%</b> já muda o seu futuro.",rodape=["Regra 50-30-20: 50% para necessidades, 30% para desejos, 20% para investir e quitar dívidas. É uma referência: ajuste à sua realidade.",NR],tsize=78,top=450),
f"Ganha R$ 3.000,00? Quanto dá pra investir? 🧮\n\nUma regra simples pra organizar o salário é a 50-30-20: 50% pras contas, 30% pros desejos e 20% pra investir. Com R$ 3.000,00, são R$ 600,00 por mês pro seu futuro. Se não dá pra começar com 20%, começa com 5% ou 10%. O importante é criar o hábito.\n\nManda pra quem tem dificuldade de organizar o salário. E me segue pra aprender a investir.\n\n👉 Quanto do seu salário você consegue guardar? Comenta aqui!\n\nA regra é uma referência, ajuste à sua realidade.\n{NR}\n\n#educacaofinanceira #organizacaofinanceira #investimentos #financaspessoais #salario")

# 13 tipos de FII
rows=[["<b>Logística</b><small>Galpões</small>","Aluguel pago por empresas que armazenam e distribuem produtos"],["<b>Shoppings</b>","Aluguel das lojas e parte das vendas dos shoppings"],["<b>Lajes corporativas</b><small>Escritórios</small>","Aluguel pago por empresas que ocupam os escritórios"],["<b>Papel</b><small>Recebíveis</small>","Juros de dívidas imobiliárias que o fundo comprou"],["<b>Fundos de fundos</b>","Dividendos de outros fundos imobiliários"]]
add("13-tipos-fii",dict(titulo="De onde vem o <span>dinheiro</span><br>dos fundos imobiliários",sub="Os 5 tipos mais conhecidos, em português simples 👇",aba="Tipos de FII",colunas=["Tipo","De onde vem o rendimento"],cols="1fr 1.6fr",lh=112,linhas=rows,fim="Quem investe em vários tipos <b>se protege melhor.</b>",rodape=["Cada fundo tem riscos próprios. Estude antes de investir.",NR],tsize=72,top=440),
f"De onde vem o dinheiro dos fundos imobiliários? 🏢\n\nExistem fundos de logística (galpões), shoppings, lajes corporativas (escritórios), papel (juros de dívidas imobiliárias) e fundos de fundos. Cada um recebe de uma fonte diferente, e por isso vale diversificar. A ideia é receber um rendimento mensal sem ser dono do imóvel inteiro.\n\nManda pra quem acha que investir em imóvel é só pra rico. E me segue pra aprender FIIs do zero.\n\n👉 Qual tipo de FII você mais gosta? Comenta aqui!\n\nCada fundo tem riscos próprios. Estude antes de investir.\n{NR}\n\n#fundosimobiliarios #FIIs #rendapassiva #dividendos #investimentos")

# 14 dobrar
rows=[[f"<b>{P(t*100)[:-1]}%</b>".replace("%%","%"),anosmeses(math.log(2)/math.log(1+t))] for t in (.06,.08,.10,.12,.15)]
add("14-dobrar",dict(titulo="Em quantos anos seu<br>dinheiro <span>dobra</span>?",sub="Depende da taxa de rendimento 👇",aba="Tempo pra dobrar",colunas=["Rende ao ano","Seu dinheiro dobra em"],cols="1fr 1.4fr",lh=96,destaque=1,linhas=rows,fim="Taxa e tempo <b>mudam tudo.</b>",rodape=["Simulação com taxa constante, sem aportes, sem imposto e sem inflação.",HIP,NR],tsize=80,top=450),
f"Em quantos anos seu dinheiro dobra? ⏱️\n\nA 6,00% ao ano, são {anosmeses(math.log(2)/math.log(1.06))}. A 10,00% ao ano, {anosmeses(math.log(2)/math.log(1.10))}. A 15,00% ao ano, {anosmeses(math.log(2)/math.log(1.15))}. A taxa faz muita diferença, mas o tempo é o que mais pesa no resultado.\n\nManda pra quem acha que investir não faz diferença. E me segue pra aprender a fazer o dinheiro render.\n\n👉 Em que investimento o seu dinheiro está hoje? Comenta aqui!\n\nSimulação com taxa constante, sem aportes, sem imposto e sem inflação.\n{HIP}\n{NR}\n\n#investimentos #jurosCompostos #educacaofinanceira #rendimento #dinheiro")

# 15 pequenos gastos
it=[("Café de R$ 8,00 por dia útil",8*22),("Delivery 2 vezes por semana (R$ 45,00)",45*2*52/12),("Assinaturas de streaming (R$ 80,00)",80),("Lanche de R$ 25,00 por dia útil",25*22)]
rows=[[f"<b>{n}</b>",R(v,2),R(fv(v,20),2)] for n,v in it]
add("15-pequenos-gastos",dict(titulo="Pequenos gastos,<br><span>grande</span> patrimônio",sub="O que acontece se você investir esse valor 👇",aba="Investindo por 20 anos",colunas=["O gasto","Por mês","Investido em 20 anos"],cols="1.5fr 0.9fr 1.2fr",lh=116,destaque=2,linhas=rows,fim="Não é cortar tudo. <b>É escolher o que vale a pena.</b>",rodape=[SIM,HIP,NR],tsize=78,top=450),
f"Pequenos gastos, grande patrimônio 💭\n\nUm café de R$ 8,00 por dia útil dá {R(8*22,2)} por mês. Investido por 20 anos, vira {R(fv(8*22,20),2)}. Não é pra cortar tudo da sua vida, é pra enxergar o que cada escolha custa lá na frente. Às vezes, trocar um pouco já abre espaço pra começar a investir.\n\nManda pra aquele amigo que gasta sem perceber. E me segue pra aprender a investir.\n\n👉 Qual gasto pequeno você cortaria pra investir? Comenta aqui!\n\n{SIM}\n{HIP}\n{NR}\n\n#educacaofinanceira #investimentos #financaspessoais #jurosCompostos #dinheiro")

for slug,cfg,leg in posts:
    d=f"../pronto/2026-11-02-lote/{slug}"; os.makedirs(d,exist_ok=True)
    json.dump(cfg,open(f"{d}/config.json","w"),ensure_ascii=False,indent=1)
    open(f"{d}/legenda.txt","w").write(leg+"\n")
    subprocess.run(["python3","gen_inst.py","tab",f"{d}/config.json","t.html","verde"],check=True)
    subprocess.run(["python3","render.py","t.html",f"{d}/1.png"],check=True)
print(len(posts))

# Rotina diária: post "Fechamento de mercado" (@infobolsainvestimentos)

Roda nos dias úteis às 18h20 (horário de Brasília), sem nenhum computador ligado.

## 1. Teve pregão hoje?
Confira se a B3 abriu hoje (feriado nacional ou da B3 = sem pregão). Pesquise "Ibovespa fecha hoje DD/MM/AAAA". Se não teve pregão, pare aqui e não poste nada.

## 2. Números do fechamento de hoje
Busque e confira em pelo menos duas fontes (InfoMoney, Suno, Money Times, Investing, Seu Dinheiro, DGABC):
- Ibovespa: pontos de fechamento (sem casas decimais, ex.: "192.114") e variação % do dia
- Dólar comercial: fechamento (R$ com 2 casas) e variação % do dia
- Variação do Ibovespa na semana
- As 5 maiores altas e as 5 maiores baixas DA CARTEIRA DO IBOVESPA no dia (ticker, nome curto da empresa, variação %)
- Se menos de 5 ações caíram (ou subiram), preencha só as que existem e use "nota_baixas" (ou "nota_altas"), ex.: "Só 4 ações do Ibovespa<br>fecharam em queda"
Se não achar números confiáveis e conferidos de fechamento, NÃO poste: avise o Douglas.

## 3. Gerar a arte
Dentro de `kit/`:
1. Crie `configs/fechamento/AAAA-MM-DD.json` copiando o mais recente e trocando os dados (campo "fonte": "Fechamento de DD/MM/AAAA. Fonte: B3").
2. Logo de ticker novo: baixe `https://raw.githubusercontent.com/thefintz/icones-b3/main/icones/TICKER.png` para `assets/logos_b3/TICKER.png` (se não existir, tente o ticker com final 3, 4 ou só as 4 letras). Natura (NATU3) usa o arquivo NTCO3.png.
3. `python3 gen_fechamento.py configs/fechamento/AAAA-MM-DD.json t.html && python3 render.py t.html t.png`
4. Olhe a imagem (Read) e confira: textos sem sobrepor, números certos, logos aparecendo.
5. Converta para JPEG: `python3 -c "from PIL import Image; Image.open('t.png').convert('RGB').save('../posts/fechamento-AAAA-MM-DD.jpg', quality=93)"` e apague t.html e t.png.

## 4. Publicar a imagem e postar
1. `git add -A && git commit -m "Fechamento DD/MM/AAAA" && git push` (branch main).
2. Confira que `https://raw.githubusercontent.com/InfoBolsaInvest/infobolsa-posts/main/posts/fechamento-AAAA-MM-DD.jpg` abre (pode levar alguns segundos).
3. Poste no Instagram com o conector Windsor.ai: `execute_action`, connector `instagram`, conta `17841445716975551`, ação `create_image_post`, com `image_url` acima e a legenda.
4. Leia a resposta: se vier qualquer erro (ex.: falta de permissão instagram_content_publish), NÃO considere postado e avise o Douglas com o texto do erro.

## 5. Legenda (modelo)
```
Fechamento de hoje (DD/MM) 📊

O Ibovespa [subiu/caiu] X,XX% e fechou aos XXX.XXX pontos. [1 frase de contexto do dia, se houver motivo claro e conferido]. Na semana, [acumula alta/queda de X,XX%].

[Empresa] liderou as altas, com X,XX%, seguida por [Empresa], com X,XX%. Na ponta de baixo, [Empresa] caiu X,XX%. O dólar fechou em R$ X,XX.

👉 Qual dessas você tem na carteira? Comenta aqui!

Não é uma recomendação de compra ou venda.

#ibovespa #fechamentodemercado #bolsadevalores #b3 #acoes #investimentos
```

## Regras
- Linguagem: siga `LINGUAGEM.md` (a mais fácil do mundo, gancho de conversa, zero economês).
- Nunca usar travessão. Linguagem simples, sem frases com cara de IA.
- Números no padrão brasileiro e percentuais com 2 casas decimais.
- Nunca prometer rentabilidade nem recomendar compra ou venda.
- Não postar no YouTube nem no Facebook nessa rotina (não dá sem o navegador do Douglas).
- No final, mande ao Douglas (SendUserMessage) a imagem postada e um resumo de uma linha. Se algo falhar, diga o que falhou.

# Rotina diária: post escuro de notícia das 12h (@infobolsainvestimentos)

Roda todos os dias por volta das 11h40 (horário de Brasília), sem nenhum computador ligado. O Douglas pediu para postar direto, sem aprovação. O post deve sair perto das 12h.

## 1. Já postou hoje?
Se `posts/noticia-AAAA-MM-DD.jpg` de hoje já existe no repositório, pare aqui e não poste de novo.

## 2. Escolher a notícia do dia
Pesquise (WebSearch) as notícias de HOJE (ou da noite anterior) que mexem com quem investe:
- Ibovespa, dólar, juros, Selic, Copom, inflação (IPCA), Tesouro Direto, poupança
- empresas da bolsa: resultados, dividendos e JCP anunciados, fusões, recordes, quedas fortes
- FIIs (só FIIs sem problema e abertos ao público geral, nunca FII restrito a investidor qualificado)
- economia e política quando afetam os investimentos: eleição, decisões do governo, Congresso, impostos, contas públicas, petróleo, commodities, exterior (Fed, EUA, China)

Regras da escolha:
- Escolha a notícia mais relevante e mais forte para o público pessoa física.
- Confirme o fato e os números em pelo menos duas fontes confiáveis (InfoMoney, Valor, Estadão, Folha, G1, CNN Brasil, Money Times, Seu Dinheiro, Exame, Suno, Agência Brasil, B3, Banco Central, site de RI da empresa).
- Nada de boato, "pode", "deve", fonte única ou opinião. Só fatos confirmados.
- Política: só os fatos e o efeito no mercado, sem tomar partido e sem opinião sobre político.
- Não repita o assunto dos últimos 3 posts (veja os arquivos mais recentes em `kit/configs/noticia/`), a não ser que tenha fato novo forte.
- Números de mercado em tempo real: use o valor mais recente das fontes e escreva o horário no campo "fonte". Dados de ação (cotação, DY, proventos) do StatusInvest quando precisar.
- Se não achar nenhuma notícia confirmada que valha o post, NÃO poste: avise o Douglas.

## 3. Montar o config
Crie `kit/configs/noticia/AAAA-MM-DD.json` (veja `exemplo-manchete.json` e `exemplo-numero.json`):
- `modo`: "manchete" (padrão) ou "numero" quando a notícia cabe num número forte (ex.: "209 mil", "15,00%", "R$ 4,98"). No modo número use `rotulo` (curto) e `numero` (até 8 caracteres). 
- `tag`: uma palavra em maiúsculas ou curta (Mercado, Bolsa, Dólar, Juros, FIIs, Dividendos, Economia, Política, Bancos, Petróleo, Agro, Inflação, Exterior).
- `titulo`: até 3 linhas de no máximo uns 20 caracteres cada, quebradas com `<br>`. Uma palavra ou número em `<em>` (fica amarelo, cor de destaque da marca). Se passar de 3 linhas, use `"ajustes": {"titulo_size": 92}`.
- `sub`: 1 ou 2 linhas de apoio (uns 48 caracteres por linha, com `<br>`), números importantes em `<b>`.
- `fonte`: "Dados de DD/MM/AAAA às HHhMM. Fontes: X e Y" (ou "Fontes: X e Y" quando não for número de mercado).
- `fundo` e `foco`: SEMPRE uma foto real de `kit/assets/fundos/` ligada ao assunto (repetir foto não tem problema). Nunca use desenho, ícone, ilustração ou fundo gerado. Veja as fotos disponíveis com `ls kit/assets/fundos` e, na dúvida, olhe a foto (Read) antes de escolher. Use `foco` (ex.: `"50% 40%"`) para centralizar o assunto da foto no corte vertical.

| Tema | fotos |
|---|---|
| Ibovespa, bolsa, ações em geral, recorde | `fundo-touro-b3.jpg` (foco `62% 50%`), `foto-b3-pregao-1.jpg` |
| Banco do Brasil | `foto-banco-do-brasil-*.jpg` |
| Itaú | `foto-itau-*.jpg` |
| Bradesco | `foto-bradesco-*.jpg` |
| Santander | `foto-santander-*.jpg` |
| Caixa, FGTS, habitação | `foto-caixa-*.jpg` |
| Petrobras | `foto-petrobras-plataforma-*.jpg`, `foto-petrobras-sede-*.jpg` |
| Combustíveis, preço da gasolina | `foto-posto-combustivel-*.jpg` |
| Vale, minério de ferro | `foto-vale-mina-*.jpg`, `foto-minerio-de-ferro-*.jpg` |
| Selic, Copom, juros, Banco Central | `foto-banco-central-*.jpg` |
| Congresso, votações, impostos, reforma | `foto-congresso-*.jpg` |
| Governo, presidente, Planalto, contas públicas | `foto-planalto-*.jpg` |
| Dólar, câmbio, exterior | `foto-dolar-*.jpg`, `foto-wall-street-1.jpg` (bolsa americana, Fed) |
| Real, salário, poupança, inflação, finanças pessoais | `foto-real-dinheiro-*.jpg` |
| Ouro | `foto-ouro-*.jpg` |
| FIIs de lajes, escritórios, mercado imobiliário | `foto-faria-lima-*.jpg`, `foto-avenida-paulista-*.jpg` |
| FIIs de shopping, varejo | `foto-shopping-*.jpg`, `foto-varejo-loja-*.jpg` |
| Agro, Fiagros, safra | `foto-agro-*.jpg`, `foto-gado-*.jpg` |
| Energia, elétricas | `foto-itaipu-energia-*.jpg`, `foto-angra-energia-nuclear-1.jpg` |

Se nenhuma foto combinar com o assunto, use a mais próxima da lista (ex.: notícia de empresa sem foto própria: `fundo-touro-b3.jpg` ou Faria Lima). O crédito da foto entra sozinho no rodapé (vem de `kit/assets/fundos/creditos.json`), não apague.

- `logo`: se a notícia cita UMA empresa da bolsa, coloque o logo dela. Baixe `https://raw.githubusercontent.com/thefintz/icones-b3/main/icones/TICKER.png` para `kit/assets/logos_b3/TICKER.png` (se não existir, tente o ticker com final 3, 4, 11 ou só as 4 letras). `logo_fundo`: cor da marca quando o logo for claro sobre fundo colorido (ex.: BB `#fcfc30`), senão deixe sem (branco).

## Identidade visual
O gen_escuro.py já está no padrão aprovado: fundo escuro sobre a foto com degradê verde da marca embaixo, faixa verde no rodapé, etiqueta verde, título grosso (Anton) em branco e destaque em amarelo da marca (#FFB400). Não usar azul nem colocar o logo da InfoBolsa no topo. Não mude cores nem fontes no config.

## 4. Gerar e conferir a arte
Dentro de `kit/`:
1. `python3 gen_escuro.py configs/noticia/AAAA-MM-DD.json t.html && python3 render.py t.html t.png`
2. Olhe a imagem (Read) e confira: texto sem cortar nem sobrepor, sem travessão, números certos, logo aparecendo, título legível sobre o fundo. Ajuste e gere de novo se precisar.
3. `python3 -c "from PIL import Image; Image.open('t.png').convert('RGB').save('../posts/noticia-AAAA-MM-DD.jpg', quality=93)"` e apague t.html e t.png.

## 5. Publicar a imagem e postar
1. `git add -A && git commit -m "Notícia DD/MM/AAAA" && git push` (branch main).
2. Confira que `https://raw.githubusercontent.com/InfoBolsaInvest/infobolsa-posts/main/posts/noticia-AAAA-MM-DD.jpg` abre (pode levar alguns segundos).
3. Poste no Instagram com o conector Windsor.ai: `execute_action`, connector `instagram`, conta `17841445716975551`, ação `create_image_post`, com `image_url` acima e a legenda.
4. Leia a resposta: se vier qualquer erro (ex.: falta de permissão instagram_content_publish), NÃO considere postado, não tente de novo por outro caminho e avise o Douglas com o texto do erro.

## 6. Legenda (modelo)
```
[Frase de gancho curta sobre a notícia] [1 emoji que combine]

[1 parágrafo curto: o que aconteceu, com os números principais e o motivo, se for confirmado.]

[1 parágrafo curto: o que isso muda para quem investe, sem recomendar nada.]

👉 [Pergunta simples para o público]? Comenta aqui!

Não é uma recomendação de compra ou venda.

#[5 ou 6 hashtags do tema, ex.: #ibovespa #bolsadevalores #investimentos #b3 #economia]
```

## Regras
- Nunca usar travessão (nem na imagem nem na legenda). Linguagem simples, sem frases com cara de IA.
- Números no padrão brasileiro (200.000,00) e percentuais com 2 casas decimais.
- Nunca prometer rentabilidade nem recomendar compra ou venda.
- Não postar no YouTube nem no Facebook nessa rotina (não dá sem o navegador do Douglas).
- Se qualquer etapa falhar, NÃO poste e avise o Douglas dizendo o que falhou.
- No final, mande ao Douglas (SendUserMessage) um resumo de uma linha (postado ou não, qual notícia) com a legenda, e a imagem com SendUserFile.

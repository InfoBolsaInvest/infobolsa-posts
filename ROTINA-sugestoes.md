# Rotina diária: sugestão de post branco para as 07h e as 15h (@infobolsainvestimentos)

Roda todos os dias às 06h50 e às 14h50 (horário de Brasília), na nuvem, sem computador ligado. Cada execução cria UMA sugestão de post: a das 06h50 é a sugestão das 07h, a das 14h50 é a das 15h.

IMPORTANTE: por enquanto NÃO POSTE em lugar nenhum (nada de Windsor execute_action, Meta, Facebook ou YouTube). Só crie a arte e a legenda e mande para o Douglas avaliar.

## 1. Ver o que está funcionando no perfil
1. Puxe os posts dos últimos 90 dias pelo conector Windsor.ai: `get_data`, connector `instagram`, conta `17841445716975551`, campos `date`, `timestamp`, `media_type`, `media_caption`, `media_reach`, `media_saved`, `media_shares`, `media_like_count`, `media_comments_count`, `date_preset` "last_90d". Se vier "pending", chame de novo com os mesmos parâmetros até vir (espere até uns 10 minutos).
2. Se o Windsor não responder, use `kit/desempenho/top-posts-historico.json` (os 100 posts de imagem com mais alcance desde jan/2025).
3. Olhe só posts de imagem e carrossel. Ranqueie por alcance e por salvamentos + compartilhamentos. Anote os formatos e temas que mais aparecem no topo (ex.: "Como juntar R$ 100 mil", "Ganho um salário mínimo", "Precisa ser rico para investir", "Quanto rendem R$ 100 mil em FIIs", comparativos entre bancos, "Hoje é a data de pagamento", "Sócio de grandes empresas").
4. Não repita: veja `sugestoes/` (sugestões dos últimos 14 dias) e as legendas dos posts dos últimos 30 dias. Não sugira o mesmo tema com os mesmos ativos de um post recente. Pode repetir um formato que funciona, com outro recorte ou outros ativos.

## 2. Escolher o post
- PRIMEIRO veja `sugestoes/proximos.md`: se houver um tema anunciado para hoje neste horário, o post é esse (é promessa feita ao seguidor). Marque como feito no arquivo.
- Escolha UM post baseado nos formatos que mais performam, refeito com números atuais ou com um ângulo novo.
- Varie: alterne entre ações, FIIs, renda fixa e educação financeira ao longo dos dias. Não faça duas sugestões seguidas do mesmo assunto.
- Sugestão: às 07h algo mais educativo e leve (simulação, metas, juntar dinheiro, comparação simples); às 15h algo com dados de mercado (dividendos, comparativos, FIIs, ações).
- Se citar empresa, coloque o logo (baixe de `https://raw.githubusercontent.com/thefintz/icones-b3/main/icones/TICKER.png` para `kit/assets/logos_b3/` se ainda não existir).
- FIIs: nada de fundo problemático (calote, corte de dividendo, inadimplência alta, provento sustentado por reserva ou ganho de capital) nem fundo restrito a investidor qualificado.

## 3. Dados
- Cotação, dividend yield, proventos de 12 meses, P/L, P/VP, ROE: StatusInvest (statusinvest.com.br, use WebFetch). Selic, CDI, poupança e PTAX: Banco Central. Confira os números antes de usar e escreva a data dos dados na imagem.
- Simulações: deixe claro que é simulação ("Rentabilidade hipotética, não é garantia de retorno").

## 4. Fazer a arte (modelo branco padrão)
Dentro de `kit/`, com os geradores do modelo branco (cabeçalho com foto, nome, selo e @, fundo branco):
- `gen_tab.py` tabela genérica (rankings, listas, simulações), `gen_pag.py` "Hoje é a data de pagamento" / dividendos em 12 meses, `gen_vs.py` comparativo entre duas empresas, `gen_rend100.py` quanto rendem R$ 100 mil, `gen_fii.py` quanto investir para receber X por mês, `gen_tempo.py` primeiros R$ 100 mil (barras), `gen_rank.py` ranking com ícones, `gen.py` salário mínimo / sócio de grandes empresas (quadros de logos com preço).
- Use como modelo os configs de `kit/configs/branco/` (exemplos, semana-05-a-11-10 e semana-12-a-18-10; o `build.py` de cada semana mostra como os números são montados).
- Crie o config em `kit/configs/sugestoes/AAAA-MM-DD-HHh.json`, depois `python3 GERADOR.py config.json t.html && python3 render.py t.html t.png`.
- Olhe a imagem (Read) e confira: nada cortado ou sobreposto, números certos, logos aparecendo, sem travessão.
- Salve em `sugestoes/AAAA-MM-DD-07h-1.png` (ou `-15h-1.png`) e a legenda em `sugestoes/AAAA-MM-DD-07h.txt`. Apague t.html e t.png.
- `git add -A && git commit -m "Sugestão DD/MM HHh" && git push` (branch main).

## 4b. Último slide: convite para seguir (carrossel)
Toda sugestão é um carrossel de 2 slides:
- Slide 1: a arte do post (seção 4), salva como `sugestoes/AAAA-MM-DD-HHh-1.png`.
- Slide 2: convite para seguir anunciando o post de AMANHÃ no mesmo horário, com `gen_segue.py` (config em `kit/configs/sugestoes/AAAA-MM-DD-HHh-segue.json`, campos `quando` "Amanhã, às <b>07h</b>, eu posto:", `tema`, `sub`, `rodape`). Salve como `sugestoes/AAAA-MM-DD-HHh-2.png`.
- Escolha o tema de amanhã seguindo as mesmas regras (formatos que performam, sem repetir, variar o assunto) e registre em `sugestoes/proximos.md` como pendente. Só anuncie algo que dá para fazer com dados públicos.

## 5. Legenda
Frase de gancho, 1 ou 2 parágrafos curtos com os números principais, "Amanhã, às XXh, eu posto [tema]. Me segue para não perder!", "👉 [pergunta]? Comenta aqui!", "Não é uma recomendação de compra ou venda." (e "Rentabilidade hipotética, não é garantia de retorno." quando for simulação) e 5 ou 6 hashtags.

## Regras
- Nunca usar travessão, nem na imagem nem na legenda. Linguagem simples, sem frases com cara de IA.
- Números no padrão brasileiro (200.000,00) e percentuais com 2 casas decimais.
- Nunca prometer rentabilidade nem recomendar compra ou venda.
- NÃO postar. Só mandar para o Douglas.

## 6. Mandar para o Douglas
SendUserMessage curto começando com "SUGESTÃO 07h DD/MM" (ou 15h), com: o post escolhido e por quê (quais posts do perfil inspiraram, com o alcance deles), os dados usados e a data, e a legenda pronta. Depois SendUserFile com as duas imagens do carrossel (slide 1 e slide 2). Se algo falhar, diga o que falhou.

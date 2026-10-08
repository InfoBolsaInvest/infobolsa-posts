# Rotina diária: sugestão de post branco para as 07h e as 15h (@infobolsainvestimentos)

Roda todos os dias às 06h50 e às 14h50 (horário de Brasília), na nuvem, sem computador ligado. Cada execução cria UMA sugestão de post: a das 06h50 é a sugestão das 07h, a das 14h50 é a das 15h.

IMPORTANTE (outubro/2026): até 31/10/2026 só existe o post das 15h. O Planner do Douglas já tem posts programados às 07h até o fim do mês, então a execução das 06h50 até 31/10/2026 não faz nada: pare logo no começo, sem criar arte, sem postar e sem mandar mensagem. A partir de 01/11/2026 volta a fazer os dois horários.

IMPORTANTE: a partir de 09/10/2026 o post é PUBLICADO DIRETO no Instagram, sem aprovação do Douglas (seção 5b). Antes dessa data, só crie e mande para ele avaliar. Facebook e YouTube ficam fora (não dá sem o navegador dele).

## Eleições: 25, 26 e 27/10/2026 (segundo turno no domingo 25)
Nesses três dias o post das 15h é EXCLUSIVAMENTE sobre a eleição e o efeito dela nos investimentos (pule a escolha normal da seção 2, mas siga o resto: dados conferidos, arte, legenda, publicação).
- 25/10 (domingo, votação): o que está em jogo para o investidor, como a bolsa, o dólar, os juros e os FIIs reagiram ao primeiro turno, o que observar na segunda-feira, horário de divulgação do resultado. ATENÇÃO: o post sai antes do fim da votação (17h), então NADA de boca de urna nem de resultado parcial.
- 26/10 (segunda): resultado oficial do segundo turno (TSE) e a reação do mercado no dia (Ibovespa, dólar, juros futuros, IFIX, ações que mais subiram e mais caíram até o horário do post, com horário escrito na arte).
- 27/10 (terça): as ações e os FIIs que mais se valorizaram (e caíram) na segunda, o que muda para Selic, juros e renda fixa segundo as projeções divulgadas (Focus, bancos, corretoras, sempre com a fonte), setores mais sensíveis ao novo governo (estatais, bancos, elétricas, construção, varejo).
Regras para esses posts:
- Neutralidade total: só fatos e efeito no mercado, sem opinião sobre candidato, partido ou governo, sem torcer, sem adjetivos sobre políticos. Trate os candidatos com o mesmo peso.
- Pesquisa eleitoral só se for registrada no TSE, com instituto, data e número de registro na arte ou na legenda. Proibido fazer enquete "quem vai ganhar?" ou "em quem você vota?" antes do resultado (enquete eleitoral é vedada pela lei eleitoral). Depois do resultado oficial, pode perguntar como o seguidor vai investir, nunca sobre voto.
- "Ações que podem subir": só como o que analistas e casas citam como mais sensíveis ao resultado, com a fonte; nunca indicar compra ou venda.
- Confirme resultado e números em pelo menos duas fontes confiáveis (TSE, B3, Banco Central, InfoMoney, Valor, Estadão, Folha, G1, CNN Brasil).
- Pode usar o formato `tab` (ranking de altas e baixas), `vs` (antes x depois) ou outro tipo do gen_inst.py; logo das empresas citadas.

## 1. Ver o que está funcionando no perfil
1. Puxe os posts dos últimos 90 dias pelo conector Windsor.ai: `get_data`, connector `instagram`, conta `17841445716975551`, campos `date`, `timestamp`, `media_type`, `media_caption`, `media_reach`, `media_saved`, `media_shares`, `media_like_count`, `media_comments_count`, `date_preset` "last_90d". Se vier "pending", chame de novo com os mesmos parâmetros até vir (espere até uns 10 minutos).
2. Se o Windsor não responder, use `kit/desempenho/top-posts-historico.json` (os 100 posts de imagem com mais alcance desde jan/2025).
3. Olhe só posts de imagem e carrossel. Ranqueie por alcance e por salvamentos + compartilhamentos. Anote os formatos e temas que mais aparecem no topo (ex.: "Como juntar R$ 100 mil", "Ganho um salário mínimo", "Precisa ser rico para investir", "Quanto rendem R$ 100 mil em FIIs", comparativos entre bancos, "Hoje é a data de pagamento", "Sócio de grandes empresas").
4. Não repita: veja `sugestoes/` (sugestões dos últimos 14 dias) e as legendas dos posts dos últimos 30 dias. Não sugira o mesmo tema com os mesmos ativos de um post recente. Pode repetir um formato que funciona, com outro recorte ou outros ativos.

## 2. Escolher o post
Antes de escolher, leia `PESQUISA-CRESCIMENTO.md` (o que traz seguidor, pelo perfil e pela pesquisa de mercado) e siga o que está lá. Às segundas, na execução das 07h, atualize esse arquivo com uma pesquisa rápida na web, se achar algo novo e confiável.
O objetivo é GANHAR SEGUIDORES. Dados do perfil (Windsor, campo `media_follows`, 90 dias até 08/10/2026): os 3 posts que mais trouxeram seguidores foram "Precisa ser rico para investir..." (187 seguidores, 55 mil de alcance), "a maior barreira é mental, com pouco mais de cem reais..." (84) e "dá pra começar em FII com bem menos dinheiro" (45), quase metade de todos os seguidores ganhos por posts de imagem. Posts de notícia e de dados de mercado têm alcance alto, mas trazem poucos seguidores (ex.: "Bolsa amanheceu em festa", 31 mil de alcance e 22 seguidores). Puxe também `media_follows` no passo 1 e ranqueie por ele.
- Prefira temas que quebram uma crença de quem ainda não investe ou está começando ("precisa ser rico", "não sobra nada", "é arriscado", "dinheiro parado") e mostram com números que dá.

- USE BASTANTE O FORMATO `prefere` (enquete "Qual você prefere?"): pelo menos UMA sugestão por dia deve ser desse tipo, alternando entre 07h e 15h. Varie as duplas/trios: bancos (Itaú x BB x Bradesco), elétricas (Taesa x Cemig x Copel), Petrobras x Vale, B3 x BTG, varejo, FII de tijolo x FII de papel, FIIs de shopping, logística, etc. Sempre empresas/fundos conhecidos do público, com preço e indicadores reais do StatusInvest do dia. Título curto ("Qual ação você <span>prefere?</span>", "Qual banco você <span>prefere?</span>", "Qual FII você <span>prefere?</span>") e uma frase final de 1 ou 2 linhas que dá contexto simples sobre cada opção e chama para comentar. Na legenda, peça para comentar o ticker escolhido e o motivo.
- Escolha UM post baseado nos formatos que mais performam, refeito com números atuais ou com um ângulo novo.
- Varie: alterne entre ações, FIIs, renda fixa e educação financeira ao longo dos dias. Não faça duas sugestões seguidas do mesmo assunto.
- Sugestão: às 07h algo mais educativo e leve (simulação, metas, juntar dinheiro, comparação simples); às 15h algo com dados de mercado (dividendos, comparativos, FIIs, ações).
- Se citar empresa, coloque o logo (baixe de `https://raw.githubusercontent.com/thefintz/icones-b3/main/icones/TICKER.png` para `kit/assets/logos_b3/` se ainda não existir).
- FIIs: nada de fundo problemático (calote, corte de dividendo, inadimplência alta, provento sustentado por reserva ou ganho de capital) nem fundo restrito a investidor qualificado.

## 3. Dados
- Cotação, dividend yield, proventos de 12 meses, P/L, P/VP, ROE: StatusInvest (statusinvest.com.br, use WebFetch). Selic, CDI, poupança e PTAX: Banco Central. Confira os números antes de usar e escreva a data dos dados na imagem.
- Simulações: deixe claro que é simulação ("Rentabilidade hipotética, não é garantia de retorno").

## 4. Fazer a arte (padrão novo desde 08/10/2026: estilo institucional, fundo claro levemente verde, cores da InfoBolsa)
Use `kit/gen_inst.py` com o tema `verde` (é o padrão): cabeçalho pequeno com foto, nome, selo e @, título grande com uma palavra em verde (`<span>`), subtítulo, conteúdo dentro de uma "pasta" com aba (bolinha amarela), rodapé discreto. Base #162526, verde #0f7a43, amarelo #FFB400. Sem azul.
- `python3 gen_inst.py TIPO config.json t.html verde && python3 render.py t.html t.png`
- Tipos: `tab` tabela genérica (rankings, listas, simulações, comparativos de renda fixa), `socio` empresas com logo e preço de 1 ação + total (formato "Precisa ser rico" / "sócio de grandes empresas"), `vs` comparativo entre duas empresas, `pag` dividendos / data de pagamento, `fii` quanto investir para receber X por mês. Exemplos: `kit/configs/sugestoes/2026-10-08-07h-inst.json` (socio) e `2026-10-08-teste-inst.json` (tab); para `vs`, `pag` e `fii` os json de `kit/configs/branco/` servem.
- `prefere`: enquete "Qual ação/FII/banco você prefere?" com 2 ou 3 opções (ticker, nome, logo, preço e até 2 indicadores, ex.: DY 12M e P/L ou P/VP). Exemplos: `kit/configs/sugestoes/exemplo-prefere.json` (2 opções) e `exemplo-prefere-3.json` (3 opções). O Douglas gosta muito desse formato porque gera muito comentário.
- Se precisar de um formato que o gen_inst.py ainda não tem, crie um novo tipo nele seguindo o mesmo visual (não volte para o modelo branco antigo).
- Crie o config em `kit/configs/sugestoes/AAAA-MM-DD-HHh.json`.
- Olhe a imagem (Read) e confira: nada cortado, sobreposto ou quebrando linha feio (título, frase final e rodapé), números certos, logos aparecendo, sem travessão.
- Salve o slide 1 em `sugestoes/AAAA-MM-DD-07h-1.png` (ou `-15h-1.png`) e a legenda em `sugestoes/AAAA-MM-DD-07h.txt`. Apague t.html e t.png.
- `git add -A && git commit -m "Sugestão DD/MM HHh" && git push` (branch main).

## Linguagem (para trazer seguidor)
- Título = gancho de conversa, não título de relatório. Use a frase que a pessoa pensa entre aspas ("“Bolsa é coisa de rico”", "“Não sobra nada pra investir”") ou uma afirmação que provoca ("Dinheiro parado nunca vai dobrar"). Nada de "Comparativo de...", "Análise de...".
- Subtítulo fala com "você" e manda olhar a tabela ("Olha quanto custa...", "Olha em quanto tempo... 👇").
- Cabeçalhos e frases da arte em linguagem de gente ("Você vira sócio de", "Tudo isso por"), não termos técnicos sem explicação.
- Frase final na arte com a lição em uma linha ("Não precisa ser rico. Precisa começar.").
- Legenda: primeira linha é o gancho, frases curtas, "pra" e "tá" pode, sem economês. Antes dos avisos, peça para mandar para alguém específico ("Manda pra aquele amigo que acha que precisa ser rico pra investir") e para seguir ("me segue se você tá começando agora").

## 4b. Último slide: convite para seguir (carrossel)
Toda sugestão é um carrossel de 2 slides:
- Slide 1: a arte do post (seção 4), salva como `sugestoes/AAAA-MM-DD-HHh-1.png`.
- Slide 2: convite genérico para seguir e salvar, SEM anunciar tema do dia seguinte (a programação muda com as notícias): `python3 gen_inst.py segue - t.html verde && python3 render.py t.html t.png`. Salve como `sugestoes/AAAA-MM-DD-HHh-2.png`.

## 5. Legenda
Frase de gancho, 1 ou 2 parágrafos curtos com os números principais, "Manda pra [alguém específico]. E me segue se [identificação, ex.: você tá começando agora].", "👉 [pergunta]? Comenta aqui!", "Não é uma recomendação de compra ou venda." (e "Rentabilidade hipotética, não é garantia de retorno." quando for simulação) e 3 a 5 hashtags do nicho. Coloque a palavra principal do tema na primeira frase da legenda.

## Regras
- Linguagem: siga `LINGUAGEM.md` (a mais fácil do mundo, gancho de conversa, zero economês).
- Nunca usar travessão, nem na imagem nem na legenda. Linguagem simples, sem frases com cara de IA.
- Números no padrão brasileiro (200.000,00) e percentuais com 2 casas decimais.
- Nunca prometer rentabilidade nem recomendar compra ou venda.
- A partir de 09/10/2026: postar no Instagram (seção 5b). Se algum número não estiver conferido ou algo falhar, NÃO poste e avise.

## 5b. Publicar no Instagram (a partir de 09/10/2026)
0. Não publique duas vezes: logo no começo da execução (antes da seção 1), veja se `posts/sugestao-AAAA-MM-DD-HHh-1.jpg` deste dia e horário já existe no repositório. Se existir, já foi postado: pare e avise o Douglas.
1. Converta os dois slides para JPEG: `python3 -c "from PIL import Image; [Image.open(f'../sugestoes/AAAA-MM-DD-HHh-{i}.png').convert('RGB').save(f'../posts/sugestao-AAAA-MM-DD-HHh-{i}.jpg', quality=93) for i in (1,2)]"` (rode dentro de `kit/`).
2. `git add -A && git commit -m "Post DD/MM HHh" && git push` (branch main).
3. Confira que os dois links abrem: `https://raw.githubusercontent.com/InfoBolsaInvest/infobolsa-posts/main/posts/sugestao-AAAA-MM-DD-HHh-1.jpg` e `-2.jpg` (pode levar alguns segundos).
4. Publique com o conector Windsor.ai: `execute_action`, connector `instagram`, conta `17841445716975551`, ação `create_carousel_post`, `image_urls` = [link do slide 1, link do slide 2] (nessa ordem), `caption` = legenda.
5. Leia a resposta: se vier qualquer erro, NÃO considere postado, não tente por outro caminho e avise o Douglas com o texto do erro.

## 6. Mandar para o Douglas
SendUserMessage curto começando com "POSTADO 07h DD/MM" ou "NÃO POSTADO 07h DD/MM" (com o motivo) a partir de 09/10/2026, ou "SUGESTÃO 07h DD/MM" antes disso (ou 15h), com: o post escolhido e por quê (quais posts do perfil inspiraram, com o alcance deles), os dados usados e a data, e a legenda pronta. Depois SendUserFile com as duas imagens do carrossel (slide 1 e slide 2). Se algo falhar, diga o que falhou.

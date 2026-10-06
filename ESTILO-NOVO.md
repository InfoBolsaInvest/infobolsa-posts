# Estilo novo dos posts (em espera)

Status: aprovado como visual, mas em espera. Só usar quando o Douglas pedir posts de novo.
Quando ele pedir, gerar os posts nesse formato institucional:

- Gerador: `kit/gen_inst.py TIPO config.json saida.html TEMA` (tipos: pag, vs, fii; lê os mesmos json dos geradores antigos).
- Temas: `azul` (degradê azul), `claro` (fundo branco), `preto`. Alternar entre eles, sem deixar o perfil todo de uma cor só (principalmente branco e azul intercalados).
- Foto: `kit/assets/foto.png` (foto nova, de microfone, enquadramento aberto). Cabeçalho com foto, nome e @ maiores.
- Tipos que ainda não têm versão nova (gen_tab, gen_tempo, gen_rank, gen_rend100, gen.py) seguem a mesma linha: título com parte em azul, conteúdo dentro de uma "pasta" com aba, rodapé discreto.

## Cores (atualizado em 06/10/2026)
A identidade da InfoBolsa é verde, amarelo e branco, sem azul. Base principal #162526, amarelo #FFB400 como destaque, verde e branco de apoio; verde/vermelho só para altas e baixas.
Os temas "azul" e "preto" do gen_inst.py precisam ser trocados por versões nessas cores antes de usar (o gen_fechamento.py já está nas cores novas). Não colocar o logo da InfoBolsa no topo dos posts.

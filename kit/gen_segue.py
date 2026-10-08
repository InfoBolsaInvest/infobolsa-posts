#!/usr/bin/env python3
"""Último slide do carrossel no modelo branco: convite para seguir anunciando o post do dia seguinte.
cfg: quando ("Amanhã, às <b>07h</b>, eu posto:"), tema (HTML, pode ter <br> e <b>), sub (opcional),
chamada (opcional, padrão "Me segue para não perder"), rodape [..] (opcional), ajustes {..}."""
import json, sys
from base import pagina

CSS = """
.quando{position:absolute;left:102px;top:%(quando_top)spx;font-size:50px;line-height:60px;font-weight:400;white-space:nowrap}
.quando b{font-weight:700}
.caixa{position:absolute;left:102px;width:876px;top:%(caixa_top)spx;border:2.5px solid #161616;border-radius:30px;padding:%(caixa_pad)spx 48px;background:#fcfdff}
.tema{font-family:"Poppins";font-weight:400;font-size:%(tema_size)spx;line-height:%(tema_lh)spx;color:#161616}
.tema b{font-weight:800}
.sub{margin-top:18px;font-family:"Aileron";font-weight:400;font-size:30px;line-height:38px;color:#3d3d3d}
.chamada{position:absolute;left:0;width:1080px;top:%(chamada_top)spx;text-align:center;font-family:"Poppins";font-weight:700;font-size:54px;line-height:64px;color:#161616}
.botao{position:absolute;left:50%%;transform:translateX(-50%%);top:%(botao_top)spx;display:flex;align-items:center;gap:22px;padding:22px 46px;border-radius:999px;background:#2799ff;color:#fff;font-family:"Poppins";font-weight:600;font-size:38px;line-height:44px;white-space:nowrap}
.botao .mais{font-weight:700;font-size:46px}
.rod{font-size:%(rod_size)spx}
"""
DEF = dict(quando_top=372, caixa_top=478, caixa_pad=46, tema_size=56, tema_lh=68,
           chamada_top=930, botao_top=1030, rod_size=24, rod_top=1214)


def build(cfg):
    p = dict(DEF); p.update(cfg.get("ajustes", {}))
    sub = f'<div class="sub">{cfg["sub"]}</div>' if cfg.get("sub") else ""
    rod = "".join(f'<div class="rod" style="top:{p["rod_top"] + i * 32}px">{t}</div>'
                  for i, t in enumerate(cfg.get("rodape", [])))
    corpo = f"""<div class="quando">{cfg['quando']}</div>
<div class="caixa"><div class="tema">{cfg['tema']}</div>{sub}</div>
<div class="chamada">{cfg.get('chamada', 'Me segue para não perder')}</div>
<div class="botao"><span class="mais">+</span>Seguir @infobolsainvestimentos</div>
{rod}"""
    return pagina(CSS % p, corpo)


if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    open(sys.argv[2], "w").write(build(cfg))

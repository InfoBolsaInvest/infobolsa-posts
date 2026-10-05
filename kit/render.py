import os
import sys, asyncio
from playwright.async_api import async_playwright
async def main(src, out, scale=1):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':1080,'height':1350}, device_scale_factor=scale)
        await pg.goto('file://'+os.path.dirname(os.path.abspath(__file__))+'/'+src)
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(300)
        await pg.screenshot(path=out, clip={'x':0,'y':0,'width':1080,'height':1350})
        await b.close()
asyncio.run(main(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv)>3 else 1))

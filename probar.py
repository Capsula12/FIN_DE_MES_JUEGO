"""Prueba automática del juego: recorre todas las opciones hasta el final y guarda
capturas de cada pantalla. Uso: python probar.py [carpeta_de_capturas]"""
import base64, pathlib, sys, time
from playwright.sync_api import sync_playwright

aqui = pathlib.Path(__file__).parent
out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else aqui / "_capturas"
out.mkdir(exist_ok=True)

with sync_playwright() as p:
    nav = p.chromium.launch(channel="msedge", headless=True)
    page = nav.new_page(viewport={"width": 540, "height": 960})
    errores = []
    page.on("pageerror", lambda e: errores.append(str(e)))
    page.goto((aqui / "index.html").as_uri())
    page.wait_for_function("document.fonts.status === 'loaded'")
    time.sleep(.5)

    # 1) recorrido: siempre la primera opción habilitada (prueba que todo lleva al final)
    camino = []
    for paso in range(120):
        estado = page.evaluate("""() => {
          G.textT0 = -1e9; if (G.pop) G.pop.t0 = -1e9;
          return { id: G.id, pop: !!G.pop, opts: visibleOpts().map(o => o.txt + (isOff(o) ? ' [gris]' : '')) };
        }""")
        if not camino or camino[-1] != estado["id"]:
            camino.append(estado["id"])
        if estado["id"] == "fin":
            break
        page.evaluate("""() => {
          if (G.pop) { press(null); return; }
          const v = visibleOpts(); const i = v.findIndex(o => !isOff(o)); G.sel = i; press(null);
        }""")
        time.sleep(.05)
    print("camino:", " > ".join(camino))

    # 2) una captura por pantalla, con el texto completo
    for sid in page.evaluate("Object.keys(SCREENS)"):
        page.evaluate("id => { G.pop = null; go(id); G.textT0 = -1e9; G.fade = -9; }", sid)
        time.sleep(1.2 if sid in ("ciudad", "explica", "cuota") else .5)
        data = page.evaluate("c.toDataURL('image/png').split(',')[1]")
        (out / f"{sid}.png").write_bytes(base64.b64decode(data))
    print("errores:", errores or "ninguno")
    nav.close()

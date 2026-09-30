# Fin de mes - el juego

Juego de elecciones que no se pueden elegir: toda decisión lleva a endeudarse, a no poder pagar y a la mora. Hecho en pixel art, con música de 8 bits generada en el navegador.

- `index.html`: el juego completo, en un solo archivo. Se abre en cualquier navegador, en celular o computadora. No necesita instalar nada.
- `probar.py`: prueba automática; recorre el juego hasta el final y guarda una captura de cada pantalla en `_capturas/` (no se sube al repositorio).

## Cómo se juega

Tocar o hacer clic en las opciones. En computadora también: flechas para moverse, Enter para elegir, M para silenciar. El ícono del parlante arriba a la derecha prende y apaga el sonido.

## Recorrido

1. Pantalla de inicio y elección de personaje (multimillonario: "los cupos están ocupados").
2. La heladera vacía: las opciones ridículas no sacian el hambre; pedir plata prestada está desde el principio, al final de la lista.
3. Tarjeta y préstamo del banco rechazados; aparece Mercado Libre.
4. Tasas de 15 %, 50 % y 70 % "no disponibles para vos"; sólo queda la de 150 %.
5. La cuota se lleva medio sueldo: pagar o comprar comida.
6. Si paga, a los diez días no hay comida y aparece Naranja: una deuda para pagar otra.
7. Dos cuotas que superan el sueldo; mora; llamados que no se pueden cortar.
8. El banco da la deuda por irrecuperable y la saca de su balance.
9. En la tele: "bajó la mora". Qué mide ese número y a quién deja afuera.
10. La ciudad: 5.761.876 personas en mora.
11. El Congreso: la última elección no es tuya.

## Cómo editar

Todo el contenido está en el objeto `SCREENS` de `index.html`: cada pantalla tiene su texto, su música (`song`), sus barras (`hud`) y sus opciones. Tipos de opción:

- `go`: lleva a otra pantalla.
- `fail`: muestra un mensaje y la opción queda tachada.
- `deny`: queda gris con una nota en rojo.
- `msg`: muestra un mensaje (y si además tiene `go`, sigue).
- `hidden`: aparece sólo cuando se agotaron las demás.

Los temas musicales están en `SONGS` (notas por corchea, `null` es silencio).

## Publicarlo

Es un archivo estático: alcanza con servir `index.html` desde cualquier servidor web.

**GitHub Pages:** en el repositorio, *Settings > Pages > Build and deployment*, elegir *Deploy from a branch*, rama `main`, carpeta `/ (root)`, y guardar. En uno o dos minutos queda en `https://capsula12.github.io/FIN_DE_MES_JUEGO/`.

**Otro servidor:** copiar `index.html` a una carpeta del sitio (por ejemplo `/fin-de-mes/`).

## Probarlo

`probar.py` necesita `pip install playwright` y usa el Edge instalado en la computadora.

La tipografía se carga desde Google Fonts, así que el juego necesita conexión a internet.

Los datos salen de la Central de Deudores del BCRA (julio y agosto 2026, elaboración propia). Las tasas del juego son ilustrativas.

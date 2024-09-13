# Proyecto_Equipo2_TC1001S
Repositorio para integrar juegos modificados del Equipo 2

## Memorama
### Gabriela Chimali Nava Ramírez --- A01710530

El programa 'memorama.py' despliega en una ventana emergente un tablero con 8x8 fichas "volteadas", en este tienes que encontrar pares de números, las modificaciones que se le hicieron fueron:

* **Reescribir el código en español:** Para unificar el idioma de los commits con el del juego.
* **Revisar el código con flake 8:** Para asegurar que siga el estándar de codificacón PEP8, realizando las modificaciones correspondientes.
* **Agregar un contador de clics:** Que muestra al usuario, en la parte superior de la ventana, las veces que hizo clic sobre el tablero hasta que encuentra todos los pares del memorama. Para esto se incrementó el tamaño de la ventana en el eje 'y', se agregó un contador para los clics, este sólo aumenta cuando se hace clic sobre el tablero, y finalmente, se mostró en la pantalla el contador con la función 'write()'.
* **Agregar un mensaje al encontrar todos los pares:** Se agregó una condicional en la que se declara que cuando las 64 fichas dejen de estar ocultas se muestre un mensaje generado igualmente con la función 'write()' en la parte inferior de la ventana.

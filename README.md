# Proyecto_Equipo2_TC1001S
## Repositorio para integrar juegos modificados del Equipo 2
#### Angelo Segura A01711723: After downloading the original code of the game, modifications were made to it in a branch called A01711723,the changes were: 
- game board changes.
- change in the number of ghosts and their speed.
- code documentation.
- code fix based on flake 8.

### Tic Tac Toe
Juan Carlos Calderón García -- A01625696

Cambios:
* Modificar el tamaño y el color de los símbolos "X" y "O" y centrarlos.

Para lograr esto en el setup ,después de crear la grid, se aumentó el tamaño de la línea con la que se dibujan las O y X.

Para las funciones de dibujo se añadió una línea para definir el color de cada figura. Y en el caso de la X se modificaron los puntos de inicio de las líneas para que se mantuvieran dentro de los bordes de la grid

* Validar si una casilla ya se encuentra ocupada.

Para la validación de las casillas se creó una mtariz que representa el estado del tablero con 0 para una casilla vacía, 1 para una con una X y 2 para una casilla con O.

La matriz se actualiza cuando se dibujan las X y O, para obtener la celda de la matriz que le corresponde a cada función se agregó la función findCoords y en base a si esa posición está libre o no es si se dibuja la figura y se hace la modificación y regresa un boleano que representa esta decisión.

Finalemente, en base al boleano de las funciones de dibujo es si se cambia el turno al siguiente jugador

## Memorama
### Gabriela Chimali Nava Ramírez --- A01710530

El programa 'memorama.py' despliega en una ventana emergente un tablero con 8x8 fichas "volteadas", en este tienes que encontrar pares de números, las modificaciones que se le hicieron fueron:

* **Reescribir el código en español:** Para unificar el idioma de los commits con el del juego.
* **Revisar el código con flake 8:** Para asegurar que siga el estándar de codificacón PEP8, realizando las modificaciones correspondientes.
* **Agregar un contador de clics:** Que muestra al usuario, en la parte superior de la ventana, las veces que hizo clic sobre el tablero hasta que encuentra todos los pares del memorama. Para esto se incrementó el tamaño de la ventana en el eje 'y', se agregó un contador para los clics, este sólo aumenta cuando se hace clic sobre el tablero, y finalmente, se mostró en la pantalla el contador con la función 'write()'.
* **Agregar un mensaje al encontrar todos los pares:** Se agregó una condicional en la que se declara que cuando las 64 fichas dejen de estar ocultas se muestre un mensaje generado igualmente con la función 'write()' en la parte inferior de la ventana.

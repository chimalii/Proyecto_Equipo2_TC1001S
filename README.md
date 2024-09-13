# Proyecto_Equipo2_TC1001S
Repositorio para integrar juegos modificados del Equipo 2

## Tic Tac Toe
Juan Carlos Calderón García -- A01625696
Cambios:
* Modificar el tamaño y el color de los símbolos "X" y "O" y centrarlos.

Para lograr esto en el setup ,después de crear la grid, se aumentó el tamaño de la línea con la que se dibujan las O y X.

Para las funciones de dibujo se añadió una línea para definir el color de cada figura. Y en el caso de la X se modificaron los puntos de inicio de las líneas para que se mantuvieran dentro de los bordes de la grid

* Validar si una casilla ya se encuentra ocupada.

Para la validación de las casillas se creó una mtariz que representa el estado del tablero con 0 para una casilla vacía, 1 para una con una X y 2 para una casilla con O.

La matriz se actualiza cuando se dibujan las X y O, para obtener la celda de la matriz que le corresponde a cada función se agregó la función findCoords y en base a si esa posición está libre o no es si se dibuja la figura y se hace la modificación y regresa un boleano que representa esta decisión.

Finalemente, en base al boleano de las funciones de dibujo es si se cambia el turno al siguiente jugador


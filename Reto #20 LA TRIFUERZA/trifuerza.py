"""
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible!
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 *
 *    *
 *   ***
 *  *   *
 * *** ***
 *
"""


def trifuerza(n: int):
    long = 2 * n

    for i in range(1, n + 1):
        text = "*" * (2 * i - 1)
        text = text.center(long * 2)
        print(text)

    for i in range(1, n + 1):
        text = "*" * (2 * i - 1)
        text = text.center(long)
        text = text * 2
        print(text)

noseque = 2
trifuerza(noseque)

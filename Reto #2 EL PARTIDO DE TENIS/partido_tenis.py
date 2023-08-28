"""
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 *
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
"""


class PartidoTenis:
    def __init__(self):
        self.puntuacion = ["Love", 15, 30, 40, "Deuce", "Ventaja", "Ha ganado"]
        self.secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
        self.P1 = 0
        self.P2 = 0

    def mostrar_puntuacion(self):
        print(f"{self.puntuacion[self.P1]} - {self.puntuacion[self.P2]}")

    def juego(self):
        for jugada in self.secuencia:
            if jugada == "P1":
                self.P1 += 1
            elif jugada == "P2":
                self.P2 += 1

            if self.P1 == 4 and self.P2 == 4:
                self.puntuacion[self.P1] = "Deuce"
                self.puntuacion[self.P2] = "Deuce"
            elif self.P1 >= 4 and self.P1 > self.P2:
                self.puntuacion[self.P1] = "Ventaja"
                self.puntuacion[self.P2] = 40
            elif self.P2 >= 4 and self.P2 > self.P1:
                self.puntuacion[self.P1] = 40
                self.puntuacion[self.P2] = "Ventaja"

            self.mostrar_puntuacion()

            if (self.P1 >= 4 and self.P1 >= self.P2 + 2) or (self.P2 >= 4 and self.P2 >= self.P1 + 2):
                print(f"{self.puntuacion[6]} el jugador {jugada}")
                break


if __name__ == '__main__':
    p: PartidoTenis = PartidoTenis()
    p.juego()

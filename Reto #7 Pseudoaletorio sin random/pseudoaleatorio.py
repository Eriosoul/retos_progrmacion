"""
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del
 *   lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
"""
import datetime
import time


def random():
    return datetime.datetime.now().microsecond % 100
    # return time.time_ns() % 100


for _ in range(0, 101):
    print(random())

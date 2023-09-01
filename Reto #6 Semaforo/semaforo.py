"""
Crear un programa simulando un semaforo en el cual vaya cambiando las luces
Verde dura 2s
Amarillo dura 0.5s
Rojo dura 2s
"""

import time
from itertools import cycle
from colorama import Fore
lights = [
    (Fore.GREEN + 'Green', 2),
    (Fore.YELLOW + 'Yellow', 0.5),
    (Fore.RED + 'Red', 2)
]

colors = cycle(lights)
while True:
    c, s = next(colors)
    print(c)
    time.sleep(s)

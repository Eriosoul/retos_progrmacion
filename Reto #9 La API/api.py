"""
* Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs:
 * https://github.com/public-apis/public-apis
"""

import requests
from pprint import pprint

from requests import Response

url: str = "https://rickandmortyapi.com/api/character"

r: Response = requests.get(url)

if r.status_code == 200:
    content = r.json()
    pprint(content)
else:
    print(f"Error en la solicitud: {r.status_code}")

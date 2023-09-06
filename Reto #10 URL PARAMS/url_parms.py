"""
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
"""
import re


def parms():
    url = "https://retosdeprogramacion.com?year=2023&challenge=0"
    components = url.split("&")
    for component in components:
        if "=" in component:
            param = component.split("=")
            if len(param) == 2 and param[1] != "":
                print(param[1])

    regex = r"=([a-zA-Z0-9]+)"
    params = re.findall(regex, url)
    print(params)

parms()

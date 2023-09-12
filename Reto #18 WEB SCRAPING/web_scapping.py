"""
* El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 *
"""

import requests
from bs4 import BeautifulSoup


class Eventos:
    def __init__(self):
        self.url = 'https://holamundo.day'
        self.response = None

    def get_status(self):
        try:
            self.response = requests.get(self.url)
            self.response.raise_for_status()
            print("Conexion aceptada: ", self.response.status_code)
            return self.response.status_code
        except requests.exceptions.RequestException as e:
            print("Error en la conexion: ", e)

    def ger_status(self):
        if self.response is not None:
            return self.response.status_code
        else:
            return self.get_status()

    def get_data(self):
        if self.response is not None:
            try:
                soup = BeautifulSoup(self.response.text, "html.parser")
                content = soup.find_all("blockquote")
                for data in content[21:]:
                    print(data.text)
                return soup
            except Exception as e:
                print("Error al analizar los datos: ", e)
                return None
        else:
            print("No se ha realizado la solicitud HTTP")
            return None


if __name__ == '__main__':
    e = Eventos()
    status_code = e.ger_status()
    if status_code == 200:
        data = e.get_data()
        if data is not None:
            print("Datos obtenidos exitosamente.")
        else:
            print("No se pudo obtener datos debido al estado de la conexión.")

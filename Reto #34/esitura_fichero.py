# /*
#  * Crea un programa capaz de interactuar con un fichero TXT.
#  * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección.
#  * Únicamente el código.
#  *
#  * - Si no existe, debe crear un fichero llamado "text.txt".
#  * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
#  *   en una nueva línea cada vez que se pulse el botón "Enter".
#  * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
#  *   a continuación o borrar su contenido y comenzar desde el principio.
#  * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
#  *   el texto que ya posee el fichero.
#  */

import os

file_name = "text.txt"

if os.path.exists(file_name):
    print("El fichero extiste. ¿Que quieres hacer?")
    text = input("Pula \"enter\" para contunuar o escribe \"delete\" para eliminar: ")

    if text == "delete":
        os.remove(file_name)
    else:
        # abrir fichero modo lectura
        file = open(file_name, "r")
        print(file.read())
# para que el texto se quede guardado usando "a" se usa el texto anterior del fichero
# con "w" se borraria el contenido del fichero y solo apareceria lo ultimo escrito
file = open(file_name, "a")

while True:
    text = input("Introduce el texto a continuacion o \"exit\" para salir: ")

    if text == "exit":
        break

    file.write(text + "\n")
    file.flush()

file.close()

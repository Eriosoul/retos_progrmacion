"""
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
"""

import re


def word_exercise(text: str):
    word_content = 0
    number_sentence = 0
    letter_count = 0
    long_word = []

    words = text.replace("\n", "  ").split(" ")

    for word in words:
        if len(word) != 0:
            if "." in word:
                number_sentence += 1

            current_word = re.sub(r"[^\w]", "", word)

            print(current_word)

            word_content += 1
            letter_count += len(current_word)

            if len(long_word) == 0 or len(long_word[0]) == len(current_word):
                long_word.append(current_word)
            elif len(current_word) > len(long_word[0]):
                long_word.clear()
                long_word.append(current_word)

    print("Total de palabras: ", word_content)
    print("Media de longitud: ", letter_count / word_content)
    print("Cantidad oraciones: ", number_sentence)
    print("Palabra larga : ", long_word)


# Mi desarrollo
def tema_palabras(text):
    palabra = text.split()
    cantidad_palabra = len(palabra)
    return cantidad_palabra


def longitud_palabras(text):
    palabra = text.split()
    longitud = []
    for longi_palabra in palabra:
        longitud.append(len(longi_palabra))
    return longitud


def oraciones(text):
    oraciones = text.split(".")
    numero_oraciones = 0

    for oracion in oraciones:
        palabra = oracion.split()
        if palabra:
            numero_oraciones += 1

    return numero_oraciones

    # oraciones = text.split(".")
    # oraciones = [oracion.strip() for oracion in oraciones if oracion.strip()]
    # numero_oraciones = len(oraciones)
    #
    # return numero_oraciones


def palabra_larga(text):
    palabras = text.split()
    if not palabras:
        return None  # Devolver None si el texto está vacío
    palabra_mas_larga = max(palabras, key=len)
    return palabra_mas_larga


text = "Monster Hunter: World es un videojuego perteneciente al género de rol y acción. Desarrollado y publicado por la empresa Capcom, siendo el sexto título principal de la franquicia de videojuegos Monster Hunter."

word_exercise("""
Monster Hunter: World es un videojuego perteneciente al género de rol y acción. 
Desarrollado y publicado por la empresa Capcom, siendo el sexto título 
principal de la franquicia de videojuegos Monster Hunter.
""")

cantidad = tema_palabras(text)
print("Numero de palabras: ", cantidad)
longitud = longitud_palabras(text)
print("Longitud de palabras: ", longitud)
oracion = oraciones(text)
print("Cantidad de oraciones: ", oracion)
palabra_larga = palabra_larga(text)
print("Palabra las larga : ", palabra_larga)

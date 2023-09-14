"""
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
"""


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


text = """ Monster Hunter: World es un videojuego perteneciente al género de rol y acción. Desarrollado y publicado por 
       la empresa Capcom, siendo el sexto título principal de la franquicia de videojuegos Monster Hunter.
       """

cantidad = tema_palabras(text)
print("Numero de palabras: ", cantidad)
longitud = longitud_palabras(text)
print("Longitud de palabras: ", longitud)
oracion = oraciones(text)
print("Cantidad de oraciones: ", oracion)
palabra_larga = palabra_larga(text)
print("Palabra las larga : ", palabra_larga)

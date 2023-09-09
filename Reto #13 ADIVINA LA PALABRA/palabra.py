"""
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
 *   ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
"""

palabra = "mouredev"
letras = list(palabra)
adivinas = ["_"] * len(letras)

vidas = 5

while vidas > 0:
    print("La palabra a adivinar contiene:", adivinas)
    adivina_palabra = str(input("Introduce la letra: ")).lower()
    if adivina_palabra in letras:
        print("¡Correcto! La letra", adivina_palabra, "está en la palabra.")
        for i in range(len(letras)):
            if letras[i] == adivina_palabra:
                adivinas[i] = adivina_palabra
        if "".join(adivinas) == palabra:
            print("Esas la plabara", palabra)
            break
    else:
        vidas -= 1

if vidas == 0:
    print("¡GAME OVER!")
#
# palabra = "mouredev"
# letras = list(palabra)
# adivinadas = ["_"] * len(letras)
#
# # Número de vidas
# vidas = 5
# while vidas > 0:
#     adivina = input("Introduce la letra: ").lower()
#
#     for p in palabra:
#         p.split()
#
#         letras.append(p)
#     if adivina in letras:
#         print("¡Correcto, la letra", adivina, "esta en la palabra")
#         for i in range(len(letras)):
#             if letras[i] == adivina:
#                 adivinadas[i] = adivina
#             if "".join(adivinadas) == palabra:
#                 print("¡Felicidades! Has adivinado la palabra: ", palabra)
#                 break
#     else:
#         vidas -= 1
#         print("No ta: ", vidas, "vidas")
#
# if vidas == 0:
#     print("GAME OVER!")

"""
* Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""


def leet_speak(text):
    leet_dict = {
        'a': '4', 'b': '8', 'c': '(', 'd': 'd', 'e': '3', 'f': 'f', 'g': '9',
        'h': '#', 'i': '1', 'j': 'j', 'k': 'k', 'l': '1', 'm': 'm', 'n': 'n',
        'o': '0', 'p': 'p', 'q': 'q', 'r': '2', 's': '5', 't': '7', 'u': 'u',
        'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': '2', '0': '0', '1': '1',
        '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8',
        '9': '9'
    }
    return "".join(leet_dict.get(c.lower(), c) for c in text)


print(leet_speak("Hello World!"))

"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""
import string
import random


class PasswordGenerator:
    def __init__(self):
        self.letters = string.ascii_letters
        self.numbers = string.digits
        self.symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    def generate_random(self):
        letter_pass = self.letters
        number_pass = self.numbers
        symbols = self.symbols
        option = input("Generar contraseñas, "
                       "Escribe letras: \"letras\" para una contraseña solo con letras, \n"
                       "Escribe numeros \"numero\" para una contraseña con letras y numero \n"
                       "Escribe numeros \"symbols\" para una contraseña con letras, numero y symbols "
                       ": \n")
        length = random.randint(8, 16)
        if option == "letras":
            password = ''.join(random.choice(letter_pass) for _ in range(length))
            return password
        elif option == "numero":
            password = ''.join(random.choice(letter_pass + number_pass) for _ in range(length))
            return password
        elif option == "symbols":
            password = ''.join(random.choice(letter_pass + number_pass + symbols) for _ in range(length))
            return password
        else:
            print('opcion no valida')


if __name__ == '__main__':
    p: PasswordGenerator = PasswordGenerator()
    generated_password = p.generate_random()
    if generated_password:
        print("Contraseña generada:", generated_password)

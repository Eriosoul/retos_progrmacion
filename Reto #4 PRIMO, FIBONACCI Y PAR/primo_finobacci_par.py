"""
* Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""


class Programa:
    def __init__(self, num):
        self.num = num

    def check_primo(self):
        es_primo: bool = True
        for n in range(2, self.num):
            if self.num % n == 0:
                es_primo = False
                return "No es primo", es_primo
        if es_primo:
            return "Es primo"

    def check_par_impar(self):
        if self.num % 2 == 0:
            return "es par"
        else:
            return "es impar"

    def fibonacci(self):
        a, b = 0, 1
        fibonacci = False
        while b < self.num:
            a, b = b, a+ b
            if b == self.num:
                fibonacci = True
                break
        return "es fibonacci" if fibonacci else "no es fibonacci"


if __name__ == '__main__':
    nums = [2, 7]
    for n in nums:
        p: Programa = Programa(n)
        print(f"Con el número {p.num} {p.check_primo()}, {p.fibonacci()} y {p.check_par_impar()}\n")


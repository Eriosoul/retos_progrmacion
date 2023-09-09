def bin(decimal: int):
    current_decimal = decimal
    bin_values = "01"
    binario = ""
    while current_decimal > 0:
        binario = bin_values[current_decimal % 2] + binario
        # funcion de division y sasignaicon
        current_decimal //= 2
    binario = 0 if binario == "" else binario
    print(f"{decimal} en octal {binario}")


def octal(decimal: int):
    current_decimal = decimal
    octa = ""
    while current_decimal > 0:
        octa = str(int(current_decimal % 8)) + octa
        # funcion de division y sasignaicon
        current_decimal //= 8
    octa = 0 if octa == "" else octa
    print(f"{decimal} en octal {octa}")


def hexa(decimal: int):
    num_decimal = decimal
    hexa_values = "0123456789ABCDEF"
    hex = ""
    while num_decimal > 0:
        hex = hexa_values[num_decimal % 16] + hex
        num_decimal //= 16
    hex = 0 if hex == "" else hex
    print(f"{decimal} en hexa {hex}")


bin(3650)
octal(3650)
hexa(3650)

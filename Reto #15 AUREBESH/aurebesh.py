"""
 * Crea una función que sea capaz de transformar Español al lenguaje básico
 * del universo Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
"""
# Eeste reto me costo mas de lo debido y al final cai en mirar el codigo de Mouredev
from unidecode import unidecode


def transform_sp_sw(text: str, aurebesh: bool) -> str:
    basic_alphabet = {
        "a": "aurek", "b": "besh", "c": "cresh", "d": "dorn", "e": "esk", "f": "forn", "g": "grek", "h": "herf",
        "i": "isk", "j": "jenth", "k": "krill", "l": "leth", "m": "merm", "n": "nern", "o": "osk", "p": "peth",
        "q": "qek", "r": "resh", "s": "senth", "t": "trill", "u": "usk", "v": "vev", "w": "wesk", "x": "xesh", "y": "yirt",
        "z": "zerek", "ae": "enth", "eo": "onith", "kh": "krenth", "ng": "nen", "oo": "orenth", "sh": "sen", "th": "thesh"}

    aurebesh_alphabet = dict()

    for key, value in basic_alphabet.items():
        aurebesh_alphabet[value] = key

    unidecode_text = unidecode(text.lower().replace("ñ", "[?]")).replace("[?]", "ñ")
    translate_text = ""

    if aurebesh:
        char_index = 0
        text_len = len(text)

        while char_index < text_len:
            simple_char = unidecode_text[char_index]
            double_character = ""

            if char_index < text_len - 1:
                double_character = simple_char + unidecode_text[char_index + 1]

            if double_character in basic_alphabet:
                translate_text += basic_alphabet[double_character]
                char_index += 2
            else:
                translate_text += basic_alphabet.get(
                    simple_char, simple_char)
                char_index += 1
    else:
        translate_text = text
        for key, value in aurebesh_alphabet.items():
            translate_text = translate_text.replace(key, value)

    return translate_text


aurebesh = transform_sp_sw("Amistandolarasuardon giminsastargustoquermos hormsitaporynsile", True)
print(aurebesh)
basic = transform_sp_sw(aurebesh, False)
print(basic)

aurebesh = transform_sp_sw("La fuerza se desvancece..", False)
print(aurebesh)
basic = transform_sp_sw(aurebesh, True)
print(basic)

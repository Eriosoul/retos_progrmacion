"""
* Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
"""
import re


def _text_counter(text: str) -> dict[str, int]:
    no_number_text = re.sub(r"\d+", "", text.lower())
    no_punt_text = re.sub(r"[^\w\s]", "", no_number_text)
    char_counter = dict()

    for char in text:
        if char in char_counter.keys():
            char_counter[char] += 1
        else:
            char_counter[char] = 1

    return char_counter


def heterograma(text: str) -> bool:
    # Los heterogramas son palabras que no repiten ninguna letra
    for counter in _text_counter(text).values():
        if counter > 1:
            return False
    return True


def isograma(text: str) -> bool:
    main_counter = 0
    for counter in _text_counter(text).values():
        if main_counter is 0:
            main_counter = counter
        if main_counter is not counter:
            return False
    return True


def pangrama(text: str) -> bool:
    # Debe contener todas las letas del dicionario
    return len(_text_counter(text).keys()) is 27


text = _text_counter("palabra")

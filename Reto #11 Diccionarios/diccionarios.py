"""
* Crea un diccionario llamado persona con las llaves nombre, apellido,. edad y su valores respectivos.
* Agrega una llave puede_votar con tipo dato bool
* Agrega ota llave juegos_vaforitos con un lista de strings
* Modifica lista juegos_favoriots para agregar el juego "Duck Hunt"
* Elimina la llave apellido
* Concatenar los sigientes diccionarios para crear uno nuevo con todos los pares de llaves/valores
dict1 = {1:"uno"}
dict1 = {2:"dos"}
dict1 = {3:"tres"}
"""

personas = { "nombre": "Andrei", "apellido": "Apostol", "edad": 25 }
personas["puede_votar"] = True
personas["juegos_favoriots"] = ["Naruto", "Lol", "Black Desert"]
personas["juegos_favoriots"].append("Duck Hunt")

print(personas)


def puede_votar() -> bool:
    if personas["edad"] >18:
        print(f"La persona {personas['nombre']} {personas['apellido']} puede votar")
        return True
    else:
        print("No puede votar")
        return False


puede_votar()
del personas["apellido"]
print(personas)

dict1 = {1: "uno"}
dict2 = {2: "dos"}
dict3 = {3: "tres"}
new_dict = {}
new_dict.update(dict1)
new_dict.update(dict2)
new_dict.update(dict3)
print(new_dict)

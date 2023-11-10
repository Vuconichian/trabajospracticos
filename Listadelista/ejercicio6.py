
class Superheroe:
    def __init__(self, nombre, año_aparicion, casa, biografia):
        self.nombre = nombre
        self.año_aparicion = año_aparicion
        self.casa = casa
        self.biografia = biografia

# Crear una lista de Superhéroes
superheroes = [
    Superheroe("Linterna Verde", 1960, "DC", "Biografía de Linterna Verde"),
    Superheroe("Wolverine", 1974, "Marvel", "traje"),
    Superheroe("Dr. Strange", 1963, "Marvel", "Biografía de Dr. Strange"),
    Superheroe("Iron Man", 1963, "Marvel", "armadura"),
    Superheroe("Spider-Man", 1962, "Marvel", "traje"),
    Superheroe("Thor", 1962, "Marvel", "armadura"),
    Superheroe("Hulk", 1962, "Marvel", "Biografía de Hulk"),
    Superheroe("Captain America", 1941, "Marvel", "armadura"),
    Superheroe("Black Widow", 1964, "Marvel", "traje"),
    Superheroe("Black Panther", 1966, "Marvel", "traje"),
    Superheroe("Scarlet Witch", 1964, "Marvel", "Biografía de Scarlet Witch"),
    Superheroe("Ant-Man", 1962, "Marvel", "Biografía de Ant-Man"),
    Superheroe("Superman", 1938, "DC", "traje"),
    Superheroe("Capitana Marvel", 1967, "Marvel", "Biografía de Capitana Marvel"),
    Superheroe("Batman", 1939, "DC", "armadura"),
    Superheroe("Mujer Maravilla", 1941, "DC", "traje"),
    Superheroe("The Flash", 1940, "DC", "traje"),
    Superheroe("Aquaman", 1941, "DC", "Biografía de Aquaman"),
    Superheroe("Batwoman", 1956, "DC", "traje"),
    Superheroe("Star-Lord", 1976, "Marvel", "Biografía de Star-Lord"),
]

# a. Eliminar el nodo que contiene la información de Linterna Verde
def eliminar_superheroe(superheroes, nombre):
    for superheroe in superheroes:
        if superheroe.nombre == nombre:
            superheroes.remove(superheroe)
            break

eliminar_superheroe(superheroes, "Linterna Verde")
print("A. Superheroe 'Linterna Verde' eliminado")

# b. Mostrar el año de aparición de Wolverine
def mostrar_año_wolverine(superheroes, nombre):
    for superheroe in superheroes:
        if superheroe.nombre == nombre:
            return superheroe.año_aparicion
    return None

print("____________________")
print("B. Año de aparicion de Wolverine: ",(mostrar_año_wolverine(superheroes, "Wolverine")))

# c. Cambiar la casa de Dr. Strange a Marvel
def cambiar_casa_dr_strange(superheroes, nombre):
    for superheroe in superheroes:
        if superheroe.nombre == nombre:
            superheroe.casa = "Marvel"

cambiar_casa_dr_strange(superheroes, "Dr. Strange")
print("____________________")
print("C. El superheroe 'Dr. Strange' ha sido cambiado de casa, desde casa DC a casa Marvel")

# d. Mostrar el nombre de superhéroes que mencionan "traje" o "armadura" en su biografía
def superheroes_con_palabra(superheroes, palabra):
    nombres = []
    for superheroe in superheroes:
        if palabra in superheroe.biografia.lower():
            nombres.append(superheroe.nombre)
    return nombres

print("____________________")
print("D. Superheroes con traje: ", (superheroes_con_palabra(superheroes, "traje")))
print("   Superheroes con armadura: ", (superheroes_con_palabra(superheroes, "armadura")))

# e. Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
def superheroes_anteriores_1963(superheroes, año_limite):
    info_superheroes = []
    for superheroe in superheroes:
        if superheroe.año_aparicion < año_limite:
            info_superheroes.append((superheroe.nombre, superheroe.casa))
    return info_superheroes

print("____________________")
print("E. Los siguientes superheroes tuvieron su primera aparición antes de 1963: ",(superheroes_anteriores_1963(superheroes, 1963)))

# f. Mostrar la casa a la que pertenecen Capitana Marvel y Mujer Maravilla
def casa_de_superheroes(superheroes, nombres):
    casas = {}
    for superheroe in superheroes:
        if superheroe.nombre in nombres:
            casas[superheroe.nombre] = superheroe.casa
    return casas

print("____________________")
print("F. Las superheroinas Capitana Marvel y Mujer maravilla pertenecen a las siguientes casas respectivamente: ", (casa_de_superheroes(superheroes, ["Capitana Marvel", "Mujer Maravilla"])))

# g. Mostrar toda la información de Flash y Star-Lord
def informacion_superheroes(superheroes, nombres):
    info = []
    for superheroe in superheroes:
        if superheroe.nombre in nombres:
            info.append(superheroe.__dict__)
    return info

print("____________________")
print("G. Información sobre los superheroes 'The Flash' y 'Star-Lord': ", (informacion_superheroes(superheroes, ["The Flash", "Star-Lord"])))

# h. Listar los superhéroes que comienzan con la letra B, M y S
def superheroes_por_letra(superheroes, letras):
    nombres = []
    for superheroe in superheroes:
        if superheroe.nombre[0].upper() in letras:
            nombres.append(superheroe.nombre)
    return nombres
print("____________________")
print("H. Los siguientes superhéroes comienzan con la letra B, M y S: ", (superheroes_por_letra(superheroes, ["B", "M", "S"])))

# i. Determinar cuántos superhéroes hay de cada casa de comic
def contar_superheroes_por_casa(superheroes):
    conteo = {}
    for superheroe in superheroes:
        if superheroe.casa in conteo:
            conteo[superheroe.casa] += 1
        else:
            conteo[superheroe.casa] = 1
    return conteo

print("____________________")
print("I. Cantidad de superheroes por casa : ", (contar_superheroes_por_casa(superheroes)))
print("____________________")

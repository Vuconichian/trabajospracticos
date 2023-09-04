#Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
#casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias 
#para poder realizar las siguientes actividades:
# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.
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

# A
def eliminar_superheroe(superheroes, nombre):
    for superheroe in superheroes:
        if superheroe.nombre == nombre:
            superheroes.remove(superheroe)
            break

eliminar_superheroe(superheroes, "Linterna Verde")
print("A. Superheroe 'Linterna Verde' eliminado")

# B
def mostrar_año_wolverine(superheroes, nombre):
    for superheroe in superheroes:
        if superheroe.nombre == nombre:
            return superheroe.año_aparicion
    return None

print("____________________")
print("B. Año de aparicion de Wolverine: ",(mostrar_año_wolverine(superheroes, "Wolverine")))

# C
def cambiar_casa_dr_strange(superheroes, nombre):
    for superheroe in superheroes:
        if superheroe.nombre == nombre:
            superheroe.casa = "Marvel"

cambiar_casa_dr_strange(superheroes, "Dr. Strange")
print("____________________")
print("C. El superheroe 'Dr. Strange' ha sido cambiado de casa, desde casa DC a casa Marvel")

# D
def superheroes_con_palabra(superheroes, palabra):
    nombres = []
    for superheroe in superheroes:
        if palabra in superheroe.biografia.lower():
            nombres.append(superheroe.nombre)
    return nombres

print("____________________")
print("D. Superheroes con traje: ", (superheroes_con_palabra(superheroes, "traje")))
print("   Superheroes con armadura: ", (superheroes_con_palabra(superheroes, "armadura")))

# E
def superheroes_anteriores_1963(superheroes, año_limite):
    info_superheroes = []
    for superheroe in superheroes:
        if superheroe.año_aparicion < año_limite:
            info_superheroes.append((superheroe.nombre, superheroe.casa))
    return info_superheroes

print("____________________")
print("E. Los siguientes superheroes tuvieron su primera aparición antes de 1963: ",(superheroes_anteriores_1963(superheroes, 1963)))

# F
def casa_de_superheroes(superheroes, nombres):
    casas = {}
    for superheroe in superheroes:
        if superheroe.nombre in nombres:
            casas[superheroe.nombre] = superheroe.casa
    return casas

print("____________________")
print("F. Las superheroinas Capitana Marvel y Mujer maravilla pertenecen a las siguientes casas respectivamente: ", (casa_de_superheroes(superheroes, ["Capitana Marvel", "Mujer Maravilla"])))

# G
def informacion_superheroes(superheroes, nombres):
    info = []
    for superheroe in superheroes:
        if superheroe.nombre in nombres:
            info.append(superheroe.__dict__)
    return info

print("____________________")
print("G. Información sobre los superheroes 'The Flash' y 'Star-Lord': ", (informacion_superheroes(superheroes, ["The Flash", "Star-Lord"])))

# H
def superheroes_por_letra(superheroes, letras):
    nombres = []
    for superheroe in superheroes:
        if superheroe.nombre[0].upper() in letras:
            nombres.append(superheroe.nombre)
    return nombres
print("____________________")
print("H. Los siguientes superhéroes comienzan con la letra B, M y S: ", (superheroes_por_letra(superheroes, ["B", "M", "S"])))

# I
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

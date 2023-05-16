#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre 
#y la cantidad de películas de la saga en la que participó, implementar las funciones necesarias para 
#resolver las siguientes actividades:

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;

#b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de
#películas en la que aparece;

#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);

#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from pila import Pila


pila_MarvelUniverse = Pila()


pila_MarvelUniverse .push({"nombre": "Black Widow", "peliculas": 8})
pila_MarvelUniverse .push({"nombre": "Thor", "peliculas": 9})
pila_MarvelUniverse .push({"nombre": "Rocket Raccoon", "peliculas": 5})
pila_MarvelUniverse .push({"nombre": "Doctor Strange", "peliculas": 3})
pila_MarvelUniverse .push({"nombre": "Iron Man", "peliculas": 10})
pila_MarvelUniverse .push({"nombre": "Capitán América", "peliculas": 6})
pila_MarvelUniverse .push({"nombre": "Groot", "peliculas": 4})
pila_MarvelUniverse .push({"nombre": "Hulk", "peliculas": 7})


personajes_con_mas_de_cinco_peliculas = []
for personaje in pila_MarvelUniverse ._Pila__elements:
    if personaje["peliculas"] > 5:
        personajes_con_mas_de_cinco_peliculas.append(personaje)
        print(personaje["nombre"], "- Películas:", personaje["peliculas"])


posicion_rocket_raccon = pila_MarvelUniverse.size() - pila_MarvelUniverse ._Pila__elements.index({"nombre": "Rocket Raccoon", "peliculas": 5}) + 1
posicion_groot = pila_MarvelUniverse .size() - pila_MarvelUniverse ._Pila__elements.index({"nombre": "Groot", "peliculas": 4}) + 1
print("Posición de Rocket Raccoon:", posicion_rocket_raccon)
print("Posición de Groot:", posicion_groot)

contador_peliculas_Black_Widow = 0
for personaje in pila_MarvelUniverse._Pila__elements:
    if personaje["nombre"] == "Black Widow":
        contador_peliculas_Black_Widow += personaje["peliculas"]
print("Número de películas de Viuda Negra:", contador_peliculas_Black_Widow)

iniciales = ["C", "D", "G"]
personajes_iniciales = []
for personaje in pila_MarvelUniverse ._Pila__elements:
    if personaje["nombre"][0] in iniciales:
        personajes_iniciales.append(personaje)
for personaje in personajes_iniciales:
    print(personaje["nombre"])
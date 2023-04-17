# El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste)
# está atrapado, pero muy cerca está su mochila que contiene muchos objetos. 
#Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” 
#realizar las siguientes actividades:

#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;

#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;

#c. Utilizar un vector para representar la mochila.


def usar_la_fuerza(mochila, objetos_sacados=0):
    if  mochila == []:  # Si la mochila está vacía, no se encontró el sable de luz.
        print("No se encontró un sable de luz en la mochila.")
        return
    else:
        objeto = mochila.pop(0)
        objetos_sacados += 1
        if objeto == "sable de luz":
            print(("Se encontró un sable de luz después de sacar"),(objetos_sacados),("objetos."))
            return
        else:  # Si el objeto no es un sable de luz, se sigue buscando
            usar_la_fuerza(mochila, objetos_sacados)


mochila = ["libro", "botella de agua", "linterna", "sable de luz", "comida"]
usar_la_fuerza(mochila)
#Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno,
# desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los nombre películas estrenadas en el año 2014;
# b. indicar cuántas películas se estrenaron en el año 2018;
# c. mostrar las películas de Marvel Studios estrenadas en el año 2016

from pila import Pila

class Pelicula:                #crea la clase pelicula con sus respectivos atributos
    def __init__(self, titulo, estudio, anio):
        self.titulo = titulo
        self.estudio = estudio
        self.anio = anio

#funcion que filtra todas las peliculas de la pila por año, si es = 2014 se muestra en pantalla
def mostrar_peliculas_2014(pila_peliculas):
    pila_temporal = Pila()
    while pila_peliculas.size() > 0:
        pelicula = pila_peliculas.pop()
        if pelicula.anio == 2014:
            print(pelicula.titulo)
        pila_temporal.push(pelicula)
    while pila_temporal.size() > 0:
        pila_peliculas.push(pila_temporal.pop())

#funcion que filtra todas las peliculas de la pila por año, si es = 2018, se suma el contador
def contar_peliculas_2018(pila_peliculas):
    contador = 0
    pila_temporal = Pila()
    while pila_peliculas.size() > 0:
        pelicula = pila_peliculas.pop()
        if pelicula.anio == 2018:
            contador += 1
        pila_temporal.push(pelicula)
    while pila_temporal.size() > 0:
        pila_peliculas.push(pila_temporal.pop())
    return contador

#funcion que filtra todas las peliculas de Marvel Studios de la pila en el año 2016, suma el contador
def mostrar_peliculas_marvel_2016(pila_peliculas):
    pila_temporal = Pila()
    while pila_peliculas.size() > 0:
        pelicula = pila_peliculas.pop()
        if pelicula.anio == 2016 and pelicula.estudio == "Marvel Studios":
            print(pelicula.titulo)
        pila_temporal.push(pelicula)
    while pila_temporal.size() > 0:
        pila_peliculas.push(pila_temporal.pop())


#creamos unas cuantas peliculas y las ingresamos a la pila
pila_peliculas = Pila()
pila_peliculas.push(Pelicula("Doctor Strange", "Marvel Studios", 2016))
pila_peliculas.push(Pelicula("Straight Outta Compton", "Universal Studios", 2015))
pila_peliculas.push(Pelicula("Black Panther", "Marvel Studios", 2018))
pila_peliculas.push(Pelicula("Project X", "Warner Bros. Pictures", 2012))
pila_peliculas.push(Pelicula("Spider-Man: Homecoming", "Marvel Studios", 2017))
pila_peliculas.push(Pelicula("Captain America: Civil War", "Marvel Studios", 2016))
pila_peliculas.push(Pelicula("Creed II", "Warner Bros. Pictures", 2018))


print("Películas estrenadas en 2014:")
mostrar_peliculas_2014(pila_peliculas)

print("Cantidad de películas estrenadas en 2018:")
print(contar_peliculas_2018(pila_peliculas))

print("Películas de Marvel Studios estrenadas en 2016:")
mostrar_peliculas_marvel_2016(pila_peliculas)

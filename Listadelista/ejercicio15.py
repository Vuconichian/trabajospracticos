from lista_de_lista import Lista
from random import randint


# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas.
# Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo.
# Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:

# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;


class Entrenador():

    def __init__(self, nombre, ct_ganados=0, cb_perdidas=0, cb_ganadas=0):
        self.nombre = nombre
        self.ct_ganados = ct_ganados
        self.cb_perdidas = cb_perdidas
        self.cb_ganadas = cb_ganadas

    def __str__(self):
        return f'{self.nombre} --> ctg:{self.ct_ganados}-cbg{self.cb_ganadas}-cbp{self.cb_perdidas}'

class Pokemon():

    def __init__(self, nombre, tipo, nivel=1, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre}-{self.nivel}-{self.tipo}-{self.subtipo}'


e1 = Entrenador('Juan', ct_ganados=randint(1, 10))
e2 = Entrenador('Maria', ct_ganados=randint(1, 10))
e3 = Entrenador('Ana', ct_ganados=randint(1, 10))

entrenadores = [e1, e2, e3]

lista_entrenadores = Lista()

p1 = Pokemon('pikachu', 'electrico', randint(1, 20))
p2 = Pokemon('jolteon', 'electrico', randint(1, 20))
p3 = Pokemon('vaporeon', 'agua', randint(1, 20))
p4 = Pokemon('flareon', 'fuego', randint(1, 20))
p5 = Pokemon('leafeon', 'planta', randint(1, 20))

pokemons = [p1, p2, p3, p4, p5]

#! lista principal
for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, 'nombre')

#! lista secundaria
for pokemon in pokemons:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')


lista_entrenadores.barrido_entrenadores()
print("_________")

#A
pos = lista_entrenadores.search('Juan', 'nombre')
if pos is not None:
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]
    print(f'{entrenador.nombre} tiene {sublista.size()} pokemons')

print("_________")
#! B
lista_entrenadores.barrido_cantidad_torneos_ganados(6)

print("_________")
#! C
mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].ct_ganados
pos_mayor = 0

for pos in range(1, lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(pos)[0]
    if entrenador.ct_ganados > mayor_cantidad:
        pos_mayor = pos
        mayor_cantidad = entrenador.ct_ganados

valor = lista_entrenadores.get_element_by_index(pos_mayor)
entrenador, sublista = valor[0], valor[1]

if sublista.size() > 0:
    pokemon_mayor = sublista.get_element_by_index(0)
    for pos in range(1, sublista.size()):
        pokemon = sublista.get_element_by_index(pos)
        if pokemon.nivel > pokemon_mayor.nivel:
            pokemon_mayor = pokemon

print(f'El pokemon de mayor nivel del entrenador {entrenador.nombre} es {pokemon_mayor.nombre} {pokemon_mayor.nivel} ')


print("_________")

# D.
nombre_entrenador = 'Juan' 
pos = lista_entrenadores.search(nombre_entrenador, 'nombre')
if pos is not None:
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos)
    print(f'Datos del entrenador: {entrenador}')
    print('Pokémons:')
    sublista.barrido()

print()

# E. 
mayor_al_porcentaje = 79
for entrenador, sublista in lista_entrenadores:
    if entrenador.cb_ganadas + entrenador.cb_perdidas == 0:
        continue  
    porcentaje_ganadas = (entrenador.cb_ganadas / (entrenador.cb_ganadas + entrenador.cb_perdidas)) * 100
    if porcentaje_ganadas > mayor_al_porcentaje:
        print(f'{entrenador.nombre} tiene un porcentaje de batallas ganadas del {porcentaje_ganadas:.2f}%')

print()

# F
tipo = 'fuego'  
subtipo = 'planta'  
for i in range(lista_entrenadores.size()):
    entrenador, sublista = lista_entrenadores.get_element_by_index(i)
    tiene_tipo_subtipo = False
    for j in range(sublista.size()):
        pokemon = sublista.get_element_by_index(j)
        if pokemon.tipo == tipo and pokemon.subtipo == subtipo:
            tiene_tipo_subtipo = True
            break
    if tiene_tipo_subtipo:
        print(f'{entrenador.nombre} tiene Pokémon de tipo {tipo} y subtipo {subtipo}')

print()

# G
nombre_entrenador = 'Juan'  
pos = lista_entrenadores.search(nombre_entrenador, 'nombre')
if pos is not None:
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos)
    total_nivel = 0
    for i in range(sublista.size()):
        pokemon = sublista.get_element_by_index(i)
        total_nivel += pokemon.nivel
    if sublista.size() > 0:
        promedio = total_nivel / sublista.size()
        print(f'El promedio de nivel de los Pokémon de {entrenador.nombre} es {promedio:.2f}')

print()
# H
nombre_pokemon = 'pikachu'  
count = 0
for i in range(lista_entrenadores.size()):
    entrenador, sublista = lista_entrenadores.get_element_by_index(i)
    for j in range(sublista.size()):
        pokemon = sublista.get_element_by_index(j)
        if pokemon.nombre == nombre_pokemon:
            count += 1
            break 

print(f'{count} entrenadores tienen a {nombre_pokemon}')

print()

# I
for i in range(lista_entrenadores.size()):
    entrenador, sublista = lista_entrenadores.get_element_by_index(i)
    pokemon_set = set()
    tiene_repetidos = False
    for j in range(sublista.size()):
        pokemon = sublista.get_element_by_index(j)
        if pokemon.nombre in pokemon_set:
            tiene_repetidos = True
            break
        else:
            pokemon_set.add(pokemon.nombre)
    if tiene_repetidos:
        print(f'{entrenador.nombre} tiene Pokémon repetidos')

print()

# J
pokemon_lista = ['Tyrantrum', 'Terrakion', 'Wingull']  
for i in range(lista_entrenadores.size()):
    entrenador, sublista = lista_entrenadores.get_element_by_index(i)
    for j in range(sublista.size()):
        pokemon = sublista.get_element_by_index(j)
        if pokemon.nombre in pokemon_lista:
            print(f'{entrenador.nombre} tiene a {pokemon.nombre}')

print()

# K
nombre_entrenador = 'Juan'
nombre_pokemon = 'pikachu'  
pos_entrenador = lista_entrenadores.search(nombre_entrenador, 'nombre')
if pos_entrenador is not None:
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos_entrenador)
    for i in range(sublista.size()):
        pokemon = sublista.get_element_by_index(i)
        if pokemon.nombre == nombre_pokemon:
            print(f'{entrenador.nombre} tiene a {pokemon.nombre}')
            break
    else:
        print(f'{nombre_entrenador} no tiene a {nombre_pokemon}')

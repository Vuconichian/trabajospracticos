from arbol_binario import BinaryTree

# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU),
#  desarrollar un algoritmo que contemple lo siguiente:
# A. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica
#      si es un héroe o un villano, True y False respectivamente;
# B. listar los villanos ordenados alfabéticamente;
# C. mostrar todos los superhéroes que empiezan con C;
# D. determinar cuántos superhéroes hay el árbol; 
# E. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol 
#       y modificar su nombre;
# F. listar los superhéroes ordenados de manera descendente;
# G. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos,
#  luego resolver las siguiente tareas:
#          I. determinar cuántos nodos tiene cada árbol;
#          II. realizar un barrido ordenado alfabéticamente de cada árbol.



lista_heroes = [
    {'name': 'iron man', 'heroe': True},
    {'name': 'thanos', 'heroe': False},
    {'name': 'capitana marvel', 'heroe': True},
    {'name': 'capitan america', 'heroe': True},
    {'name': 'red skull', 'heroe': False},
    {'name': 'hulk', 'heroe': True},
    {'name': 'black widow', 'heroe': True},
    {'name': 'rocket raccon', 'heroe': True},
    {'name': 'dotor strage', 'heroe': True},
    {'name': 'doctor octopus', 'heroe': True},
    {'name': 'deadpool', 'heroe': True},
]

arbol = BinaryTree()
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

# Punto A
print('Punto A')
for heroe in lista_heroes:
    arbol.insert_node(heroe['name'], heroe['heroe'])
print('heroes')
arbol.inorden_super_or_villano(True)
print()

print('villanos')
arbol.inorden_super_or_villano(False)
print()

# Punto B
print('Punto B')
villanos = arbol.inorden_super_or_villano(False)
if villanos is not None:
    print("Listado en orden alfabético de villanos:")
    villanos.inorden()
print()


# Punto C
print('Punto C')
print("Heroes que empiezan con 'C':")
arbol.search_by_coincidence('c')
print()

# Punto D
print("Punto D")
print('cantidad de heroes', arbol.contar_heroes())
print()

#Punto E
print("Punto E")
arbol.search_by_coincidence('do')
value = input('ingrese el nombre que desea modificar ')
pos = arbol.search(value)
if pos:
        is_hero = pos.other_values
        arbol.delete_node(value)
        print('modificar')
        new_value = input('ingrese en nuevo nombre ')
        arbol.insert_node(new_value, is_hero)
else:
    print('no esta')
    print()
    arbol.inorden()

print()
#Punto F
print("Punto F")
print()
print("Heroes en orden descendente:")
arbol.inorden_descendente(arbol.root)

#Punto G
print("Punto G")
print()
arbol.dividir_arbol_heroesyvillanos()
print("arbol de heroes:")
arbol.arbol_heroes.inorden()
print()
print("Cantidad de nodos en el arbol de heroes:", arbol.arbol_heroes.contar_heroes())
print()
print("arbol de villanos:")
arbol.arbol_villanos.inorden()
print()
print("Cantidad de nodos en el arbol de villanos:", arbol.arbol_villanos.contar_villanos())



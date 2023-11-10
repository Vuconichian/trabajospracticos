from grafo import Grafo

casa = Grafo(dirigido=False)

# Punto A
print("Punto A")
print("Vertices creados")
casa.insert_vertice("cocina")
casa.insert_vertice("cochera")
casa.insert_vertice("quincho")
casa.insert_vertice("baño 1")
casa.insert_vertice("baño 2")
casa.insert_vertice("habitacion 1")
casa.insert_vertice("habitacion 2")
casa.insert_vertice("sala de estar")
casa.insert_vertice("terraza")
casa.insert_vertice("patio")
casa.insert_vertice("comedor")

# Punto B
print()
print("Punto B")
print("aristas insertadas")
casa.insert_arist("cocina", "comedor", 2)
casa.insert_arist("cocina", "baño 1", 1)
casa.insert_arist("cocina", "habitación 1", 5)
casa.insert_arist("cocina", "quincho", 10)
casa.insert_arist("cocina", "baño 2", 7)
casa.insert_arist("comedor", "habitación 1", 7)
casa.insert_arist("comedor", "quincho", 12)
casa.insert_arist("comedor", "baño 2", 9)
casa.insert_arist("cochera", "sala de estar", 2)
casa.insert_arist("cochera", "terraza", 12)
casa.insert_arist("cochera", "patio", 15)
casa.insert_arist("cochera", "cocina", 3)
casa.insert_arist("cochera", "habitación 2", 10)
casa.insert_arist("quincho", "patio", 1)
casa.insert_arist("quincho", "baño 2", 2)
casa.insert_arist("quincho", "habitación 2", 5)
casa.insert_arist("baño 1", "cocina", 1)
casa.insert_arist("baño 1", "cochera", 4)
casa.insert_arist("baño 1", "habitación 1", 6)
casa.insert_arist("baño 2", "comedor", 3)
casa.insert_arist("baño 2", "baño 1", 2)
casa.insert_arist("baño 2", "habitación 1", 5)
casa.insert_arist("habitación 1", "baño 2", 5)
casa.insert_arist("habitación 1", "cochera", 2)
casa.insert_arist("habitación 1", "patio", 5)
casa.insert_arist("habitación 2", "quincho", 5)
casa.insert_arist("habitación 2", "terraza", 2)
casa.insert_arist("habitación 2", "sala de estar", 15)
casa.insert_arist("sala de estar", "baño 1", 2)
casa.insert_arist("sala de estar", "cocina", 1)
casa.insert_arist("sala de estar", "habitación 1", 4)
casa.insert_arist("terraza", "habitación 2", 2)
casa.insert_arist("terraza", "cochera", 12)
casa.insert_arist("terraza", "patio", 7)
casa.insert_arist("patio", "habitación 1", 5)
casa.insert_arist("patio", "quincho", 1)
casa.insert_arist("patio", "cocina", 11)


# Punto C
print()
print("Punto C")


arbol_expansion_minima = casa.kruskal()


# Calcular la longitud total de los cables
longitud_total_cables = 0
for arbol in arbol_expansion_minima:
    partes = arbol.split('-')
    print(arbol)
    if len(partes) == 3:
        origen, destino, peso = partes
        peso = int(peso)
        longitud_total_cables += peso

print("Longitud total de cables necesarios: ", longitud_total_cables," metros")



print()
# Punto D
print("Punto D")

origen = "habitación 1"
destino = "sala de estar"

# Calcular el camino más corto
camino_mas_corto = casa.dijkstra(origen, destino)

cont=0

while camino_mas_corto.size()>0:
    value = camino_mas_corto.pop()
    if value[0] == "sala de estar":
        cont+=value[1]

print("Para conectar la habitacion 1 y la sala de estar se necesitan", cont , "metros")
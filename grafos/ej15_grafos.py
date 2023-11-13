from grafo import Grafo

mi_grafo = Grafo(dirigido=False)


class Maravilla:
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo


mi_grafo.insert_vertice(Maravilla("coliseo de Roma", "italia", "arquitectonica"), criterio="nombre")
mi_grafo.insert_vertice(Maravilla("machu picchu", "peru", "arquitectonica"), criterio="nombre")
mi_grafo.insert_vertice(Maravilla("cristo redentor", "brasil", "arquitectonica"), criterio="nombre")
mi_grafo.insert_vertice(Maravilla("chichen itza", "mexico", "arquitectonica"), criterio="nombre")
mi_grafo.insert_vertice(Maravilla("piramides de giza", "egipto", "arquitectonica"), criterio= "nombre")
mi_grafo.insert_vertice(Maravilla("opera de sydney", "australia", "arquitectonica"), criterio= "nombre")
mi_grafo.insert_vertice(Maravilla("gran muralla", "china", "arquitectonica"), criterio="nombre")

mi_grafo.insert_vertice(Maravilla("gran barrera de coral", "australia", "natural"), criterio="nombre")
mi_grafo.insert_vertice(Maravilla("montania de la mesa", "sudafrica", "natural"), criterio= "nombre")
mi_grafo.insert_vertice(Maravilla("bahia de halong", "vietnam", "natural"), criterio="nombre")
mi_grafo.insert_vertice(Maravilla("parque de komodo", "indonesia", "natural"), criterio= "nombre")
mi_grafo.insert_vertice(Maravilla("rio subterráneo de puerto princesa", "filipinas", "natural"), criterio= "nombre")
mi_grafo.insert_vertice(Maravilla("cataratas de iguazu", ['argentina', 'brasil'], "natural"), criterio="nombre")
mi_grafo.insert_vertice(Maravilla("isla jeju", "corea del sur", "natural"), criterio= "nombre")


mi_grafo.insert_arist('machu picchu', 'coliseo de roma', 20, criterio_vertice='nombre')
mi_grafo.insert_arist('machu picchu', 'cristo redentor', 10, criterio_vertice='nombre')
mi_grafo.insert_arist('machu picchu', 'chichen itza', 10, criterio_vertice='nombre')
mi_grafo.insert_arist('machu picchu', 'piramides de giza',15, criterio_vertice='nombre')
mi_grafo.insert_arist('machu picchu', 'opera de sydney', 25, criterio_vertice='nombre')
mi_grafo.insert_arist('machu picchu', 'gran muralla', 20, criterio_vertice='nombre')
mi_grafo.insert_arist('coliseo de roma', 'cristo redentor', 25, criterio_vertice='nombre')
mi_grafo.insert_arist('coliseo de roma', 'chichen itza', 20, criterio_vertice='nombre')
mi_grafo.insert_arist('coliseo de roma', 'piramides de giza', 20, criterio_vertice='nombre')
mi_grafo.insert_arist('coliseo de roma', 'opera de sydney', 30, criterio_vertice='nombre')
mi_grafo.insert_arist('coliseo de roma', 'gran muralla', 25, criterio_vertice='nombre')
mi_grafo.insert_arist('cristo redentor', 'chichen itza', 15, criterio_vertice='nombre')
mi_grafo.insert_arist('cristo redentor', 'opera de sydney', 30, criterio_vertice='nombre')
mi_grafo.insert_arist('cristo redentor', 'piramides de giza', 20, criterio_vertice='nombre')
mi_grafo.insert_arist('cristo redentor', 'gran muralla', 25, criterio_vertice='nombre')
mi_grafo.insert_arist('chichen itza', 'opera de sydney', 30, criterio_vertice='nombre')
mi_grafo.insert_arist('chichen itza', 'piramides de giza', 20, criterio_vertice='nombre')
mi_grafo.insert_arist('chichen itza', 'gran muralla', 25, criterio_vertice='nombre')
mi_grafo.insert_arist('piramides de giza', 'opera de sydney', 20, criterio_vertice='nombre')
mi_grafo.insert_arist('piramides de giza', 'gran muralla', 20, criterio_vertice='nombre')
mi_grafo.insert_arist('gran muralla', 'opera de sydney', 10, criterio_vertice='nombre')



mi_grafo.insert_arist('gran barrera de coral', 'montania de la mesa', 20, criterio_vertice='nombre')
mi_grafo.insert_arist('gran barrera de coral', 'bahia de halong', 10, criterio_vertice='nombre')
mi_grafo.insert_arist('gran barrera de coral', 'parque de komodo', 10, criterio_vertice='nombre')
mi_grafo.insert_arist('gran barrera de coral', 'rio subterráneo de puerto princesa',15, criterio_vertice='nombre')
mi_grafo.insert_arist('gran barrera de coral', 'cataratas de iguazu', 30, criterio_vertice='nombre')
mi_grafo.insert_arist('gran barrera de coral', 'isla jeju', 10, criterio_vertice='nombre')
mi_grafo.insert_arist('montania de la mesa', 'bahia de halong', 15, criterio_vertice='nombre')
mi_grafo.insert_arist('montania de la mesa', 'parque de komodo', 20, criterio_vertice='nombre')
mi_grafo.insert_arist('montania de la mesa', 'rio subterráneo de puerto princesa', 20, criterio_vertice='nombre')
mi_grafo.insert_arist('montania de la mesa', 'cataratas de iguazu', 30, criterio_vertice='nombre')
mi_grafo.insert_arist('montania de la mesa', 'isla jeju', 25, criterio_vertice='nombre')
mi_grafo.insert_arist('bahia de halong', 'parque de komodo', 20, criterio_vertice='nombre')
mi_grafo.insert_arist('bahia de halong', 'rio subterráneo de puerto princesa', 15, criterio_vertice='nombre')
mi_grafo.insert_arist('bahia de halong', 'cataratas de iguazu', 30, criterio_vertice='nombre')
mi_grafo.insert_arist('bahia de halong', 'isla jeju', 15, criterio_vertice='nombre')
mi_grafo.insert_arist('parque de komodo', 'rio subterráneo de puerto princesa', 30, criterio_vertice='nombre')
mi_grafo.insert_arist('parque de komodo', 'cataratas de iguazu', 30, criterio_vertice='nombre')
mi_grafo.insert_arist('parque de komodo', 'isla jeju', 15, criterio_vertice='nombre')
mi_grafo.insert_arist('rio subterráneo de puerto princesa', 'cataratas de iguazu', 30, criterio_vertice='nombre')
mi_grafo.insert_arist('rio subterráneo de puerto princesa', 'isla jeju', 15, criterio_vertice='nombre')
mi_grafo.insert_arist('cataratas de iguazu', 'isla jeju', 30, criterio_vertice='nombre')

maravillas_arquitectonicas = [
    Maravilla("coliseo de Roma", "italia", "arquitectonica"),
    Maravilla("machu picchu", "peru", "arquitectonica"),
    Maravilla("cristo redentor", "brasil", "arquitectonica"), 
    Maravilla("chichen itza", "mexico", "arquitectonica"), 
    Maravilla("opera de sydney", "australia", "arquitectonica"), 
    Maravilla("gran muralla", "china", "arquitectonica")
] 

maravillas_naturales = [
    Maravilla("gran barrera de coral", "australia", "natural"),
    Maravilla("montania de la mesa", "sudafrica", "natural"),
    Maravilla("bahia de halong", "vietnam", "natural"),
    Maravilla("parque de komodo", "indonesia", "natural"),
    Maravilla("rio subterráneo de puerto princesa", "filipinas", "natural"),
    Maravilla("cataratas de iguazu", ['argentina', 'brasil'], "natural"),
    Maravilla("isla jeju", "corea del sur", "natural")
]

#Punto C
print("Punto C")

#ARQUITECTONICAS

arbol_expansion_minima_arquitectonicas = Grafo(dirigido=False)

for maravilla in maravillas_arquitectonicas:
    arbol_expansion_minima_arquitectonicas.insert_vertice(maravilla.nombre)

bosque_1 = arbol_expansion_minima_arquitectonicas.kruskal()

for arbol in bosque_1:
    for nodo in arbol.split(';'):
        print(nodo)
print()


#NATURALES
arbol_expansion_minima_naturales = Grafo(dirigido=False)

for maravilla in maravillas_naturales:
    arbol_expansion_minima_naturales.insert_vertice(maravilla.nombre)

bosque_2 = arbol_expansion_minima_naturales.kruskal()

for arbol in bosque_1:
    for nodo in arbol.split(';'):
        print(nodo)
print()


#Punto D
print("Punto D")
Pais_a_buscar_con_maravillas = mi_grafo.contar_maravillas("brasil")
print(Pais_a_buscar_con_maravillas)


#Punto E
print("Punto E")
pais_con_mas_de_una_maravilla = mi_grafo.multiples_maravillas("brasil")
print(pais_con_mas_de_una_maravilla)

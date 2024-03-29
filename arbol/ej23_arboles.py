from arbol_binario import BinaryTree

lista_creatures = [
    {'name': 'ceto', 'defeated by': '-', 'description': 'monstruo acuático femenino', 'captured by': ''},
    {'name': 'tifon', 'defeated by': 'zeus', 'description': 'divinidad primitiva relacionada con los huracanes', 'captured by': ''},
    {'name': 'equidna', 'defeated by': 'argos panoptes', 'description': 'monstruosa ninfa serpentina femenina', 'captured by': ''},
    {'name': 'dino', 'defeated by': '-', 'description': 'otras veces llamada Persis, es una de las grayas. Su nombre quiere decir "temor".', 'captured by': ''},
    {'name': 'pefredo', 'defeated by': '-', 'description': 'es una de las tres Grayas junto con Enio y Dino', 'captured by': ''},
    {'name': 'enio', 'defeated by': '-', 'description': 'Compañera perfecta del dios Ares (dios de la guerra), puesto que ella era la diosa de las batallas', 'captured by': ''},
    {'name': 'escila', 'defeated by': '-', 'description': 'monstruo marino, con torso de mujer y cola de pez', 'captured by': ''},
    {'name': 'caribdis', 'defeated by': '-', 'description': 'monstruo marino que tragaba enormes cantidades de agua tres veces al día', 'captured by': ''},
    {'name': 'euriale', 'defeated by': '-', 'description': 'Una de las tres gorgonas, junto con Medusa y Esteno', 'captured by': ''},
    {'name': 'esteno', 'defeated by': '-', 'description': 'era una de las tres gorgonas junto con sus hermanas Euríale y Medusa', 'captured by': ''},
    {'name': 'medusa', 'defeated by': 'perseo', 'description': 'convertía en piedra a aquellos que la miraban fijamente a los ojos. Fue decapitada por Perseo', 'captured by': ''},
    {'name': 'ladon', 'defeated by': 'heracles', 'description': 'dragón de cien cabezas, era el encargado de custodiar el jardín de las Hespérides', 'captured by': ''},
    {'name': 'aguila del caucaso', 'defeated by': '-', 'description': 'es un águila gigante nacida de los monstruos Tifón y Equidna', 'captured by': ''},
    {'name': 'quimera', 'defeated by': 'belerofonte', 'description': 'monstruo híbrido del que en general se considera que es hija de Tifón y Equidna', 'captured by': ''},
    {'name': 'hidra de lerna', 'defeated by': 'heracles', 'description': 'bestia de aliento venenoso, que tenía la característica de regenerar dos cabezas por cada una que le cercenaran', 'captured by': ''},
    {'name': 'leon de nemea', 'defeated by': 'heracles', 'description': 'monstruo que vivía en Nemea. Fue vencido por Heracles.', 'captured by': ''},
    {'name': 'esfinge', 'defeated by': 'edipo', 'description': 'criatura mítica de destrucción y mala suerte, que se representaba con rostro de mujer, cuerpo de león y alada', 'captured by': ''},
    {'name': 'dragon de colquida', 'defeated by': '-', 'description': 'hijo de Equidna y Tifón. Tenía la capacidad de no dormir nunca y era el encargado de custodiar el vellocino de oro', 'captured by': ''},
    {'name': 'cerbero', 'defeated by': '-', 'description': 'perro del dios Hades; un monstruo de tres cabezas, con una serpiente en lugar de cola.', 'captured by': ''},
    {'name': 'cerda de cromion', 'defeated by': 'teseo', 'description': 'cerda monstruosa hija de Tifón y Equidna, derrotada por Teseo', 'captured by': ''},
    {'name': 'ortro', 'defeated by': 'heracles', 'description': 'perro de dos cabezas, hijo de Equidna y Tifón, y hermano de Cerbero', 'captured by': ''},
    {'name': 'toro de creta', 'defeated by': 'teseo', 'description': 'Padre del minotauro; Minos lo incorporó a sus rebaños como semental', 'captured by': ''},
    {'name': 'jabali de calidon', 'defeated by': 'atalanta', 'description': 'Enviado por Artemisa para devastar Etolia y murio en la Cacería de Calidón', 'captured by': ''},
    {'name': 'carcinos', 'defeated by': '-', 'description': 'cangrejo gigante que habitaba en el Princesa Andrómeda.', 'captured by': ''},
    {'name': 'gerion', 'defeated by': 'heracles', 'description': 'gigante hijo de Crisaor y Calírroe. Ser antropomorfo formado por tres cuerpos humanos gigantes', 'captured by': ''},
    {'name': 'cloto', 'defeated by': '-', 'description': 'es una de las tres Moiras, hijas de Zeus y Temis que presidían el destino del hombre', 'captured by': ''},
    {'name': 'laquesis', 'defeated by': '-', 'description': 'Determina el futuro de las personas, decide la longitud del hilo de cada una de las vidas humanas', 'captured by': ''},
    {'name': 'atropos', 'defeated by': '-', 'description': 'Elegía el mecanismo de la muerte y terminaba con la vida de cada mortal', 'captured by': ''},
    {'name': 'minotauro de creta', 'defeated by': 'teseo', 'description': 'monstruo con cuerpo de hombre y cabeza de toro. vivia en un laberinto', 'captured by': ''},
    {'name': 'harpias', 'defeated by': '-', 'description': 'ser con apariencia de hermosa mujer alada, cuyo cometido era hacer cumplir el castigo impuesto por Zeus', 'captured by': ''},
    {'name': 'argos panoptes', 'defeated by': 'hermes', 'description': 'gigante con cien ojos, que servía como pastor y guardián de la vaca Ío', 'captured by': ''},
    {'name': 'aves del estinfalo', 'defeated by': '-', 'description': 'aves que tenían picos, alas y garras de bronce, excrementos venenosos y también eran carnívoras', 'captured by': ''},
    {'name': 'talos', 'defeated by': 'medea', 'description': 'autómata gigante hecho de bronce que protegía a la Creta minoica de piratas e invasores', 'captured by': ''},
    {'name': 'sirenas', 'defeated by': '-', 'description': 'seres híbridos con rostro y torso de mujer y cuerpo de pez', 'captured by': ''},
    {'name': 'piton', 'defeated by': 'apolo', 'description': 'gran serpiente que participa en las leyendas de la fundación del santuario del oráculo de Delfos', 'captured by': ''},
    {'name': 'cierva de cerinea', 'defeated by': '-', 'description': 'tenía pezuñas de bronce y cornamenta de oro, estaba consagrada por la pléyade Táigete a la diosa Artemisa', 'captured by': ''},
    {'name': 'basilisco', 'defeated by': '-', 'description': 'serpiente gigante cargada de veneno letal y que podía matar con la simple mirada, el rey de las serpientes.', 'captured by': ''},
    {'name': 'jabali de erimanto', 'defeated by': '-', 'description': 'criatura que causaba estragos en todo el contorno y que vivía en Erimanto, ', 'captured by': ''},
]

creature_tree = BinaryTree()

for creature in lista_creatures:
    name = creature.get("name")
    creature_tree.insert_node(name, creature)
print()

#Punto A
print('Punto A')
print('Barrido inorden de criaturas ordenados por nombre y quien las derroto:')
creature_tree.inorden_creatures()
print()

#Punto C
print('Punto C')
print("Información de Talos:")
creature_tree.inorden_start_with_creatures("talos")

#Punto D
print('Punto D')
best_creatures = creature_tree.maximos_derrotadores()
print("Los 3 principales criaturas que derrotaron la mayor cantidad de criaturas:")
for creature, count in best_creatures:
    print(f"{creature}: {count} criaturas derrotadas")
print()


#Punto E
print('Punto E')
print()
print("Nombres de criaturas derrotadas por Heracles:")
creature_tree.defeated_by_heracles()
print()


#Punto F
print('Punto F')
print()
print("Nombres de criaturas que no fueron derrotadas: ")
creature_tree.not_defeated()
print()


#Punto H
print('Punto H')
print()
cerbero_node = creature_tree.search("cerbero")
if cerbero_node:
    cerbero_node.other_values["captured by"] = "heracles"
    creature_tree.inorden_start_with_creatures("cerbero")

toro_de_creta_node = creature_tree.search("toro de creta")
if toro_de_creta_node:
    toro_de_creta_node.other_values["captured by"] = "heracles"
    creature_tree.inorden_start_with_creatures("toro de creta")

cierva_cerinea_node = creature_tree.search("cierva de cerinea")
if cierva_cerinea_node:
    cierva_cerinea_node.other_values["captured by"] = "heracles"
    creature_tree.inorden_start_with_creatures("cierva de cerinea")

jabali_erimanto_node = creature_tree.search("jabali de erimanto")
if jabali_erimanto_node:
    jabali_erimanto_node.other_values["captured by"] = "heracles"
    creature_tree.inorden_start_with_creatures("jabali de erimanto")

print()

#Punto I
#print('Punto I')
#print()
#busqueda = input("Ingrese la criatura que quiere buscar: ")
#encontradas = creature_tree.inorden_start_with_creatures(busqueda)

#if not encontradas:
#    print("No se encontraron coincidencias para:", busqueda)

#Punto J
print('Punto J')
print()
creature_tree.delete_node("basilisco")
creature_tree.delete_node("sirenas")
print('Barrido inorden de criaturas sin las sirenas y basilisco:')
creature_tree.inorden_creatures()
print()


#Punto K
print('Punto K')
print()
aves_del_estinfalo_node = creature_tree.search("aves del estinfalo")
if aves_del_estinfalo_node:
    aves_del_estinfalo_node.other_values["defeated by"] = "heracles"
    creature_tree.inorden_start_with_creatures("aves del estinfalo")
print()

#Punto L
print('Punto L')
print()
ladon_node = creature_tree.search("ladon")
if ladon_node:
    creature_tree.delete_node("ladon")
    creature_tree.insert_node("dragon ladon", {'name': 'dragon ladon', 'defeated by': 'heracles', 'description': 'gigante con cien ojos, que servía como pastor y guardián de la vaca Ío'})
    creature_tree.inorden_start_with_creatures("dragon ladon")
print()

#Punto M
print('Punto M')
print()
print("Listado por nivel del árbol:")
creature_tree.by_level()
print()


#Punto N
print('Punto N')
print()
print("Nombres de criaturas capturadas por Heracles:")
creature_tree.captured_by_heracles()
print()
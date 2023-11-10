from arbol_binario import BinaryTree


lista_jedis = [
    {'name': 'qui-gon jin', 'ranking': 'jedi master', 'specie': 'human','master': "-", 'lightsaber color': 'green', 'birthdate year': '79ABY'},
    {'name': 'obi-wan kenobi', 'ranking': 'jedi master', 'specie': 'human','master': 'qui-gon jin' 'yoda', 'lightsaber color': 'blue', 'birthdate year': '57ABY'},
    {'name': 'anakin skywalker/' 'darth vader', 'ranking': 'jedi knight', 'specie': 'human','master': 'obi-wan kenobi', 'lightsaber color': 'blue', 'birthdate year': '41ABY'},
    {'name': 'quinlan vos', 'ranking': 'jedi master', 'specie': 'human' 'kiffar','master': 'tholme', 'lightsaber color': 'green', 'birthdate year': '59ABY'},
    {'name': 'yoda', 'ranking': 'grand master', 'specie': '-','master': '-', 'lightsaber color': 'green', 'birthdate year': '896ABY'},
    {'name': 'mace windu', 'ranking': 'jedi master/''master of the order', 'specie': 'human','master': "cyslin myr", 'lightsaber color': 'purple', 'birthdate year': '72ABY'},
    {'name': 'ki-adi-mundi', 'ranking': 'jedi master', 'specie': 'cerean','master': "-", 'lightsaber color': 'purple/' 'blue', 'birthdate year': '92ABY'},
    {'name': 'plo koon', 'ranking': 'jedi master', 'specie': 'kel for','master': "-", 'lightsaber color': 'yellow/' 'blue/' 'orange', 'birthdate year': '71ABY'},
    {'name': 'saesee tiin', 'ranking': 'jedi master', 'specie': 'human','master': "iktotchi", 'lightsaber color': 'green', 'birthdate year': '-'},
    {'name': 'yaddle', 'ranking': 'jedi master', 'specie': '-','master': "-", 'lightsaber color': 'green', 'birthdate year': '509ABY'},
    {'name': 'even pieli', 'ranking': 'jedi master', 'specie': 'lannik','master': "-", 'lightsaber color': 'green', 'birthdate year': '-'},
    {'name': 'oppo rancisis', 'ranking': 'jedi master', 'specie': 'thisspiasian','master': "yaddle", 'lightsaber color': 'green', 'birthdate year': '206ABY'},
    {'name': 'adi gallia', 'ranking': 'jedi master', 'specie': 'tholothian','master': "-", 'lightsaber color': 'green/' 'blue', 'birthdate year': '-'},
    {'name': 'yarael poof', 'ranking': 'jedi master', 'specie': 'quermian','master': "-", 'lightsaber color': 'blue', 'birthdate year': '-'},
    {'name': 'eeth koth', 'ranking': 'jedi master', 'specie': 'zabrak','master': "-", 'lightsaber color': 'green/' 'blue', 'birthdate year': '-'},
    {'name': 'depa billaba', 'ranking': 'jedi master', 'specie': 'chalactan','master': "-", 'lightsaber color': 'green', 'birthdate year': '-'},
    {'name': 'kit fisto', 'ranking': 'jedi master', 'specie': 'nautolan','master': "-", 'lightsaber color': 'green', 'birthdate year': '-'},
    {'name': 'luminara unduli', 'ranking': 'jedi master', 'specie': 'mirialan','master': "-", 'lightsaber color': 'green', 'birthdate year': '58ABY'},
    {'name': 'barriss offe', 'ranking': 'padawan', 'specie': 'mirialan','master': "luminara unduli", 'lightsaber color': 'blue', 'birthdate year': '40ABY'},
    {'name': 'shaak ti', 'ranking': 'jedi master', 'specie': 'togruta','master': "-", 'lightsaber color': 'blue', 'birthdate year': '-'},
    {'name': 'coleman trebor', 'ranking': 'jedi master', 'specie': 'vurk','master': "-", 'lightsaber color': 'green', 'birthdate year': '-'},
    {'name': 'jocasta nu', 'ranking': 'jedi master', 'specie': 'human','master': "-", 'lightsaber color': 'blue', 'birthdate year': '-'},
    {'name': 'aayla secura', 'ranking': 'jedi knight', 'specie': 'twi-lek','master': "quinlan vos", 'lightsaber color': 'blue', 'birthdate year': '47ABY'},
    {'name': 'sifo-dyas', 'ranking': 'jedi master', 'specie': 'human','master': "-", 'lightsaber color': 'green', 'birthdate year': '75ABY'},
    {'name': 'count dooku', 'ranking': 'jedi master', 'specie': 'human','master': "yoda", 'lightsaber color': 'blue/' 'red', 'birthdate year': '102ABY'},
    {'name': 'pablo-jill', 'ranking': 'jedi knight', 'specie': '-','master': "-", 'lightsaber color': 'blue', 'birthdate year': '-'},
    {'name': 'bultar swan', 'ranking': 'jedi knight', 'specie': 'human','master': "plo koon", 'lightsaber color': 'green', 'birthdate year': '-'},
    {'name': 'agen kolar', 'ranking': 'jedi master', 'specie': 'zabrak','master': "-", 'lightsaber color': 'green', 'birthdate year': '-'},
    {'name': 'stass allie', 'ranking': 'jedi master', 'specie': 'tholothian','master': "-", 'lightsaber color': 'green', 'birthdate year': '-'},
    {'name': 'ahsoka tano', 'ranking': 'padawan', 'specie': 'togruta','master': "anakin skywalker", 'lightsaber color': 'green/' 'blue/' 'yellow/' 'white', 'birthdate year': '36ABY'},
    {'name': 'luke skywalker', 'ranking': 'jedi knight', 'specie': 'human','master': "yoda", 'lightsaber color': 'blue', 'birthdate year': '36ABY'},
]

print()
# Punto A
print('Punto A')
name_tree = BinaryTree()
specie_tree = BinaryTree()
ranking_tree = BinaryTree()
print("Name tree, Specie tree y Ranking tree han sido creadas")
print()

#Punto B
print('Punto B')
for jedi in lista_jedis:
    name = jedi.get("name")
    name_tree.insert_node(name, jedi)
print('Barrido inorden de Jedis ordenados por nombre:')
name_tree.inorden()


print()
for jedi in lista_jedis:
    ranking = jedi.get("ranking") 
    ranking_tree.insert_node(ranking, jedi)
print('Barrido inorden de Jedis ordenados por ranking:')
ranking_tree.inorden()

print()

#Punto C
print('Punto C')
for jedi in lista_jedis:
    specie = jedi.get("specie") 
    specie_tree.insert_node(specie, jedi) 
print('Barrido por nivel de Jedis ordenados por Specie:')
specie_tree.by_level()
print()
print('Barrido por nivel de Jedis ordenados por ranking:')
ranking_tree.by_level()
print()

#Punto D 
print('Punto D')
print()
print("Información de Yoda:")
name_tree.inorden_start_with_jedi("yoda")
print()
print("Información de Luke Skywalker:")
name_tree.inorden_start_with_jedi("luke skywalker")
print()


#Punto E
print('Punto E')
print()
print("Nombres de Jedi con ranking 'Jedi Master':")
name_tree.inorden_ranking_jedi_master()

print()

#Punto F
print('Punto F')
print()
print("Nombres de Jedi con sable de color verde (green):")
name_tree.inorden_jedi_with_greensaber()
print()

#Punto G
print('Punto G')
print("Jedi cuyos maestros son distintos de '-':")
name_tree.listar_jedi_with_master()
print()

#Punto H
print('Punto H')
especies_buscadas = ["togruta", "cerean"]
print("Jedi de especie 'Togruta' o 'Cerean':")
name_tree.mostrar_jedi_specie(especies_buscadas)
print()

#Punto I
print('Punto I')
print("Jedi cuyos nombres comienzan con 'A':")
name_tree.inorden_start_with_jedi("a")
print()
print("Jedi cuyos nombres contienen un guion :")
name_tree.listar_jedi_con_guion()




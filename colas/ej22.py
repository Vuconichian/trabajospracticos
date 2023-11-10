from cola import Cola


cola_personajes = Cola()
cola_personajes.arrive({"nombre": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"})
cola_personajes.arrive({"nombre": "Tony Stark", "superheroe": "Iron Man", "genero": "M"})
cola_personajes.arrive({"nombre": "Thor Odinson", "superheroe": "Thor", "genero": "M"})
cola_personajes.arrive({"nombre": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"})
cola_personajes.arrive({"nombre": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"})
cola_personajes.arrive({"nombre": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"})
cola_personajes.arrive({"nombre": "Peter Parker", "superheroe": "Spider-Man", "genero": "M"})
cola_personajes.arrive({"nombre": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"})


def encontrar_personaje_por_superheroe(cola, superheroe):
    while cola.size() > 0:
        personaje = cola.on_front()
        if personaje["superheroe"] == superheroe:
            return personaje["nombre"]
        cola.move_to_end()
    return None

nombre_capitana_marvel = encontrar_personaje_por_superheroe(cola_personajes, "Capitana Marvel")
print(f"1. Nombre del personaje de la Capitana Marvel: {nombre_capitana_marvel}")

def mostrar_superheroes_femeninos(cola):
    cola_temporal = Cola()
    personaje_actual = cola.on_front()
    while personaje_actual is not None:
        if personaje_actual["genero"] == "F":
            print(personaje_actual["superheroe"])
        cola_temporal.arrive(cola.atention()) #se quita de la cola original y se ingresa a la cola temporal
        personaje_actual = cola.on_front()

    while cola_temporal.size() > 0:
        cola.arrive(cola_temporal.atention())

print("2. Nombres de los superhéroes femeninos:")
mostrar_superheroes_femeninos(cola_personajes)

def mostrar_personajes_masculinos(cola):
    cola_temporal = Cola()
    personaje_actual = cola.on_front()
    while personaje_actual is not None:
        if personaje_actual["genero"] == "M":
            print(personaje_actual["nombre"])
        cola_temporal.arrive(cola.atention())
        personaje_actual = cola.on_front()

    while cola_temporal.size() > 0:
        cola.arrive(cola_temporal.atention())

print("3. Nombres de los personajes masculinos:")
mostrar_personajes_masculinos(cola_personajes)

def encontrar_superheroe_por_personaje(cola, personaje):
    cola_temporal = Cola()
    superheroe_encontrado = None
    while cola.size() > 0:
        personaje_actual = cola.on_front()
        if personaje_actual["nombre"] == personaje:
            superheroe_encontrado = personaje_actual["superheroe"]
        cola_temporal.arrive(cola.atention())

    while cola_temporal.size() > 0:
        cola.arrive(cola_temporal.atention())
    
    return superheroe_encontrado

nombre_superheroe_scott_lang = encontrar_superheroe_por_personaje(cola_personajes, "Scott Lang")
print(f"4. Nombre del superhéroe del personaje Scott Lang: {nombre_superheroe_scott_lang}")

def mostrar_personajes_letra_s(cola):
    cola_temporal = Cola()
    personaje_actual = cola.on_front()
    while personaje_actual is not None:
        if personaje_actual["nombre"][0].lower() == "s":
            print(personaje_actual)
        cola_temporal.arrive(cola.atention())
        personaje_actual = cola.on_front()
    
    while cola_temporal.size() > 0:
        cola.arrive(cola_temporal.atention())

print("5. Datos de los personajes cuyos nombres comienzan con la letra S:")
mostrar_personajes_letra_s(cola_personajes)

nombre_superheroe_carol_danvers = encontrar_superheroe_por_personaje(cola_personajes, "Carol Danvers")
if nombre_superheroe_carol_danvers is not None:
    print(f"6. El personaje Carol Danvers se encuentra en la cola. Su nombre de superhéroe es: {nombre_superheroe_carol_danvers}")
else:
    print("6. El personaje Carol Danvers no se encuentra en la cola.")
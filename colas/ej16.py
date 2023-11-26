from colaprioridad import ColaPrioridad

cola= ColaPrioridad()

#A
empleados=[{'nombre':'Luis','prioridad':1},
        {'nombre':'Pedro','prioridad':1},
        {'nombre':'Maria','prioridad':1}]

for i in empleados:
    cola.arrive(i['nombre'],i['prioridad'])

#B
print('B')
print(cola.atention()[1])
print()

#C
empleados=[{'nombre':'Jose','prioridad':2},
        {'nombre':'Monica','prioridad':2}]

for i in empleados:
    cola.arrive(i['nombre'],i['prioridad'])

#D
empleados=[{'nombre':'Maria Laura','prioridad':3}]

for i in empleados:
    cola.arrive(i['nombre'],i['prioridad'])

#E
print('E')
for i in range(2):
    print(cola.atention()[1])
print()

#F
empleados=[{'nombre':'Juan','prioridad':1},
        {'nombre':'Jorge','prioridad':1},
        {'nombre':'Axel','prioridad':3}]

for i in empleados:
    cola.arrive(i['nombre'],i['prioridad'])

#G
print('G')
while cola.size()>0:
    print(cola.atention()[1])
print()
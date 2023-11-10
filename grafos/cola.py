class Cola():

    def __init__(self):
        self.__elementos = []

#agrega un dato a la cola
    def arrive(self, value):
        self.__elementos.append(value)

#Quita el primer elemento de la cola y lo devuelve
    def atention(self):
        if self.size() > 0:
            return self.__elementos.pop(0)

#devuelve el tamaño de la cola
    def size(self):
        return len(self.__elementos)

#Devuelve el primer elemento de la cola sin quitarlo
    def on_front(self):
        if self.size() > 0:
            return self.__elementos[0]

#quita el primer elemento y lo envia al final
def move_to_end(self):
    if self.size() > 0:
        aux = self.__elementos.pop(0)
        self.arrive(aux)
        return aux


# cola = Cola()
# cola_aux = Cola()

# from random import randint

# for i in range(5):
#     value = randint(1, 50)
#     # print(value)
#     cola.arrive(value)

# print()
# print(cola.atention())
# print(cola.atention())
# print(cola.on_front())
# print(cola.__elementos)
# print(cola.size())

# while cola.size() > 0:
#     value = cola.atention()
#     print(value)
#     cola_aux.arrive(value)

# print(cola.size())
# print(cola_aux.__elementos)
# print(cola.__elementos)
# print()
# cont = 0
# while cont < cola.size():
#     value = cola.move_to_end()
#     print(value)
#     cont += 1

# print(cola.__elementos)

class Pila():
    """Stack class"""

    def __init__(self):
        self.__elements = []

#agrega un dato a la pila
    def push(self, dato):
        self.__elements.append(dato)

#quita un dato de la pila
    def pop(self):
        if self.size() > 0:
            dato = self.__elements.pop()
            return dato

#devuelve el tamaño de la pila
    def size(self):
        return len(self.__elements)

#devuelve el dato que esta encima de la pila, o sea el ultimo agregado
    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1]


#pila_1 = Pila()
#pila_aux = Pila()
#pila_1.push(3)
#pila_1.push(6)
#pila_1.push(1)


#print(f'la pila tiene {pila_1.size()} elementos')

#print('barrido')

#while pila_1.size() > 0:
#    dato = pila_1.pop()
#    print(dato)
#    pila_aux.push(dato)

#while pila_aux.size() > 0:
#    dato = pila_aux.pop()
#    pila_1.push(dato)

#print('tamanio', pila_1.size(), pila_aux.size())


#stack_palabra = Pila()

# #! carga
# palabra = input('ingrese una palabra ')
# for i in palabra:
#     stack_palabra.push(i)

# palabra_invertida = ''
# while stack_palabra.size() > 0:
#     palabra_invertida += stack_palabra.pop()

# print(palabra_invertida)

#stack_letras = Pila()

#! carga
#for i in range(10):
#    stack_letras.push(chr(randint(65, 90)))

#contador_vocales = 0
#while stack_letras.size() > 0:
#    valor = stack_letras.pop()
#    if valor in ['A', 'E', 'I', 'O', 'U']:
#        contador_vocales += 1

#print(f'la cantidad de vocales son {contador_vocales}')

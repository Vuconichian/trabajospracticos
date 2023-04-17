#Desarrollar una función que permita convertir un número romano en un número decimal.


def romano_a_decimal(numeros_romanos):
    valores_numeros_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(numeros_romanos) == 0:
        return 0
    if len(numeros_romanos) == 1:
        return valores_numeros_romanos[numeros_romanos]
    if valores_numeros_romanos[numeros_romanos[0]] < valores_numeros_romanos[numeros_romanos[1]]:
        # Si el primer digito es menor que el segundo, se resta al resultado de la conversión del resto, por ejemplo V-I (5-1)
        return romano_a_decimal(numeros_romanos[1:]) - valores_numeros_romanos[numeros_romanos[0]]
    else:
        # Y si es al reves, se suma el primer digito al resultado de la conversión del resto, por ejemplo V+I (5+1)
        return romano_a_decimal(numeros_romanos[1:]) + valores_numeros_romanos[numeros_romanos[0]]
    
print(romano_a_decimal("IV"))
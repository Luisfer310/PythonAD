# Calcula el maximo de 3 numeros
lista_numeros = []
contador = 0

while contador < 3:
    numero = int(input(f'Numero {contador + 1}: '))
    lista_numeros.append(numero)
    contador += 1

print(f'El mayor numero de los 3 es: {max(lista_numeros)}')
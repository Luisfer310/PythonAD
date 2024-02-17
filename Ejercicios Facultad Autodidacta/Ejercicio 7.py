# Calcula el promedio de una lista de numeros
lista = []
suma = 0
contador = 0

while contador < 5:
    numero = int(input('Dame el numero a agregar a la lista: '))
    lista.append(numero)
    contador += 1

for n in lista:
    suma += n

print(f'El promedio de tu lista de numeros es {suma/contador}')

# Con la funcion matematica sum()
lista_numeros = []
contador = 0

while contador < 15:
    numero = int(input('Dame el numero a afregar a la lista: '))
    contador += 1
    lista_numeros.append(numero)

promedio = sum(lista_numeros) / len(lista_numeros) # De esta manera me evito escribir el ciclo for para sumar cada elemento de la lista
print(f'El promedio de tu lista de numeros es {promedio}')
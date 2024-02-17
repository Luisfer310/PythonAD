# Ordena una lista de numeros de menor a mayor
lista = []
contador = 0

while contador < 5:
    numero = int(input('Dame el numero a agregar a la lista: '))
    lista.append(numero)
    contador += 1

lista.sort() # Este metodo lo ordenara de menor a mayor
print(lista)
# Genera una lista de numeros de 1 a 200
lista = []
for i in range(1, 201): # Se pone hasta el 201 por que el rango abarcara hasta uno antes del final
    lista.append(i)
print(lista)

# Podemos esta misma lista con la funcion list
numeros = list(range(1, 201))
print(numeros)
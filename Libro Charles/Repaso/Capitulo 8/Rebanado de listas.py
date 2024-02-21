# El rebanado se emplea de la misma menera que en las cadenas
lista = ['a', 'b', 'c', 'd', 'e',]
rebanado = lista[1:4]
print(rebanado)

# Y el manejo de los indices es la misma manera. Tenemos el rebanado con el primer indice
print(lista[2:])

# Rebanado con solo el segundo indice
print(lista[:3])

# Como ya sabemos las listas son mutables y podemos mutarlas con un rebanado
lista[1:3] = ['Rebanado1', 'Rebanado2']
print(lista)
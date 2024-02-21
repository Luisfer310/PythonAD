lista = ['Luis', 'Fernando', 23, True, ['Mara', 23, (True, 5)]]
# Para poder mutar una lista usaremos los indices
lista[2] = 'Nuevo' # Con este se podra cambiar el elemento indicado con el indice en los parentesis (Recordar que los indices de las listas son por elemento y no por caracter)
print(lista)

# Los indices y el largo de una lista es por elemento y no por caracter
print(len(lista))

# Se puede usar el operador in, para retornar un bool el cual indica que si el elemento se encuentra en la lista
comprobacion = 'Luis' in lista
print(comprobacion)
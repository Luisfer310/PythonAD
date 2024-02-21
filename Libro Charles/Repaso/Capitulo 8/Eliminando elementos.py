# Para eliminar elementos de una lista podremos usar diferentes metodos dependiendo la accion que deseamos

# pop agregado a una variable a para guardar el valor eliminado
lista = ['a', 'b', 'c', 'd', 'e']
eliminado = lista.pop() # De esta forma eliminara el ultimo elemento
eliminado0 = lista.pop(2) # y con este, se elimina el elemento indicado con el indice entre parentesis
print(eliminado)
print(eliminado0)

# con el operador del no hace falta definir una variable para este por que no retorna el elemento eliminado
lista0 = ['Luis', 'Fernando', 'Mara', 23,45,67]
del lista0[2]
print(lista0)
# tambien se puede con un rebanado
del lista0[1:3]
print(lista0)

# remove va a remover el elemento indicado por su valor y no por el indice (Este no retorna el elemetno por lo cual no es necesario definirlo en una variable)
lista1 = ['Luis', 'Fernando', 'Mara', 23,45,67]
lista1.remove('Fernando')
print(lista1)
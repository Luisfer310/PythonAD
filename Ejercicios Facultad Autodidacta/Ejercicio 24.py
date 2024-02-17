# Elimina un elemento especifico de una lista
lista = ['Manzana', 'Pera', 'Uva', 'Mango']
lista.remove('Mango')
print(lista)

# Tambien esta el metodo .pop(), el cual si lo ponemos como valor de una nueva variable, lo que hara este metodo es retornar el valor eliminado
valor_eliminado = lista.pop(1) # Este se maneja con argumentos de indices
print(lista)
print(valor_eliminado)
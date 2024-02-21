# En la definicion de funciones, podemos pasar listas como parametro. Pero la accion que se ejecute afectara a la lista original.
def eliminar_primero(lista):
    del lista[0]

lista = [1,2,3,4]
eliminar_primero(lista)
print(lista)

# Recordar que hay operaciones que modifican las listas y hay otras que crean una nueva lista por la modificacion que se ha hecho.
lista1 = lista.append(5)
print(lista1) # Regresara None, debido a que los metodos modifican las listas ya creadas y no se deben de poner como valor de una variable

lista2 = [5,6,7,8]
lista3 = lista + lista2 # Esta si hara la operacion debido a que el operador +, une las listas y esto creara una nueva lista
print(lista3)
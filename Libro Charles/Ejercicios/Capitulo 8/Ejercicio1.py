# Ejercicio 1: Escribe una función llamada recortar que tome una lista y la modifica, removiendo el primer y ultimo elemento, y regresa None. Despues escribe una función
# llamada medio que toma una lista y regresa una nueva lista que contiene todo excepto el primero y ultimo elementos.

def recortar(lista):
    del lista[0]
    del lista[len(lista) - 1]
    print(lista)

lista = [1,2,3,4,5,6,7]
recortar(lista)

def medio(lista):
    longitud = len(lista) - 1
    nueva = lista[1:longitud]
    return nueva

lista1 = ['a', 'b', 'c', 'd', 'e', 'f']
listaNueva = medio(lista1)
print(listaNueva)
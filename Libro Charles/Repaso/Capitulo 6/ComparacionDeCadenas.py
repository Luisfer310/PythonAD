# La comparacion de cadenas puede servir cuando el usuario ingresa una cadena y queremos condicionar que dependiendo
# lo que se ingrese sera el camino que siga
while True:
    palabra = input('Ingresa la palabra: ')
    if palabra == 'fin':
        print('Terminamos')
        break
    else:
        print('Seguimos')
        pass

# En la comparacion tambien se puede comparar el orden alfabetico. Redordar que Python es sensible a mayusculas, por lo
# cual las mayusculas tienen mayor jerarquia a comparacion de las minusculas
palabra = 'banana'
cadena = input('Ingresa la palabra: ')
if palabra < cadena:
    print('Tu palabra esta despues de mi palabra')
elif palabra > cadena:
    print('Tu palabra esta antes de mi palabra')

# Una similitud entre las cadenas y las listas es que son secuencias, pero las listas son de valores y las cadenas son de caracteres.
# Podemos convertir una cadena en una lista. La funcion list, hara esta accion pero separara caracter por caracter de la cadena y los covetira en valores para la lista.
cadena = 'banana'
lista = list(cadena)
print(type(lista))
print(lista)

# Para diividir una cadena por palabras se usara el metodo split
cadena0 = 'Esta es una cadena'
lista0 = cadena0.split()
print(lista0)

# Lo que iria en los parentesis de split, seria el delimitador de la funcion, el cual sera el caracter con el cual ser hara la separacion de la cadena.
# Si lo dejamos en blanco, por defecto el separador sera cuando encuentre un espacio en blanco, pero podemos pasar cualquier caracter.
cadena1 = 'Esta es una cedena, mas larga'
lista1 = cadena1.split(',')
print(lista1)

# El metodo join sera a lo contrario. Este unira los valores de la lista para crear una cadena.
lista2 = ['Mi','niña','de','cristal']
cadena2 = ' '.join(lista2) # Antes del punto debemos indicar cual sera el operador que separe los valores de la lista.
print(cadena2)
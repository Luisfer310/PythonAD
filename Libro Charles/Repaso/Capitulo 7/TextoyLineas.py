# Es importante saber que un archivo son un conjunto de lineas asi como una cadena puede ser considerada el conjunto de
# caracteres. Para poder separar un archivo en lineas, python maneja un caracter especial con el cual se dara saltos de
# linea. El salto de linea se representa con '\n'.

print('Hola\nMundo')  # Se podria pensar que el salto de linea cuenta como 2 caracteres, pero python lo lee como uno solo

palabra = 'X\nY'  # Si contamos podemos decir que son 4 caracteres en esta sentencia pero para python son 3
print(palabra)
print(len(palabra))

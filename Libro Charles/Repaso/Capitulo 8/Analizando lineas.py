# Los metodos dentro del tema de las listas tambien las podemos usar fuera de esta.
# Por ejemplo el metodo de split, este metodo nos ayudara a separar en palabras una linea de algun archivo.

archivo = open('mbox.txt') # Se abre el archivo
for n in archivo: # Iteramos las lineas del archivo
    n = n.rstrip() # Se eliminan los espacios en blanco al inicio y fin de la linea (en caso de tener)
    if not n.startswith('From '): # Se indica que si no empieza por la peticion dentro delos parentesis, continue sin ejecutar nada y brinque al else
        continue
    else:
        palabras = n.split() # Las lineas del archivo se separaran para crear la lista palabras y asi acceder al indice de los elementos
        print(palabras[2]) # Pintamos la palabra con el indice 2, en este caso sera el dia.
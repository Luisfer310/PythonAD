archivo = open('romeo.txt') # Abrimos el archivo
palabras_unicas = [] # Definimos una lista para agregar las palabras y no agregar las que esten repetidas

for linea in archivo: # Esto nos ayudara a leer linea por linea del archivo
    palabras = linea.split() # Con esto dividiremos en palabras nuestra linea (en una lista)
    for i in palabras: # Por cada palabra en la lista de palabras
        if i not in palabras_unicas: # Si la palabra no se encuentra en la lista de palabras_unicas
            palabras_unicas.append(i) # Se le agregara a la lista de palabras_unicas

archivo.close() # Cerramos el archivo

# Acomodar alfabeticamente las palabras unicas
palabras_unicas.sort()
for i in palabras_unicas:
    print(i)
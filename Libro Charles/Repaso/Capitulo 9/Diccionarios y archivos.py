# Primero se le pedira al usuario que proporcione el nombre de un archivo
archivo = input('Archivo: ')
palabras_dicc = dict()
try: # Se usara una estrucutra de try/except para asegurar que no arroje error si no se encuentra el archivo
    abrir_archivo = open(archivo) # Si se encuentra el archivo lo abrira
except:
    print(f'El archivo {archivo} no existe') # si no se encuentra el archivo se imprime este print y se termina el programa
    exit()

# Ahora se iterara el archivo para extraer las palabras dentro de estas y contar cuatas veces aparecen
for linea in abrir_archivo:
    linea = linea.rstrip()
    palabras = linea.split()
    for palabra in palabras:
        if palabra not in palabras_dicc:
            palabras_dicc[palabra] = 1
        else:
            palabras_dicc[palabra] += 1

print(palabras_dicc)
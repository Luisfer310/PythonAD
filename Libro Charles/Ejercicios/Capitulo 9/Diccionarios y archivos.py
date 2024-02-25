archivo = input('Ingresa el nombre del archivo: ')
try:
    abrir_archivo = open(archivo)
except:
    print(f'El archivo {archivo} no existe')
    exit()

palabras_dicc = dict()
for lineas in abrir_archivo:
    lineas = lineas.rstrip()
    palabras = lineas.split()
    for palabra in palabras:
        if palabra not in palabras_dicc:
            palabras_dicc[palabra] = 1
        else:
            palabras_dicc[palabra] += 1
print(palabras_dicc)
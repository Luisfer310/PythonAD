archivo = open('words.txt')
palabras_dicc = dict()

for linea in archivo:
    linea = linea.rstrip()
    palabras = linea.split()
    for palabra in palabras:
        palabras_dicc[palabra] = None

palabra_buscar = input('Dame la cadena a buscar en el diccionario: ')
revision = palabra_buscar in palabras_dicc
if revision:
    print('La palabra se encuentra en el diccionario')
else:
    print('La palabra no se encuentra en el diccionario')
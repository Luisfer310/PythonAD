# Si el usuario ingresa 'na na boo boo' lo marcaremos como un 'error' y le regresaremos el texto de 'NA NA BOO BOO PARA TI - Te he atrapado!' al usuario.
nombre_archivo = input('Ingresa un nombre de archivo: ')
contador = 0
try:
    abrir_archivo = open(nombre_archivo)
    for n in abrir_archivo:
        contador += 1
    print(contador)
except:
    if nombre_archivo == 'na na boo boo':
        print('NA NA BOO BOO PARA TI - Te he atrapado!')
        exit()

# Escribir un programa para leer a través de datos de una bandeja de entrada de correo y cuando encuentres una linea que comience con 'From', dividir la linea en palabras
# utilizando la funcion split. Estamos interesados en quien envio el mensaje, lo cual es la segunda palabra en las linea que comienzan con From. Dentro de el archivo, las
# lineas que empiezan con la palabra 'From' se verian algo asi:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Entonces deberemos dividir en palabras cada linea 'From' e imprimir la segunda palabra de estas lineas. (En indices seria el 1)
# y por ultimo debemos de contar el total de lineas que incien con From e imprimir el total.

archivo = open('mbox-short.txt')
contador = 0

for linea in archivo:
    if linea.startswith('From:'):
        linea = linea.strip()
        palabras = linea.split()
        contador += 1
        print(palabras[1])

print(f'Hay {contador} lineas que empiezan por "From"')
# Le pediremos al usuario un nombre para un archivo que desee abrir, pero usaremos try y except para asegurar el programa en caso de que no de el nombre de un archivo existente
nombre_archivo = input('Nombre del archivo: ')
try:
    abrir_archivo = open(nombre_archivo)
except:
    print(f'El archivo {nombre_archivo} no existe')
    exit()
contador = 0 # De aqui en adelante el codigo ya no esta indentado en la sentencia de except, por lo cual se ejecuta si entra en la sentencia try.
for i in abrir_archivo:
    contador += 1
print(f'El archivo {nombre_archivo} tiene un total de {contador} lineas')
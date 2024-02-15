# Para no tener que hacer una variable con cada nombre de archivo diferente, podemos hacer que el usuario eliga el nombre de archivo a abrir o manejar
nombre_archivo = input('Dame el nombre del archivo: ')
abrir_archivo = open(nombre_archivo)
leer_archivo = abrir_archivo.read()
print(f'El archivo {nombre_archivo} tiene un total de {len(leer_archivo)} caracteres')
# Debemos de abrir el archivo, pero pasando un segundo parametro en el open, el cual sera la 'w'
abrir_archivo = open('mbox.txt', 'w')
print(abrir_archivo)

# Podemos escribir pasando diresctamente dentro de los parentesis lo que queremos escribir
escribir_archivo = abrir_archivo.write('Hola, esta es una prueba de escritura en archivos con Python')
print(escribir_archivo) # Este retornara el numero de caracteres que escribimos

# Tambien podemos crear una variable aparte en la cual su valor sea lo que queremos escribir en el archivo
texto = 'Hola, esta es una prueba de escritura en archivos con Python'
escribir_archivo = abrir_archivo.write(texto)
print(escribir_archivo)
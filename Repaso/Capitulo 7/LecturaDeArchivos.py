# Usare el ciclo for para contar las lineas dentro del archivo
archivo = open('mbox.txt')
contador = 0
for linea in archivo:
    contador += 1
print(f'El archivo tiene un total de {contador} lineas')

# En el siguiente script abrire el archivo y usare el manejador de read, para que lea el archivo y despues con las
# sentencias print acceder a el largo del archivo y rebanar parte de este
archivo0 = open('mbox.txt')
leer = archivo0.read()
print(len(leer))
print(leer[0:21])

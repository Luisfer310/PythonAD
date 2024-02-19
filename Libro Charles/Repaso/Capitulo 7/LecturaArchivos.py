# Al querer leer un archivo, tenemos que tener una cosa muy presente; si usaremos un ciclo for o while para leerlo o si lo leeremos simplemente con la función open. Esto ya que
# si el archivo sobrepasa la capacidad de nuestra memoria principal lo mejor sera leerlo con uno de los ciclos, pero si no sobre pasa esa capacidad no es necesario nada mas que
# abrirlo e indicar que lo lea con el manejador .read()

# Con ciclo for
archivo = open('mbox.txt')
contador = 0
for i in archivo: # Con este ciclo for lo que haremos es que sin leer el archivo por lo pesado que es, indicaremos que por cada linea en el archivo le incremente por 1 a la
    # variable de contador y asi saber cuantas lineas contiene. Tambien podriamos hacer que nos imprima linea por linea, sin usar el metodo de .read()
    contador += 1
print(contador)

# Si quisieramos saber cuantos caracteres tiene podriamos usar el manejador de read para que lo lea y despues usar la funcion de len.
archivo0 = open('mbox.txt')
leer = archivo0.read()
print(len(leer))
print(leer[0:51]) # Y podemos rebanar parte del archivo

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
# # Para poder buscar condiciones especificas dentro de los archivos podemos combinar el manejador con metodos de cadenas y con esto crear un mecanismo de busqueda.
archivo = open('mbox.txt')
contador = 0
for i in archivo:
    i = i.rstrip() # Esta linea indica que se borren los espacios en blanco al final de cada linea y los saltos de linea. (Probar comentando esta linea para observar como se veria)
    if i.startswith('From:'):
        print(i)
        contador += 1
print(contador)

# Estructura usando el condiciolan not
archivo = open('mbox.txt')
contador = 0
for i in archivo:
    i = i.rstrip()
    if not i.startswith('From:'):
        continue
    else:
        contador += 1
    print(i)
print(contador)

# Condicionales con el metodo find
archivo = open('mbox.txt')
for i in archivo:
    i = i.rstrip()
    if i.find('From') == 0:
        print(i)

# Condicion negativa
archivo = open('mbox.txt')
for i in archivo:
    i = i.rstrip()
    if i.find('From') == -1:
        continue
    else:
        print(i)
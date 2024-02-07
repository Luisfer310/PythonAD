# Escribe otro programa que pida una lista de números como la anterior y al final muestre por pantalla el máximo y
# mínimo de los números, en vez de la media.
listaNumeros = []
while True:
    try:
        num = input('Dame un numero: ')
        if num == 'fin':
            break
        else:
            numero = int(num)
            listaNumeros.append(num)
    except:
        print('Dato erroneo.')
        continue


print(listaNumeros)
print(max(listaNumeros))
print(min(listaNumeros))

# Las funciones siempre seran utilies en la programacion y en las listas tenemos diferentes funciones para cada tipo de acciones que queramos hacer
# La funcion de max nos regresara el valor mas alto de la lista
lista = [5,2,89,3,45]
print(max(lista))

# La funcion de min retorna el elemento menor de la lista
print(min(lista))

# La funcion de len retorna el largo de la lista
print(len(lista))

# La funcion de sum retorna la suma de los elementos de la lista
print(sum(lista))

# Si usamos 2 o mas funciones dentro de una sentencia podemos hacer de nustro script un poco mas 'funcional'
lista1 = [4,8,1,5,20]
promedio = sum(lista1)/len(lista)
print(promedio)

# Si no usaramos las funciones pasadas el scrip que deberiamos escribir seria algo asi
contador = 0
total = 0

while True:
    numero = input('Numero: ')
    try:
        if numero == 'fin':
            break
        else:
            numero = float(numero)
            contador += 1
            total += numero
    except:
        print('Dato erroneo')

try:
    print(f'La meida e tus numeros es de {total/contador}')
except ZeroDivisionError:
    print('No se pueden dividir por cero')

cadena = 'Luis'
listan = list(cadena)
print(listan)
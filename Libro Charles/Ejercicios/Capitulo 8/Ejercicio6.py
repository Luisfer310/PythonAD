# Reescribe el programa que pide al usario una lista de numeros e imprime el maximo y el minimo de los numeros al fianl cuando el usuario ingresa 'hecho'. Escribe el
# porgrama para almacenar los numeros que el usuario ingrese en una lista y utiliza las funciones max() y min() para calcular el maximo y el minimo despues de que el
# bucle termine.

lista_numeros = []

while True:
    numero = input('Numero: ')
    try:
        if numero == 'hecho':
            break
        else:
            numero = int(numero)
            lista_numeros.append(numero)
        
    except:
        print('Dato erroneo')
try:
    print(f'Numero mas alto: {max(lista_numeros)}')
    print(f'Numero mas bajo: {min(lista_numeros)}')
except:
    print('No se han ingresado numeros')        
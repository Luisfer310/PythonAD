# Pide un numero y comprueba si el numero es par o impar utilizando if y modulo
numero = int(input('Dame un numero: '))
if numero%2 == 0:
    print('Tu numero es un numero par.')
elif numero%2 != 0:
    print('Tu numero es un numero impar.')
# Pide un numero y verifica si es positivo, negativo o cero
numero = int(input('Dame un numero: '))

if numero == 0:
    print('Es cero')
elif numero > 0:
    print('Es positivo')
elif numero < 0:
    print('Es negativo')
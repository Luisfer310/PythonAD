# Determina si un numero es divisible entre 5 y 7
numero = float(input('Numero: '))
if numero % 5 == 0 and numero % 7 == 0:
    print(f'El numero {numero} es divisible entre 5 y 7')
else:
    print(f'El numero {numero} no es divisible entre 5 y 7')
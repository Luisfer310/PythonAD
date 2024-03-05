from decimal import DivisionByZero


try:
    numero1 = int(input('Dame el primer numero: '))
    numero2 = int(input('Dame el segundo numero: '))

    resultado = numero1 / numero2
    print(f'El resultado es: {resultado}')

except DivisionByZero:
    print('No se pueden dividir por cero')
except ValueError:
    print('No se pueden sumar dos numeros que no sean numeros')
else:
    print('El codigo se ejecuto correctamente')
finally:
    print('Codigo finalizado')
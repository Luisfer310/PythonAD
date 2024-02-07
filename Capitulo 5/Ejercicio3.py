listaNumeros = []
suma = 0
contador = 0
while True:
    try:
        num = input('Ingrese un numero: ')
        if num == 'fin':
            break
        else:
            num = int(num)
            listaNumeros.append(num)
            contador += 1
            suma = suma + num
    except:
        print('Dato erroneo.')
        continue


print(listaNumeros)
print(min(listaNumeros))
print(max(listaNumeros))
print(f'Suma de todos los numeros {suma}')
print(f'Proporcionaste un total de {contador} numeros')
print(f'La media de estos numeros es {suma/contador}')

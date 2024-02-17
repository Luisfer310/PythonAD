# Cuenta las ocurrecias de un caracter especifico en una cadena
cadena = 'Esternocleidomastoideo'
contador = 0
caracter = input('Introduce el caracter: ')

for n in cadena:
    if n == caracter:
        contador += 1

if contador == 0:
    print('No se encontro ninguna ocurrencia.')
else:
    print(f'El caracter "{caracter}" aparece {contador} veces.')

# Cuenta de ocurrencias con el metodo .count()
ocurrencias = cadena.count(caracter)
print(ocurrencias)
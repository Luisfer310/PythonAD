# Codigo para hacer iteracion de inicio a fin
palabra = 'Esternocleidomastoideo'
longitud = len(palabra) - 1
contador = 0
while contador <= longitud:
    letra = palabra[contador]
    print(letra)
    contador += 1

# Codigo para hacer iteracion de fin a inicio
palabra = 'Esternocleidomastoideo'
longitud = len(palabra)
contador = longitud - 1
while contador >= 0:
    letra = palabra[contador]
    print(letra)
    contador -= 1

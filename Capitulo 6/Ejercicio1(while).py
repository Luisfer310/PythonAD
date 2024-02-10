# Iteracion de fin a inicio
palabra = input("Ingrese una palabra: ")
longitud = len(palabra)
contador = longitud - 1
while contador >= 0:
    letra = palabra[contador]
    print(letra)
    contador -= 1

# Iteracion de inicio a fin
palabra = input("Ingrese una palabra: ")
longitud = len(palabra) - 1
contador = 0
while contador <= longitud:
    letra = palabra[contador]
    print(letra)
    contador += 1

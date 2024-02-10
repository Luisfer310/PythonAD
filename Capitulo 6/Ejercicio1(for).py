# Iteracion de inicio a fin con bucle for
palabra = input("Ingrese una palabra: ")
for letra in palabra:
    print(letra)

# Iteracion de fin a inicio con bucle for
palabra = input("Ingrese una palabra: ")
for letra in range(len(palabra)-1, -1, -1):
    print(palabra[letra])
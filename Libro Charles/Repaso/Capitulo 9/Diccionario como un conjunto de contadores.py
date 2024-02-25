# Usaremos como ejemplo que el usuario nos dara una cadena de la cual crearemos un diccionario, en el cual se le dara como clave cada una de las letras, pero sin repetir letras, y como valor de cada variable
# se le dara un contador de cuantas veces aparece su letra

palabra = input('Ingrese una palabra: ')
diccPalabras = dict()

for letra in palabra:
    if letra not in diccPalabras:
        diccPalabras[letra] = 1
    else:
        diccPalabras[letra] += 1
print(diccPalabras)

# Usando el metodo get para recortar el codigo, quitando la condicional if
miDicc = {'a': 1, 'b':2, 'c':3, 'd':4}
valor = miDicc.get('f', 'Este elemento no se enccuentra')
print(valor)
# Verifica si una palabra es un palindromo
palabra = input('Palabra: ')
palabra = palabra.lower()
if palabra == palabra[::-1]: # Este hace que nuestra cadena vaya de atras hacia adelante
    print('Tu palabra es un palíndromo')
else:
    print('Tu palabra no es un palíndromo')
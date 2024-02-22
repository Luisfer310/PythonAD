# Pide un caracter y determina si es una vocal
caracter = input('Dame un caracter: ')
caracter = caracter.lower()
lista_vocales = ['a', 'e', 'i', 'o', 'u']
if caracter in lista_vocales:
    print('Es una vocal')
else:
    print('No es una vocal')
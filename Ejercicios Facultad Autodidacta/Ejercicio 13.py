# Remplaza un caracter de una cadena
cadena = 'Hola Mundo'
cambio = cadena[:3] + 'e' + cadena[4:]
print(cambio)

# Remplazo con el metodo .replace()
nueva_cadena = cadena.replace('o', 'e')
print(nueva_cadena)
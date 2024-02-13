# Para este ejercicio me indicaron leer sobre el metodo .replace()
# En el metodo replace se pediran 3 argumentos, los 2 primeros siendo obligatorios y el 3ero opcional. El primer
# argumetno es indicar que subcadena de la cadena deseamos remplazar y el segundo argumento es la subcadena que
# remplazara a la que inidcamos en el primer argumento
palabra = 'Mi casa es azul y mi carro es azul'
palabra = palabra.replace('azul', 'roja')  # Al no indicar el 3er argumento cambiara todas las subcadenas
# con el primer argumento por la subcadena del 2do argumento
print(palabra)


palabra = 'Mi casa es azul y mi carro es azul'
palabra = palabra.replace('azul', 'roja', 1)  # Aqui indicamos en el 3er argumento que solo una
# subcadena se remplazara, por lo cual cambiara la primer subcadena del primer argumento
print(palabra)

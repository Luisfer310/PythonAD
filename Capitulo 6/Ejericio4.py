#Escribe una invocación de count que cuenta el número de veces que una letra aparece en “banana”.
palabra = 'banana'
conteo = palabra.count('a')  # .count es el metodo que se usa para contar cuantas veces aparece dicho caracter o subcadena que se pase en argumento
print(conteo)
conteo2 = palabra.count('a', 0, 3)  # Tambien podemos pasar como argumetno un rango de indices en el que se buscara la subcadena
print(conteo2)

# En este repaso veremos el rebanado de una cadena y explicare como se puede manejar el rebanado con los argumentos de indice
palabra = input("Ingrese una palabra: ")
print('Rebanado con ambos indices'.center(40, '-'))
rebanado = palabra[0:3]  # Debemos tener en cuenta que el primer indice es de donde empezara y el segundo es donde
# termina el rebanado, pero este ultimo no se incluye en el retorno si no un indice antes
print(rebanado)

# Si al pasar los argumentos indices no pasamos el primer indice, python lo tomara como que queremos empezar desde el 0
print('Rebanado con solo el segundo indice'.center(40, '-'))
print(palabra[:5])

# Tambien podemos omitir el segundo indice y python tomara como que queremos rebanar hasta el ultimo indice
print('Rebanado con solo el primer indice'.center(40, '-'))
print(palabra[4:])

# Y si no escribimos ninguno de los 2 indices, seria como si no rebanaramos
print('"Rebanado" sin indices'.center(40, '-'))
print(palabra[:])

# Realiza operaciones basicas con contujos union e interseccion

# Union
# Set 1
uno = {1,2,3}
# Set 2
dos = {4,5,6,1} # La magia de este conjunto es que los numeros que encuentre repetidos solo los imprime una sola vez
conjunto = uno.union(dos) # Conjunto union
print(conjunto)

# Usando el elemento '|' (Este elemento tambien imprimira solo una vez los caracteres repetidos)
conjunto0 = uno|dos
print(conjunto0)

# Interseccion
interseccion = uno.intersection(dos) # A diferencia del union, este imprimira solo los repetidos pero solo uno de ellos, por ejemplo en este caso imprimira solo el 1 pero una vez
print(interseccion)

# Usando el elemento '&'
interseccion0 = uno&dos
print(interseccion0)
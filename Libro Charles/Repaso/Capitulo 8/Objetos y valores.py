# Cuando se crean 2 variables con el mismo valor, normalmente estas variables apuntan hacia el mismo objeto. Por lo cual python solo crea un solo valor y ambas variables apuntaran hacia ese objeto en python. Esto lo podemos comprobar con el operador 'is'.
a = 'banana'
b = 'banana'
print(a is b)

# Pero esto no pasara con las listas. A pesar de que tengan los mismos elementos no seran iguales, no apuntaran hacia el mismo objeto
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
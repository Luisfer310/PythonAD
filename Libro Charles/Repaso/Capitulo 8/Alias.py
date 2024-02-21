# Asignare un valor a la variable 'a' y a la variable 'b' le dare como valor la variable 'a'
a = [1,2,3,4,5]
b = a # Esta variable seria un alias, ya que hace referencia a mas de 1 referencia (La referencia es la asociacion de una variable a un objeto)

# Si el alias del objeto es mutado, los cambios hechos en el alias afectan al otro...
b[0] = 6
print(a)
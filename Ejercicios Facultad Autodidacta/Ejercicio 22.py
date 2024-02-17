# Divide una cadena en una lista de subcadenas
cadena = 'Hola mi nombre es Luis'
division = cadena.split()
print(division)

# Dentro de los parentesis de split, se puede pasar con que letra o caracter se hara el split, el caracter que se pase no se agrega a la lista con las subcadenas
division2 = cadena.split('o')
print(division2)
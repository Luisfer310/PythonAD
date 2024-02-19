# Dentro de la función dir, pondremos el valor de cualquier tipo de dato, esto nos ayudara a saber que metodos estan
# disponibles para ese valor
texto = 'Hola'
print(dir(texto))

# Para poder usar estos metodos debemos de llamarlos despues de la variable con el valor o por ejemplo de una cadena.
# Por ejemplo el metodo .lower(), este sirve para hacer que toda una cadena sea en minusculas.
palabra = 'Administradora'
print(palabra)

print('lower'.center(40, '-'))
palabra = palabra.lower()
print(palabra)

# Tambien esta el metodo de .find(), este buscara un caracter o subcadena dentro de una cadena.
print('find'.center(40, '-'))
print(palabra.find('a'))  # En los parentesis ponemos la subcadena o caracter que queremos buscar y nos regresara el
# indice en el que se encuentra

# Con el metodo find lo buscara desde el indice 0 al ultimo y para hacerlo a la inversa se usara .rfind()
print('rfind'.center(40, '-'))
print(palabra.rfind('a'))

# Tambien podemos usar el metodo find con un segundo argumento para indicar a partir de que indice se quiere buscar
# dicha subcadena…
print('find con el segundo argumento'.center(40, '-'))
print(palabra.find('a', 3))

# Uno mas de los metodos es el de strip, este metodo quitara los espacios al inicio y fin de una cadena. Por ejemplo que
# como cadena tuvieramos la palabra ' Universidad ', pero como podemos ver tiene un espacio al inicio y otro al final,
# con este metodo los podemos eliminar
print(' sin strip'.center(40, '-'))
palabra = ' Universidad '
print(palabra)
print(' con strip'.center(40, '-'))
palabra = palabra.strip()
print(palabra)

# Como ultimo ejmeplo usare el metodo de .starswith(), este comprueba si nuestra cadena con el caracter o la subcadena
# que indiquemos en los parentesis, este nos lo retorna en booleanos y recordar la sensibilidad a las mayusculas, por lo
# cual si empieza con mayuscula y nosotros le indicamos que nos retorne si empieza con minuscula, sera falso. Obvio
# estos no son los unicos metodos que maneja python, pero mientras avance en los cursos ire aprendiendo nuevos metodos
print('starswith'.center(40, '-'))
print(palabra.startswith('u'))
print(palabra.startswith('U'))
print(palabra.startswith('uni'))
print(palabra.startswith('Uni'))


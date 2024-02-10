# Es muy comun querer saber el largo de una cadena, por lo cual python nos tiene un metodo con el cual nos retorna el
# largo de la cadena que le pasemos como variable. Podemos demostrar esto con 2 tipos de entradas en los argumentos...
print(len('prueba'))  # En esta forma lo que hacemos es pasar directamente la cadena

palabra = 'prueba'
print(len(palabra))  # En esta forma declaramos una variable para guardar la cadena en esta y pasar la variable como argumento

# Esta funcion de 'len', nos puede ser muy util si queremos acceder a la ultima letra de una cadena o en scripts para
# tener el control de una cadena en loops o mas tipos de controles
palabra1 = 'Esternocleidomastoideo'  # Se define la variable con su valor (también lo podriamos hacer son un input)

largo = len(palabra1) -1  # Defenimos otra variable en la cual usaremos la función len para guardar en esta el total de
# caracteres que tiene y le restareos 1 ya que debemos de recordar que el indice inicia en 0, por lo cual la funcion de
# len estaria desfasado por un numero

print(palabra1[largo])  # Usaremos la sentencia de print para pintar en consola la ultima letra de nuestra palabra,
# para esto accedemos a la variable con la cadena y le indexamos la variable que guarda el largo de caracteres, al este
# tener como valor el ultimo indice de la cadena nos retorna ese caracter.


# Otra forma es usar el indice negativo, este sera una forma mucho mas facil
palabra2 = 'Pasatiempo'
print(palabra2[-1])  # El indice negativo recorre desde el ultimo caracter hasta el primero, siendo el ultimo caracter
# el indice -1, el penultimo el indice -2 y asi consecutivamente

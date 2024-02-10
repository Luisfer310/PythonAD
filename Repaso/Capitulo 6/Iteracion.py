# La iteracion de cadenas nos servira para recorrer elemento por elemento de esta cadena
palabra = input("Ingrese una palabra: ")

# Iteracion de fin a inicio con ciclo while
largo = len(palabra) - 1  # Definimos una variable para tener el largo de la cadena y le restamos 1 para tener los
# valores de un indice de este

contador = largo  # Esta variable de contador servira para que el ciclo while tenga un fon, ya que lo usaremos como condicional
while contador >= 0:  # Indicamos en la cabecera de while que este se ejecutara mientras contador sea mayor o igual a 0
    letra = palabra[contador]  # Mientras la condicion sea verdadera, la variable letra sera igual a el indice de la
    # palabra y el indice sera el valor que tenga contador en el momento en el que de vuelta en el ciclo
    print(letra)  # Y se pintara el valor de letra
    contador -= 1  # Por cada vuelta del ciclo, a contador se le restara 1, para que el ciclo tenga un fin, ya que la
    # condicon es que se ejecutara mientras contador sea mayor o igual a 0


# Iteracion de inicio a fin con ciclo while
largo = len(palabra) - 1  # Definimos una variable para tener el largo de la cadena y le restamos 1 para tener los
# valores de un indice de este
contador = 0  # En el ejemplo de fin a inicio, esta variable tenia como valor el largo de la cadena y le aplicabamos
# decrementos de 1 por cada vuelta, pero en este le daremos valor de 0 y le increntaremos 1 en cada vuelta para que
# mientras contador sea menor o igual al largo se ejecute el cuerpo de while
while contador <= largo:
    letra = palabra[contador]  # Mientras la condicion sea verdadera, la variable letra sera igual a el indice de la
    # palabra y el indice sera el valor que tenga contador en el momento en el que de vuelta en el ciclo
    print(letra)
    contador += 1  # Por cada vuelta del ciclo, a contador se le sumara 1, para que el ciclo tenga un fin, ya que la
    # condicon es que se ejecutara mientras contador sea mayor o igual a largo


# Iteracion de fin a inicio con ciclo for
for i in range(len(palabra) - 1, -1, -1):  # En el caso de los ciclos for es mas facil y mas corto que los de tipo
    # while, en el for por cada elemento en el rango del largo de la palabra se le restara 1 para igualar al contenido
    # del indice
    print(palabra[i])

# Iteracion de inicio a fin con ciclo for
for i in palabra:
    print(i)

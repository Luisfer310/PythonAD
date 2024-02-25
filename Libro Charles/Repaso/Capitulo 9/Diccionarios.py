# iniciar un diccionario vacio
miDicc = dict()
print(miDicc)

# Sintaxis de un diccionario con elementos
midicc = {'nombre': 'Luis', 'edad': 23, 'color': 'Azul', 'Numero telefonico': '6672919394'}
# Para poder pintar un valor del diccionario se usara solo la clave en la sentencia print
print(midicc['nombre'])

# Si queremos agregar un nuevo elemento a diccionario debemos hacer uso de los corchetes antes de el signo de asiognacion y en los corchetes ira el nommbre de la clave y despues de los signos de asignacion el valor.
midicc['Fruta'] = 'Mango'
print(midicc)

# La funcion len contara cuantos elementos (par clave-valor es un elemento) y no como lo hace con las cadenas, que es contar los caracteres.
print(len(midicc))

# El operador in verifica si cierta clave se encuentra en en el diccionario
print('nombre' in midicc)

# Para poder hacerlo con los valores tendremos que pasar estos a una lista y verificar si se encuentra
midicc = list(midicc)
print('edad' in midicc)
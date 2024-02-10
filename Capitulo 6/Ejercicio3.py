# Definicion de funcion que cuente las veces que aparece una letra
def contar_letra(palabra, letra):
    contador = 0
    palabra = palabra.lower()
    for i in palabra:
        if i == letra:
            contador += 1
    return contador


print(contar_letra("Administradora", 'a'))

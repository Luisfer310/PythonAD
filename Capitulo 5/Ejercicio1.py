# Escribe un programa que lea repetidamente números hasta que el usuario introduzca “fin”. Una vez se haya introducido
# “fin”, muestra por pantalla el total, la cantidad de números y la media de esos números. Si el usuario introduce
# cualquier otra cosa que no sea un número, detecta su fallo usando try y except, muestra un mensaje de error y pasa al
# número siguiente.
contador = 0
total = 0
while True:
    try:
        numero = input("> ")
        if numero == 'fin':
            break
        else:
            numero = float(numero)
            contador = contador + 1
            total = total + numero
    except:
        print('Dato erroneo.')
        continue


print(contador, total, (contador/total))
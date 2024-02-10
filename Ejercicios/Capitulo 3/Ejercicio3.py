try:
    calificacion = float(input('Dame tu calificación entre los valores 0.0 y 1.0: '))

    if calificacion >= 0.9 and calificacion <= 1.0:
        print('Sobresaliente')
    elif calificacion >= 0.8 and calificacion < 0.9:
        print('Notable')
    elif calificacion >= 0.7 and calificacion < 0.8:
        print('Bien')
    elif calificacion >= 0.6 and calificacion < 0.7:
        print('Suficiente')
    elif calificacion < 0.6 and calificacion>= 0.0:
        print('Insuficiente')
    else:
        print('El dato proporcionado es incorrecto.')

except:
    print('El dato proporcionado no es un numero.')
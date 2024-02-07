# Reescribir el programa de calificaciones del capitulo anterior usando la funcion llamada calcula_calificacion, que
# reciba una puntuacion como parametro y devuelva una calificacion como cadena.
def calcula_calificacion(calificacion):
    if 0.9 <= calificacion <= 1.0:
        calificacion_cadena = 'Sobresaliente'
        return calificacion_cadena
    elif 0.8 <= calificacion < 0.9:
        calificacion_cadena = 'Notable'
        return calificacion_cadena
    elif 0.7 <= calificacion < 0.8:
        calificacion_cadena = 'Bien'
        return calificacion_cadena
    elif 0.6 <= calificacion < 0.7:
        calificacion_cadena = 'Suficiente'
        return calificacion_cadena
    elif 0.0 <= calificacion < 0.6:
        calificacion_cadena = 'Insuficiente'
        return calificacion_cadena
    else:
        return 'El valor de calificacion no es valido.'


try:
    calificacion = float(input("Dame tu calificacion: "))
    print(calcula_calificacion(calificacion))
except:
    print("El valor de calificacion no es valido.")

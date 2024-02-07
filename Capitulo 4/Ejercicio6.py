try:
    horas = float(input("Ingrese las horas laboradas en esta semana: "))
    try:
        tarifa = float(input("Ingrese la tarifa por hora: "))

        def calcular_salario(horas, tarifa):
            salario = horas * tarifa
            return f'Tu salario de esta semana es de {salario} pesos.'

        print(calcular_salario(horas, tarifa))
    except:
        print('Dato incorrecto para tarifa.')
except:
    print('Dato incorrecto para horas.')

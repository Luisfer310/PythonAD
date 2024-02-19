horas = int(input("Introduce las horas laboradas en esta semana: "))
tarifa = int(input("Introduce la tarifa por hora: "))

if horas > 40:
    tarifa = tarifa * 1.5
    salario = horas * tarifa
    print(f'Esta semana trabajaste mas de las 40 horas, por lo cual tu salario semanal es de: {salario} pesos.')
else:
    salario = horas * tarifa
    print(f'Tu salario semanal es de: {salario} pesos.')

# Escribe un programa para pedirle al usuario el numero de horas y la tarifa por hora para calcular el salario bruto
print('Coca-Cola'.center(50, '-'))
horas = float(input('Introduzca las horas laboradas: '))
tarifa = float(input('Introduzca la tarifa por hora: '))
salario = tarifa*horas
print(f'El salario es de: {salario}/semanal')

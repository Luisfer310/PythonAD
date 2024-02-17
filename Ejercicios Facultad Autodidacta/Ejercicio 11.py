# Calcula el area de un rectangulo pide base y altura al usuario
try:
    base = float(input('Base del rectangulo: '))
    altura = float(input('Altura del rectangulo: '))

    area = altura * base
    
    print(f'El area del rectangulo es {area}')
except:
    print('Dato erroneo')
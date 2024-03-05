# Calcula el IMC
def imc(peso1, altura1):
    return peso1 / altura1 ** 2


peso = float(input('Dame tu peso en Kg: '))
altura = float(input('Dame tu altura en metros: '))
imc1 = imc(peso, altura)
print(f'Tu IMC es {imc1}')

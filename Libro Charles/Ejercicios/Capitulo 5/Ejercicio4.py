mayor = 0
menor = 0

while True:
    try:
        num = input("Ingrese un numero: ")
        if num == 'fin':
            break
        else:
            num = int(num)
            if mayor == 0 or num > mayor:
                mayor = num
            else:
                pass
            if menor == 0 or num < menor:
                menor = num
            else:
                pass

    except:
        print("Dato erroneo.")

print(mayor, menor)
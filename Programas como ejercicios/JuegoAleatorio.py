from random import *

# Juego de adivinar el numero
numero = randint(1, 100)
vidas = 8
contador = 0
while vidas > 0:
    try:
        numerousa = int(input('Dame un numero: '))
        if numerousa == numero:
            print('¡Ganaste!'.center(50, '-'))
            print('El numero que ingresaste es igual al numero alateorio')
            break
        else:
            contador += 1
            vidas -= 1
            if numerousa > numero:
                print('El numero que ingresaste es incorrecto, es mayor a el numero aleatorio')
            elif numerousa < numero:
                print('El numero que ingresste es incorrecto, es menor a el numero aleatorio')

    except:
        print('Dato erroneo.')
        pass

if vidas > 1:
    print(f'Te quedaron {vidas} vidas y lo lograste en el intento {contador}')
elif vidas == 1:
    print(f'Te quedo {vidas} vidas y lo lograste en el intento {contador} ')
elif vidas == 0:
    print('¡Perdiste!'.center(50, '-'))
    print('Se te acabor las vidas =(')

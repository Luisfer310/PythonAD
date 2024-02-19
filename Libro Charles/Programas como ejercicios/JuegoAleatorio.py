from random import *

# Juego de adivinar el numero
iniciar = input('Bienvenido al juego de "Adivina el numero", escribe "Inicio" para iniciar el juego: ')
iniciar = iniciar.lower()
numero = randint(1, 100)
vidas = 8
contador = 0
if iniciar == "inicio" or iniciar == "iniciar":
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
elif iniciar == "fin" or iniciar == "final":
    print('Quieres finalizar sin iniciar aun.')
else:
    print('Para Iniciar debes de escribir "Inicio".')

if contador > 0:
    if vidas > 1:
        print(f'Te quedaron {vidas} vidas y lo lograste en el intento {contador}')
    elif vidas == 1:
        print(f'Te quedo {vidas} vida y lo lograste en el intento {contador} ')
    elif vidas == 0:
        print('¡Perdiste!'.center(50, '-'))
        print(f'Se te acabaron las vidas =( El numero era {numero}')

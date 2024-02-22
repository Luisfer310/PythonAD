# Verifica si la palabra ingresada es python
palabra = input('Dame una palabra y yo escogere una también, a ver si escogemos la misma: ')
palabra = palabra.lower()
if palabra == 'python':
    print('Tu palabra es igual a la mia')
else:
    print('Tu palabra no es igual a la mia')
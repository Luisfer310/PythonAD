# Podria sonar buena idea que si queremos cambiar un caracter de una cadena lo hagamos de la siguiente forma...
palabra = 'Americano'
# palabra[0] = 'O'

# Esto provocara un error, debido a que las cadenas son inmutables. Para hacer algo similar a lo que se queria conseguir
# con el metodo de rebanado, puedo crear una nuva variable la cual su valor sea igual a el nuevo carcter a ingresar e
# indicando en que parte del rebanado se agregara
nueva_palabra = 'f' + palabra[1:]  # De esta forma estamos agregando un caracter antes del rebanado
print(nueva_palabra)

# Tambien podriamos poner un caracter entre 2 rebanados...
nueva_palabra0 = palabra[:3] + 'f' + palabra[3:]
print(nueva_palabra0)

# Para poner en practica un poco de lo que hemos estado viendo en este capitulo. Creare un script en el cual pueda
# recibir un correo por parte del usuario y una vez que nos lo proporcione, crear una variable la cual su valor sera el
# dominio del email y pintarlo en consola
email = input("Ingrese su email: ")
arrobainx = email.find('@')
dominio = email[arrobainx+1:]  # Si tuviera una oracion despues del email, debemos de crear una variable igual que
# 'arrobainx', pero que busque el caracter espacio despues del arroba que incluya hasta ahi el dominio
print(f'El dominio de tu email es: {dominio}')

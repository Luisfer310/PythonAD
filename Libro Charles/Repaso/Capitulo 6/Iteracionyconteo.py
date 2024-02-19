# Es muy util que en las iteraciones tengamos algun conteo de algo, puede ser de caracteres dentro de una cadena o una
# suma de numeros, estos numeros podrian estar dentro de una lista, la cual se iteraraia con un ciclo for o podemos
# pedirle los numeros al usuario y por cada numero que nos de lo ira sumando, esto seria con ciclo while

# Conteo en una cadena
palabra = 'Administradora'
palabra = palabra.lower()
contadorLetra = 0
for letra in palabra:
    if letra == 'a':
        contadorLetra += 1
print(contadorLetra)

# Conteo o suma de valores numericos con for
numeros = [1,2,3,4,5,6,7,8]
suma = 0
for n in numeros:
    suma += n
print(suma)

# El siguiente script sera pedirle al usuario 9 numeros y sumarlos en una variable. Para esto lo haremos con el ciclo
# while y la condicon sera que mientras el contador de numeros sea menor o igual a 9 le pedira un numero al usuario
contador = 0
suma = 0
while contador < 9:
    numero = int(input('Dame un numero: '))
    suma += numero
    contador += 1
print(f'La suma de tus {contador} numeros es: {suma}')

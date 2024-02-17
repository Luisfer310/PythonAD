# Escribe un programa que solicite un nombre de archivo y después lea ese archivo buscando las líneas que tengan la siguiente forma:
# X-DSPAM-Confidence: 0.8475

nombre_archivo = input('Nombre del archivo: ')
try:
    abrir_archivo = open(nombre_archivo)
except:
    print(f'No se encontro el archivo {nombre_archivo}')
    exit()

# leer_archivo = abrir_archivo.read()
# ubi_spam = leer_archivo.find('X-DSPAM-Confidence:')
suma_spam = 0
longitud = len('X-DSPAM-Confidence: ')
rebanado = ' '
contador = 0

for n in abrir_archivo:
    if n.find('X-DSPAM-Confidence:') == 0:
        rebanado = n[longitud:]
        rebanado = float(rebanado)
        suma_spam += rebanado
        contador += 1

promedio = suma_spam / contador
print(f'Promedio Spam-confidence: {promedio}')

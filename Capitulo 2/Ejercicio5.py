# Ejercicio 5: Escribe un programa que le pida al usuario una temperatura en grados celcius, la convertira a grados
# Farenheit en imprima en pantalla la temperatura convertida.
gradosc = float(input("Dame la temeratura en celcius: "))
gradosf = (gradosc * 9/5) + 32
print(f"Los grados {gradosc} Celcius son {gradosf} Fahrenheit.")

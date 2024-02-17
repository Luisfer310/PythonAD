# Calcula 2 elevado a la 4a potencia sin utilizar el operador **
a = 2
b = 4

potencia = a

while b-1 > 0: # Para que la potencia se ejecute bien se le debe de restar 1 al exponente ya que al elevarlo pa primera vez dara el mismo resultado que la base ya definida
    # si imaginamos esta operacion escrita en una libre sera: 2x2x2x2, podemos ver que hay solo 4 numeros por que sera elevado a la 4a potencia, entonces como ya tenemos uno de
    # estos escritos en la variable potencia, solo quedaria escribir tres numeros 2 mas y esto lo hacemos restando 1 a la variable b.
    potencia = potencia * a
    b -= 1

print(potencia)
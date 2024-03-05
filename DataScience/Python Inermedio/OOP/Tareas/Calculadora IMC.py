class IMC:
    def __init__(self, peso, estatura):
        self._peso = peso
        self._estatura = estatura

    def calcular_imc(self):
        return self._peso / self._estatura**2
    
IMC1 = IMC(67, 1.81)
print(IMC1.calcular_imc())
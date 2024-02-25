class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    # Metodo publico
    def obtener_saldo(self):
        return self.__saldo
    
    # Metodo publico
    def depositar(self, cantidad):
        self.__saldo += cantidad

    # Metodo publico
    def retirar(self, cantidad):
        if cantidad <= self.__saldo and cantidad>0:
            self.__saldo -= cantidad

    # Metodo privado (Este no sera alcanzado por el usuario, este solo se emplea para que haga un calculo)
    def ___Calcular_interes(self, tasa):
        return self.__saldo * tasa / 100

    # Metodo publico    
    def aplicar_interes(self, tasa):
        intereses = self.___Calcular_interes(tasa)
        self.__saldo += intereses
        print(f'Interes aplicados: {self.__saldo}')

cuenta = CuentaBancaria(1000)
print(cuenta.obtener_saldo())
cuenta.depositar(100)
print(cuenta.obtener_saldo())
cuenta.retirar(300)
print(cuenta.obtener_saldo())
# Empezamos importando una libreria
from abc import ABC, abstractmethod

# Creamos una clase abstracta
class Forma(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Forma):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2
    
class Rectangulo(Forma):
    def __init__(self, ancho, alto, color):
        super().__init__(color)
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto
    
circulo = Circulo(10, 'Rojo')
rectangulo = Rectangulo(10, 5, 'rojo')

print(f'Area del circulo: {circulo.calcular_area()}')
print(f'Area del rectangulo: {rectangulo.calcular_area()}')
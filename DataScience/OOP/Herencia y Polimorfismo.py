# Creando una clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def obterner_informacion(self):
        return f'Nombre: {self.nombre}, edad: {self.edad}'
    
persona0 = Persona('Luis', 24) # Se crea una instancia de la clase (estee seria el objeto)
print(persona0.obterner_informacion()) # Para acceder a un metodo se debe de hacer con un punto

# Herencia
class Estudiante(Persona): # Lo que esta entre parentesis sera la clase de la que heredara∫
    def __init__(self, nombre, edad, curso): # A el constructor hijo se le pasa como parametro los atributos del padre y se la agrega la nueva para el hijo
        super().__init__(nombre, edad) # Con esta funcion se extrae el constructor padre
        self.curso = curso

    def presentarse(self):
        return f'Hola, me llamo {self.nombre} y tengo {self.edad} años, soy un estudiante de {self.curso}'
    
Estudiante0 = Estudiante('Luis', 23, 'Python') # Se crea el objeto
print(Estudiante0.presentarse()) # Se accede a el metodo

# Polimorfismo

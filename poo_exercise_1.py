
class Persona:
    def __init__(self, nombre, apellidos, edad , estatura, peso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    def nombre_completo(self):
        print(f'El nombre completo es: {self.nombre} {self.apellidos}')

    def calcular_IMC(self):
        IMC = (self.peso/(self.estatura)**2)
        print('Tu índice de masa corporal es: ',IMC)

nombre = input('Ingresa tu nombre:')
apellidos = input('Ingresa tus apellidos:')
edad = input('Ingresa tu edad:')
estatura = float(input('Ingresa tu estatura:'))
peso = float(input('Ingresa tu peso:'))

persona_1 = Persona(nombre,apellidos,edad,estatura,peso)
persona_1.nombre_completo()
persona_1.calcular_IMC()


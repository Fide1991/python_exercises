class Alumno:
    def __init__(self, matricula, nombre, apellidos, promedio, edad, año_escolar):
        self.matricula = matricula
        self.nombre = nombre
        self.apellidos = apellidos
        self.promedio = promedio
        self.edad = edad 
        self.año_escolar = año_escolar

    def get_matricula(self):
        return self.matricula
    
    def get_nombre(self):
        return self.nombre
    
    def get_apellidos(self):
        return self.apellidos

    def get_promedio(self):
        return self.promedio
    
    def get_edad(self):
        return self.edad

    def get_año_escolar(self):
        return self.año_escolar

    def set_matricula(self, matricula):
        self.matricula = matricula
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_apellidos(self, apellidos):
        self.apellidos = apellidos

    def set_promedio(self, promedio):
        self.promedio = promedio

    def set_edad(self, edad):
        self.edad = edad

    def set_año_escolar(self, año_escolar):
        self.año_escolar = año_escolar    
    
    def ingreso_estudiar(self):
        año_ingreso = 2020-self.año_escolar
        print(f'El año es que ingresaste a estudiar fue: {año_ingreso}')

    def inicio_estudiar(self):
        edad_inicio = self.edad-self.año_escolar
        print(f'Cuando comenzaste a estudiar tenias {edad_inicio} años')

    def imprime_datos(self):
        print(f'Nombre: {self.nombre} {self.apellidos}. Matrícula:{self.matricula}. Promedio:{self.promedio}')
    

alumno_1 = Alumno('L03113261', 'Fidencio', 'Moguel Velez', 87, 28, 5)
alumno_1.ingreso_estudiar()
alumno_1.inicio_estudiar()
alumno_1.imprime_datos()

alumno_1.set_promedio(90)
print('promedio actualizado: ', alumno_1.get_promedio())





    
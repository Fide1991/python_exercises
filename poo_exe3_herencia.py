class Persona:
    def __init__(self, nombre, apellidos, edad, sexo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo

    def get_nombre_completo(self):
        return f'{self.nombre} {self.apellidos}'

    def get_edad_completa(self):
        return f'{self.edad} años'
        
    def set_nombre(self, nombre):
       self.nombre = nombre


class Alumno(Persona):
    def __init__(self, nombre, apellidos, edad, sexo, matricula, promedio):#se indican los atributos tanto de la clse padre como la hija
        super().__init__(nombre, apellidos, edad, sexo)#se indica cuales atributos de la clase padre se mandan a llamar
        #usamos el metodo super para llamar el contructor de la clase padre, en este caso Persona       
        self.matricula = matricula#se inicializan los atributos de la clase hija
        self.promedio = promedio

    def get_informacion_estudiante(self):
        return f'{self.get_nombre_completo()} Matricula: {self.matricula}' 


class Profesor(Persona):
    def __init__(self, nombre, apellidos, edad, sexo, cedula, correo_institucional):
        super().__init__(nombre, apellidos, edad, sexo)
        self.cedula = cedula
        self.correo_institucional = correo_institucional

    def get_informacion_profesor(self):
        return f'{self.get_nombre_completo()} Cédula: {self.cedula}' 


alumno_1 = Alumno('Fide', 'Moguel Velez', 28, 'M', 'L03113261', 87)
print(alumno_1.get_nombre_completo())
print(alumno_1.get_informacion_estudiante())

profesor_1 = Profesor('Juan Manuel', 'Gonzalaz Sobac', 45, 'M', '454DGS5F5', 'juan.msobac@itsh.mx')
print(profesor_1.get_nombre_completo())
print(profesor_1.get_informacion_profesor())

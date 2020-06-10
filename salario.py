
respuesta = 'si'

while respuesta == 'si':
    nombre=input('Ingresa tu nombre:')
    salario=float(input('Ingresa tu salario:'))
    salario_bruto = salario * 0.84
    print('El salario bruto de:', nombre, ' es:', salario_bruto)
    respuesta = input('¿Deseas calcular el salario de otra persona?')


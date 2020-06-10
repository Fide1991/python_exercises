nombres = []
respuesta = 'si'

while respuesta == 'si':
    nombre=input('Ingresa tu nombre:')
    nombres.append(nombre)
    respuesta = input('¿Deseas añadir otra persona?')

nombres_unidos = ','.join(nombres)
print(nombres_unidos)


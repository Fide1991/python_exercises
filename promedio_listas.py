calificaciones = []
nombre = input('Ingresa el nombre:')

respuesta = 'si'

while respuesta == 'si':
    contador = 0
    calificacion = float(input('Ingresa la calificación:'))
    calificaciones.append(calificacion)
    respuesta = input('¿Deseas agregar otra calificación?')

suma = 0
longitud = int(len(calificaciones))
for i in range(0,longitud):
    suma += calificaciones[i]
    promedio = suma / longitud

print('El promedio de', nombre , 'es:', promedio)
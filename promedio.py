
nombre = input('Ingresa tu nombre:')


calif_1 = float(input('Ingresa tu primer calificación:'))
calif_2 = float(input('Ingresa tu segunda calificación:'))
calif_3 = float(input('Ingresa tu tercer calificación:'))

prom = (calif_1 + calif_2 + calif_3)/3

#saber si aprobe el año (min. aprobatoria 7).
if prom >= 7:
    print('Aprobaste el año, felicidades!')
else:
    print('Reprobaste el año, lo siento.')

print('Alumno', nombre, 'tu promedio fue:', prom)
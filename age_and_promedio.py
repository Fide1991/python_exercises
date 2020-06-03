edad = float(input('Ingresa tu edad:'))
promedio = float(input('Ingresa tu promedio:'))


if edad < 6:
    print('Kinder, no aplica')
elif edad >= 6  and edad < 12:
    if promedio >= 9.5:
        print('Promedio aceptable primaria')
    else:
        print('Promedio deficiente primaria')
elif edad >= 12 and edad < 15:
    if promedio >= 9:
        print('Promedio aceptable secundaria')
    else:
        print('Promedio deficiente secundaria')
elif edad >= 15 and edad < 18:
    if promedio >= 8.5:
        print('Promedio aceptable bachillerato')
    else:
        print('Promedio deficiente bachillerato')
elif edad >= 18 and edad < 23:
    if promedio >= 8:
        print('Promedio aceptable universidad')
    else:
        print('Promedio deficiente universidad')
else:
    print('Profesionista, tu ya no estudias')
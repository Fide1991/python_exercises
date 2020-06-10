#en este ejercicio se separa un string usando las listas y su metodo split() 

texto = 'Martin_8/9$Juan_5/4/9/8$Francisco_10/10/10/9'
lista_estudiantes=texto.split('$')

for student in lista_estudiantes:
    valores = student.split('_')
    print('Nombre y calificaciones', valores)
    nombre = valores[0]
    print('El nombre es:', nombre)
    calificaciones = valores[1].split('/')
    print(f'Las calificaciones de {nombre} son: {calificaciones}')
    suma=0
    for calif in calificaciones:
        suma += float(calif)
    promedio = suma / len(calificaciones)
    print(f'La calificacion final de {nombre} es: {promedio}')

    


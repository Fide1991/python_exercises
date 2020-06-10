meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

respuesta = 'si'

while respuesta == 'si':
    numero = int(input('Ingresa el numero del mes que deseas ver:'))
    if numero >= 1 and numero <=12:
        print('El mes es:', meses[numero-1])
    else:
        print('Numero inválido')
    respuesta = input('¿Deseas visualizar otro mes?')



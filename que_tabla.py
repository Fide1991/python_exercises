respuesta = 'si'

while respuesta == 'si':
    contador = 1
    numero = int(input('Ingresa el numero del cual quieres realizar la tabla:'))
    while contador <=25:
        tabla = numero * contador
        print(numero, 'x', contador, '=', tabla)
        contador += 1
    respuesta = input('¿Deseas calcular la tabla de otro numero?')    

nombre = input('Ingresa tu nombre:')
apellidos = input('Ingresa tus apellidos:')
edad = input('Ingresa tu edad:')
correo = input('Ingresa tu correo:')

datos = {'Nombre':nombre, 'Apellidos':apellidos, 'Edad':edad, 'Correo':correo}

#print(datos)

print(f'Hola mi nombre es {datos["Nombre"]} {datos["Apellidos"]}, tengo {datos["Edad"]} años y correo es {datos["Correo"]}')




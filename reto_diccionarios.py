#1.- recibir del teclado un pais, y la contidad de personas que viven ahi (en millones)
#2- el usuario podra ingresar la cantidad de paises que desee
#3.- construye un diccionario donde, cada pais va a ser la clave y la cantidad de personas el valor
#paises = {'USA':50, 'México:30'}

# imprime todos los paises dentro del diccionario con la cantidad de habitantes

#4.- despues pide al usuario que ingrese el nombre de un pais, para poder ver la cantidad de personas
#5.- accede al elemento del diccionario que contiene ese dato

paises = {}
respuesta = 'si'

while respuesta == 'si':
    pais = input('Ingresa el nombre del país:')
    cantidad = input('Ingresa la cantidad de personas que viven ahí:')
    paises[pais] = cantidad 
    respuesta=input('Deseas agregar otro país?')

for clave,valor in paises.items():
    print(f'El nombre del pais es: {clave} y su cantidad de habitantes es: {valor}')

ver_pais = input('Ingresa el pais que deseas ver:')
print(f'La cantidad de habitantes es: {paises[ver_pais]}')




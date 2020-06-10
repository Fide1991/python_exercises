#El objetivo del programa es contar cuantas veces se repite una palabra en un texto
#1.-separar el texto, guardando cada palabra como un elemento de un lista
#2.-itera la lista y guarda cada palabra como un elemento de un diccionario, 
#donde su valor va a ser la cantidad de veces que aparece esa palabra

texto = 'Este texto tiene algunas palabras Este es otro texto con algunas palabras diferentes'

palabras_texto = texto.split(' ')

diccionario = {}

for palabra in palabras_texto:
    print(palabra)
    if palabra in diccionario:
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1
     
print(diccionario)

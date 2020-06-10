
nombres = input('Ingresa los nombres separados por una coma:')
lista_nombres = nombres.split(',')

print('los nombres son:', lista_nombres)

tupla_nombres = tuple(lista_nombres)

print('La cantidad de nombres introducidos es:', len(tupla_nombres))

print('El valor máximo de la tupla es:', max(tupla_nombres))

print('El valor mínimo de la tupla es:', min(tupla_nombres))





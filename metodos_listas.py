#archivo que ejemplifica el uso de algunos metodos de las listas.

paises = ['MX', 'US', 'UK', 'MX', 'MX', 'US', 'UK', 'FR', 'CH', 'CH']
print('lista incial de paises:', paises)

paises.append('JP')
print('paises con JP añadido:', paises)

print('MX se encuetra', paises.count('MX'), 'veces')

print('UK aparece por primera vez en el indice:',paises.index('UK'))

lista_2 = paises.copy()
print('Copia de la lista 2:', lista_2)

lista_2.extend(['COL', 'ARG', 'BR'])
print('Lista 2 extendida: ', lista_2)

lista_2.remove('CH')
print('Lista 2 sin el CH:', lista_2)



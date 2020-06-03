#reto 1 Imprime los 300 primeros números pares
for i in range(2, 301, 2):
    print(i)

#reto 2 Imprime la tabla del 15. Muestra el resultado de los primeros 20 números
for i in range(1, 21):
    tabla = 15*i
    print(tabla)

#reto 3 Calcula la suma de los números impares ubicados entre el 50 y el 100
suma=0

for i in range(51, 100, 2):
    suma += i
    print(i)

print('la suma es:', suma)

#reto 4 calcula la suma de los numeros pares entre el 10 y el 100 (utilizar el operador aritmético módulo)
suma_par = 0

for i in range(10,101):
    if (i%2) == 0:
        print('Número par:', i)
        suma_par+=i

print('La suma de los numeros pares es:', suma_par)


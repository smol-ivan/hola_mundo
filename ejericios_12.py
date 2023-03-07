"""
Ejercicio 1

Dados dos numeros enteros x > 0 y n >= 0, calcula x**n. Por ejemplo, si x ← 6 y n ← 4, 6**4 se calcula con la multiplicacion 6 x 6 x 6 x 6. Considera que, para cualquier numero x, si n ← 0, x**n es 1.

numero      = False

while not numero:
    x = input('Ingrese un valor (x>0): ')
    n = input('Ingrese el valor (n>=0): ')
    if x.isdigit() and n.isdigit() == True:
        if int(x) > 0 and int(n) > 0:
            numero = True

acumulado = int(x)
i = 1

while i != int(n):
    if int(x) > 0:
        if int(n) > 0:
            acumulado = acumulado * int(x)
            i = i + 1
        else:
            acumulado = 1
            break
print(acumulado)
print()
"""

"""
Ejercicio 2

Dado un numero entero positivo n, calcula n! (factorial de n!). n! se define como n x (n - 1)!. Por ejemplo, si n ← 5, su factorial se calcula como 5 * 4 * 3 * 2 * 1
"""
numero = False

while not numero:
    n = input('Ingrese el factorial (n!) a calcular: ')
    if n.isdigit() == True:
        numero = True

i = int(n)
acumulado = 1

while i >= 1:
    if int(n) != 0:
        acumulado = acumulado * i
        i = i - 1

print(acumulado)
print()


"""
Ejercicio 3

Dados dos numeros enteros positivos{a, b}, donde a < b, calcula la suma de todos los numeros impares en el rango [a, b]. Por ejemplo, si a ← 10 y b ← 19, la suma debe de ser 11 + 13 + 15 + 17 + 19

numero = False

while not numero:
    a = input('Ingrese un numero entero: ')
    b = input('Ingrese un numero mayor al anterior: ')
    if a.isdigit() and b.isdigit() == True:
        numero = True
        
if int(a) % 2 == 0:
    num_a = int(a) + 1
else:
    num_a = int(a)

if int(b) % 2 == 0:
    num_b = int(b) -1
else:
    num_b = int(b)

i = 1
acumulado = num_a
resultado = num_a

while i <= (num_b - num_a) / 2:
    acumulado = acumulado + 2
    resultado = resultado + acumulado
    i = i + 1

print(resultado)
print()
"""
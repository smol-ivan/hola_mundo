"""
Ejercicio 1

Encontrar el máximo de tres números a, b y c.

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
c = float(input("Ingrese el tercer numero: "))

if a >= b and b <= c:
    numMaximo = a
elif a <= b and b >= c:
    numMaximo = b
else:
    numMaximo = c

print(numMaximo)
"""

"""
Ejercicio 2

Los lados de un triángulo miden a, b y c. ¿Qué tipo de triángulo es?

a = float(input("Ingrese el lado 'a' del triangulo: "))
b = float(input("Ingrese el lado 'b' del triangulo: "))
c = float(input("Ingrese el lado 'c' del triangulo: "))

if a == b and b == c and c == a:
    triangulo = 'Equilatero'
elif a != b and b != c and c != a:
    triangulo = 'Escaleno'
else:
    triangulo = 'Isosceles'

print("El triangulo ingresado corresponde a uno: " + triangulo)
"""

"""
Ejercicio 3

Dados dos números a y b, decir si “a es divisor de b”, si “b es divisor de a“ o si “no son divisores”.

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

if a % b == 0:
    entero = True
    dividendo = 'a'
    divisor = 'b'
elif b % a == 0:
    entero = True
    dividendo = 'b'
    divisor = 'a'
else:
    entero = False

if entero == True:
    print("El numero " + divisor + " divide al numero " + dividendo)
else:
    print("Los valores no son divisores.")
"""

"""
Ejercicio 4

Una frutería vende manzanas a $45 el kilo, peras a $40 el kilo y naranjas a $25 el kilo. Si un cliente compra n kilos de la fruta x, ¿cuánto tiene que pagar?

fruta = input("Ingrese la fruta que compró (Manzana, Pera o  Naranja): ")
kilos = float(input("Ingrese la cantidad en kilos que compró: "))

if fruta.lower() == "manzana":
    total = kilos * 45
elif fruta.lower() == "pera":
    total = kilos * 40
else:
    total = kilos * 25

print("El total por su compra es de: $" + str(total))
"""

"""
Ejercicio 5

A partir de un peso (en kg) y una estatura (en m) de una persona, su índice de masa corporal (IMC) se calcula como

IMC =peso/(estatura * estatura)

Indicar si una persona tiene “bajo peso” (IMC menor que 18.5), “peso normal” (IMC entre 18.5 y 25), “sobrepeso” (IMC mayor que 25 y menor que 30) u “obesidad” (IMC 30 o mayor).

peso     = float(input("Ingrese el peso de la persona en kilogramos: "))
estatura = float(input("Ingrese la estatura en metros: "))

imc = peso / (estatura * estatura)

if imc < 18.5:
    indicacion = 'bajo peso'
elif imc <= 25:
    indicacion = 'peso normal'
elif imc < 30:
    indicacion = 'sobrepeso'
else:
    indicacion = 'obesidad'

print("De acuerdo con su IMC se arroja la siguiente indicacion: " + indicacion)
"""

"""
Ejercicio 6

¿Cuántos días tiene el mes m?

mes = int(input("Ingrese el mes en formato numerico: "))

if mes == 2:
    dias = 28
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias = 30
else:
    dias = 31

print("El mes " + str(mes) + " tiene " + str(dias) + " dias.")
"""

"""
Ejercicio 7
"""

"""
Ejercicio 8
"""

"""
Ejercicio 9
"""

"""
Ejercicio 10

Doña Lore tiene una cocina económica que vende comidas de tres tiempos. En el primer tiempo ofrece sopa de lentejas a $20, crema de elote a $25 y sopa de fideos a $15. En el segundo tiempo tiene arroz a $15, espagueti a $20 y ensalada a $10. En el tercer tiempo tiene pollo con papas a $35, bistec en morita a $45 y chile relleno a $30. ¿Cuánto tiene que pagar un comensal que elige una opción de cada tiempo?

tiempoUno   = input("Ingrese lo que desee comer en el primer tiempo (Sopa de lentejas, Crema de elote): ")
tiempoDos   = input("Ingrese lo que desee comer en el segundo tiempo (Arroz, Spaguetti, Ensalada): ")
tiempoTres  = input("Ingrese lo que desee comer en el tercer tiempo (Pollo con papas, Bistec de morita, Chile releno): ")

if tiempoUno.lower = 
"""

"""
Ejercicio 11

El zodiaco chino asigna animales a años en un ciclo de 12 años. En la siguiente tabla se muestra un ciclo de 12 años. El patrón se repite como se indica, siendo 2012 otro año del dragón y 1999 otro año de la liebre.

"""
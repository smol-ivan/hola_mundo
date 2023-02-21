"""
Ejercicio 2

Encontrar en maximo de dos numeros [a, b]

numero_a = float(input("Ingrese un numero: "))
numero_b = float(input("Ingrese un numero: "))

if numero_a >= numero_b:
    print("El numero maximo es: " + str(numero_a))
else:
    print("El numero maximo es: " + str(numero_b))
"""

"""
Ejercicio 3 

Una frutería vende manzanas a $45 el kilo y naranjas a $25 el kilo. Si un cliente compra n kilos de la fruta x, ¿cuánto tiene que pagar?

fruta.lower() = input("Ingrese la fruta que compró (Manzana o Naranja): ")
kilos = float(input("Ingrese la cantidad en kilos que compró: "))

if fruta == "manzana":
    total = kilos * 45
else:
    total = kilos * 25

print("El total por su compra es de: $" + str(total))
"""

"""
Ejercicio 4

La calificación final de un curso es el promedio de las calificaciones parciales c1 y c2. Para que un alumno tenga derecho a su calificación final, ambas calificaciones parciales c1 y c2 deben ser aprobatorias, además de que su porcentaje de asistencia a clase p debe ser al menos del 80%. ¿Cuál es la calificación de un alumno?

parcial_1 = float(input("Ingrese la calificacion del parcial C1: "))
parcial_2 = float(input("Ingrese la calificacion del parcial C2: "))

asistencias = float(input("Ingrese el porcentaje de asistencias del alumno: "))

if parcial_1 >= 6 and parcial_2 >= 6 and asistencias >= 80:
    print("El alumno si tiene derecho a Examen Final : D")
else:
    print("El alumno no tiene derecho a Examen Final : C")
"""

"""
Ejercicio 5

Determinar cuánto se debe pagar por n lápices considerando que si son 1000 o más el costo es de $2.50, de lo contrario, el precio es de $3.00.

lapices = int(input("Ingrese la cantidad de lapices a comprar: "))

if lapices >= 1000:
    total = lapices * 2.5
else:
    total = lapices * 3

print("El total a pagar por " + str(lapices) + " lapices es de : $" + str(total))
"""

"""
Ejercicios 6 

“El palacio de papel” tiene la siguiente promoción: todos los trajes que tienen un precio superior a $5,000.00 tienen un descuento del 15% y todos los demás tienen un descuento del 8%. ¿Cuál es el precio final que debe pagar un cliente que compra un traje que cuesta $x y de cuánto es el descuento que obtendrá?

precioTraje = float(input("Ingrese el precio marcado en la etiqueta del traje: $"))

if precioTraje > 5000:
    precioFinal = precioTraje * 0.85
else:
    precioFinal = precioTraje * 0.92

print("El precio con descuento del traje elegido es de: $" + str(precioFinal))
"""

"""
Ejercicios 7

En la tienda “Mascotas Primero” venden diferentes marcas de alimento para perro y todas las semanas ofrecen descuentos. Por ejemplo, esta semana, las marcas Hills Science Diet, Royal Canin y ProPlan tienen 20% de descuento. Si un cliente lleva alimento de la marca x, ¿cuál es el descuento que le hacen?

marcaAlimento = input("Ingrese la marca de alimento para perro a llevar: ")


if marcaAlimento.lower() == "hills science" or marcaAlimento.lower() == "diet" or marcaAlimento.lower() == "royal canin" or marcaAlimento.lower() == "proplan":
    print("El descuento del alimento elegido es de 20%")
else:
    print("El alimento elegido no tiene descuento esta semana.")
"""

"""
Ejercicio 8

Comúnmente se dice que un año humano es equivalente a 7 años perro. Sin embargo, esta simple conversión no reconoce que los perros alcanzan la edad adulta en aproximadamente dos años. Como resultado, algunas personas creen que es mejor contar cada uno de los dos primeros años humanos como 10.5 años perro y luego contar cada año humano adicional como 4 años perro.

Tomando en cuenta la conversión descrita en el párrafo anterior, ¿a cuántos años caninos equivalen x años humanos?

humanYears = float(input("Ingrese los años del humano: "))

if humanYears <= 2:
    dogYears   = humanYears * 10.5
else:
    humanYears = humanYears - 2
    dogYears   = humanYears * 4 + 21

print("La conversion de años humanos a años perrunos es de: " + str(dogYears))
"""

"""
Ejercicio 9

Nuestro planeta gira 365.24219 veces durante una órbita completa alrededor del sol, por lo tanto un año dura 365 días, 5 horas, 48 minutos y 56 segundos, y no únicamente 365 días. Con el fin de corregir este error, al emperador Julio César se le ocurrió crear el año bisiesto. Si cada año nosotros contamos esos 365 días, perdemos esas 5 horas que deberemos recuperar. Durante tres años contamos esos 365 y al cuarto recuperamos el día que falta, el día 29 de febrero, el año bisiesto.

Fue en el año 44 a. C., al adaptarse al calendario juliano, cuando los años pasaron a tener 365 días, divididos en doce meses de 30 o 31 días, salvo febrero con 28. Siendo conscientes los romanos de que los 365 días no eran un cálculo exacto, cada cuatro años añadían un día más al calendario.

Posteriormente, en el año 1582, el calendario gregoriano sustituyó al juliano y ajustó un poco más el desfase que todavía existía con el calendario juliano, añadiendo excepciones a los años bisiestos: no lo serán los años múltiplos de 100, salvo si son también divisibles por 400. Por este motivo, el año 1900, que debería haber sido año bisiesto, no lo fue (es múltiplo de 100 y no es divisible por 400). Y el año 2000, que es múltiplo de 100 y también es divisible por 400, sí lo fue. Del mismo modo, los años 2100 y 2200 no serán años bisiestos. 

¿Un año x es bisiesto?


year  = int(input("Ingrese el año: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("El año " + str(year) + " es bisiesto.")
else:
    print("El año " + str(year) + " no es bisiesto.")
"""

"""
Ejercicio 10 

En la tienda “La mejor compra” venden dos modelos de computadoras portátiles: el modelo “D” y el “M”. Los precios de las computadoras son los siguientes: $20,000.00 el modelo “D” y $27,000.00 el modelo “M”.

Independientemente de la marca, a cada modelo se le pueden hacer las siguientes mejoras opcionales a su configuración básica: procesador Intel Core i7 cuatro núcleos de séptima generación por $3,000.00, unidad de estado sólido de 256 GB por $5,000, memoria RAM de 8 GB LPDDR3 de 2133 MHz por $4,000.00 y una unidad gráfica Intel UHD Graphics 617 por $6,000.00.

¿Cuánto tiene que pagar un cliente que compra una de estas computadoras y por las configuraciones opcionales?

laptopModel  = input("Which laptop model do you want to buy? (D or M): ")

cpuUpgrade   = input("For extra $150, want to upgrade the CPU for a Intel Core i7 7th gen? (Yes or No): ")
ssdUpgrade   = input("Want to add an SSD drive for $250 extra? (Yes or No): ")
ramUpgrade   = input("Want to add an extra 8GB RAM for $200 extra? (Yes or No): ")
gpuUpgrade   = input("Want to upgrade GPU to Intel UHD Graphics 617 for $300? (Yes or No): ")

if laptopModel.lower() == "d":
    total = 1000
else: 
    total = 1350

if cpuUpgrade.lower() == "yes":
    total = total + 150
else:
    total = total

if ssdUpgrade.lower() == "yes":
    total = total + 250
else:
    total = total

if ramUpgrade.lower() == "yes":
    total = total + 200
else:
    total = total

if gpuUpgrade.lower() == "yes":
    total = total + 300
else:
    total = total

print(total)
"""
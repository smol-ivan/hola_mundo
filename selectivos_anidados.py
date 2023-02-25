"""
Ejercicio 7

Las posiciones en un tablero de ajedrez se identifican con una letra y un número. La letra identifica la columna, mientras que el número identifica la fila, como se muestra a continuación:

Dada una posición del tablero, determinar de qué color es esa casilla. Por ejemplo, si la posición es a1, el cuadrado es negro. Si la posición es d5, el cuadrado es blanco. En caso de que la posición no sea válida, indicarlo.

"""
columna = input('Ingrese la columna en la que se encuentra la ficha (a-h): ')
fila    = int(input('Ingrese la fila en la que se encuentra la ficha (1-8): '))

if columna == 'a' or columna == 'c' or columna == 'e' or columna == 'g':
    if fila % 2 == 0:
        print('El color de la casilla es negro!')
    else:
        print('El color de la casilla es blanco!')
elif columna == 'b' or columna == 'd' or columna == 'f' or columna == 'h':
    if fila % 2 == 0:
        print('El color de la casilla es blanco!')
    else:
        print('El color de la casilla es negro!')
else: 
    print('La posicion ingresada no es valida!')

"""
Ejercicio 9

Dada una fecha, calcular la fecha del siguiente día. Por ejemplo, si la fecha es 2018-10-30, entonces la fecha del siguiente día es 2018-10-31. Si la fecha es 2018-10-31, entonces el día siguiente es 2018-11-01. Si la fecha es 2018-12-31 el día siguiente es 2019-01-01. Considera que la fecha tiene formato con tres valores numéricos: año, mes y día. Asegúrate de que tu programa funcione correctamente para los años bisiestos.

dia   = int(input('Ingrese el dia actual en formato numerico: '))
mes   = int(input('Ingrese el mes actual en formato numerico: '))
año   = int(input('Ingrese el año actual: '))

bis1    = año % 4 == 0 and año % 100 != 0
bis2    = año % 400 == 0

mes_31   = mes == 4 or mes == 6 or mes == 9 or mes == 11 
mes_30   = mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10

if mes == 2:
    if bis1 or bis2:
        if dia == 29:
            dia = 1
            mes = mes + 1
        else:
            dia = dia + 1
    else:
        if dia == 28:
            dia = 1
            mes = mes + 1
        else: 
            dia = dia + 1
elif mes == mes_31:
    if dia == 31:
        dia = 1
        mes = mes + 1
    else: 
        dia + 1
elif mes == mes_30:
    if dia == 30:
        dia = 1
        mes = mes + 1
    else:
        dia = dia + 1
else:
    if dia == 31:
        año = año + 1
        mes = 1
        dia = 1
    else:
        dia = dia + 1

print('El dia consecutivo es el siguiente: ' + str(año) + '-' + str(mes) + '-' + str(dia))
"""

"""
Ejercicio 10

Una ruleta tiene 38 espacios. De estos espacios, 18 son negros, 18 son rojos y dos son verdes. Los espacios verdes están numerados con 0 y 00. Los espacios rojos están numerados con 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 y 36. Los enteros restantes entre 1 y 36 se utilizan para numerar los espacios negros.

Se pueden hacer muchas apuestas diferentes en la ruleta. En este ejercicio sólo consideraremos el siguiente subconjunto de estas:

Número único (1 a 36, 0 o 00)
Rojo contra negro
Impar contra par (ten en cuenta que 0 y 00 no pagan por par)
1 a 18 contra 19 a 36

Dado un número x, mostrar todas las apuestas que deben pagarse. Por ejemplo, si x = 13, el programa debería mostrar:

Paga 13
Paga negro
Paga impar
Paga 1 a 18

Si x es 0 o 00, entonces el programa debería mostrar Paga 0 o Paga 00 sin ningún resultado adicional.


numeroCasilla = input('Ingrese el numero sorteado en la ruleta: ')

if numeroCasilla == '0' or numeroCasilla == '00':
    print('Paga ' + numeroCasilla)

elif numeroCasilla == '1' or numeroCasilla == '3' or numeroCasilla == '5' or numeroCasilla == '7' or numeroCasilla == '9' or numeroCasilla == '12' or \
     numeroCasilla == '14' or numeroCasilla == '16' or numeroCasilla == '18' or numeroCasilla == '21' or numeroCasilla == '23' or numeroCasilla == '25' or \
     numeroCasilla == '27' or numeroCasilla == '30' or numeroCasilla == '32' or numeroCasilla == '34' or numeroCasilla == '36':
    print('Paga Rojo')
    print('Paga ' + numeroCasilla)
    if int(numeroCasilla) % 2 == 0:
        print('Paga Par')
        if int(numeroCasilla) <= 18:
            print('Paga 1 a 18')
        else:
            print('Paga 19 a 36')
    else:
        print('Paga Impar')
        if int(numeroCasilla) <= 18:
            print('Paga 1 a 18')
        else:
            print('Paga 19 a 36')
else:
    print('Paga Negro')
    print('Paga ' + numeroCasilla)
    if int(numeroCasilla) % 2 == 0:
        print('Paga Par')
        if int(numeroCasilla) <= 18:
            print('Paga 1 a 18')
        else:
            print('Paga 19 a 36')
    else:
        print('Paga Impar')
        if int(numeroCasilla) <= 18:
                print('Paga 1 a 18')
        else:
                print('Paga 19 a 36')
"""
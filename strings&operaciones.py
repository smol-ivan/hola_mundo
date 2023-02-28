"""
Ejercicio 1.

Dada una palabra, crea un string formado por los caracteres primero, medio y último.

palabra = input("Ingrese una palabra: ")

lengthWord = len(palabra)
primero = palabra[0]
ultimo  = palabra[len(palabra) - 1]

if lengthWord % 2 == 0:
    medio = palabra[(lenght_palabra - 1) // 2] + palabra[(lenght_palabra + 1) // 2]
else:
    medio = palabra[lenght_palabra // 2] 

resultado = primero + medio + ultimo
print('resultado')
"""

"""
Ejercicio 2.

Dada una palabra, crea un string hecha de los tres caracteres de enmedio.

palabra = input('Ingrese una palabra: ')

lengthWord = len(palabra)

if lengthWord % 2 != 0:    
    medio_1 = palabra[lengthWord // 2 - 1]
    medio_2 = palabra[lengthWord // 2]
    medio_3 = palabra[lengthWord // 2 + 1]
    resultado = medio_1 + medio_2 + medio_3
else:
    resultado = 'La palabra ingresada no es valida!'

print(resultado)
"""

"""
Ejercicio 3.

Agrega una nueva cadena en medio de un string dado.

palabra = input("Ingrese una palabra: ")
nuevaPalabra = input("Ingrese una palabra a agregar: ")

lengthWord = len(palabra)

if lengthWord % 2 != 0:
    resultado = palabra[:(lengthWord - 1) // 2 ] + nuevaPalabra + palabra[(lengthWord + 1) // 2:]
else:
    resultado = palabra[:lengthWord  // 2 ] + nuevaPalabra + palabra[lengthWord // 2:]

print(resultado)
"""

"""
Ejercicio 4.

Dados tres strings de entrada, crea un nuevo string compuesto por el primero, medio y último carácter respectivamente de la primera cadena, de la segunda y de la tercera. 

"""
string_1 = input('Ingrese el primer string: ')
string_2 = input('Ingrese el segundo string: ')
string_3 = input('Ingrese el tercer string: ')

if len(string_1) % 2 == 0:
    
mainString = 
"""
Ejercicio 1.

Dada una palabra, crea un string formado por los caracteres primero, medio y último.

palabra = input("Ingrese una palabra: ")

length_palabra = len(palabra)
primero = palabra[0]
ultimo  = palabra[len(palabra) - 1]

if length_palabra % 2 == 0:
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

length_palabra = len(palabra)

if length_palabra % 2 != 0:    
    medio_1 = palabra[length_palabra // 2 - 1]
    medio_2 = palabra[length_palabra // 2]
    medio_3 = palabra[length_palabra // 2 + 1]
    resultado = medio_1 + medio_2 + medio_3
else:
    resultado = 'La palabra ingresada no es valida!'

print(resultado)
"""

"""
Ejercicio 3.

Agrega una nueva cadena en medio de un string dado.
"""
palabra = input("Ingrese una palabra: ")
nuevaPalabra = input("Ingrese una palabra a agregar: ")

length_palabra = len(palabra)

if length_palabra % 2 != 0:
    resultado = palabra[:(length_palabra - 1) // 2 ] + nuevaPalabra + palabra[(length_palabra + 1) // 2:]
else:
    resultado = palabra[:length_palabra  // 2 ] + nuevaPalabra + palabra[length_palabra // 2:]


print(resultado)

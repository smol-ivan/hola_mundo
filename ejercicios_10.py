"""
Ejercicio 1.

Considera que la variable datos se refiere a la lista [5, 3, 7]. Escribe el valor que resulta de las siguientes expresiones:
a. datos[2] 
b. datos[-1] 
c. len(datos) 
d. datos[0:2] 
e. 0 in datos 
f. datos + [2, 10, 5] 

datos = [5, 3, 7]
#a = 7
#b = 7
#c = 3
#d = 5, 3, 7
#e = false
#f = [5, 3, 7, 2, 10, 5]
print(datos[2])
print(datos[-1])
print(len(datos))
print(datos[0:2])
print(0 in datos)
print(datos + [2, 10, 5])
"""

"""
Considera que la variable datos se refiere a la lista [5, 3, 7]. Escribe las expresiones que realizan las siguientes tareas:
    a-Reemplazar el valor en la posición 0 en datos con el negativo de ese valor.
    b-Agregar el valor 10 al final de datos.
    c-Insertar el valor 22 en la posición 2 en datos.
    d-Eliminar el valor en la posición 1 en datos.
    e-Agregar los valores en la lista nuevosDatos al final de datos.
    f-Localizar el índice del valor 7 en datos, de forma segura.
    g-Ordenar los valores en los datos.
"""
datos = [5, 3, 7]
# a
datos.pop(0)
print(datos)

datos.insert(0, -5)
print(datos)

#b
datos.append(10)
print(datos)

#c
datos.insert(2, 22)
print(datos)

#d
datos.pop(1)
print(datos)

#e
datosNuevos = [11, 9, 1, 5]
datos.extend(datosNuevos)
print(datos)

#f
print(datos.index(7))

#g 
datos.sort()
print(datos)

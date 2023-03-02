"""
Programa practica2.py
Programa para calcular sueldo neto de un empleado dentro de una empresa.
    -Calcular el sueldo bruto mensual de un empleado de acuerdo con las siguientes indicaciones:
        -Cada empleado tiende un salario por horas laboradas
        
        -Si las horas trabajadas son:
            -Inferiores o iguales a 160:        Se paga el salario por hora indicado
            -Exceden las 160, sin pasar 200:    Las primeras 160 horas se pagan de acuerdo al salario indicado
                                                y las excedentes se pagan como extra a 1.5 del salario normal
            -Exceden las 200:                   Se aplica el criterio anterior y las horas excedentes de 200 
                                                se pagan como doble extra, siendo el doble del salario normal

    -Los impuestos a deducir se calcular con lo siguientes criterios:
        -Sueldo menos o igual a $4,000:         No paga impuesto
        -Hasta $20,000:                         Paga el 20% del excedente de $4,000
        -Hasta $30,000:                         Paga el impuesto anterior mas 25% del excedente de $20,000
        -Arriba de $30,00:                      Paga impuestos anteriores, mas 35% del excedente de $30,00

    -Seguridad social:
        -Todos los empleados                    Pagan 2.5% del sueldo bruto sin importar cantidad

    -Caja de ahorro de la empresa(Si es miembro):
        -Se le descuenta dependiendo del tipo de participacion:
            -Cuota fija:                        $1,000 mensuales
            -Cuota porcentual:                  3% o 5% (del sueldo bruto mensual)

    -Fondo de ahorro para el retiro, ahorro solidario(Si participa):
        -Cuotas:                                1% o 2% (del sueldo bruto mensual)

1. Constantes.

2. Datos de entrada.
    hrs_laboradas
    salario_hr
    participe_ahorro
    participe_retiro

3. Calculos.
    Para el salario (Percepciones):
        -Horas trabajadas inferiores o iguales a 160
            salario_mensualBruto = hrs_laboradas * salario_hr

        -Horas que exceden las 160, sin pasar 200
            hrs_extra         = (hrs_laboradas - 160) 
            salario_mensualBruto = (160 * salario_hr) + hrs_extra * (salario_hr * 1.5) 

        -Horas que exceden las 200
            hrs_dobleExtra    = (hrs_laboradas - 200) 
            salario_mensualBruto = (160 * salario_hr) + 39 * (salario_hr 1.5) + horas_dobleExtra * (salario_hr * 2)
    
    Aportacion de Seguridad Social
        impuesto_SS = salario_mensualBruto * 0.025

    Para los impuestos deducibles en sueldos:
        -Menores o iguales a $4,000
            ¡No pagan impuestos!

        -Hasta $20,000 
            Pagan el 20% del excedente de $4,000
                excedente  = salario_mensualBruto - 4000
                impuestos  = excedente * 0.2
        
        -Hasta $30,000
            Pagan el impuesto anterior y el excedente de $20,000
                excedente  = salario_mensualBruto - 20000
                impuestos  = (16000 * 0.2) + excedente * 0.25
        
        -Arriba de $30,000
            Pagan impuestos anteriores, mas el 35% del excedente de $30,000
                excedente  = salario_mensualBruto - 30000
                impuestos  = (16000 * 0.2) + (10000 * 0.25) + excedente * 0.35

    Para los miembros de la caja de ahorros de la empresa con una cuota porcentual:
        -Con una participacion del sueldo mensual bruto del 3% o 5%
            cajaAhorro = salario_mensualBruto * 0.03
            o
            cajaAhorro = salario_mensualBruto * 0.05

    Para los miembros del fondo de ahorro para el retiro, ahorro solidario:
        -Con una participacion de 1% o 2%
            fondoRetiro = salario_mensualBruto * 0.01
            o
            fondoRetiro = salario_mensualBruto * 0.02

4. Datos de salida.
    -Percepciones 
    -Deducciones
    -Sueldo neto
"""
print(' Programa para calcular salario neto dentro de la empresa' + '\n')
hrs_laboradas    = float(input("Ingrese las horas laboradas del mes: "))
salario_hr       = float(input("Ingrese el salario por hora correspondiente al empleado: $"))
participe_ahorro = input("¿El empleado participa en la caja de ahorro de la empresa? (Si - No): ")
participe_retiro = input("¿El empleado participa en el fondo de ahorro para el retiro? (Si - No): ")

#Estructura para calcular el salario mensual bruto
if hrs_laboradas <= 160:
    salario_mensualBruto = hrs_laboradas * salario_hr
elif hrs_laboradas <= 200:
    hrs_extra            = (hrs_laboradas - 160) 
    salario_mensualBruto = (160 * salario_hr) + (hrs_extra * salario_hr * 1.5)
else:
    hrs_dobleExtra       = (hrs_laboradas - 200) 
    salario_mensualBruto = (160 * salario_hr) + (40 * salario_hr * 1.5) + (hrs_dobleExtra * salario_hr * 2)

#Calculo para aporte de Seguro Social
aporte_SS = salario_mensualBruto * 0.025

#Estructura para calcular impuestos
if salario_mensualBruto <= 4000:
    impuestos  = 0
elif salario_mensualBruto <= 20000:
    excedente  = salario_mensualBruto - 4000
    impuestos  = excedente * 0.2
elif salario_mensualBruto <= 30000:
    excedente  = salario_mensualBruto - 20000
    impuestos  = (16000 * 0.2) + (excedente * 0.25)
else:
    excedente  = salario_mensualBruto - 30000
    impuestos  = (16000 * 0.2) + (10000 * 0.25) + (excedente * 0.35)

#Estructura para calcular cuota en Caja de Ahorro
if participe_ahorro.lower() == 'si':
    tipoCuota = input("\nIndique la cuota que maneja el empleado en la caja de ahorro (Fija o Porcentual): ")
    if tipoCuota.lower() == "fija":
        caja_ahorro = 1000
    else:
        cuotaPorcentual = input("¿Que porcentaje aporta el empleado? (3 o 5): ")
        if cuotaPorcentual == '3':
            caja_ahorro = salario_mensualBruto * 0.03
        else:
            caja_ahorro = salario_mensualBruto * 0.05
else:
    caja_ahorro = 0

#Estructura para calcular aporte para el retiro
if participe_retiro.lower() == 'si':
    tipoRetiro = input("\n¿Con que porcentaje participa el empleado para el retiro? (1 o 2): ")
    if tipoRetiro == '1':
        fondoRetiro = salario_mensualBruto * 0.01
    else:
        fondoRetiro = salario_mensualBruto * 0.02
else:
    fondoRetiro = 0

#Calculo de sueldo neto, despues de deducciones
salario_mensualNeto = salario_mensualBruto - impuestos - caja_ahorro - fondoRetiro - aporte_SS

#Datos de Salida (Percepciones, deducciones y sueldo neto)
print('\n')
print('Las percepciones del empleado fueron de: $' + str(salario_mensualBruto) + ' en el mes\n')
print('Las deducciones correspondientes son las siguientes:')
print('-Impuestos: $' + str(impuestos))
print('-Seguro Social: $' + str(aporte_SS))
if participe_ahorro.lower() == 'si':
    print('-Caja de ahorro: $' + str(round((caja_ahorro), 1)) + '\n')

if participe_retiro.lower() == 'si':
    print('-Ahorro solidario: $' + str(round((fondoRetiro), 1)) + '\n')

print('Salario mensual neto: $' + str(round(salario_mensualNeto, 1)))
print("\n\n~Ivan Javier Gordillo Solis \n~2223028708")
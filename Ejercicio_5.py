    #-------------------------------------------------------------------------------
# Name:        Ejercicio 4
# Created:     26/07/2022
# Copyright:   (c) BadBoy_Deivid 2022
#-------------------------------------------------------------------------------

# Enunciado:
# Programa que solicite al usuario los datos para calcular el área de un Cuadrado (■), finalmente mostrar el resultado en pantalla.

#Declaración de variables
int_Lado = 0
int_Area = 0

# Solicitud de datos
Lado = int(input("Introduzca la medida del lado del cuadrado: "))

int_Area = int_Lado ** 2

print ("El area total del cuadrado es de:  " + str(int_Area))

#Solución 2
#print ("El area del cuadrado es: %d" %(int_Area)
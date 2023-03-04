#-------------------------------------------------------------------------------
# Name:        Ejercicio 6
# Created:     26/07/2022
# Copyright:   (c) BadBoy_Deivid 2022
#-------------------------------------------------------------------------------

#Enunciado:

#Programa que solicite al usuario los datos para calcular el área de un Triángulo (▲), 
#finalmente mostrar el resultado en pantalla.

# Declaración de variables
int_Base = 0
int_Altura = 0
float_Area = 0.0

#Petición de datos
int_Base = int(input("Introduce el valor de la base de triangulo: "))
int_Altura = int(input("Ahora, introduce el valor de la altura del triangulo: "))

float_Area = (int_Base * int_Altura)/2
print ("el área del triangulo es de: %0.2f" %(float_Area))
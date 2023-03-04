#-------------------------------------------------------------------------------
# Name:        Ejercicio 6
# Created:     26/07/2022
# Copyright:   (c) BadBoy_Deivid 2022
#-------------------------------------------------------------------------------

#Enunciado:
# Programa que solicite al usuario los datos para calcular el área de un Círculo (●), 
# finalmente mostrar el resultado en pantalla.

# Declaración de variables
PI = 0
int_radio = 0
float_Area = 0.0

# Solicitud de datos
int_radio = int(input("Introduzca el valor del Radio del circulo"))

# Calculo del Area 
float_Area = PI*(int_radio**2)
print("El área del circulo es de: %0.2f" %(float_Area))
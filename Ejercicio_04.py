#-------------------------------------------------------------------------------
# Name:        Ejercicio 4
# Created:     26/07/2022
# Copyright:   (c) BadBoy_Deivid 2022
#-------------------------------------------------------------------------------

#Enunciado:

#Escribir un programa que lea un entero positivo, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1.

# Declaración de variables
numero = 0
Suma = 0

#inicio del programa
numero = int(input("Introduzca un numero entero, aquí >>>"))

suma = numero * (numero+1) / 2

#Solucion del profesor
#print("La suma desde 1 hasta " + str(numero) + " es " + str(suma))

#Mi solución
print (f"La suma de de los enteros desde 1 hasta {str(numero)} es de {str(suma)}")

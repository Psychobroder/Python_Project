# Ejercicio_diagonal

# Declaracion de variables 
from cmath import sqrt


# a_Cuadrada = 60
a_Cuadrada = int(input("Ingrese la medida de un lado del cuadrado: > "))
# inicio del programa

a = sqrt(a_Cuadrada)

#solucion 1: 
d = a * sqrt(2) 

#Solucion 2: 
d2 = sqrt(2 * (a**2)) 

#Solucion 3: 
d3 = sqrt((a**2) + (a** 2))

print(f"El valor de la diagonal es de: {d.real}")

print(f"El valor de la diagonal es de: {d2.real}")

print(f"El valor de la diagonal es de: {d3.real}")

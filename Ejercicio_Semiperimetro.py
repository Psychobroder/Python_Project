from math import *

#Declaracion de variables
a = 5
b = 6
c = 8 # Lados del triangulo
s = 0.0 # Area del triangulo
t = 0.0

# inicio del programa
t= (a + b + c)/2

s = sqrt(t * (t-a)*(t-b)*(t-c))

print(s)
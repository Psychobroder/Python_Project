# Enunciado: Escribir un programa en el cual se solicite al usuario un número 
# y se imprima la tabla de potencias del 1 al 10 del valor introducido.

# Declaracion de variables
numero = int(input("Ingrese el numero a elevar: "))

for i in range(1,64):
    print(f"{numero} elevado a {i} -> {numero ** i}")

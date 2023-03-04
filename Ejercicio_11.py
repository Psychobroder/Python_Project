# Enunciado:
#Escribir un programa que solicite al usuario un número entero y muestre en pantalla si el número es
#  Positivo (+) o Negativo (-). En caso de que el número sea igual a cero (0) se debe mostrar en pantalla: 
# El número no es Positivo ni Negativo.

#Declaracion de variables
Numero_Neutron = 0

#Declaracion de constantes
ERROR_FORMATO =  "SOLO SE PERMITEN NUMEROS"


# Inicio del Programa
try:
    Numero_Neutron = int(input("Ingrese un numero entero: "))

    if(Numero_Neutron > 0 ):
        print("El numero introducido es Positivo")
    elif(Numero_Neutron < 0):
        print("El numero introducido es negativo")
    else:
        print("El número no es Positivo ni Negativo.")
except:
     print(ERROR_FORMATO)
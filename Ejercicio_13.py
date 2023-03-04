#Enunciado:
#Introducir un número por teclado y que se muestre un mensaje indicando si es par o impar.

#Declaracion de variables
IsPar = 0
#Declaracion de constantes
ERROR_FORMATO =  "SOLO SE PERMITEN NUMEROS"

# Inicio del Programa
try:
    IsPar = int(input("Ingrese un numero > "))
    if(IsPar // 2 == IsPar / 2):
        print("El numero introducido es un numero par")
    else:
        print("El numero introducido es un numero impar")
    
except:
     print(ERROR_FORMATO)
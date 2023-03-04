#Enunciado:
#Introducir un número por teclado y que se muestre un mensaje indicando si es múltiplo de 3.

#Declaracion de variables
IsMultiplo = 0
#Declaracion de constantes
ERROR_FORMATO =  "SOLO SE PERMITEN NUMEROS"

# Inicio del Programa
try:
    IsMultiplo = int(input("Ingrese un numero > "))
    if(IsMultiplo == (IsMultiplo // 3) * 3):
        print(f"El numero {IsMultiplo} es multiplo de 3")
    else:
        print(f"El numero {IsMultiplo} no es un multiplo de 3")
    
except:
     print(ERROR_FORMATO)
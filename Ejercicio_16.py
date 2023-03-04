#Enunciado:
#Escribir un programa que solicite al usuario 3 números, compararlos y decir cual es mayor.

# Declaracion de variables
primer_numero = 0
segundo_numero = 0
tercer_numero = 0

#Declaracion de constantes
ERROR_FORMATO =  "SOLO SE PERMITEN NUMEROS"

try:
    primer_numero = int(input("Ingrese el primer numero"))
    segundo_numero = int(input("Ingrese el segundo numero"))
    tercer_numero = int(input("Ingrese el tercer numero"))

    if(primer_numero > segundo_numero and primer_numero > tercer_numero):
        print(f"El primer numero, {primer_numero}, es el mayor")
    elif(segundo_numero > primer_numero and segundo_numero > tercer_numero):
        print(f"El segundo numero, {segundo_numero}, es el mayor")
    else:
        print(f"El tercer numero, {tercer_numero}, es el mayor")

except:
     print(ERROR_FORMATO)
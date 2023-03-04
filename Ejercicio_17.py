# Enunciado:
# Escribir un programa que solicite al usuario 5 números, compararlos y decir cual es mayor.

# Declaracion de variables
primer_numero  = 0.0
segundo_numero = 0.0
tercer_numero  = 0.0
cuarto_numero  = 0.0
quinto_numero  = 0.0
 
#Declaracion de constantes
ERROR_FORMATO =  "SOLO SE PERMITEN NUMEROS"

# Solicitud de datos
primer_numero  = float(input('Introduce el Primer  numero: '))
segundo_numero = float(input('Introduce el Segundo numero: '))
tercer_numero  = float(input('Introduce el Tercer  numero: '))
cuarto_numero  = float(input('Introduce el Cuarto  numero: '))
quinto_numero  = float(input('Introduce el Quinto  numero: '))

# Inicio del programa
posible_maximo = primer_numero

if (posible_maximo < segundo_numero):
    posible_maximo = segundo_numero
if (posible_maximo < tercer_numero):
    posible_maximo = tercer_numero
if (posible_maximo < cuarto_numero):
    posible_maximo = cuarto_numero
if (posible_maximo < quinto_numero):
    posible_maximo = quinto_numero

#print (f"El numero mayor es: {posible_maximo}")
print ("El numero mayor es: %0.2f" %(posible_maximo))
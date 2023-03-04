# Enunciado:
# Escribir un Programa que solicite al usuario la edad de 2 personas, y diga cuál es mayor.

#Declaracion de variables
int_Edad1,int_Edad2 = 0, 0

#Declaracion de constantes
ERROR_FORMATO =  "SOLO SE PERMITEN NUMEROS"

# Inicio del Programa
try:
    int_Edad1 = int(input("Ingrese la edad de la primera persona > "))
    print("Excelente!")
    int_Edad2 = int(input("Ingrese la edad de la segunda persona > "))

    if(int_Edad1 > int_Edad2):
        print("- La primera persona es mayor!")
    elif(int_Edad1 < int_Edad2):
        print("- La segunda persona es mayor")
    else:
        print("- Ambos tienen la misma edad!")
except:
     print(ERROR_FORMATO)
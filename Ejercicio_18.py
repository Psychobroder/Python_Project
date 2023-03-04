#Enunciado:
# Escribir un programa en el cual Dados 5 números enteros solicitados al usuario, 
# determinar cuál de los 4 números enteros es más cercano al primero.

# Declaración de variables 
int_PrimerNumero = 0
int_SegundoNumero = 0
int_TercerNumero = 0
int_CuartoNumero= 0
int_QuintoNumero= 0
int_Diferencia = 0
int_Comparador = 0
int_MasCercano = 0

#ingreso de Datos
int_PrimerNumero =  int(input("Ingrese el primer número: "))
int_SegundoNumero = int(input("Ingrese el segundo número: "))
int_TercerNumero =  int(input("Ingrese el tercer número: "))
int_CuartoNumero =  int(input("Ingrese el cuarto número: "))
int_QuintoNumero =  int(input("Ingrese el quinto número: "))

#Comparacion
int_MasCercano = int_SegundoNumero

int_Diferencia = int_PrimerNumero - int_SegundoNumero
if (int_Diferencia < 0):
    int_Diferencia = int_Diferencia * (-1)

int_Comparador = int_PrimerNumero - int_TercerNumero
if(int_Comparador < 0):
    int_Comparador = int_Comparador * -1
if (int_Comparador < int_Diferencia):
    int_MasCercano = int_TercerNumero
    int_Diferencia = int_Comparador

int_Comparador = int_PrimerNumero - int_CuartoNumero
if(int_Comparador < 0):
    int_Comparador = int_Comparador * -1
if (int_Comparador < int_Diferencia):
    int_MasCercano = int_CuartoNumero
    int_Diferencia = int_Comparador

int_Comparador = int_PrimerNumero - int_QuintoNumero
if(int_Comparador < 0):
    int_Comparador = int_Comparador * -1
if (int_Comparador < int_Diferencia):
    int_MasCercano =  int_QuintoNumero

print(f"El numero mas cercano a {str(int_PrimerNumero)} es el {str(int_MasCercano)}")
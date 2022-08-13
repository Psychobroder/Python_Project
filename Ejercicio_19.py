# Enunciado: Crear un Algoritmo que permita hallar la solución a una ecuación de primer grado, de la forma: ax + b = 0

#El objetivo es despejar la x y validar los posibles datos para arrojar la respuesta. Al despejar la x tendremos que:x = -b/a
#Por lo tanto tendremos los siguientes escenarios:
#1) Si a es DIFERENTE de 0 (a != 0) la ecuación tiene solución.
#2) Si a es IGUAL a 0 (a == 0) tendremos que:
#Si b es DIFERENTE de 0 (b != 0) la ecuación no tiene solución.
#Si b es IGUAL a 0 (b == 0) la ecuación tiene Infinitas Soluciones.

# Valores para Dibujar la Tabla
ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
MENSAJE_INICIAL = "ECUACIÓN DE PRIMER GRADO: ax + b = 0"

# Declaracion Variables:

a = 2 #Coeficiente principal.

b = 6 #Término Independiente.

x = 0 #Incógnita.

# Formato de Salida Final en Pantalla
Formato_Ecuacion = "ECUACION: {} x + {} = 0"

# LINEA 1: Parte superior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))

# Mensaje Centrado
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))

# LINEA 2: Separador de la tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))

#######################################################################

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
print(CADENA_VACIA.center(ANCHO,RELLENO1))

print(Formato_Ecuacion.format(a,b)) 

print(CADENA_VACIA.center(ANCHO,RELLENO1))

try :
    x = -b/a
    print("Solucion: x = " , x)
except:
    if b != 0:  
        print("La ecuación no tiene solución")
    else :
        print("La ecuación tiene infinitas soluciones")
    
#######################################################################

print(CADENA_VACIA.center(ANCHO,RELLENO1))

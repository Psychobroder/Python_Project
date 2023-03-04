#-------------------------------------------------------------------------------
# Name:        Ejercicio 9
# Created:     26/07/2022
# Copyright:   (c) BadBoy_Deivid 2022
#-------------------------------------------------------------------------------

#Enunciado:
# Un radar común de detección de velocidad de la policía de caminos emite un rayo de microondas a una frecuencia f0. 
# El rayo es reflejado por un automóvil que se aproxima y el rayo reflejado es captado y analizado por la unidad de radar. 
# La frecuencia del rayo reflejado es cambiada ligeramente de f0 a f1 debido al movimiento del automóvil.

# Valores para Dibujar la Tabla
ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
MENSAJE_INICIAL = "RADAR DE VELOCIDAD"

#Declaración de variables
Velocidad = 0.0
Frecuencia0 = 2e-10 
Frecuencia1 = 2.0000004e-10

# Formato de Salida Final en Pantalla
Formato_Respuesta = ">>> La Velocidad es: %0.2f millas/hora."

# Encabezado del Programa
# LINEA 1: Parte superior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
# Mensaje Centrado
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))

#inicio del programa: Calculo de la VELOCIDAD del radar
# velocidad = 6.685x10^8 x (f1 - f0) / (f1 + f0)
Velocidad=6.685e8*(Frecuencia1-Frecuencia0)/(Frecuencia1+Frecuencia0)
    
# LINEA 2: Separador de la tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
# Se muestra el mensaje en Pantalla
print(Formato_Respuesta.center(ANCHO,RELLENO2) %(Velocidad))

# LINEA 3: Parte Inferior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))

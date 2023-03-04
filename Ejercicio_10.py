#Enunciado:

# Un Freelancer desea saber cuánto puede cobrar por su trabajo semanal y mensualmente, 
#para ello solo necesita establecer el precio de su trabajo por hora.
#Se estiman 40 horas de trabajo a la semana.

# Valores para Dibujar la Tabla
ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""

# Declaracion de Constantes
HORAS_SEMANALES = 40
HORAS_MENSUALES = 160

#Mensajes a mostrar
    #Mensaje Inicial
MENSAJE_INICIAL = "CALCULADORA FREELANCER"
    #Mensaje de solicitud de datos
SOLICITAR_PRECIO = ">>> Precio en dolares por hora:"
    #Mensaje en caso de error
ERROR_FORMATO =  "SOLO SE PERMITEN NUMEROS"
    #Formato de salida final en pantalla
Formato_Respuesta = ">>> PAGO SEMANAL: %4.2f\n>>> PAGO MENSUAL: %4.2f"

# Declaracion de variables
Pago_Semanal, Pago_Mensual, Dolares_Hora = 0.0, 0.0,0.0

# Encabezado del Programa
# LINEA 1: Parte superior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
# Mensaje Centrado
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))

# LINEA 2: Separador de la tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
# Se muestra el mensaje en Pantalla
# Inicio del Programa:

try:
    # Solicitud de Datos
    Dolares_Por_Hora   = float(input(SOLICITAR_PRECIO))
 
    # Cálculos para el pago Semanal y Mensual
    Pago_Semanal = Dolares_Por_Hora * HORAS_SEMANALES
    Pago_Mensual = Dolares_Por_Hora * HORAS_MENSUALES
 
    # LINEA 3: Separador de la tabla
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
    # Se muestra el mensaje en Pantalla
    print(Formato_Respuesta %(Pago_Semanal,Pago_Mensual))
 
except ValueError:
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
    print(ERROR_FORMATO.center(ANCHO,RELLENO2))
 
######################################################################
 
# LINEA 4: Parte Inferior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
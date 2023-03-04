#Enunciado: 
# Haz un programa que pida un entero positivo n y almacene en una variable M la matriz identidad de n × n
# (la que tiene unos (1) en la diagonal principal y ceros (0) en el resto de celdas). 
# Imprime la matriz en pantalla.

# Declaracion de Variables:
M = []
longitud = 0
dimension = 0
 
######################################################################
 
# Pedimos la dimensión de la matriz,
dimension = int(input(">>> Dimension de la matriz de tamaño n x n: "))

# Creamos una matriz nula...
for elemento in range(dimension):
        M.append ([0] * dimension)
        M[elemento][elemento] = 1
 
######################################################################
 
print("\n>>> MATRIZ M(%dx%d): %s\n" %(dimension,dimension,M))

# Se imprime cada fila de la matriz

for valor in range(dimension):
    print(M[valor])
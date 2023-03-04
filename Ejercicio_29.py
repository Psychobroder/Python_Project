Matriz = []
Filas = 0
Columnas = 0
print("Creacion de la matriz")
Filas = int(input("Ingrese el numero de filas"))
Columnas = int(input("Ingrese el numero de columnas"))

# Se agregan los elementos a la Matriz
for elemento in range(Filas):
    Matriz.append ([0] * Columnas)

# Longitud de la Matriz
Longitud = len(Matriz)

# Se imprime cada fila de la matriz
for fila in range(Longitud):
    print(">>> FILA %d: %s" %(fila+1, Matriz[fila]))
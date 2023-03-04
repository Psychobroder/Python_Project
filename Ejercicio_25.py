# Enunciado: Escribir un programa que imprima los números pares de forma creciente hasta un número introducido por el usuario.
numero = 0

print("Este programa imprime los numeros pares de forma creciente, introduzca un numero y compruebelo:")

numero = int(input(">>> "))

for i in range(1,numero+1):
    if (i//2)*2 == i:
        print(i)
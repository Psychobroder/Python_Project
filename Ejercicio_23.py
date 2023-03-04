# Enunciado:Escribir un programa que imprima los números pares entre 0 y 200 de forma creciente.

print('Imprimir los numeros pares entre 0 y 200 de forma Creciente')

for i in range(1,201):
    if (i // 2)*2 == i:
        print(i)
# Enunciado:Escribir un programa que imprima los números pares entre el 0 y 200 de forma decreciente.

print('Imprimir los numeros pares entre 0 y 200 de forma Decreciente')

for i in range(201,-1,-1):
    if (i // 2)*2 == i:
        print(i)
#Enunciado:
#Escribir un programa que solicite al usuario una letra y diga si esta es MAYÚSCULA o minúscula.
# La "a" es el número 97. La "A" es el número 65.

Str_Letra = ""

Str_Letra = input("Ingrese una Letra: ")

if(Str_Letra >= 'A' and Str_Letra <= 'Z'):
    print(f"La letra {Str_Letra} es mayuscula")
elif(Str_Letra >= 'a' and Str_Letra <= 'z'):
    print(f"La letra {Str_Letra} es minuscula")
else:
    print("El caracter introducido no es una letra")
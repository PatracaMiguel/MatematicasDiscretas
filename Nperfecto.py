#Programa para saber si un numero N es perfecto
def Perfecto (numero):
    suma = 0
    for i in range(1,numero):
        if numero % i == 0:
            suma += i
    if numero == suma :
        print("El numero es perfecto")
    else: 
        print("El numero no es perfecto")

numero = (int(input("Ingresa un numero ")))
Perfecto(numero)

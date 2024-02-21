#Programa que muestre todos los numeros enteros hasta 

def Limite(Numero):
    for i in range(1,Numero + 1):
        suma = 0
        for j in range (1, i):
            if i % j == 0:
                suma+= j
        if i == suma:
            print(i)

numero = (int(input("Ingresa el numero limite ")))
Limite(numero)

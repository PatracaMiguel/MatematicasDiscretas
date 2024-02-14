#Factores de un numero entero N 

numero = int(input("Ingresa un numero "))
Factor = 1

for factor in range (Factor,numero + 1):
    if numero % Factor == 0:
        print(factor)
        
        
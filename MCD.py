numero1 = int(input("Ingresa un numero "))
numero2 = int(input("Ingresa un numero "))

while numero2 > 0:
    numero1 = numero2
    numero2 = numero1 % numero2

print(numero1) 

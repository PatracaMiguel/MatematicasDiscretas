numero1 = int(input("Ingresa un numero "))
numero2 = int(input("Ingresa un numero "))

while numero2 > 0:
    Res = numero1 % numero1
    numero1 = numero2
    numero2 = Res

print(numero1) 
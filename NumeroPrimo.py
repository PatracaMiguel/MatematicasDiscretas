numero = int(input("Ingrese un numero: "))
z = 0

for x in range(1, numero + 1):
    if numero % x == 0:
        z += 1

if z == 2:
    print("El numero es primo")
else:
    print("El numero no es primo")

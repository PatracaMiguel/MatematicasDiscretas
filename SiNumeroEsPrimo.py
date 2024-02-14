#Solicita un numero y diga si es primo o no 

numero = int(input("Ingrese un numero "))
x = 1
z = 0

while x <= numero:
    if numero % x == 0:
     z = z +1
    x = x +1
if z ==2:
    print("El numero es primo")
else:
    print("El numero no es primo")



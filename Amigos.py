#Programa para saber si 2 numeros son amigos 

n1 = (int(input("Ingresa un numero ")))
n2 = (int(input("Ingresa un numero ")))
suma = 0
suma2 = 0
for i in range(1,n1):
    if n1 % i == 0:
            suma += i

for j in range(1,n2):
    if n2 % j == 0:
            suma2 += j
            
if n1 == suma2 and n2 == suma:
      print("Los numeros son amigos")
else:
      print("Los numeros no son amigos")
lugar = int(input("Lugar de la sucesion "))
for i in range (1,lugar+1):
    print((i - 1)* (-1)**i, end= " ")
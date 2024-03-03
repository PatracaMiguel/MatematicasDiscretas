lugar = int(input("Lugar en la sucesion "))
for i in range(1, lugar + 1):
    print((i - 1) * (-1)**(i + 1),"/", i)
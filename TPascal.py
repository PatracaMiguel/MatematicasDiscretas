def triangulo(filas):
    fila = [1]
    columna = [0]

    for i in range(filas):
        print(fila)
        fila = [ i + d for i,d in zip (fila + columna, columna + fila)]

filas = (int(input("Ingresa las filas ")))
triangulo(filas)
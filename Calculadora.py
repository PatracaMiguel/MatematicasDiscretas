def suma (numero1, numero2):
    return numero1 + numero2 

def resta (numero1, numero2):
    return numero1 - numero2 

def producto (numero1, numero2):
    return numero1 * numero2 

def division (numero1, numero2):
    return numero1 / numero2 


while True :
    print("Calculadora")
    print("\t 0 suma")
    print("\t 1 resta")
    print("\t 2 multiplicación")
    print("\t 3 división")
    print("\t 4 salir")

    seleccion = int( input ("¿Qué operación deseas realizar? "))

    if seleccion >=4 or seleccion<0:
        print("Fin del programa")
        break

    else:
        print("Ingresa los numeros")

        numero1 = int( input())
        numero2 = int( input())

        if seleccion == 0:
            print(suma(numero1,numero2))

        if seleccion == 1:
            print(resta(numero1,numero2))
        
        if seleccion == 2:
            print(producto(numero1,numero2))

        if seleccion == 3:
            print(division(numero1,numero2))
        
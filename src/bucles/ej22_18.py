"""
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
"""

def bucle_numeros(entero):
    suma_num = 0

    while entero != 0:

        if entero > 0:
            suma_num = suma_num + entero
        entero = int(input("Introduce un número: "))


    return suma_num

def main():
    entero = int(input("Introduce un número: "))
    print(bucle_numeros(entero))


if __name__ == "__main__":
    main()


    def bucle_numeros():
    suma_num = 0
    salir = False

    while not salir != 0:
        entero = int(input("Introduce un número: "))
        

        if entero == 0:
            salir = True

    if salir:
        return (suma_num)

    

def main():
    print(bucle_numeros())


if __name__ == "__main__":
    main()
"""
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
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
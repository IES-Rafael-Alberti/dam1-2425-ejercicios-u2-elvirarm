"""
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
"""


def bucle_numeros():
    suma_num = 0
    salir = False

    while not salir != 0:
        entero = int(input("Introduce un número: "))
        suma_num += entero

        if entero == 0:
            salir = True

    if salir:
        return (suma_num)

    

def main():
    print(bucle_numeros())


if __name__ == "__main__":
    main()
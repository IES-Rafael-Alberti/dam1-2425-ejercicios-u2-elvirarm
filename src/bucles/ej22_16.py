"""
Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
"""

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
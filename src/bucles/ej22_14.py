"""
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
"""

def pedir_entero():
    entero = int(input("Introduce un entero: "))
    return entero

def bucle_numeros(entero):
    while entero != 0:
        suma_num = entero + entero
        entero = int(input("Introduce un numero: "))
    if entero == 0:
        print (suma_num)

def main():
    entero = pedir_entero()
    suma_num = bucle_numeros(entero)


if __name__ == "__main__":
    main()
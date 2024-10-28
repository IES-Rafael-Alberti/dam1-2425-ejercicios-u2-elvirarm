"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""


def pedir_entero():
    num = int(input("Introduce un número entero: "))
    return num

def mostrar_impares(num):
    impares = 1
    while impares <= num:
        print(impares)
        impares = impares + 2

def main():
    num = pedir_entero()
    impares = mostrar_impares(num)


if __name__ == "__main__":
    main()
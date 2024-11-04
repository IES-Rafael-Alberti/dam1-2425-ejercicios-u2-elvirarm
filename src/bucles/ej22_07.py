"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""


def tabla_mult():
    for i in range (1,11):
        for n in range (0,11):
            print (f"{i} * {n} = {i*n}")
        print("\n")

def main():
    tabla_mult()

if __name__ == "__main__":
    main()
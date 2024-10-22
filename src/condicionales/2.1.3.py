"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
"""
def pedir_numeros():
    dividendo = float(input("Introduce el dividendo: "))
    divisor = float(input("Introduce el divisor: "))
    return dividendo,divisor

def comprobar_divisor(divisor):
    while divisor == 0:
        divisor = float(input("Error, el divisor no puede ser 0, inténtalo de nuevo: "))
    return divisor

    
    
def hacer_division(dividendo,divisor):
    division = (dividendo/divisor)
    return division


def main():
    dividendo,divisor = pedir_numeros()
    divisor = comprobar_divisor(divisor)
    print(hacer_division(dividendo,divisor))


if __name__ == "__main__":

    main()



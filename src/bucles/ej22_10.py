"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""

def pedir_entero():
    entero = int(input("Introduce un entero: "))
    return entero

def es_primo_basico_2(entero):
    if entero < 2:
        return False
    for i in range(2, entero):
        if entero % i == 0:
            return False
    return True
    

def main():
    entero = pedir_entero()
    if es_primo_basico_2(entero):
        print (f"{entero} es primo")
    else:
        print (f"{entero} no es primo")


if __name__ == "__main__":
    main()



"""
Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
"""

def suma_digitos(entero_positivo):
    suma = 0

    if entero_positivo > 0:
        entero_positivo = str(entero_positivo)
    
    for i in entero_positivo:
        suma += int(i)
    return suma



def main():
    entero_positivo = int(input("Introduce un número entero positivo:"))
    print (suma_digitos(entero_positivo))

if __name__ == "__main__":
    main()
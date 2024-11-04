"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****
"""

def pedir_num():
    num_altura = int(input("Introduce un número: "))
    return num_altura

def piramide(num_altura):
    triangulo = ""
    for i in range (0,num_altura + 1):
        triangulo += "*" * i + "\n"

    return triangulo

def main():
    num_altura = pedir_num()
    print(piramide(num_altura))


if __name__ == "__main__":
    main()
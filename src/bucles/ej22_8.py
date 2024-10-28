"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""

#jajan't, piensa más, no va ni a la de 3.

def pedir_entero():
    num = int(input("Introduzca un entero: "))
    return num

def triangulo (num):
    generar_piramide = ""
    for i in range (1, num + 1, 2):
        generar_piramide += str(i) + " "
        for n in range (i -2, -1, -2):
            generar_piramide += str(n) + " "

        if i != num:
            generar_piramide += "\n"

    return generar_piramide



def main():
    num = pedir_entero()
    print (triangulo(num))


if __name__ == "__main__":
    main()
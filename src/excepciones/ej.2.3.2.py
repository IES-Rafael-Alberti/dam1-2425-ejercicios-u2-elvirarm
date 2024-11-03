"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

def pedir_num():
    error = True
    while error:
        try:
            num = int(input("Introduce un número entero positivo: "))
            if num == 0:
                raise ValueError ("El número debe ser mayor que 0")
            if num < 1:
                raise ValueError ("El número debe ser positivo.")

            error = False
        except ValueError as e:
            print (e)
    return num

def mostrar_impares(num):
    lista = ""
    for i in range (1, num +1):
        if i % 2 != 0 and i < num:
           lista += str(i) + ","
        if i == num:
            lista += str(i)
    print (lista)
    
    
           


def main():
    num = pedir_num()
    mostrar_impares(num)
    
if __name__ == "__main__":
    main()
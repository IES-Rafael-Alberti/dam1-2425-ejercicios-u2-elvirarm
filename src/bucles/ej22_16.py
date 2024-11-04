"""
Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
"""


def leer_numeros():
    numeros = []
    salir = False

    
    while not salir:
       
        num = input("Introduce un número: ")
        if num == "0":
            salir = True
        else:
            num = int(num)
            numeros.append(num)
    return numeros
        
def determinar_mayor(numeros):
    numero_mayor = numeros[0]
    
    for num in numeros:
        if num > numero_mayor:
            numero_mayor = num
    return numero_mayor

def main():
    numeros = leer_numeros()
    numero_mayor = determinar_mayor(numeros)
    print (f"El número mayor que has ingresado es : {numero_mayor}")

if __name__ == "__main__":
    main()
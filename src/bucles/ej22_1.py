"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""

def pedir_palabra():
    palabra = str(input("Introduce una palabra: "))
    return palabra

def repetir_palabra (palabra):
    
    for i in range (10):
        print (palabra)

def main():
    palabra = pedir_palabra()
    palabra = repetir_palabra(palabra)


if __name__ == "__main__":
    main()
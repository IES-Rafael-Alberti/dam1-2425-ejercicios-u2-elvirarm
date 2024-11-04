"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""
 

def pedir_palabra():
    palabra = input("Introduce una palabra: ")
    return palabra

def mostrar_letras(palabra):
    num_letras = len(palabra)
    palabra_reves = ""

    for i in range (num_letras -1, -1, -1):
        palabra_reves += palabra[i] + "\n"
    return palabra_reves
    

    

def main():
    palabra = pedir_palabra()
    print(mostrar_letras(palabra))
    

if __name__ == "__main__":
    main()
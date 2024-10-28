"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

#ARREGLAR PARA QUE IMPRIMA EN UNA SOLA LÍNEA Y PONERLE LAS COMAS

def pedir_entero_positivo():
    entero = int(input("Introduce un número entero positivo: "))
    return entero

def mostrar_numero(entero):
    
    for i in range(entero, -1, -1):
        
        print (f"{i},")

def main():
    entero = pedir_entero_positivo()
    mostrar_numero(entero)

if __name__ == "__main__":
    main()
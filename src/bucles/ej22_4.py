"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

def pedir_entero_positivo():
    entero = int(input("Introduce un número entero positivo: "))
    return entero

def mostrar_numero(entero):
    serie = ""
    for i in range(entero, -1, -1):
        serie += str(i) + ","
    
    print (serie.rstrip(","))

def main():
    entero = pedir_entero_positivo()
    mostrar_numero(entero)

if __name__ == "__main__":
    main()
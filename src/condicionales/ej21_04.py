'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''

def pedir_numero():
    numero = int(input("Introduzca un número: "))
    return numero

def numero_par_impar(numero):
    if numero %2 == 0:
        return "Este número es par."
    else:
        return "Este número es impar."

def main():
    numero = pedir_numero()
    print(numero_par_impar(numero))

if __name__ == "__main__":
    main()
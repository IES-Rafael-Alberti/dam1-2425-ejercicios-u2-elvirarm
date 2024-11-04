"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

def pedir_edad():
    edad = int(input("Introduce tu edad: "))
    return edad

def mostrar_edad(edad):
    for i in range (1,edad + 1):
        print (i)


def main():
    edad = pedir_edad()
    mostrar_edad(edad)

if __name__ == "__main__":
    main()
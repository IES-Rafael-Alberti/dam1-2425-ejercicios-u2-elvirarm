'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''


def pedir_edad():
    edad = int(input("Introduce un número: "))
    return edad

def comprobar_edad(edad):
    if edad <= 18:
        print("Eres menor de edad.")
    else:
        print("Eres mayor de edad.")


def main():
    edad = pedir_edad()
    comprobar_edad(edad)


if __name__ == "__main__":
    main()
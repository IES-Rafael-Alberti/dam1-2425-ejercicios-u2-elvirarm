"""
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
"""

def pedir_edad():
    edad = int(input("Introduce tu edad: "))
    return edad

def comprobar_edad(edad):
    if edad < 4:
        print("Felicidades, puedes entrar gratis.")
    if (edad > 4) and (edad <= 18):
        print("Tienes que pagar 5 euros.")
    if edad > 18:
        print ("Tienes que pagar 10 euros.")


def main():
    edad = pedir_edad()
    comprobar_edad(edad)

if __name__ == "__main__":
    main()
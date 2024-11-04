'''
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
'''


def pedir_edad():
    edad = int(input("Introduzca su edad: "))
    return edad

def pedir_ingresos():
    ingresos = float(input("Introduce tus ingresos mensuales: "))
    return ingresos

def comprobar_tributacion(edad,ingresos):
    if (edad < 16) or (ingresos <= 1000):
        return "No puedes tributar."
    else:
        return "Puedes tributar."

def main():
    edad = pedir_edad()
    ingresos = pedir_ingresos()
    print(comprobar_tributacion (edad,ingresos))


if __name__ == "__main__":
    main()
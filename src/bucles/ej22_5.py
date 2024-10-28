"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# Formula para calcular El capital tras un año.
amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 
"""


def preguntar_datos():
    cant_inversion = float(input("Introduzca la cantidad a invertir: "))
    int_anual = int(input("Introduzca el interés anual: "))
    cant_anios = int(input("Introduzca la cantidad de años: "))
    return cant_inversion, int_anual, cant_anios

def calcular_capital(cant_inversion, int_anual, cant_anios):

    for i in range (1, cant_anios + 1):
        cant_inversion *= 1 + int_anual / 100
        print (f"El capital obtenido en el año {i} es: {cant_inversion:.2f} euros.")

def main():
    cant_inversion, int_anual, cant_anios = preguntar_datos()
    calcular_capital(cant_inversion, int_anual, cant_anios)



if __name__ == "__main__":
    main()
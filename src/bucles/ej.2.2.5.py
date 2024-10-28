"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# Formula para calcular El capital tras un año.
amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 
"""


#COMPROBAR LUEGO, CREO QUE ESTOY HACIENDO LA FÓRMULA MAL 

def preguntar_datos():
    cant_inversion = float(input("Introduzca la cantidad a invertir: "))
    int_anual = int(input("Introduzca el interés anual: "))
    cant_anios = int(input("Introduzca la cantidad de años: "))
    return cant_inversion, int_anual, cant_anios

def calcular_capital(cant_inversion, int_anual, cant_anios):
    capital_anio1 = cant_inversion * (1 + int_anual / 100)
    for i in range (0, cant_anios + 1):
        capital_obtenido = capital_anio1 * cant_anios
    print (capital_obtenido)

def main():
    cant_inversion, int_anual, cant_anios = preguntar_datos()
    calcular_capital(cant_inversion, int_anual, cant_anios)



if __name__ == "__main__":
    main()
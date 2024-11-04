"""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""

def pedir_renta():
    renta_anual = int(input("Introduzca su renta anual: "))
    return renta_anual

def asignar_tipo_impositivo(renta_anual):

    if renta_anual < 10000:
        tipo_impositivo = '5%'

    if (renta_anual == 10000) and (renta_anual < 20000):
        tipo_impositivo = '15%'

    if (renta_anual == 20000) and (renta_anual < 35000):
        tipo_impositivo = '20%'

    if (renta_anual == 35000) and (renta_anual < 60000):
        tipo_impositivo = '30%'

    if renta_anual > 60000:
        tipo_impositivo = '45%'

    return tipo_impositivo


def main():
    renta_anual = pedir_renta()
    tipo_impositivo = asignar_tipo_impositivo(renta_anual)
    print (tipo_impositivo)
    
if __name__ == "__main__":
    main()
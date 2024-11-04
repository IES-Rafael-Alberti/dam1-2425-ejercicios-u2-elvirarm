"""
Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

"""

def pedir_monto():
    monto = float(input("Introduce el monto: "))
    return monto


def gestionar_monto():
    parar = False
    suma_montos = 0
    while not parar:
        monto = pedir_monto()

        if monto == 0:
            parar = True
        elif monto == monto < 0:
            pedir_monto()
        else:
            suma_montos += monto

    if parar:
        if suma_montos > 1000:
            print (f"{suma_montos * 0.1:.2f}")
        else:
            print (f"{suma_montos:.2f}")
    



def main():
    gestionar_monto()

if __name__ == "__main__":
    main()
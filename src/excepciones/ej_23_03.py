"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.
"""

def pedir_numero():
    error = True
    while error:
        try:
            num = int(input("Introduce un número entero positivo: "))

            if num == 0:
                raise ValueError ("El número debe ser mayor que 0")

            if num < 1:
                raise ValueError ("El número debe ser positivo")

            error = False
        except ValueError as e:
            print (e)
        
    return num

def mostrar_cuenta_atras(num):
    acumulador = ""
    for i in range(num, -1, -1):
        if i > 0:
            acumulador += str (i) + " ,"
        else:
            acumulador += str(i)
    print (acumulador)

def main():
    num = pedir_numero()
    mostrar_cuenta_atras(num)




if __name__ == "__main__":
    main()
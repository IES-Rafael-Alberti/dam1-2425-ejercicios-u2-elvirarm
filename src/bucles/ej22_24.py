"""
Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
"""

def pedir_num_mayor_uno():
    num = int(input("Introduce un número (debe ser mayor de 1): "))
    return num

def bucle_num(num):
    while num 

def main():

if __name__ == "__main__":
    main()


"""
def es_primo_basico_2(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def main():
    numero = int(input("Introduzca un número: "))
    if es_primo_basico_2(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

if __name__ == "__main__":
    main()
"""
"""
Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
"""

def pedir_num():
    num = int(input("Introduce un número (debe ser mayor de 1): "))
    return num

def bucle_num():
    parar = False
    cont_num = 0

    
    while not parar:
        num = pedir_num()
        if num == 0:
            parar = True
        if num < 0:
            print ("El número debe ser mayor que 1 si no quieres terminar.")
        else:
            comprobar_primo(num)
            cont_num += 1
    if parar:
        print (f"Hay {cont_num} números primos.")



def comprobar_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def main():
    bucle_num()

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
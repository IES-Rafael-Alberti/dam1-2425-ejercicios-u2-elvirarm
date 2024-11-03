"""
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
"""

def pedir_numeros():
    lista_numeros = []
    salir = False
    
    while not salir:
        

        num = input("Introduce números enteros positivos: ")
        if num == "-1":
            salir = True
        
        else:
            num = int(num)
            suma = 0

            for digito in str(num):
                suma += int(digito) 

            print (f" La suma de los dígitos de {num} es igual a {suma}")

            lista_numeros.append(num)

            #.append se utiliza para agregar el valor () a una lista
    
    return lista_numeros



def contar_pares (lista_numeros):
    num_pares = 0
    for num in lista_numeros:
        if num %2 == 0:
            num_pares += 1
    return num_pares

def main():
    lista_numeros = pedir_numeros()
    num_pares = contar_pares(lista_numeros)
    print (f"Ingresaste {num_pares} números pares.")


if __name__ == "__main__":
    main()
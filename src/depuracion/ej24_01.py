"""

Algoritmo burbuja
Implementación en Python y utiliza el debugger para asegurarte que funciona adecuadamente y entiendes su funcionamiento

"""





def algoritmo_burbuja():
    
    """
    Ordena una lista de enteros que le hemos dado desordenada utilizando el algoritmo burbuja.
    Este algoritmo recorre la lista, comparando los números adyacentes, si es mayor, lo intecambia de posición.
    Esto se va repitiendo hasta que la lista está ordenada correctamente.

    Returns: lista de los números ordenados.
    """
    a = [8, 3, 1, 19, 14]

    n = len(a)

    for i in range(n):
        
        for j in range (0, n-i-1):
            
            if a[j] > a[j+1]:
                
                a[j], a[j+1] = a[j+1], a[j]

    return a


def main():
    a = algoritmo_burbuja()
    print (a)


if __name__ == "__main__":
    main()

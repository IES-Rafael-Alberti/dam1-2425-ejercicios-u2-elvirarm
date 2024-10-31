"""
Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.
"""


def pedir_frase():
    frase = input("Introduce una frase: ").lower()
    return frase

def pedir_letra():
    letra = input("Introduce una letra: ").lower()
    return letra

def comprobar_letra(frase,letra):
    posicion = 0
    letra_encontrada = False

    for busqueda_letra in frase:
        if busqueda_letra == letra:
            print (f"Hay coincidencia en la posición {posicion}")
            letra_encontrada = True 
            return

        else:
            print (f"No hay coincidencia en la posición {posicion}")
            

        posicion += 1

    if not letra_encontrada:
        print ("No se encontraron coincidencias")
   

def main():
    frase = pedir_frase()
    letra = pedir_letra()
    comprobar_letra(frase,letra)

if __name__ == "__main__":
    main()
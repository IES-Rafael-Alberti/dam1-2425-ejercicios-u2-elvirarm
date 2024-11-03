"""
Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
"""

def pedir_frase():
    frase = input("Introduce una frase: ")
    return frase

def separar_frase(frase):
    palabras = frase.split()
    return palabras



def encontrar_palabra_mas_larga(palabras):
    palabra_mas_larga = ""
    longitud_mas_larga = 0

    for i in palabras:
        if len(i) > longitud_mas_larga:
            palabra_mas_larga = i
            longitud_mas_larga = len(i)
    return palabra_mas_larga, longitud_mas_larga

def contar_num_palabras(palabras):
    cantidad_palabras = len(palabras)
    return cantidad_palabras



    


def main():
    frase = pedir_frase()
    palabras = separar_frase(frase)
    palabra_mas_larga, longitud_mas_larga = encontrar_palabra_mas_larga(palabras)
    cantidad_palabras = contar_num_palabras(palabras)
    print(f"La palabra más larga es: '{palabra_mas_larga}' con longitud {longitud_mas_larga}")
    print(f"Cantidad total de palabras: {cantidad_palabras}")


  

if __name__ == "__main__":
    main()
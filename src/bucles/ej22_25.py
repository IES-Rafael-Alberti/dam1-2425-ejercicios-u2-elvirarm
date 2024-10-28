"""
Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
"""

def pedir_frase():
    frase = str(input("Introduce una frase: "))
    return frase

def pedir_letra():
    letra = str(input("Introduce una letra: "))
    return letra
    


def main():
    frase = pedir_frase()
  

if __name__ == "__main__":
    main()
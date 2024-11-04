"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

def pedir_frase():
    frase = input("Introduce una frase: ").lower()
    return frase

def pedir_letra():
    letra = input("Introduce una letra: ").lower()
    return letra

def mostrar_letra(frase, letra):
    num_letras = 0
    for i in frase:
        if i == letra:
            num_letras += 1
    return num_letras
        

        

    
    

def main():
    
    frase = pedir_frase()
    
    letra = pedir_letra()
    
    print(mostrar_letra(frase, letra))

    
if __name__ == "__main__":
    main()
"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""

def eco_usuario():
    
    salir = False

    while not salir:
        texto = input("Escribe algo: ")
        if texto.lower() == "salir":
            salir = True
        else:
            print (texto)
        

def main():
    eco_usuario()

if __name__ == "__main__":
    main()
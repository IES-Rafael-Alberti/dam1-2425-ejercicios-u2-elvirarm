"""
Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
"""

def pedir_numero():
    error = True
    
    while error:
        try:
            num = input ("Introduce un número entero: ")
            
            if(not isinstance(num, int)):
                raise ValueError("La entrada no es correcta: "+num+".")
            
        except ValueError as e:
            print (e)
            


def main():
    pedir_numero()
if __name__ == "__main__":
    main()
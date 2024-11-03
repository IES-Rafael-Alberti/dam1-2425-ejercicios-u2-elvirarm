"""
Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"
"""

def pedir_contrasenia(contrasenia_ok):
    
    error = True
    
    while error:
        try:
            contrasenia = input("Introduce una contraseña: ")
            if contrasenia != contrasenia_ok:
                raise NameError ("Incorrect Password!!")
            error = False
        

        except NameError as e:
            print (e)


def main():
    contrasenia_ok = "password"
    pedir_contrasenia(contrasenia_ok)

if __name__ == "__main__":
    main()
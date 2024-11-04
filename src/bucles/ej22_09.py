"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

def cadena_contrasenia():
    contrasenia_correcta = str ("contraseña")
    return contrasenia_correcta

def pedir_contrasenia (contrasenia_correcta):
    contrasenia_usuario = str(input("Introduzca la contraseña: "))
    return contrasenia_usuario

def comprobar_contrasenia (contrasenia_correcta, contrasenia_usuario):
    while contrasenia_usuario != contrasenia_correcta:
        contrasenia_usuario = str(input("**ERRROR** La contraseña es incorrecta, inténtalo de nuevo: "))
    return contrasenia_usuario

def main():
    contrasenia_correcta = cadena_contrasenia()
    contrasenia_usuario = pedir_contrasenia (contrasenia_correcta)
    contrasenia_usuario = comprobar_contrasenia (contrasenia_correcta, contrasenia_usuario)
    print (contrasenia_usuario)



if __name__ == "__main__":
    main()
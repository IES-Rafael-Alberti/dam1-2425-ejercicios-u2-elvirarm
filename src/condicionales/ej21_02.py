'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''


def pedir_contrasenia():
    
    contrasenia = input("Ingrese contraseña: ")

    return contrasenia

def mostrar_contrasenia(contrasenia_buena, contrasenia):
    
    if  contrasenia == contrasenia_buena:
        return contrasenia
    else:
        return "La contraseña no coincide, inténtalo de nuevo."

def main():
    contrasenia_buena = "contraseña"
    contrasenia = pedir_contrasenia()
    print (mostrar_contrasenia(contrasenia_buena, contrasenia))



if __name__ == "__main__":
    main()
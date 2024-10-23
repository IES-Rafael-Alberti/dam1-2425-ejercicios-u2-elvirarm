'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''


def pedir_contraseña():
    
    contraseña = str(input("Ingrese contraseña: "))

    return contraseña

def mostrar_contraseña(contraseña_buena, contraseña):
    
    if  contraseña == contraseña_buena:
        print(contraseña)
    else:
        print("La contraseña no coincide, inténtalo de nuevo.")

def main():
    contraseña_buena = "contraseña"
    contraseña = pedir_contraseña()
    mostrar_contraseña(contraseña_buena, contraseña)



if __name__ == "__main__":
    main()
"""
Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

"""
def mostrar_menu():
    menu =  "1- comenzar programa \n 2- imprimir listado \n 3- finalizar programa"
    return menu

def selec_opcion(menu):
    opcion = input("Elige una opción (1,2 o 3): ")
    
    while opcion not in menu:
        print (f"**ERROR** La opción tiene que ser 1,2 o 3. \n {mostrar_menu()}")
        print (selec_opcion(menu))
            
    while opcion in menu:
        if opcion == "1" or opcion == "2":
            print (f"Opción correcta \n {mostrar_menu()}")
            print (selec_opcion(menu))
        elif opcion == "3":
            return False



def main():
    menu = mostrar_menu()
    selec_opcion(menu)



if __name__ == "__main__":
    main()
"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""


def pedir_edad():
    edad_correcta = False
    

    while not edad_correcta:
        try:
            edad = None
            edad = int(input("Introduce tu edad: "))
            
            if edad < 1:
                raise ValueError("La edad debe ser un número positivo.")
            if edad == 0:
                raise ValueError ("La edad debe ser un número positivo mayor que cero.")
            if edad > 125:
                raise ValueError ("La edad debe ser un número inferior o igual a 125.")
            edad_correcta = True
    
            
        except ValueError as e:
            if edad is None:
                print (f"*ERROR* El número introducido no es un entero válido. Intentálo de nuevo")
            else:
                print (f"ERROR* {e} Intentalo de nuevo ")
        
    return edad
    
    
   
def mostrar_anios_cumplidos(edad):
    for i in range (1,edad + 1):
        if i== edad:
            print (i)
        else:
            print(i, end= ",")


def main():
    edad = pedir_edad()
    mostrar_anios_cumplidos(edad)
    

if __name__ == "__main__":
    main()
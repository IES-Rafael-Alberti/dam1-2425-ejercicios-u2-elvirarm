"""
Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

"""
def pedir_enteros():
    entero = int(input("Introduce un número entero positivo: "))
    return entero

def gestionar_bucle():
    parar = False
    total_impares = 0
    total_pares = 0
    
    
    while not parar:
        entero = pedir_enteros()

        if entero == 0:
            parar = True

        else:
            num_pares = 0
            num_impares = 0
        
        for digito in str(entero):
            digito = int(digito)
            
            if digito %2 == 0:
                num_pares += 1
                total_pares += 1
            else:
                num_impares += 1
                total_impares += 1
        print (f"El número {entero} tiene {num_pares} dígitos pares y {num_impares} dígitos impares")
    
    
        print (f"EL TOTAL DE LOS DIGITOS PARES son {total_pares} y los impares son {total_impares}")



def main():
    gestionar_bucle()

if __name__ == "__main__":
    main()
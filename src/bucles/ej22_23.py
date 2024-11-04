"""
Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.

Ejemplo de ejecución:
Libro: Los 3 mosqueteros
Libro: Historia de 2 ciudades
Libro: /
Línea completa. Aparecen 2 dígitos numéricos.
Libro: 20000 leguas de viaje submarino
Libro: El señor de los anillos
Libro: /
Línea completa. Aparecen 5 dígitos numéricos.
Libro: 20 años después
Libro: *
Fin. Se leyeron 2 líneas completas.

"""
def contar_numeros_titulos(serie_titulos):

    
    contador = 0
    for caracter in serie_titulos:
        if caracter.isdigit(): 
            contador += 1
    return contador


def introducir_titulos():
    titulo = input("Libro: ")
    return titulo


def main():
   
    serie_titulos =""
    lineas_completas = 0
    titulos = introducir_titulos()
    while not titulos == "*":
        serie_titulos +=  titulos + ","
        titulos = introducir_titulos()

        if titulos == "/":
            lineas_completas += 1
            contar_numeros = contar_numeros_titulos(serie_titulos)
            print(f"Línea completa. Aparecen {contar_numeros} dígitos numéricos.")
            contar_numeros = 0
            serie_titulos =""

    print(f"Se leyeron {lineas_completas} líneas completas.")
        

if __name__ == "__main__":
    main()
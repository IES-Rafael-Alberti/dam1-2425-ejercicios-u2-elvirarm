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

##DARLE VUELTAS
def introducir_titulo():
    titulo = input("Introduce el título de un libro: ")
    return titulo

def leer_libros():
    parar = False
    
    

    while not parar:
        titulo = introducir_titulo()
        if titulo == "*":
            parar = True
        if titulo == "/":
            terminar_linea(titulo)
   

def terminar_linea(titulo):
    cont_num = 0
    for digito in str(titulo):
        if digito.isdigit:
            cont_num += 1
    print (f"En el {titulo} se han ingresado {cont_num} digitos")


def main():
    leer_libros()
    

if __name__ == "__main__":
    main()
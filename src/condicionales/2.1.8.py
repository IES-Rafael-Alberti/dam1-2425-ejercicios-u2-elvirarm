"""
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
"""

def pedir_puntuacion():
    puntuacion = float(input("Escribe los puntos del usuario (0.0, 0.4, 0.6 o más): "))
    return puntuacion


def comprobar_puntuacion(puntuacion):

    while puntuacion == 0.0:
        nivel_rendimiento = 'inaceptable'
        return nivel_rendimiento

    while puntuacion == 0.4:
        nivel_rendimiento = 'aceptable'
        return nivel_rendimiento

    while puntuacion == 0.6 or puntuacion > 0.6:
        nivel_rendimiento = 'meritorio'
        return nivel_rendimiento

    else:
        nivel_rendimiento = float(input("Introduzca un valor válido: "))

    




def dinero_conseguido(nivel_rendimiento,puntuacion):
    if nivel_rendimiento == 'inaceptable':
        dinero_conseguido = 2400 * puntuacion
        return dinero_conseguido
    
    if nivel_rendimiento == 'aceptable':
        dinero_conseguido = 2400 * puntuacion
        return dinero_conseguido
    
    if nivel_rendimiento == 'meritorio':
        dinero_conseguido = 2400 * puntuacion
        return dinero_conseguido

    

def main():
    puntuacion = pedir_puntuacion()
    nivel_rendimiento = comprobar_puntuacion(puntuacion)
    dinero_conseguido(nivel_rendimiento,puntuacion)
    
    print(f"Su nivel de rendimiento es {nivel_rendimiento}, le corresponden {dinero_conseguido(nivel_rendimiento,puntuacion)}euros.")


    

if __name__ == "__main__":
    main()

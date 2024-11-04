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
    if puntuacion == 0.0:
        return 'inaceptable'
    elif puntuacion == 0.4:
        return 'aceptable'
    elif puntuacion >= 0.6:
        return 'meritorio'
    else:
        return None


def dinero_conseguido(nivel_rendimiento, puntuacion):
    return 2400 * puntuacion


def mostrar_mensaje(puntuacion):
    nivel_rendimiento = comprobar_puntuacion(puntuacion)
    
    
    dinero = dinero_conseguido(nivel_rendimiento, puntuacion)
    return f"Su nivel de rendimiento es {nivel_rendimiento}, le corresponden {dinero} euros."


def main():
    puntuacion = pedir_puntuacion()
    print(mostrar_mensaje(puntuacion))


if __name__ == "__main__":
    main()


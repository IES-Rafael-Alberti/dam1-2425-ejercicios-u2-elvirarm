"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""



def opcion_pizza():
    opcion_de_pizza = str(input("¿Quieres que tu pizza sea vegetariana?")).lower
    return opcion_de_pizza

def mostrar_ingredientes(opcion_de_pizza, INGREDIENTES_VEGETARIANOS, INGREDIENTES_NO_VEGETARIANOS):
    if opcion_de_pizza == 'sí':
        print(INGREDIENTES_VEGETARIANOS)

    if opcion_de_pizza == 'no':
        print(INGREDIENTES_NO_VEGETARIANOS)

def elegir_ingredientes():
    ingrediente = str(input("Elige un ingrediente de la lista: "))
    if ingrediente.find(',') or ingrediente.find(' '):
        str(input("Solo puedes elegir un ingrediente"))
    return ingrediente

def pizza_final(ingrediente, INGREDIENTES_VEGETARIANOS, INGREDIENTES_NO_VEGETARIANOS):
    if ingrediente in INGREDIENTES_VEGETARIANOS:
        print (f"Tu pizza es vegetariana y lleva {ingrediente}, mozarella y tomate.")

    if ingrediente in INGREDIENTES_NO_VEGETARIANOS:
        print (f"Tu pizza no es vegetariana y lleva {ingrediente}, moazarrella y tomate.")



def main():

    INGREDIENTES_VEGETARIANOS = 'Pimiento y tofu'
    INGREDIENTES_NO_VEGETARIANOS = 'Peperoni, jamón y salmón'
    opcion_de_pizza = opcion_pizza()
    mostrar_ingredientes(opcion_de_pizza, INGREDIENTES_VEGETARIANOS, INGREDIENTES_NO_VEGETARIANOS)
    ingrediente = elegir_ingredientes()
    pizza_final(ingrediente, INGREDIENTES_VEGETARIANOS, INGREDIENTES_NO_VEGETARIANOS)

if __name__ == "__main__":
    main()
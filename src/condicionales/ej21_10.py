"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

def elegir_tipo_pizza():
    tipo = input("¿Quieres una pizza vegetariana? (sí/no): ").lower()
    if tipo == "sí":
        return True
    else:
        return False

def elegir_ingrediente(vegetariana):
    if vegetariana:
        print("Ingredientes vegetarianos disponibles: Pimiento, Tofu")
        ingrediente = input("Elige un ingrediente: ").lower()
        if ingrediente == "pimiento" or ingrediente == "tofu":
            return ingrediente
    
    else:
        print("Ingredientes no vegetarianos disponibles: Peperoni, Jamón, Salmón")
        ingrediente = input("Elige un ingrediente: ").lower()
        
        if ingrediente in ["peperoni", "jamón", "salmón"]:
            return ingrediente
    
    print("Ingrediente no válido, elige de nuevo.")
    
    return elegir_ingrediente(vegetariana)

def main():
    vegetariana = elegir_tipo_pizza()
    ingrediente = elegir_ingrediente(vegetariana)
    
    if vegetariana:
        tipo_pizza = "vegetariana"
    else:
        tipo_pizza = "no vegetariana"
    
    print(f"Has elegido una pizza {tipo_pizza} con los siguientes ingredientes:")

    print(f"Mozzarella, Tomate y {ingrediente}")

if __name__ == "__main__":
    main()
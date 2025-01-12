# Programa que calcula el área de un círculo basado en el radio proporcionado por el usuario
# Utiliza diferentes tipos de datos (integer, float, string, boolean) y sigue la convención snake_case

import math  # Importamos la biblioteca matemática para usar el valor de PI

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    :param radio: Radio del círculo (float)
    :return: Área del círculo (float)
    """
    return math.pi * radio ** 2

def main():
    # Solicitar al usuario el radio del círculo
    radio = float(input("Ingresa el radio del círculo (en metros): "))

    # Calcular el área utilizando la función
    area = calcular_area_circulo(radio)

    # Mostrar el resultado al usuario
    print(f"El área del círculo con radio {radio} metros es: {area:.2f} metros cuadrados.")

    # Definir un umbral para comparación
    umbral = 50.0  # Float

    # Verificar si el área es mayor que el umbral (boolean)
    es_mayor = area > umbral
    if es_mayor:
        print("El área es mayor que el umbral de 50.0 metros cuadrados.")
    else:
        print("El área no supera el umbral de 50.0 metros cuadrados.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()

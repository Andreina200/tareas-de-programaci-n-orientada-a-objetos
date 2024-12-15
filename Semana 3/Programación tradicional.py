## Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    # Datos simulados en lugar de entrada manual
    temperaturas = [28, 29, 28.8, 29.9, 30, 30, 31]
    print("Temperaturas ingresadas automáticamente:", temperaturas)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Función principal
def main():
    print("Programa de cálculo del promedio semanal de temperaturas (Programación Tradicional)")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

# Ejecución del programa
if __name__ == "__main__":
    main()

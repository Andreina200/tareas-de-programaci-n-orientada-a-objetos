class ClimaSemanal:
    def __init__(self):
        # Datos simulados en lugar de entrada manual
        self.temperaturas = [29, 29, 28, 31, 29, 30, 29]

    # Método para ingresar temperaturas diarias
    def ingresar_temperaturas(self):
        print("Temperaturas ingresadas automáticamente:", self.temperaturas)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

# Clase heredada para mostrar detalles (Ejemplo de herencia)
class ClimaDetallado(ClimaSemanal):
    def mostrar_temperaturas(self):
        print("Temperaturas ingresadas:")
        for dia, temp in enumerate(self.temperaturas, start=1):
            print(f"Día {dia}: {temp:.2f}°C")

# Programa principal
if __name__ == "__main__":
    print("Programa de cálculo del promedio semanal de temperaturas (POO)")
    clima = ClimaDetallado()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    clima.mostrar_temperaturas()
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")


# Clase heredada para mostrar detalles (Ejemplo de herencia)
class ClimaDetallado(ClimaSemanal):
    def mostrar_temperaturas(self):
        print("Temperaturas ingresadas:")
        for dia, temp in enumerate(self.temperaturas, start=1):
            print(f"Día {dia}: {temp:.2f}°C")


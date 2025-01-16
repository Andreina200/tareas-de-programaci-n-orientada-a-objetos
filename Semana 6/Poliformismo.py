# Clase base
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def descripcion(self):
        raise NotImplementedError("Este método debe ser implementado por las clases derivadas.")

# Clase derivada: Coche
class Coche(Vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)
        self.puertas = puertas

    def descripcion(self):
        return f"Soy un coche de la marca {self.marca} con {self.puertas} puertas."

# Clase derivada: Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, marca, tipo):
        super().__init__(marca)
        self.tipo = tipo

    def descripcion(self):
        return f"Soy una bicicleta de la marca {self.marca} para {self.tipo}."

# Clase derivada: Camión
class Camion(Vehiculo):
    def __init__(self, marca, capacidad_toneladas):
        super().__init__(marca)
        self.capacidad_toneladas = capacidad_toneladas

    def descripcion(self):
        return f"Soy un camión de la marca {self.marca} con capacidad de {self.capacidad_toneladas} toneladas."

# Función que demuestra polimorfismo
def mostrar_descripcion(vehiculo):
    print(vehiculo.descripcion())

# Crear instancias de las clases derivadas
if __name__ == "__main__":
    vehiculos = [
        Coche("Toyota", 4),
        Bicicleta("Trek", "montaña"),
        Camion("Volvo", 10),
    ]

    for vehiculo in vehiculos:
        mostrar_descripcion(vehiculo)

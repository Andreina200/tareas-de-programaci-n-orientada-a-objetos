# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado en una clase derivada.")

    def describir(self):
        return f"{self.nombre} tiene {self.edad} años."

# Clase derivada para perros
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau"

    def describir(self):
        return f"{super().describir()} Es un perro de raza {self.raza}."

# Clase derivada para gatos
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        return "Miau"

    def describir(self):
        return f"{super().describir()} Es un gato de color {self.color}."

# Crear instancias de las clases
if __name__ == "__main__":
    perro = Perro("Rex", 5, "Labrador")
    gato = Gato("Luna", 3, "Blanco")

    # Probar métodos
    print(perro.describir())
    print(f"Sonido: {perro.hacer_sonido()}")

    print(gato.describir())
    print(f"Sonido: {gato.hacer_sonido()}")
    


# Clase que representa una habitación en el hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False

    def ocupar(self):
        if not self.ocupada:
            self.ocupada = True
            return True
        return False

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            return True
        return False

# Clase que representa un cliente
class Cliente:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

# Clase que gestiona las reservas
class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion

    def realizar_reserva(self):
        if self.habitacion.ocupar():
            print(f"Reserva realizada para {self.cliente.nombre} en la habitación {self.habitacion.numero}.")
        else:
            print(f"La habitación {self.habitacion.numero} ya está ocupada.")

    def cancelar_reserva(self):
        if self.habitacion.liberar():
            print(f"Reserva cancelada para {self.cliente.nombre}.")
        else:
            print(f"La habitación {self.habitacion.numero} ya estaba libre.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear habitaciones
    habitacion1 = Habitacion(102, "Individual", 100)
    habitacion2 = Habitacion(120, "Doble", 200)

    # Crear cliente
    cliente1 = Cliente("Jose Catillo", "1206385690")

    # Realizar una reserva
    reserva1 = Reserva(cliente1, habitacion1)
    reserva1.realizar_reserva()

    # Intentar reservar la misma habitación
    reserva2 = Reserva(cliente1, habitacion1)
    reserva2.realizar_reserva()

    # Cancelar la reserva
    reserva1.cancelar_reserva()

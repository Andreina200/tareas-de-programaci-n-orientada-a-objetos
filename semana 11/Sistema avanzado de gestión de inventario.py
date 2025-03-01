import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar(self, cantidad=None, precio=None):
        if cantidad is not None:
            self.cantidad = cantidad
        if precio is not None:
            self.precio = precio

    def to_dict(self):
        return vars(self)

    @staticmethod
    def from_dict(data):
        return Producto(**data)


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto

    def eliminar_producto(self, id_producto):
        self.productos.pop(id_producto, None)

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            self.productos[id_producto].actualizar(cantidad, precio)

    def buscar_producto(self, nombre):
        return [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]

    def mostrar_productos(self):
        for p in self.productos.values():
            print(f"ID: {p.id_producto}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")

    def guardar_en_archivo(self, archivo):
        with open(archivo, "w") as f:
            json.dump([p.to_dict() for p in self.productos.values()], f)

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, "r") as f:
                self.productos = {p['id_producto']: Producto.from_dict(p) for p in json.load(f)}
        except FileNotFoundError:
            pass


def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo("inventario.json")

    # Productos iniciales
    for p in [
        Producto("1", "Laptop", 10, 750.99),
        Producto("2", "Mouse", 50, 25.50),
        Producto("3", "Teclado", 30, 45.99),
        Producto("4", "Monitor", 20, 199.99),
        Producto("5", "Silla Gamer", 15, 299.99),
        Producto("6", "Sansung s23 ultra", 10, 300.99),
        Producto("7", "Iphone 14 pro max", 20, 809.99),
        Producto("8", "Iphone 15 pro max", 30, 1040.99),
        Producto("9", "Iphone 16 pro max", 30, 1200.99),

    ]:
        inventario.agregar_producto(p)

    opciones = {
        "1": lambda: inventario.agregar_producto(Producto(
            input("ID: "), input("Nombre: "), int(input("Cantidad: ")), float(input("Precio: ")))),
        "2": lambda: inventario.eliminar_producto(input("ID del producto a eliminar: ")),
        "3": lambda: inventario.actualizar_producto(
            input("ID: "),
            int(c) if (c := input("Nueva cantidad: ")) else None,
            float(p) if (p := input("Nuevo precio: ")) else None),
        "4": lambda: [print(f"ID: {p.id_producto}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}") for
                      p in inventario.buscar_producto(input("Nombre: "))],
        "5": inventario.mostrar_productos,
        "6": lambda: (inventario.guardar_en_archivo("inventario.json"), exit())
    }

    while True:
        print("\n1. Agregar\n2. Eliminar\n3. Actualizar\n4. Buscar\n5. Mostrar\n6. Guardar y salir")
        opciones.get(input("Seleccione opción: "), lambda: print("Opción inválida"))()


if __name__ == "__main__":
    menu()

import os


class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def to_dict(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}\n"


class Inventario:
    FILE_NAME = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        if not os.path.exists(self.FILE_NAME):
            return
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    id, nombre, cantidad, precio = line.strip().split(',')
                    self.productos.append(Producto(id, nombre, int(cantidad), float(precio)))
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al leer el archivo: {e}")

    def guardar_en_archivo(self):
        try:
            with open(self.FILE_NAME, "w") as file:
                for producto in self.productos:
                    file.write(producto.to_dict())
        except (PermissionError) as e:
            print(f"Error al escribir en el archivo: {e}")

    def agregar_producto(self, id, nombre, cantidad, precio):
        if any(prod.id == id for prod in self.productos):
            print("Error: El ID ya existe.")
            return
        nuevo_producto = Producto(id, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        self.guardar_en_archivo()
        print("Producto agregado con éxito.")

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print("Producto eliminado.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id == id:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_en_archivo()
                print("Producto actualizado.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [prod for prod in self.productos if nombre.lower() in prod.nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            inventario.agregar_producto(id, nombre, cantidad, precio)

        elif opcion == "2":
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()

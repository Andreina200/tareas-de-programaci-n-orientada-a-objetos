class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos = (autor, titulo)  # Tupla para autor y título (inmutables)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.datos[1]} por {self.datos[0]} (ISBN: {self.isbn}, Categoría: {self.categoria})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios_registrados = set()  # Conjunto para IDs de usuario únicos
        self.prestamos = {}  # Diccionario para registrar libros prestados (ISBN -> ID de usuario)

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    def eliminar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios_registrados:
            print("El ID de usuario ya está registrado.")
        else:
            self.usuarios_registrados.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario}")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, isbn, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            print("Usuario no registrado.")
            return
        if isbn in self.prestamos:
            print("El libro ya está prestado.")
        elif isbn in self.libros_disponibles:
            usuario.libros_prestados.append(self.libros_disponibles[isbn])
            self.prestamos[isbn] = usuario.id_usuario
            print(f"Libro prestado a {usuario.nombre}: {self.libros_disponibles[isbn]}")
        else:
            print("Libro no encontrado en la biblioteca.")

    def devolver_libro(self, isbn, usuario):
        if isbn in self.prestamos and self.prestamos[isbn] == usuario.id_usuario:
            usuario.libros_prestados = [libro for libro in usuario.libros_prestados if libro.isbn != isbn]
            del self.prestamos[isbn]
            print(f"Libro devuelto: {isbn} por {usuario.nombre}")
        else:
            print("El libro no está prestado a este usuario.")

    def buscar_libro(self, **kwargs):
        resultados = []
        for libro in self.libros_disponibles.values():
            if ("titulo" in kwargs and kwargs["titulo"].lower() in libro.datos[1].lower()) or \
               ("autor" in kwargs and kwargs["autor"].lower() in libro.datos[0].lower()) or \
               ("categoria" in kwargs and kwargs["categoria"].lower() == libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, usuario):
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f"  - {libro}")
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")


# Pruebas del sistema
biblioteca = Biblioteca()
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "1234567890")
libro2 = Libro("El principito", "Antoine de Saint-Exupéry", "Fábula", "0987654321")
libro3 = Libro("1984", "George Orwell", "Distopía", "1122334455")
libro4 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", "6677889900")
usuario1 = Usuario("Julio Castillo", "U001")
usuario2 = Usuario("Victoria Lamilla", "U002")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)

biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)
biblioteca.prestar_libro("1234567890", usuario1)
biblioteca.prestar_libro("0987654321", usuario2)
biblioteca.listar_libros_prestados(usuario1)

biblioteca.devolver_libro("1234567890", usuario1)
biblioteca.listar_libros_prestados(usuario1)

print("\nBúsqueda por título: ", biblioteca.buscar_libro(titulo="principito"))

class ConexionServidor:
    def __init__(self, servidor, puerto):
        """
        Constructor de la clase ConexionServidor.
        Inicializa la conexión al servidor.

        :param servidor: Dirección del servidor.
        :param puerto: Puerto para la conexión.
        """
        self.servidor = servidor
        self.puerto = puerto
        self.conectado = False
        self.conectar()

    def conectar(self):
        """
        Simula la conexión al servidor.
        """
        self.conectado = True
        print(f"Conectado al servidor {self.servidor} en el puerto {self.puerto}.")

    def enviar_datos(self, datos):
        """
        Simula el envío de datos al servidor.

        :param datos: Datos a enviar al servidor.
        """
        if self.conectado:
            print(f"Enviando datos al servidor {self.servidor}: {datos}")
        else:
            print("Error: No hay conexión establecida.")

    def __del__(self):
        """
        Destructor de la clase ConexionServidor.
        Simula la desconexión del servidor.
        """
        if self.conectado:
            self.conectado = False
            print(f"Desconectado del servidor {self.servidor}.")


# Programa sobre el uso de constructores y destructores
if __name__ == "__main__":
    # Crear una conexión al servidor
    conexion = ConexionServidor("191.0.0.1", 8080)

    # Enviar datos al servidor
    conexion.enviar_datos("Hola, este es un mensaje para el servidor.")

    # Eliminar manualmente el objeto para demostrar el destructor
    del conexion

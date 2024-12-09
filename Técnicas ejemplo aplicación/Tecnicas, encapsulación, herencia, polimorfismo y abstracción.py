# Clase base con encapsulación y métodos generales
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self._nombre = nombre
        self._fuerza = fuerza
        self._inteligencia = inteligencia
        self._defensa = defensa
        self._vida = vida

    # Métodos para la encapsulación
    def get_nombre(self):
        return self._nombre

    def atributos(self):
        print(f"{self._nombre}:")
        print(f"· Fuerza: {self._fuerza}")
        print(f"· Inteligencia: {self._inteligencia}")
        print(f"· Defensa: {self._defensa}")
        print(f"· Vida: {self._vida}")

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self._fuerza += fuerza
        self._inteligencia += inteligencia
        self._defensa += defensa

    def esta_vivo(self):
        return self._vida > 0

    def morir(self):
        self._vida = 0
        print(f"{self._nombre} ha muerto")

    # Método abstracto para calcular el daño (se redefinirá en las subclases)
    def daño(self, enemigo):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo._vida -= daño
        print(f"{self._nombre} realizó {daño} puntos de daño a {enemigo.get_nombre()}")
        if enemigo.esta_vivo():
            print(f"Vida restante de {enemigo.get_nombre()}: {enemigo._vida}")
        else:
            enemigo.morir()


# Clase Guerrero que hereda de Personaje
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self._espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10: "))
        if opcion == 1:
            self._espada = 8
        elif opcion == 2:
            self._espada = 10
        else:
            print("Opción inválida. No se cambió el arma.")

    def atributos(self):
        super().atributos()
        print(f"· Espada: {self._espada}")

    def daño(self, enemigo):
        return self._fuerza * self._espada - enemigo._defensa


# Clase Mago que hereda de Personaje
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self._libro = libro

    def mejorar_libro(self, nivel):
        self._libro += nivel
        print(f"{self._nombre} mejoró su libro. Nivel actual: {self._libro}")

    def atributos(self):
        super().atributos()
        print(f"· Libro: {self._libro}")

    def daño(self, enemigo):
        return self._inteligencia * self._libro - enemigo._defensa


# Función de combate que utiliza polimorfismo
def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\nTurno {turno}")
        jugador_1.atacar(jugador_2)
        if jugador_2.esta_vivo():
            jugador_2.atacar(jugador_1)
        turno += 1

    # Resultado del combate
    if jugador_1.esta_vivo():
        print(f"\n¡{jugador_1.get_nombre()} ha ganado!")
    elif jugador_2.esta_vivo():
        print(f"\n¡{jugador_2.get_nombre()} ha ganado!")
    else:
        print("\nEl combate terminó en empate.")


# Creación de personajes
personaje_1 = Guerrero("Jose", 20, 15, 4, 120, 3)
personaje_2 = Mago("Andreina", 20, 15, 4, 100, 3)

# Mostrar atributos iniciales
personaje_1.atributos()
personaje_2.atributos()

# Realizar combate
combate(personaje_1, personaje_2)

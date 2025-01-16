class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        if not titular or not isinstance(titular, str):
            raise ValueError("El titular debe ser un nombre válido.")
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser positiva.")
        self.__saldo += cantidad
        print(f"Depósito realizado: ${cantidad}. Saldo actual: ${self.__saldo}.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.__saldo:
            raise ValueError("Fondos insuficientes.")
        self.__saldo -= cantidad
        print(f"Retiro realizado: ${cantidad}. Saldo actual: ${self.__saldo}.")

    def obtener_saldo(self):
        return self.__saldo

    def mostrar_informacion(self):
        return f"Titular: {self.__titular}, Saldo: ${self.__saldo}"

    # Metodo para transferencias entre cuentas
    def transferir(self, otra_cuenta, cantidad):
        if not isinstance(otra_cuenta, CuentaBancaria):
            raise ValueError("El destinatario debe ser una instancia de CuentaBancaria.")
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser positiva.")
        if cantidad > self.__saldo:
            raise ValueError("Fondos insuficientes para la transferencia.")
        self.retirar(cantidad)
        otra_cuenta.depositar(cantidad)
        print(f"Transferencia realizada: ${cantidad} a {otra_cuenta.__titular}.")
if __name__ == "__main__":
    cuenta1 = CuentaBancaria("Juan Pérez", 1000)
    cuenta2 = CuentaBancaria("María López", 500)

    print(cuenta1.mostrar_informacion())
    print(cuenta2.mostrar_informacion())

    cuenta1.depositar(300)
    cuenta1.retirar(200)

    cuenta1.transferir(cuenta2, 400)

    print(cuenta1.mostrar_informacion())
    print(cuenta2.mostrar_informacion())

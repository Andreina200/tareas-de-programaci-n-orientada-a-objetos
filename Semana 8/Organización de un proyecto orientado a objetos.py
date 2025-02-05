import os


def mostrar_codigo(ruta_script):
    """Lee y muestra el contenido del archivo"""
    if not os.path.isfile(ruta_script):
        print(f" El archivo no se encontró: {ruta_script}")
        return

    try:
        with open(ruta_script, "r", encoding="utf-8") as archivo:
            print(f"\n--- Código de {os.path.basename(ruta_script)} ---\n")
            print(archivo.read())
    except Exception as e:
        print(f" Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    """Muestra el menú con los scripts disponibles y permite seleccionarlos"""

    # 🔹 Ruta base del proyecto (ajusta esta línea si es necesario)
    ruta_base = r"C:\Users\ORTEL\OneDrive - Universidad Estatal Amazónica\tareas-de-programaci-n-orientada-a-objeto"

    # 🔹 Diccionario con las opciones del menú
    opciones = {
        "1": os.path.join(ruta_base, "Semana 3", "POO.py"),
        "2": os.path.join(ruta_base, "Semana 3", "Programación tradicional.py"),
        "3": os.path.join(ruta_base, "Semana 4", "EjemplosMundoReal_POO.py"),
        "4": os.path.join(ruta_base, "Semana 5", "Tipos de datos,identificadores.py"),
        "5": os.path.join(ruta_base, "Semana 6", "Aplicación de conceptos POO.py"),
        "6": os.path.join(ruta_base, "Semana 6", "Encapsulación.py"),
        "7": os.path.join(ruta_base, "Semana 6", "Polimorfismo.py"),
        "8": os.path.join(ruta_base, "Semana 7", "Constructores y destructores.py"),
        "9": os.path.join(ruta_base, "Semana 8", "Organización de un proyecto orientado a objetos.py"),
        "10": os.path.join(ruta_base, "Técnicas ejemplo aplicación",
                           "Tecnicas, encapsulación, herencia, polimorfismo y abstracción.py"),
    }

    while True:
        print("\n*** Menú Principal - Dashboard ***")
        for key, ruta in opciones.items():
            print(f"{key} - {ruta.replace(ruta_base, '').strip(os.sep)}")  # Muestra solo la parte relativa

        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == "0":
            break
        elif eleccion in opciones:
            mostrar_codigo(opciones[eleccion])
        else:
            print(" Opción no válida. Intenta de nuevo.")


# Ejecutar el menú solo si el script es el principal
if __name__ == "__main__":
    mostrar_menu()


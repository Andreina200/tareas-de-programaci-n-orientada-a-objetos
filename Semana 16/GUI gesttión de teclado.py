import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea
def agregar_tarea():
    tarea = entrada_tarea.get()  # Obtiene el texto del campo de entrada
    if tarea:  # Solo agregar si el campo no está vacío
        lista_tareas.insert(tk.END, tarea)  # Añade la tarea a la lista
        entrada_tarea.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        messagebox.showwarning("Entrada Vacía", "Por favor, ingrese una tarea.")

# Función para marcar una tarea como completada
def marcar_completada():
    tarea_seleccionada = lista_tareas.curselection()  # Obtiene la tarea seleccionada
    if tarea_seleccionada:  # Asegura que haya una tarea seleccionada
        tarea = lista_tareas.get(tarea_seleccionada)  # Obtiene el texto de la tarea
        tarea_completada = f"✔️ {tarea}"  # Añade un símbolo de tarea completada
        lista_tareas.delete(tarea_seleccionada)  # Elimina la tarea de la lista
        lista_tareas.insert(tarea_seleccionada, tarea_completada)  # Inserta la tarea como completada
    else:
        messagebox.showwarning("Seleccionar Tarea", "Por favor, seleccione una tarea.")

# Función para eliminar una tarea
def eliminar_tarea():
    tarea_seleccionada = lista_tareas.curselection()  # Obtiene la tarea seleccionada
    if tarea_seleccionada:  # Asegura que haya una tarea seleccionada
        lista_tareas.delete(tarea_seleccionada)  # Elimina la tarea de la lista
    else:
        messagebox.showwarning("Seleccionar Tarea", "Por favor, seleccione una tarea.")

# Función para cerrar la aplicación
def cerrar_app(event=None):
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Campo de entrada para escribir nuevas tareas
entrada_tarea = tk.Entry(root, width=50)
entrada_tarea.pack(pady=10)

# Botón para añadir tarea
boton_agregar = tk.Button(root, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

# Lista para mostrar las tareas
lista_tareas = tk.Listbox(root, width=50, height=10)
lista_tareas.pack(pady=10)

# Botones para marcar como completada y eliminar tarea
boton_completada = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
boton_completada.pack(pady=5)

boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Atajos de teclado
root.bind('<Return>', lambda event: agregar_tarea())  # "Enter" para agregar tarea
root.bind('<c>', lambda event: marcar_completada())  # "C" para marcar como completada
root.bind('<Delete>', lambda event: eliminar_tarea())  # "Delete" para eliminar tarea
root.bind('<d>', lambda event: eliminar_tarea())  # "D" para eliminar tarea
root.bind('<Escape>', cerrar_app)  # "Escape" para cerrar la aplicación

# Inicia la aplicación
root.mainloop

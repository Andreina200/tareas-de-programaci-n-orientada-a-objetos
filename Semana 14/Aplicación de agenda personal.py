# Previo a ejecutar el programa es necesario instalar el componente tkcalendar
# Comando para instalar desde la consola o terminal
# pip install tkcalendar

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry

# Función para agregar un evento
def agregar_evento():
    fecha = entry_fecha.get_date()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        entry_hora.delete(0, 'end')
        entry_descripcion.delete(0, 'end')
    else:
        messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")

# Función para eliminar un evento seleccionado
def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal")

# Crear Frames para organizar la interfaz
frame_lista = tk.Frame(root)
frame_lista.pack(padx=10, pady=10)

frame_entrada = tk.Frame(root)
frame_entrada.pack(padx=10, pady=10)

frame_botones = tk.Frame(root)
frame_botones.pack(padx=10, pady=10)

# Lista de eventos (TreeView)
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Campos de entrada
label_fecha = tk.Label(frame_entrada, text="Fecha:")
label_fecha.grid(row=0, column=0, padx=5, pady=5)
entry_fecha = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

label_hora = tk.Label(frame_entrada, text="Hora:")
label_hora.grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

label_descripcion = tk.Label(frame_entrada, text="Descripción:")
label_descripcion.grid(row=2, column=0, padx=5, pady=5)
entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Botones
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.pack(side="left", padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.pack(side="left", padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=root.quit)
btn_salir.pack(side="left", padx=5)

# Ejecutar la aplicación
root.mainloop(
import tkinter as tk
from tkinter import messagebox

def agregar_dato():
    dato = entry.get()
    if dato:
        lista.insert(tk.END, dato)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingrese un dato antes de agregar.")

def limpiar_datos():
    lista.delete(0, tk.END)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Mini agenda")
root.geometry("400x300")
root.configure(bg="pink")

# Creación de componentes GUI
label = tk.Label(root, text="Ingrese un dato:", bg="pink")
label.pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

btn_agregar = tk.Button(root, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

lista = tk.Listbox(root, width=50, height=10)
lista.pack(pady=5)

btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar_datos)
btn_limpiar.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
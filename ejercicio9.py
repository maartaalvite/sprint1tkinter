import tkinter as tk
from tkinter import messagebox

def abrir_archivo():
    messagebox.showinfo("Abrir", "Función abrir archivo")

def salir_aplicacion():
    root.quit()

def acerca_de():
    messagebox.showinfo("Acerca de", "Aplicación de ejemplo con Tkinter\nEjercicio 9 - Menu")

# Crear ventana principal
root = tk.Tk()
root.title("Ejercicio 9 - Menu")
root.geometry("400x300")

# Crear la barra de menú principal
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

# Menú Archivo
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir_aplicacion)

# Menú Ayuda
menu_ayuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)

# Contenido principal de la ventana
etiqueta = tk.Label(
    root,
    text="Usa los menús en la parte superior",
    font=("Arial", 12),
    pady=50
)
etiqueta.pack()

# Ejecutar aplicación
root.mainloop()
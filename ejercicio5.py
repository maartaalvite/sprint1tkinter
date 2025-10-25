import tkinter as tk

def cambiar_color():
    color_seleccionado = var_color.get()
    root.config(bg=color_seleccionado)

# Crear ventana principal
root = tk.Tk()
root.title("Ejercicio 5 - Radiobutton")
root.geometry("300x200")
root.config(bg="white")

# Variable de control
var_color = tk.StringVar()
var_color.set("white")

# Título
titulo = tk.Label(
    root,
    text="Elige tu color favorito:",
    font=("Arial", 12),
    bg="white"
)
titulo.pack(pady=20)

# Radiobutton para Rojo
radio_rojo = tk.Radiobutton(
    root,
    text="Rojo",
    variable=var_color,
    value="red",
    command=cambiar_color,
    font=("Arial", 10),
    bg="white"
)
radio_rojo.pack(pady=5)

# Radiobutton para Verde
radio_verde = tk.Radiobutton(
    root,
    text="Verde",
    variable=var_color,
    value="green",
    command=cambiar_color,
    font=("Arial", 10),
    bg="white"
)
radio_verde.pack(pady=5)

# Radiobutton para Azul
radio_azul = tk.Radiobutton(
    root,
    text="Azul",
    variable=var_color,
    value="blue",
    command=cambiar_color,
    font=("Arial", 10),
    bg="white"
)
radio_azul.pack(pady=5)

# Ejecutar aplicación
root.mainloop()
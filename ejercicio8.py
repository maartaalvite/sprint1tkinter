import tkinter as tk

def mostrar_contenido():
    texto = entry_contenido.get()
    etiqueta_resultado.config(text=f"Contenido: {texto}")

def borrar_contenido():
    entry_contenido.delete(0, tk.END)
    etiqueta_resultado.config(text="Contenido: ")

# Crear ventana principal
root = tk.Tk()
root.title("Ejercicio 8 - Frame")
root.geometry("400x300")

# Frame superior
frame_superior = tk.Frame(root, bg="lightgray", padx=10, pady=10)
frame_superior.pack(fill="x", padx=10, pady=10)

# Widgets en el frame superior
etiqueta_instruccion = tk.Label(
    frame_superior,
    text="Ingresa texto:",
    bg="lightgray",
    font=("Arial", 10)
)
etiqueta_instruccion.grid(row=0, column=0, padx=5, pady=5)

entry_contenido = tk.Entry(
    frame_superior,
    width=20,
    font=("Arial", 10)
)
entry_contenido.grid(row=0, column=1, padx=5, pady=5)

etiqueta_resultado = tk.Label(
    frame_superior,
    text="Contenido: ",
    bg="lightgray",
    font=("Arial", 10)
)
etiqueta_resultado.grid(row=1, column=0, columnspan=2, pady=5)

# Frame inferior
frame_inferior = tk.Frame(root, bg="lightblue", padx=10, pady=10)
frame_inferior.pack(fill="x", padx=10, pady=10)

# Botones en el frame inferior
boton_mostrar = tk.Button(
    frame_inferior,
    text="Mostrar Contenido",
    command=mostrar_contenido,
    font=("Arial", 10)
)
boton_mostrar.grid(row=0, column=0, padx=10, pady=10)

boton_borrar = tk.Button(
    frame_inferior,
    text="Borrar Contenido",
    command=borrar_contenido,
    font=("Arial", 10)
)
boton_borrar.grid(row=0, column=1, padx=10, pady=10)

# Ejecutar aplicación
root.mainloop()
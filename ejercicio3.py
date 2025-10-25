import tkinter as tk


def saludar_usuario():
    # Obtener el texto de la entrada
    nombre = entrada_nombre.get()

    # Mostrar saludo personalizado
    if nombre.strip():  # Verificamos que no esté vacío
        etiqueta_saludo.config(text=f"¡Hola, {nombre}!")
    else:
        etiqueta_saludo.config(text="Por favor, escribe tu nombre")


# Crear ventana principal
root = tk.Tk()
root.title("Ejercicio 3 - Entry")
root.geometry("400x250")

# Instrucciones
etiqueta_instrucciones = tk.Label(
    root,
    text="Escribe tu nombre:",
    font=("Arial", 12)
)
etiqueta_instrucciones.pack(pady=20)

# Campo de entrada (Entry)
entrada_nombre = tk.Entry(
    root,
    width=30,
    font=("Arial", 11)
)
entrada_nombre.pack(pady=10)

# Botón para saludar
boton_saludar = tk.Button(
    root,
    text="Saludar",
    command=saludar_usuario,
    bg="lightgreen",
    font=("Arial", 10)
)
boton_saludar.pack(pady=10)

# Etiqueta para mostrar el saludo
etiqueta_saludo = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    fg="darkblue"
)
etiqueta_saludo.pack(pady=20)

# Ejecutar aplicación
root.mainloop()
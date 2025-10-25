import tkinter as tk

def cambiar_texto():
    etiqueta3.config(text="¡Texto cambiado!")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 1 - Labels")
root.geometry("400x200")

# Etiqueta 1 - Mensaje de bienvenida
etiqueta1 = tk.Label(root, text="¡Bienvenido a Tkinter!", font=("Arial", 14))
etiqueta1.pack(pady=10)

# Etiqueta 2 - Nombre completo
etiqueta2 = tk.Label(root, text="Tu Nombre Completo", font=("Arial", 12))
etiqueta2.pack(pady=5)

# Etiqueta 3 - Texto que va a cambiar
etiqueta3 = tk.Label(root, text="Texto original", font=("Arial", 12), fg="blue")
etiqueta3.pack(pady=5)

# Botón para cambiar el texto
boton = tk.Button(root, text="Cambiar Texto", command=cambiar_texto)
boton.pack(pady=10)

# Ejecutar la app
root.mainloop()
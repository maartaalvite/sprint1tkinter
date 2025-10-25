import tkinter as tk

def mostrar_mensaje():
    etiqueta.config(text="¡Has presionado el botón de mensaje!")

def cerrar_aplicacion():
    root.quit()  # Cierra la aplicación

# Crear ventana principal
root = tk.Tk()
root.title("Ejercicio 2 - Botones")
root.geometry("400x200")

# Etiqueta para mostrar mensajes
etiqueta = tk.Label(root, text="Presiona un botón", font=("Arial", 12))
etiqueta.pack(pady=20)

# Botón 1: Mostrar mensaje
boton_mensaje = tk.Button(
    root,
    text="Mostrar Mensaje",
    command=mostrar_mensaje,
    bg="lightblue",
    font=("Arial", 10)
)
boton_mensaje.pack(pady=10)

# Botón 2: Cerrar aplicación
boton_cerrar = tk.Button(
    root,
    text="Cerrar",
    command=cerrar_aplicacion,
    bg="lightcoral",
    font=("Arial", 10)
)
boton_cerrar.pack(pady=10)

# Ejecutar aplicación
root.mainloop()
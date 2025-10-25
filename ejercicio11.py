import tkinter as tk

def actualizar_valor(valor):
    etiqueta_valor.config(text=f"Valor: {valor}")

# Crear ventana principal
root = tk.Tk()
root.title("Ejercicio 11 - Scale")
root.geometry("400x200")

# Título
titulo = tk.Label(
    root,
    text="Selecciona un valor:",
    font=("Arial", 12)
)
titulo.pack(pady=20)

# Barra deslizante (Scale)
scale = tk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    length=300,
    command=actualizar_valor,
    font=("Arial", 10)
)
scale.pack(pady=10)

# Etiqueta para mostrar el valor
etiqueta_valor = tk.Label(
    root,
    text="Valor: 0",
    font=("Arial", 12, "bold"),
    fg="blue"
)
etiqueta_valor.pack(pady=20)

# Ejecutar aplicación
root.mainloop()
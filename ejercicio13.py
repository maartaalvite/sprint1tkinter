import tkinter as tk

def dibujar_circulo(event):
    x = event.x
    y = event.y
    radio = 20
    canvas.create_oval(x-radio, y-radio, x+radio, y+radio, fill="blue", outline="black")

def limpiar_canvas(event):
    canvas.delete("all")

# Crear ventana principal
root = tk.Tk()
root.title("Ejercicio 13 - Eventos de Teclado y Ratón")
root.geometry("500x400")

# Instrucciones
instrucciones = tk.Label(
    root,
    text="Haz clic en el canvas para dibujar círculos. Presiona 'c' para limpiar.",
    font=("Arial", 10),
    pady=10
)
instrucciones.pack()

# Canvas para dibujar
canvas = tk.Canvas(
    root,
    width=450,
    height=300,
    bg="white"
)
canvas.pack(pady=10)

# Vincular eventos
canvas.bind("<Button-1>", dibujar_circulo)  # Clic izquierdo
root.bind("<KeyPress-c>", limpiar_canvas)   # Tecla c

# Asegurar que la ventana captura los eventos de teclado
root.focus_set()

# Ejecutar aplicación
root.mainloop()
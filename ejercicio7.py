import tkinter as tk


def dibujar_figuras():
    # Limpiar el canvas
    canvas.delete("all")

    # Obtener coordenadas del rectángulo
    try:
        x1_rect = int(entry_rect_x1.get())
        y1_rect = int(entry_rect_y1.get())
        x2_rect = int(entry_rect_x2.get())
        y2_rect = int(entry_rect_y2.get())

        # Dibujar rectángulo
        canvas.create_rectangle(x1_rect, y1_rect, x2_rect, y2_rect, outline="red", width=2)
    except ValueError:
        pass

    # Obtener coordenadas del círculo
    try:
        x1_circ = int(entry_circ_x1.get())
        y1_circ = int(entry_circ_y1.get())
        x2_circ = int(entry_circ_x2.get())
        y2_circ = int(entry_circ_y2.get())

        # Dibujar círculo (óvalo)
        canvas.create_oval(x1_circ, y1_circ, x2_circ, y2_circ, outline="blue", width=2)
    except ValueError:
        pass


# Crear ventana principal
root = tk.Tk()
root.title("Ejercicio 7 - Canvas")
root.geometry("500x500")

# Frame para los controles
frame_controles = tk.Frame(root)
frame_controles.pack(pady=10)

# Controles para el rectángulo
tk.Label(frame_controles, text="Rectángulo (x1 y1 x2 y2):", font=("Arial", 10)).grid(row=0, column=0, padx=5)

entry_rect_x1 = tk.Entry(frame_controles, width=5)
entry_rect_x1.grid(row=0, column=1, padx=2)
entry_rect_x1.insert(0, "50")

entry_rect_y1 = tk.Entry(frame_controles, width=5)
entry_rect_y1.grid(row=0, column=2, padx=2)
entry_rect_y1.insert(0, "50")

entry_rect_x2 = tk.Entry(frame_controles, width=5)
entry_rect_x2.grid(row=0, column=3, padx=2)
entry_rect_x2.insert(0, "150")

entry_rect_y2 = tk.Entry(frame_controles, width=5)
entry_rect_y2.grid(row=0, column=4, padx=2)
entry_rect_y2.insert(0, "100")

# Controles para el círculo
tk.Label(frame_controles, text="Círculo (x1 y1 x2 y2):", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5)

entry_circ_x1 = tk.Entry(frame_controles, width=5)
entry_circ_x1.grid(row=1, column=1, padx=2)
entry_circ_x1.insert(0, "200")

entry_circ_y1 = tk.Entry(frame_controles, width=5)
entry_circ_y1.grid(row=1, column=2, padx=2)
entry_circ_y1.insert(0, "50")

entry_circ_x2 = tk.Entry(frame_controles, width=5)
entry_circ_x2.grid(row=1, column=3, padx=2)
entry_circ_x2.insert(0, "300")

entry_circ_y2 = tk.Entry(frame_controles, width=5)
entry_circ_y2.grid(row=1, column=4, padx=2)
entry_circ_y2.insert(0, "150")

# Botón para dibujar
boton_dibujar = tk.Button(
    root,
    text="Dibujar Figuras",
    command=dibujar_figuras,
    font=("Arial", 10)
)
boton_dibujar.pack(pady=5)

# Canvas para dibujar
canvas = tk.Canvas(
    root,
    width=400,
    height=300,
    bg="white"
)
canvas.pack(pady=10)

# Ejecutar aplicación
root.mainloop()
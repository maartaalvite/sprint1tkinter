import tkinter as tk


def actualizar_aficiones():
    # Lista para almacenar las aficiones seleccionadas
    aficiones_seleccionadas = []

    # Verificar cada Checkbutton
    if var_leer.get() == 1:
        aficiones_seleccionadas.append("Leer")
    if var_deporte.get() == 1:
        aficiones_seleccionadas.append("Deporte")
    if var_musica.get() == 1:
        aficiones_seleccionadas.append("Música")

    # Actualizar la etiqueta
    if aficiones_seleccionadas:
        texto_aficiones = ", ".join(aficiones_seleccionadas)
        etiqueta_resultado.config(text=f"Aficiones: {texto_aficiones}")
    else:
        etiqueta_resultado.config(text="No hay aficiones seleccionadas")


# Crear ventana principal
root = tk.Tk()
root.title("Ejercicio 4 - Checkbutton")
root.geometry("400x300")

# Título
titulo = tk.Label(
    root,
    text="Selecciona tus aficiones:",
    font=("Arial", 14, "bold")
)
titulo.pack(pady=20)

# Variables de control para los Checkbuttons
var_leer = tk.IntVar()
var_deporte = tk.IntVar()
var_musica = tk.IntVar()

# Checkbutton para Leer
check_leer = tk.Checkbutton(
    root,
    text="Leer",
    variable=var_leer,
    command=actualizar_aficiones,
    font=("Arial", 12)
)
check_leer.pack(pady=5)

# Checkbutton para Deporte
check_deporte = tk.Checkbutton(
    root,
    text="Deporte",
    variable=var_deporte,
    command=actualizar_aficiones,
    font=("Arial", 12)
)
check_deporte.pack(pady=5)

# Checkbutton para Música
check_musica = tk.Checkbutton(
    root,
    text="Música",
    variable=var_musica,
    command=actualizar_aficiones,
    font=("Arial", 12)
)
check_musica.pack(pady=5)

# Etiqueta para mostrar resultados
etiqueta_resultado = tk.Label(
    root,
    text="No hay aficiones seleccionadas",
    font=("Arial", 12),
    fg="darkgreen",
    wraplength=350  # Permite que el texto se ajuste
)
etiqueta_resultado.pack(pady=30)

# Ejecutar aplicación
root.mainloop()
import tkinter as tk

def mostrar_seleccion():
    seleccion = lista_frutas.curselection()
    if seleccion:
        indice = seleccion[0]
        fruta = lista_frutas.get(indice)
        etiqueta_resultado.config(text=f"Fruta seleccionada: {fruta}")
    else:
        etiqueta_resultado.config(text="Selecciona una fruta")

# Crear ventana principal
root = tk.Tk()
root.title("Ejercicio 6 - Listbox")
root.geometry("300x300")

# Título
titulo = tk.Label(
    root,
    text="Selecciona una fruta:",
    font=("Arial", 12)
)
titulo.pack(pady=10)

# Listbox con frutas
lista_frutas = tk.Listbox(
    root,
    height=5,
    font=("Arial", 10)
)
lista_frutas.pack(pady=10)

# Agregar frutas a la lista
frutas = ["Manzana", "Banana", "Naranja", "Pera", "Uva"]
for fruta in frutas:
    lista_frutas.insert(tk.END, fruta)

# Botón para mostrar selección
boton_mostrar = tk.Button(
    root,
    text="Mostrar Selección",
    command=mostrar_seleccion,
    font=("Arial", 10)
)
boton_mostrar.pack(pady=10)

# Etiqueta para mostrar resultado
etiqueta_resultado = tk.Label(
    root,
    text="Selecciona una fruta",
    font=("Arial", 10),
    fg="blue"
)
etiqueta_resultado.pack(pady=10)

# Ejecutar aplicación
root.mainloop()
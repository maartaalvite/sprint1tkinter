import tkinter as tk
from tkinter import messagebox


def agregar_usuario():
    nombre = entry_nombre.get()
    edad = scale_edad.get()
    genero = var_genero.get()

    if nombre.strip():
        usuario = f"{nombre} - {edad} años - {genero}"
        listbox_usuarios.insert(tk.END, usuario)
        entry_nombre.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa un nombre")


def eliminar_usuario():
    seleccion = listbox_usuarios.curselection()
    if seleccion:
        listbox_usuarios.delete(seleccion[0])
    else:
        messagebox.showwarning("Advertencia", "Selecciona un usuario para eliminar")


def salir_aplicacion():
    root.quit()


def guardar_lista():
    messagebox.showinfo("Guardar", "Función guardar lista")


def cargar_lista():
    messagebox.showinfo("Cargar", "Función cargar lista")


# Crear ventana principal
root = tk.Tk()
root.title("Ejercicio 12 - Registro de Usuarios")
root.geometry("500x500")

# Menú principal
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

# Menú Archivo
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Guardar Lista", command=guardar_lista)
menu_archivo.add_command(label="Cargar Lista", command=cargar_lista)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir_aplicacion)

# Frame para el formulario
frame_formulario = tk.Frame(root, padx=10, pady=10)
frame_formulario.pack(fill="x")

# Campo para el nombre
tk.Label(frame_formulario, text="Nombre:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
entry_nombre = tk.Entry(frame_formulario, width=30, font=("Arial", 10))
entry_nombre.grid(row=0, column=1, pady=5, padx=5)

# Scale para la edad
tk.Label(frame_formulario, text="Edad (0-100):", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
scale_edad = tk.Scale(frame_formulario, from_=0, to=100, orient="horizontal", length=200)
scale_edad.grid(row=1, column=1, pady=5, padx=5)

# Radiobuttons para el género
tk.Label(frame_formulario, text="Género:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
var_genero = tk.StringVar(value="Masculino")

frame_genero = tk.Frame(frame_formulario)
frame_genero.grid(row=2, column=1, pady=5, padx=5)

rb_masculino = tk.Radiobutton(frame_genero, text="Masculino", variable=var_genero, value="Masculino")
rb_masculino.pack(side="left", padx=5)

rb_femenino = tk.Radiobutton(frame_genero, text="Femenino", variable=var_genero, value="Femenino")
rb_femenino.pack(side="left", padx=5)

rb_otro = tk.Radiobutton(frame_genero, text="Otro", variable=var_genero, value="Otro")
rb_otro.pack(side="left", padx=5)

# Frame para los botones
frame_botones = tk.Frame(root, padx=10, pady=10)
frame_botones.pack(fill="x")

btn_agregar = tk.Button(frame_botones, text="Añadir", command=agregar_usuario, font=("Arial", 10))
btn_agregar.pack(side="left", padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminar_usuario, font=("Arial", 10))
btn_eliminar.pack(side="left", padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir_aplicacion, font=("Arial", 10))
btn_salir.pack(side="left", padx=5)

# Frame para la lista de usuarios
frame_lista = tk.Frame(root)
frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

# Listbox con scrollbar
listbox_usuarios = tk.Listbox(frame_lista, font=("Arial", 10), height=10)
listbox_usuarios.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_lista, command=listbox_usuarios.yview)
scrollbar.pack(side="right", fill="y")

listbox_usuarios.config(yscrollcommand=scrollbar.set)

# Ejecutar aplicación
root.mainloop()
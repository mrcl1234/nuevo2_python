import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo Tkinter")

# Crear una función que se ejecutará al hacer clic en el botón
def on_button_click():
    print("¡Botón clickeado!")

# Crear un botón y añadirlo a la ventana
button = tk.Button(root, text="Haz clic en mí", command=on_button_click)
button.pack(pady=20)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
import tkinter as tk

root = tk.Tk()
root.title("tk")
root.config(bg="lightblue")

# Lista de colores para los 6 cuadros
colores = ["red", "blue", "yellow", "green", "orange", "black"]

# Crear los 6 labels con un for
for i, color in enumerate(colores):
    fila = i // 2      # División entera: 0÷2=0, 1÷2=0, 2÷2=1, 3÷2=1, 4÷2=2, 5÷2=2
    columna = i % 2    # Módulo (resto): 0%2=0, 1%2=1, 2%2=0, 3%2=1, 4%2=0, 5%2=1
    
    label = tk.Label(root, bg=color, width=20, height=8)
    label.grid(row=fila, column=columna)

# Botón rojo grande a la derecha
boton = tk.Button(
    root, 
    text="No presiones el botón", 
    bg="darkred", 
    fg="#7d5c01",
    font=("Arial", 10), 
    width=70, 
    height=5
)
boton.grid(row=1, column=2)

root.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

''' Práctica 11: Lista de Selección '''

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Alumno: Magallanes López Carlos Gabriel
# NOTE: No. de Control: 24308051280865
# NOTE: Escuela: Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128
# NOTE: Grupo: 3° "J"

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

import tkinter as tk                # Framework Básico para Interfaz Gráfica

# ------------------------------------------------------------------------------------------------------------------------------------------
""" =========================================================== Helpers ================================================================ """

# Función Helper: Mostrar Selección
def show_selection() -> None:

    """
       - Función: Mostrar Selección
       - Argumentos: Ninguno
       - Retorno: Ninguno
       - Objetivo: Mostrar el elemento seleccionado en el Listbox
    """

    # Mostrar el elemento seleccionado en el Label
    try: result_label.config(text=f"Seleccionaste: {listbox.get(listbox.curselection())}")       # Mostrar el Elemento Seleccionado
    except (tk.TclError, Exception): result_label.config(text = "No hay Selección")              # Manejo de Error si no hay Selección

# ------------------------------------------------------------------------------------------------------------------------------------------
""" =========================================================== Práctica 11 ================================================================ """

# Configuración de la Ventana
window = tk.Tk()                                                     # Creación de la Ventana Principal
window.geometry("600x400")                                           # Dimensiones de la Ventana
window.title("Actividad 11 - Lista de Selección")                    # Título de la Ventana


# Label de Instrucción
instruction_label = tk.Label(window, text = "Selecciona un elemento:", font = ("Arial", 12)).pack(pady = 20)


# Lista de Selección (Listbox)
listbox = tk.Listbox(master = window, font = ("Arial", 11), height = 6, width = 30)   # Creación del Listbox
listbox.pack(pady = 10)                                                               # Empaquetado del Listbox

# Agregar elementos a la lista
for elements in  ["Python", "JavaScript", "Java", "C++", "Ruby", "Go"]: listbox.insert(tk.END, elements)  

# Label Resultado
result_label = tk.Label(master = window, font = ("Arial", 14, "bold"), fg = "#2ecc71")                     # Creación del Label para mostrar el resultado
result_label.pack(pady = 20)                                                                                  # Empaquetado del Label


# Botón para Mostrar Selección
button = tk.Button(                          # Creación del Botón
    
    master = window,                         # Ventana Principal
    text = "Mostrar Selección",              # Texto del Botón
    command = show_selection,                # Función a Ejecutar al Presionar el Botón
    bg = "#9b59b6",                        # Color de Fondo
    fg = "white",                            # Color del Texto
    font = ("Arial", 11),                    # Fuente del Texto
    padx = 20, pady = 8                      # Padding del Botón

)
button.pack(pady = 10)                       # Empaquetado del Botón


# Bucle Principal de la Ventana
window.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------

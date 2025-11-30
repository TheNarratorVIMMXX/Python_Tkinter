
# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

''' Práctica 10:  Mover Label  '''

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Alumno: Magallanes López Carlos Gabriel
# NOTE: No. de Control: 24308051280865
# NOTE: Escuela: Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128
# NOTE: Grupo: 3° "J"

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

import tkinter as tk                # Framework Básico para Interfaz Gráfica

""" =========================================================== Práctica 10 ================================================================ """

# Configuración de la Ventana
window = tk.Tk()                                                     # Creación de la Ventana Principal
window.geometry("600x400")                                           # Dimensiones de la Ventana
window.title("Actividad 10 - Mover Label")                           # Título de la Ventana


# Label que se mueve
label = tk.Label(window, text = "¡Muéveme!", font = ("Arial", 14), bg = "#e74c3c", fg = "white", padx = 20, pady = 10)   # Creación del Label
pos_x = [0]                                                                                                                # Posición Inicial en X
label.place(x = 0, y = 100)                                                                                                # Posición Inicial del Label


# Configuración del Botón
button = tk.Button(                                                       # Creación del Botón
    
    master = window,                                                      # Contenedor
    text = "Mover Derecha (+10px)",                                       # Texto del Botón
    command = lambda: label.place(x=label.winfo_x() + 10, y=100),         # Acción al presionar
    bg = "#3498db",                                                     # Color de Fondo
    fg = "white",                                                         # Color del Texto
    font = ("Arial", 12),                                                 # Nombre y Tamaño deFuente
    padx = 20, pady = 10                                                  # Espaciado Interno

)
button.place(x = 200, y = 300)                                            # Posición del Botón``


# Bucle Principal de la Ventana
window.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------

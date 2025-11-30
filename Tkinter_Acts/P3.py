
# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

''' Práctica 3: Label Personalizado con Estilo'''

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Alumno: Magallanes López Carlos Gabriel
# NOTE: No. de Control: 24308051280865
# NOTE: Escuela: Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128
# NOTE: Grupo: 3° "J"

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

import tkinter as tk                # Framework Básico para Interfaz Gráfica

# ------------------------------------------------------------------------------------------------------------------------------------------
""" =========================================================== Práctica 3 ================================================================ """

# Configuración de la Ventana
window = tk.Tk()                                                     # Creación de la Ventana Principal
window.geometry("450x300")                                           # Dimensiones de la Ventana
window.title("Actividad 3 - Label Personalizado con Estilo")         # Título de la Ventana


# Creación y Configuración del Label
label = tk.Label(                                      # Creación del Label
    
    master = window,                                   # Ventana Principal como Contenedor
    text = "Magallanes López Carlos Gabriel",          # Texto del Label
    bg = "#e74c3c",                                  # Color de Fondo del Label
    fg = "#ffffff",                                  # Color del Texto
    font = ("Arial", 20, "bold"),                      # Fuente, Tamaño y Estilo del Texto
    padx = 20, pady = 10                               # Espaciado Interno (Padding)

)
label.pack(pady = 50)                                  # Empaquetado del Label con Espaciado Vertical


# Bucle Principal de la Ventana
window.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------

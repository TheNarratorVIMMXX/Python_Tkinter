
# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

''' Práctica 8: Patrón de 4 frames (2x2) '''

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Alumno: Magallanes López Carlos Gabriel
# NOTE: Escuela: Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128
# NOTE: Grupo: 3° "J"

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

import tkinter as tk                # Framework Básico para Interfaz Gráfica

# ------------------------------------------------------------------------------------------------------------------------------------------
""" =========================================================== Práctica 8 ================================================================ """

# Configuración de la Ventana
window = tk.Tk()                                                     # Creación de la Ventana Principal
window.geometry("800x600")                                           # Dimensiones de la Ventana
window.title("Actividad 8 - Patrón de 4 Frames")                     # Título de la Ventana


# Creación de los Frames
for i, color in enumerate(["red", "blue", "yellow", "green"]):                                          # Colores y Contador de Frames 
    frame = tk.Frame(window, bg = color, width = 400, height = 300).grid(row = i // 2, column = i % 2)  # Creación y Posicionamiento de Frames


# Bucle Principal de la Ventana
window.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------

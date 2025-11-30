
# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

''' Práctica 4: Botón que Imprime en la Terminal '''

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Alumno: Magallanes López Carlos Gabriel
# NOTE: Escuela: Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128
# NOTE: Grupo: 3° "J"

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

import tkinter as tk                # Framework Básico para Interfaz Gráfica

# ------------------------------------------------------------------------------------------------------------------------------------------
""" =========================================================== Práctica 4 ================================================================ """

# Configuración de la Ventana
window = tk.Tk()                                                     # Creación de la Ventana Principal
window.geometry("450x300")                                           # Dimensiones de la Ventana
window.title("Actividad 4 - Botón Terminal")                         # Título de la Ventana


# Configuración del Botón
button = tk.Button(                                                   # Creación del Botón
    
    master = window,                                                 # Ventana Principal como Contenedor
    text = "Escribir en Terminal",                                   # Texto del Botoón
    command= lambda: print('Imprimiendo desde Tkinter...'),          # Comando al Presionar el Botón
    bg = "#2ecc71",                                                # Color de Fondo del Botón
    fg = "white",                                                    # Color del Texto
    font = ("Arial", 12),                                            # Fuente y Tamaño del Texto
    padx = 20, pady = 10                                             # Espaciado Interno (Padding)

)
button.pack(pady = 50)                                                # Empaquetado del Botón con Espaciado Vertical

# Bucle Principal de la Ventana
window.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------

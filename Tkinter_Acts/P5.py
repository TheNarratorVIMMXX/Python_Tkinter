
# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

''' Práctica 5: Mostrar/Ocultar Texto '''

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Alumno: Magallanes López Carlos Gabriel
# NOTE: Escuela: Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128
# NOTE: Grupo: 3° "J"

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

import tkinter as tk                # Framework Básico para Interfaz Gráfica

# ------------------------------------------------------------------------------------------------------------------------------------------
""" =========================================================== Práctica 5 ================================================================ """

# Configuración de la Ventana
window = tk.Tk()                                                     # Creación de la Ventana Principal
window.geometry("450x300")                                           # Dimensiones de la Ventana
window.title(" Actividad 5 - Mostrar/Ocultar Texto")                 # Título de la Ventana


# Configuración del Label
label = tk.Label(
    
    master = window,                                                 # Ventana Principal como Contenedor
    text = "¡Texto visible!",                                        # Texto del Label
    font = ("Arial", 16),                                            # Fuente y Tamaño del Texto
    fg = "#e74c3c"                                                 # Color del Texto

)
label.pack(pady = 20)                                                # Empaquetado del Label con Espaciado Vertical


# Configuración del Botón
button = tk.Button(
    
    master = window,                                                                               # Ventana Principal como Contenedor
    text = "Mostrar/Ocultar",                                                                      # Texto del Botoón
    command = lambda: label.pack_forget() if label.winfo_viewable() else label.pack(pady = 20),    # Comando al Presionar el Botón
    bg = "#9b59b6",                                                                              # Color de Fondo del Botón
    fg = "white",                                                                                  # Color del Texto
    font = ("Arial", 12),                                                                          # Fuente y Tamaño del Texto
    padx = 20, pady = 10                                                                           # Espaciado Interno (Padding)

)
button.pack(pady = 50)                                                                             # Empaquetado del Botón con Espaciado Vertical


# Bucle Principal de la Ventana
window.mainloop() 

# -----------------------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

''' Práctica 6: Entry con Botón para Impresión '''

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Alumno: Magallanes López Carlos Gabriel
# NOTE: No. de Control: 24308051280865
# NOTE: Escuela: Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128
# NOTE: Grupo: 3° "J"

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

import tkinter as tk                # Framework Básico para Interfaz Gráfica

# ------------------------------------------------------------------------------------------------------------------------------------------
""" =========================================================== Práctica 6 ================================================================ """

# Configuración de la Ventana
window = tk.Tk()                                                     # Creación de la Ventana Principal
window.geometry("450x300")                                           # Dimensiones de la Ventana
window.title("Actividad 6 - Ingresa tu Nombre")                      # Título de la Ventana

# Configuración del Label de Instrucción
name_label =tk.Label(                                                # Creación del Label
    
    master = window,                                                 # Ventana Principal como Contenedor
    text = "Ingresa tu Nombre:",                                     # Texto del Label 
    font = ("Arial", 12)                                             # Fuente y Tamaño del Texto
    
)
name_label.pack(pady = 10)                                           # Empaquetado del Label con Espaciado Vertical


# Configuración del Entry 
entry = tk.Entry(                                                    # Creación del Entry
    
    master = window,                                                 # Ventana Principal como Contenedor 
    font = ("Arial", 12),                                            # Fuente y Tamaño del Texto
    width = 30                                                       # Ancho del Entry
     
)
entry.pack(pady = 10)                                                # Empaquetado del Entry con Espaciado Vertical


# Configuración del Label de Impresión
result_label = tk.Label(                                             # Creación del Label de Resultado

    master = window,                                                 # Ventana Principal como Contenedor
    font = ("Arial", 14, "bold"),                                    # Fuente y Tamaño del Texto
    fg="#2ecc71"                                                   # Color del Texto

)
result_label.pack(pady = 20)                                         # Empaquetado del Label con Espaciado Vertical


# Configuración del Botón
button = tk.Button(                                                               # Creación del Botón
    
    master = window,                                                              # Ventana Principal como Contenedor
    text = "Mostrar Nombre",                                                      # Texto del Botón
    command = lambda: result_label.config(text=f"Hola, {entry.get()}!"),          # Acción al Presionar el Botón
    bg = "#3498db",                                                             # Color de Fondo del Botón
    fg = "white",                                                                 # Color del Texto del Botón
    font = ("Arial", 12),                                                         # Fuente y Tamaño del Texto
    padx = 20, pady = 10                                                          # Relleno Interno del Botón

)
button.pack(pady = 10)                                                           # Empaquetado del Botón con Espaciado Vertical


# Bucle Principal de la Ventana
window.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------

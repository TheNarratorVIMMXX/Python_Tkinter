
# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

''' Práctica 9: Frames Anidados '''

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Alumno: Magallanes López Carlos Gabriel
# NOTE: Escuela: Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128
# NOTE: Grupo: 3° "J"

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

import tkinter as tk                # Framework Básico para Interfaz Gráfica

# ------------------------------------------------------------------------------------------------------------------------------------------
""" =========================================================== Práctica 9 ================================================================ """

# Configuración de la Ventana
window = tk.Tk()                                                     # Creación de la Ventana Principal
window.geometry("600x400")                                           # Dimensiones de la Ventana
window.title("Actividad 9 - Frames Anidados")                        # Título de la Ventana


# Frame Externo
extern_frame = tk.Frame(master = window, bg = "#34495e", width = 300, height = 250)                                # Creación de Frame
extern_frame.pack(expand = True)                                                                                     # Empaquetar Frame Externo
extern_frame.pack_propagate(False)                                                                                   # Mantener Tamaño Fijo
tk.Label(extern_frame, text = "Frame Externo", bg = "#34495e",fg = "white", font = ("Arial", 12)).pack(pady = 15)  # Label para Información
    

# Frame interno 
intern_frame = tk.Frame(master = extern_frame, bg = "#95a5a6", width = 200, height = 150)                        # Creación de Frame Interno
intern_frame.pack()                                                                                                # Empaquetar Frame Interno
intern_frame.pack_propagate(False)                                                                                 # Mantener tamaño fijo
tk.Label(intern_frame, text = "Frame Interno", bg = "#95a5a6",fg = "white", font = ("Arial", 12)).pack(pady=15)  # Label para Información


# Botón 
button = tk.Button(                                                        # Creación de Botón
    
    master = intern_frame,                                                 # Contenedor
    text = "Botón Anidado",                                                # Texto del Botón
    command = lambda: print("¡Botón dentro de frames anidados!"),          # Acción al presionar
    bg = "#e74c3c",                                                      # Color de Fondo
    fg = "white",                                                          # Color del Texto
    font = ("Arial", 11),                                                  # Nombre y Tamaño deFuente
    padx = 15, pady = 8                                                    # Espaciado Interno

)
button.pack()                                                              # Empaquetar Botón


# Bucle Principal de la Ventana
window.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------

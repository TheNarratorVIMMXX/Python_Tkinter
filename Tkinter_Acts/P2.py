
# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

''' Práctica 2: Ventana con Título y Color de Fondo'''

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Alumno: Magallanes López Carlos Gabriel
# NOTE: No. de Control: 24308051280865
# NOTE: Escuela: Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128
# NOTE: Grupo: 3° "J"

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

import tkinter as tk                # Framework Básico para Interfaz Gráfica

# ------------------------------------------------------------------------------------------------------------------------------------------
""" =========================================================== Práctica 2 ================================================================ """

# Configuración de la Ventana
window = tk.Tk()                             # Creación de la Ventana Principal
window.geometry("400x200")                   # Dimensiones de la Ventana
window.title("Mi Ventana con Color")         # Título de la Ventana
window.configure(bg = "#040505")           # Color de Fondo de la Ventana

# Bucle Principal de la Ventana
window.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------

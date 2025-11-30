
# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

''' Práctica 12: Calculadora Simple '''

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Alumno: Magallanes López Carlos Gabriel
# NOTE: Escuela: Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128
# NOTE: Grupo: 3° "J"

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

import tkinter as tk                # Framework Básico para Interfaz Gráfica

# ------------------------------------------------------------------------------------------------------------------------------------------
""" =========================================================== Helpers ================================================================ """

# Función Helper: Calcular la Suma
def calcule() -> None:
    
    """
       - Función: Calcular Suma
       - Argumentos: Ninguno
       - Retorno: Ninguno
       - Objetivo: Obtener los valores de las entradas, calcular la suma y mostrar el resultado o un mensaje de error.
    """

    # Bloque de Validación para la Suma
    try:

        # Suma de los Números Ingresados
        num1 = float(entry1.get())                                                                        # Conversión de las Entradas a Float
        num2 = float(entry2.get())                                                                        # Conversión de las Entradas a Float
        result_label.config(text = f"Resultado: {num1 + num2}", fg = "#27ae60")                      # Mostrar el Resultado en el Label
    except ValueError: result_label.config(text = "Error: Ingresa números válidos", fg = "#e74c3c")  # Mensaje de Error si Conversión Falla

# ------------------------------------------------------------------------------------------------------------------------------------------
""" =========================================================== Práctica 12 ================================================================ """

# Configuración de la Ventana
window = tk.Tk()                                                     # Creación de la Ventana Principal
window.geometry("600x400")                                           # Dimensiones de la Ventana
window.title("Actividad 12 - Calculadora Simple")                    # Título de la Ventana

# Label de Instrucción
tk.Label(master = window, text = "CALCULADORA DE SUMA", font = ("Arial", 16, "bold"), fg = "#2c3e50").pack(pady = 20)


# Entrada para Númmero 1
tk.Label(master = window, text = "Primer número:", font = ("Arial", 11)).pack(pady = 5)     # Label para el Primer Número
entry1 = tk.Entry(master = window, font=("Arial", 12), width=20)                            # Entrada para el Primer Número
entry1.pack(pady = 5)                                                                       # Empaquetado de la Entrada


# Entrada para Númmero 2
tk.Label(master = window, text = "Segundo número:", font = ("Arial", 11)).pack(pady = 5)     # Label para el Segundo Número
entry2 = tk.Entry(master = window, font = ("Arial", 12), width = 20)                         # Entrada para el Segundo Número
entry2.pack(pady = 5)                                                                        # Empaquetado de la Entrada


# Label para Mostrar el Resultado
result_label = tk.Label(master = window, font = ("Arial", 16, "bold"), fg = "#27ae60")  # Label para el Resultado
result_label.pack(pady = 20)                                                              # Empaquetado del Label


# Botón para Calcular la Suma
boton = tk.Button(                        # Creación del Botón

    master = window,                      # Ventana Principal
    text = "Sumar",                       # Texto del Botón
    command = calcule,                    # Función a Ejecutar al Presionar el Botón
    bg = "#16a085",                     # Color de Fondo
    fg = "white",                         # Color del Texto
    font = ("Arial", 12, "bold"),         # Fuente del Texto
    padx = 30, pady = 10                  # Espaciado Interno (Padding

)
boton.pack(pady = 10)                     # Empaquetado del Botón


# Bucle Principal de la Ventana
window.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------

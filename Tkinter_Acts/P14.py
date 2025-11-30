# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

''' Práctica 14: Calculadora Básica con Tkinter'''

# NOTE: Fecha de Realización: 16/10/2025
# NOTE: Alumno: Magallanes López Carlos Gabriel
# NOTE: Escuela: Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128
# NOTE: Grupo: 3° "J"

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

import tkinter as tk                # Framework Básico para Interfaz Gráfica
from tkinter import messagebox      # Módulo para Mensajes Emergentes

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Funciones Helpers ============================================================ """

# Función Helper: Presionar Botón
def press_button(value: str) -> None:
    
    """
       - Función: Presionar Botón
       - Argumentos: Valor Presionado (str)
       - Retorno: Ninguno
       - Objetivo: Añadir el Valor Presionado a la Expresión y Actualizar la Pantalla
    """
    
    # Validación del Argumento: Valor Presionado
    if not isinstance(value, str): 
        raise TypeError("El Valor Presionado debe ser una Cadena de Texto (str).")
    elif value not in "0123456789.+-*/()":
        raise ValueError("El Valor Presionado debe ser un Número o un Operador Válido (+, -, *, /, ., (, )).")


    # Añadir el valor presionado a la expresión
    global expression                              # Variable Global para la Expresión
    expression = expression + value                # Concatenar el Valor Presionado a la Expresión
    screen.config(text = expression)             # Actualizar Pantalla con la Nueva Expresión




# Función Helper: Limpiar Pantalla
def clean_screen() -> None:

    """
       - Función: Limpiar Pantalla
       - Argumentos: Ninguno
       - Retorno: Ninguno
       - Objetivo: Limpiar toda la Expresión de la Calculadora
    """

    # Limpiar la Expresión
    global expression             # Declarar Variable Global
    expression = ""               # Reiniciar la Expresión
    screen.config(text = "0")     # Actualizar pantalla a "0"




# Función Helper: Borrar Último Carácter
def erase_last_char():
    
    """
       - Función: Borrar Último Carácter
       - Argumentos: Ninguno
       - Retorno: Ninguno
       - Objetivo: Borrar el Último Carácter de la Expresión
    """
    
    # Borrar el Ultimo Carácter de la Expresión
    global expression                                                                     # Declarar Variable Global
    expression = expression[:-1]                                                          # Eliminar el Último Carácter de la Expresión
    screen.config(text = expression) if expression != "" else screen.config(text = "0")   # Actualizar Pantalla o Mostrar "0" si está vacía
    



# Función Helper: Calcular Resultado
def calcule_result():
    
    """
       - Función: Calcular Resultado
       - Argumentos: Ninguno
       - Retorno: Ninguno
       - Objetivo: Evaluar la Expresión y Mostrar el Resultado en la Pantalla
    """
    
    # Calcular el Resultado de la Expresión
    global expression                                                          # Declarar Variable Global
    try:                                                                       # Bloque de Validación para el Cálculo
        resultado = str(eval(expression))                                      # Evaluar str como Código de Python y Convertir a str
        screen.config(text = resultado)                                        # Actualizar Pantalla con el Resultado
        expression = resultado                                                 # Actualizar la Expresión con el Resultado
    except (Exception, tk.TclError):                                           # Capturar Errores de Evaluación o Errores de Tkinter
        messagebox.showerror(title = "Error", message = "Expresión Inválida")  # Mostrar Mensaje de Error
        expression = ""                                                        # Reiniciar la Expresión
        screen.config(text = "0")                                              # Actualizar Pantalla a "0"

# ------------------------------------------------------------------------------------------------------------------------------------------
""" =========================================================== Práctica 14 ================================================================ """

# Configuración de la Ventana
window = tk.Tk()                             # Creación de la Ventana Principal
window.geometry("320x450")                   # Dimensiones de la Ventana
window.title("Calculadora Básica")           # Título de la Ventana
window.configure(bg = "#040505")           # Color de Fondo de la Ventana
window.resizable(False, False)               # Deshabilitar Redimensionamiento


# Variables Globales y Colores
expression = ""                              # Expresión Actual
num_color = "#4a5f7f"                      # Color de Números
operator_color = "#e67e22"                 # Color de Operadores
special_color = "#e74c3c"                  # Color de Botones Especiales
equal_color = "#27ae60"                    # Color del Botón Igual
text_color = "white"                         # Color del Texto


# Label para Pantalla
screen = tk.Label(                           # Etiqueta para la Pantalla
    
    master = window,                         # Ventana Principal
    text = "0",                              # Texto Inicial
    font = ("Arial", 20, "bold"),            # Fuente
    bg = "#34495e",                        # Color de fondo
    fg = "white",                            # Color de texto
    anchor = "e",                            # Alineado a la Derecha ( e = east)
    padx = 10, pady = 10                     # Espaciado Interno (Padding)                          

)
screen.grid(                               # Colocación en la Cuadrícula
    
    row = 0, column = 0,                     # Fila 0, Columna 0
    columnspan = 4,                          # Ocupa 4 Columnas
    padx = 10, pady = 15,                    # Espaciado Externo (Padding)
    sticky = "ew"                            # Expandirse Horizontalmente (east-west)
    
)


# Lista de Botones (Texto, Fila, Columna, Comando, Color)
buttons = [
    
    # Fila 1
    ("7", 1, 0, lambda: press_button("7"), num_color),
    ("8", 1, 1, lambda: press_button("8"), num_color),
    ("9", 1, 2, lambda: press_button("9"), num_color),
    ("/", 1, 3, lambda: press_button("/"), operator_color),
    
    # Fila 2
    ("4", 2, 0, lambda: press_button("4"), num_color),
    ("5", 2, 1, lambda: press_button("5"), num_color),
    ("6", 2, 2, lambda: press_button("6"), num_color),
    ("*", 2, 3, lambda: press_button("*"), operator_color),
    
    # Fila 3
    ("1", 3, 0, lambda: press_button("1"), num_color),
    ("2", 3, 1, lambda: press_button("2"), num_color),
    ("3", 3, 2, lambda: press_button("3"), num_color),
    ("-", 3, 3, lambda: press_button("-"), operator_color),
    
    # Fila 4
    ("0", 4, 0, lambda: press_button("0"), num_color),
    (".", 4, 1, lambda: press_button("."), num_color),
    ("C", 4, 2, clean_screen, special_color),
    ("+", 4, 3, lambda: press_button("+"), operator_color),
    
    # Fila 5
    ("(", 5, 0, lambda: press_button("("), num_color),
    (")", 5, 1, lambda: press_button(")"), num_color),
    ("←", 5, 2, erase_last_char, special_color),
    ("=", 5, 3, calcule_result, equal_color),

]

# Creación y Colocación de Botones
for (text, row, column, command, color) in buttons:       # Iterar sobre la Lista de Botones
    boton = tk.Button(                                    # Crear Botón

        master = window,                                   # Ventana Principal
        text = text,                                       # Texto del Botón
        command = command,                                 # Comando al Presionar
        bg = color,                                        # Color de Fondo
        fg = text_color,                                   # Color del Texto
        font = ("Arial", 16, "bold"),                      # Fuente
        width = 5, height = 2,                             # Dimensiones del Botón
        borderwidth = 0                                    # Sin Borde

    )
    boton.grid(                                            # Colocar el Botón en la Cuadrícula

        row = row, column = column,                        # Fila y Columna según la Lista
        padx = 5, pady = 5                                 # Espaciado Externo (Padding)

    )


# Peso de las Filas y Columnas para Expansión
for i in range(4): window.grid_columnconfigure(index = i, weight = 1)   


# Teclas de Atajo
window.bind("<Return>", lambda event: calcule_result())         # Enter para Calcular
window.bind("<Escape>", lambda event: clean_screen())           # Escape para Limpiar
window.bind("<BackSpace>", lambda event: erase_last_char())     # Backspace para Borrar


# Bucle para Enlaze de Teclas Numéricas y Operadores
for char in "0123456789.+-*/()": window.bind(char, lambda event, button = char: press_button(button))


# Bucle Principal de la Ventana
window.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------
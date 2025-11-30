
# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

''' Práctica 7: Cuestionario con Tkinter '''

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Alumno: Magallanes López Carlos Gabriel
# NOTE: No. de Control: 24308051280865
# NOTE: Escuela: Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128
# NOTE: Grupo: 3° "J"

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

import tkinter as tk                # Framework Básico para Interfaz Gráfica

# ------------------------------------------------------------------------------------------------------------------------------------------
""" =========================================================== Práctica 7 ================================================================ """
 
# Configuración de la Ventana
window = tk.Tk()                                                     # Creación de la Ventana Principal
window.geometry("450x300")                                           # Dimensiones de la Ventana
window.title("Actividad 7 - Cuestionario")                           # Título de la Ventana


# Etiqueta Principal
main_label = tk.Label(                                               # Creación de la Etiqueta Principal
    
    master = window,                                                 # Lugar donde se ubicará la etiqueta
    text = "CUESTIONARIO",                                           # Texto de la Etiqueta
    font = ("Arial", 18, "bold"),                                    # Fuente, Tamaño y Estilo del Texto
    fg = "#2c3e50"                                                 # Color del Texto
    
)
main_label.pack(pady = 20)                                          # Empaquetado de la Etiqueta con Espaciado Vertical


# Almacenamiento de Datos
entrys: dict[str, tk.Entry] = {}                                                                                        # Diccionario de Entradas
questions = ["1. ¿Cuál es tu nombre?", "2. ¿Cuál es tu edad?", "3. ¿Cuál es tu ciudad?", "4. ¿Cuál es tu carrera?"]     # Lista de Preguntas


# Creación de las Preguntas y Campos de Entrada
for question in questions:


    # Configuración de la Label Pregunta
    label = tk.Label(                                              # Creación de la Etiqueta para la Pregunta                                           
            
        master = window,                                           # Lugar donde se ubicará la etiqueta
        text = question,                                           # Texto de la Etiqueta
        font = ("Arial", 11)                                       # Fuente y Tamaño del Texto
    
    )
    label.pack(pady = 5)                                           # Empaquetado de la Etiqueta con Espaciado Vertical


    # Configuración del Entry Pregunta
    entry = tk.Entry(                                              # Creación del Campo de Entrada
        
        master = window,                                           # Lugar donde se ubicará el campo de entrada
        font = ("Arial", 11),                                      # Fuente y Tamaño del Texto
        width = 40                                                 # Ancho del Campo de Entrada
    
    )
    entry.pack(pady = 5)                                          # Empaquetado del Campo de Entrada con Espaciado Vertical

    # Almacenamiento de las Entradas en el Diccionario
    if "nombre" in question: entrys['name'] = entry               # Nombre
    elif "edad" in question: entrys['age'] = entry                # Edad
    elif "ciudad" in question: entrys['city'] = entry             # Ciudad
    elif "carrera" in question: entrys['career'] = entry          # Carrera



# Etiqueta para Mostrar Resultados
result_label = tk.Label(master = window, font = ("Arial", 10), fg = "#27ae60", wraplength = 500)       # Etiqueta para Mostrar Resultados
result_label.pack(pady = 20)                                                                             # Empaquetado de Etiqueta con Espaciado Vertical


# Botón para Enviar Respuestas
button = tk.Button(
   
    master = window,                                                                                                                              # Contenedor                                                                                                                     
    text="Enviar Respuestas",                                                                                                                     # Texto
    command = lambda: result_label.config(                                                                                                        # Comando 
    
        text = f"Nombre: {entrys['name'].get()}\nEdad: {entrys['age'].get()}\nCiudad: {entrys['city'].get()}\nCarrera: {entrys['career'].get()}"
    ),
    bg = "#16a085",                                                                                                                             # Color Fondo
    fg = "white",                                                                                                                                 # Color Texto
    font = ("Arial", 12),                                                                                                                         # Fuente y Tamaño Texto
    padx = 20, pady = 8                                                                                                                           # Relleno Interno 

)
button.pack(pady = 10)                                                                                                                            # Empaquetado Espaciado


# Ejecución de la Ventana
window.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------

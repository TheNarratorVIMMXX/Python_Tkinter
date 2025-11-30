# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

''' Práctica 13: Memorama 3 x 4 con Imágenes (Tkinter)'''

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Alumno: Magallanes López Carlos Gabriel
# NOTE: Escuela: Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128
# NOTE: Grupo: 3° "J"

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

import tkinter as tk                # Framework Básica para Interfaz Gráfica
from tkinter import ttk             # Módulo para Widgets con Estilo Mejorado

# ------------------------------------------------------------------------------------------------------------------------------------------
""" =========================================================== Práctica 13 ================================================================ """

# Configuración de la Ventana
window = tk.Tk()                               # Inicialización de la Ventana Raíz 
window.title("Cuadrícula de Imágenes 3x4")     # Título de la Ventana
window.geometry("520x380")                     # Tamaño de la Ventana
window.config(bg = "#ecf0f1")                # Color de Fondo           


# Título
title = ttk.Label(
    
    window,                                    # Ventana
    text = "Memorama con 12 Cartas",           # Texto 
    font = ("Arial", 11, "bold"),              # (Fuente, Tamaño, Ancho Letra)
    background = "#ecf0f1",                  # Color Fondo (Gris Claro)
    foreground = "#30455b"                   # Color Fuente (Azul Oscuro)
    
)
title.pack(pady = 5)                           # Agregamos Widget a la Ventana


# Frame Principal
main_frame = tk.Frame(window, bg = "#ecf0f1")      # Color (Gris Claro)
main_frame.pack(pady = 2)                            # Agregamos Widget a la Ventana


# Nombres de las Imágenes (Duplicadas para el Memorama)
images = [f"imgs\\img{num}.png" for num in range(1, 7)] * 2  


# Cuadros del Memorama
index = 0                                      # Índice para Imagen
for row in range(3):                           # Recorrido de 3 Filas                             
    for column in range(4):                    # Recorrido de 4 Columnas        
        
        
        # Carta
        card = tk.Frame(                       # Frame para la Carta
            
            main_frame,                        # Frame Principal
            bg = "#34495e",                  # Color de Fondo (Azul Oscuro)
            width = 100,                       # Ancho
            height = 90,                       # Alto
            relief = "solid",                  # Relieve Sólido
            borderwidth = 1                    # Ancho del Borde

        )
        card.grid(                             # Configuración Carta
            
            row = row, column = column,        # Posición Carta (Fila, olumna)
            padx = 3, pady = 3,                # Espacio Relleno Alrededor
            
        )
        

        # Bloque de Validación para Carga de Imagen
        try:
            
            # Imagen
            original_image = tk.PhotoImage(file = images[index])                    # Carga de Imagen       
            image = original_image.subsample(6, 6)                                  # Reducción de Tamaño (1/5)
            image_label = ttk.Label(card, image = image, background = "#34495e")  # Etiqueta para Imagen
            image_label.image = image                                               # Referencia para Evitar Recolección de Basura
            image_label.pack(pady = 1)                                              # Agregamos Widget
            
        # Captura de Errores
        except (tk.TclError, Exception, FileNotFoundError) as exc:                    # Erorres Posibles 
            raise SystemExit(f"Error: No se pudo cargar la imagen. Detalles: {exc}")  # Salida del Programa


        # Actualización del Contador
        index += 1


# Bucle Principal de Ventana
window.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------

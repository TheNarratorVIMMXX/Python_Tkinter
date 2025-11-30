
# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

''' Práctica 13: Semáforo con Interfaz Gráfica'''

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Alumno: Magallanes López Carlos Gabriel
# NOTE: Escuela: Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128
# NOTE: Grupo: 3° "J"

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

import tkinter as tk                # Framework Básico para Interfaz Gráfica

# ------------------------------------------------------------------------------------------------------------------------------------------
""" =========================================================== Helpers ================================================================ """

# Función Helper: Actualizar Timer
def update_timer() -> None:

    """
       - Función: Actualizar Timer
       - Argumentos: Ninguno
       - Retorno: Ninguno
       - Objetivo: Actualizar el timer que muestra el tiempo restante para el próximo cambio de luz.
    """

    # Decrementar el Tiempo Restante
    remaining_time[0] -= 1                                                    # Decrementar el Tiempo Restante en 1 Segundo 
    label_timer.config(text = f"Tiempo restante: {remaining_time[0] + 1}s")   # Actualizar el Texto del Label del Timer
    
    # Si el Tiempo Restante es Mayor a 0, Llamar a esta Función Nuevamente después de 1 Segundo (1000 ms)
    if remaining_time[0] > 0: window.after(1000, update_timer)  



# Fución Helper: Cambiar Luz del Semáforo
def change_light() -> None:

    """
       - Función: Cambiar Luz del Semáforo
       - Argumentos: Ninguno
       - Retorno: Ninguno
       - Objetivo: Cambiar la luz del semáforo y actualizar el estado actual.
    """
    
    # Declaración de Variable Global para el Estado Actual
    global actual_state
    
    # Resetear Colores de las Luces
    canvas.itemconfig(red_light, fill = "#555555")         # Luz Roja Apagada
    canvas.itemconfig(yellow_light, fill = "#555555")      # Luz Amarilla Apagada
    canvas.itemconfig(green_light, fill = "#555555")       # Luz Verde Apagada
    
    # Cambiar Luz Basado en el Estado Actual
    if actual_state == 0:                                           # Si el Estado Actual es 0 (Rojo)
        canvas.itemconfig(red_light, fill = "#e74c3c")            # Luz Roja Encendida
        state_label.config(text = "ALTO", fg = "#e74c3c")         # Actualizar el Label de Estado
        actual_state = 1                                            # Cambiar el Estado Actual a 1 (Amarillo)
    elif actual_state == 1:                                         # Si el Estado Actual es 1 (Amarillo)
        canvas.itemconfig(yellow_light, fill = "#f39c12")         # Luz Amarilla Encendida
        state_label.config(text = "PRECAUCIÓN", fg = "#f39c12")   # Actualizar el Label de Estado
        actual_state = 2                                            # Cambiar el Estado Actual a 2 (Verde)
    else:                                                           # Si el Estado Actual es 2 (Verde)
        canvas.itemconfig(green_light, fill = "#2ecc71")          # Luz Verde Encendida
        state_label.config(text = "SIGA", fg = "#2ecc71")         # Actualizar el Label de Estado
        actual_state = 0                                            # Cambiar el Estado Actual a 0 (Rojo)

    # Reiniciar timer
    remaining_time[0] = 5   # Reiniciar el Tiempo Restante a 5 segundos
    update_timer()          # Iniciar el Timer

    # Programar el Próximo Cambio de Luz después de 5 segundos (5000 ms)
    window.after(5000, change_light)
    

# ------------------------------------------------------------------------------------------------------------------------------------------
""" =========================================================== Práctica 12 ================================================================ """

# Configuración de la Ventana
window = tk.Tk()                                                     # Creación de la Ventana Principal
window.geometry("600x400")                                           # Dimensiones de la Ventana
window.title("Actividad 13 - Semáforo")                              # Título de la Ventana
window.configure(bg="#2c3e50")                                     # Color de Fondo de la Ventana


# Label de Título
tk.Label(master = window, text = "SEMÁFORO", font = ("Arial", 20, "bold"), bg = "#2c3e50", fg = "white").pack(pady=20)


# Creación del Semáforo
canvas = tk.Canvas(master = window, width = 120, height = 280, bg = "#34495e", highlightthickness = 0)        # Lienzo para el Semáforo
canvas.pack(pady = 20)                                                                                          # Empaquetado del Lienzo

# Creación de Colores para el Semáforo
red_light = canvas.create_oval(                # Luz Roja
    
    20, 20,                                    # Coordenadas de Inicio del Óvalo
    100, 100,                                  # Coordenadas de Término del Óvalo
    fill = "#555555",                        # Color de Relleno
    outline = "#000000",                     # Color de Contorno del Óvalo
    width = 2                                  # Ancho del Contorno      
    
)
yellow_light = canvas.create_oval(             # Luz Amarilla
    
    20, 110,                                   # Coordenadas de Inicio del Óvalo
    100, 190,                                   # Coordenadas de Término del Óvalo
    fill="#555555",                          # Color de Relleno
    outline="#000000",                       # Contorno del Óvalo
    width=2                                    # Ancho del Contorno

)
green_light = canvas.create_oval(              # Luz Verde

    20, 200,                                   # Coordenadas de Inicio del Óvalo
    100, 280,                                  # Coordenadas de Término del Óvalo
    fill="#555555",                          # Color de Relleno
    outline="#000000",                       # Contorno del Óvalo
    width=2                                    # Ancho del Contorno

)


# Label Estado del Semáforo (ALTO, PRECAUCIÓN, SIGA)
state_label = tk.Label(master = window, text = "ALTO", font = ("Arial", 16, "bold"), bg = "#2c3e50", fg ="#e74c3c")   # Creación
state_label.pack(pady = 10)                                                                                               # Empaquetado


# Label para el Timer
label_timer = tk.Label(master = window, text = "Tiempo restante: 5s", font = ("Arial", 12), bg = "#2c3e50", fg = "#ecf0f1")   # Creación
label_timer.pack(pady = 5)                                                                                                         # Empaquetado

# Variables de Control
actual_state = 0           # Estado del Semáforo (Rojo = 0, Amarillo = 1, Verde = 2) 
remaining_time = [5]       # Tiempo Restante para el Cambio de Luz (en segundos)

# Iniciar el Cambio de Luz del Semáforo
change_light()

# Bucle Principal de la Ventana
window.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------
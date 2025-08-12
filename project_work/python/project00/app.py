# -*- coding: utf-8 -*-
import tkinter as tk

# función
def calculate_distance():
    distance = float(entry_velocity.get()) * float(entry_timer.get())
    label_result.configure(text=f'El móvil recorrio {distance} distancia')


# Crear la ventana
root = tk.Tk()

# Configuración de la ventana 
root.title('Distancia recorrida por un móvil')
root.minsize(320, 130)
root.resizable(True, True)
root.geometry('+500+80')

# Elements
# Labels
label__title = tk.Label(root, text='Distancia recorrida por un móvil')
label_result = tk.Label(root, text='El móvil recorrio x distancia')
label_velocity = tk.Label(root, text='Velocidad')
label_timer = tk.Label(root, text='Tiempo')

# Text box
velocity_text = tk.Entry()
timer_text = tk.Entry()

# Entry text
entry_velocity = tk.StringVar(root, width=20, textvariable=velocity_text)
entry_timer = tk.StringVar(root, width=20, textvariable=timer_text)

# Buttons
bt = tk.Button(root, text='Evaluar', command=lambda: calculate_distance())

# Positions to elements
# Labels

# Entry

# Buttons

# Inicializar la ventana
root.mainloop()
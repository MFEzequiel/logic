# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk

# functions
def calculate_distance():
    distance = float(entry_velocity.get()) * float(entry_timer.get())
    label_result.configure(text=f'El móvil recorrio {distance} distancia')


# Crear la ventana
root = tk.Tk()
root.title('Distancia recorrida por un móvil')
root.minsize(320, 130)
root.resizable(True, True)
root.geometry('+500+80')
# Elements
# Labels
label__title = ttk.Label(root, text='Distancia recorrida por un móvil')
label_result = ttk.Label(root, text='El móvil recorrio x distancia')
label_velocity = ttk.Label(root, text='Velocidad')
label_timer = ttk.Label(root, text='Tiempo')

# Text box
velocity_text = tk.StringVar()
timer_text = tk.StringVar()

# Entry text
entry_velocity = ttk.Entry(root, width=20, textvariable=velocity_text)
entry_timer = ttk.Entry(root, width=20, textvariable=timer_text)

# Buttons
bt = ttk.Button(root, text='Evaluar', command=lambda: calculate_distance())

# Positions to elements
# Labels
label__title.grid(column=0, row=0)
label_result.grid(column=0, row=4)
label_velocity.grid(column=0, row=1)
label_timer.grid(column=0, row=2)

# Entry
entry_velocity.grid(column=1, row=1)
entry_timer.grid(column=1, row=2)

# Buttons
bt.grid(column=0, row=3)

# Inicializar la ventana
root.mainloop()
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk

# functions
def mean_student():
    mean = float(entry_note_one.get()) + float(entry_note_two.get()) + float(entry_note_three.get()) / 3
    label_result.configure(text=f'Promedio del estudiante: {mean}')

# Crear la ventana
root = tk.Tk()
root.title('promedio simple de un estudiante')
root.minsize(350, 120)
root.geometry('+500+180')
root.resizable(True, True)
# Elements
# Labels
label_title = ttk.Label(root, text='Promedio simple de un estudiante')
label_result = ttk.Label(root, text='Promedio del estudiante: ')
label_one = ttk.Label(root, text='Primera nota')
label_two = ttk.Label(root, text='Segunda nota')
label_three = ttk.Label(root, text='Tercera nota')

# Textbox
text_note__one = tk.StringVar()
text_note__two = tk.StringVar()
text_note__three = tk.StringVar()
# Entry
entry_note_one = ttk.Entry(root, width=20, textvariable=text_note__one)
entry_note_two = ttk.Entry(root, width=20, textvariable=text_note__two)
entry_note_three = ttk.Entry(root, width=20, textvariable=text_note__three)

# Buttons
bt = ttk.Button(root, text='Evaluar', command=lambda: mean_student())

# Positions to elements
# Labels
label_title.grid(column=0, row=0)
label_one.grid(column=0, row=1)
label_two.grid(column=0, row=2)
label_three.grid(column=0, row=3)
label_result.grid(column=0, row=5)

# Entry
entry_note_one.grid(column=1, row=1)
entry_note_two.grid(column=1, row=2)
entry_note_three.grid(column=1, row=3)
# Buttons
bt.grid(column=0, row=4)

# Inicializar la ventana
root.mainloop()
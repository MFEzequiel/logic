# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk

# functions
def questios():
    rc = float(correct_answers.get())
    ri = float(incorrect_answers.get())
    rb = float(blank_answers.get())
    
    prc = rc * 3
    pri = ri * -1
    prb = rb * 0
    pf = prc + pri + prb
    question_correct_label_result.configure(text=f'Puntos de respuesta correcta: {prc}')
    question_incorrect_label_result.configure(text=f'Puntos de respuesta incorrecta: {pri}')
    question_blank_label_result.configure(text=f'Puntos de respuesta en blank: {prb}')
    all_question_result.configure(text=f'Puntos total de las respuestas: {pf}')

# Crear la ventana
root = tk.Tk()
root.title('Respuestas correctas, incorrectas y en blanco')
root.minsize(400, 200)
root.geometry('+500+80')

# Elements
# Labels
label_title = ttk.Label(root, text='Respuestas correctas, incorrectas y en blanco')
question_correct_label = ttk.Label(root, text='Respuesta correcta') 
question_incorrect_label = ttk.Label(root, text='Respuesta incorrecta')
question_blank_label = ttk.Label(root, text='Respuesta en blanco')

# Label configure
question_correct_label_result = ttk.Label(root, text='Puntos de respuesta correcta') 
question_incorrect_label_result = ttk.Label(root, text='Puntos de respuesta incorrecta')
question_blank_label_result = ttk.Label(root, text='Puntos de respuesta en blanco')
all_question_result = ttk.Label(root, text='Puntos total de las respuestas')

# TextBox
question_correct_text = ttk.Label(root, text='Respuesta correcta') 
question_incorrect_text = ttk.Label(root, text='Respuesta incorrecta')
question_blank_text = ttk.Label(root, text='Respuesta en blanco')

# Entry text
correct_answers = ttk.Entry(root, width=20, textvariable=question_correct_text)
incorrect_answers = ttk.Entry(root, width=20, textvariable=question_incorrect_text)
blank_answers = ttk.Entry(root, width=20, textvariable=question_blank_text)

# Buttons
bt = ttk.Button(root, text='Evaluar', command=lambda: questios())

# Positions to elements
# Labels
label_title.grid(column=0, row=0)
question_correct_label.grid(column=0, row=1)
question_incorrect_label.grid(column=0, row=2)
question_blank_label.grid(column=0, row=3)
#Labels configure
question_correct_label_result.grid(column=0, row=5)
question_incorrect_label_result.grid(column=0, row=6)
question_blank_label_result.grid(column=0, row=7)
all_question_result.grid(column=0, row=8)

# Entry text
correct_answers.grid(column=1, row=1)
incorrect_answers.grid(column=1, row=2)
blank_answers.grid(column=1, row=3)

# Buttons
bt.grid(column=0, row=4)
# Inicializar la ventana
root.mainloop()
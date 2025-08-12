# -*- coding: utf-8 -*-

# functions
def questios():
    rc = float(correct_answers.get())
    ri = float(incorrect_answers.get())
    rb = float(blank_answers.get())    
    
    prc = rc * 3
    pri = ri * -1
    prb = rb * 0
    pf = prc + pri + prb
    
    # agregar las variables a su correspondiente contenido
    question_correct_label_result.configure(text=f'Puntos de respuesta correcta: {}')
    question_incorrect_label_result.configure(text=f'Puntos de respuesta incorrecta: {}')
    question_blank_label_result.configure(text=f'Puntos de respuesta en blank: {}')
    all_question_result.configure(text=f'Puntos total de las respuestas: {}')

# Crear la ventana
root = 

# Configuración de la ventana 
root.title('Respuestas correctas, incorrectas y en blanco')
root.minsize(400, 200)
root.geometry('+500+80')
root.resizable(True, True)

# Elements
# Labels
label_title = tk.Label(root, text='')
question_correct_label = tk.Label(root, text='') 
question_incorrect_label = tk.Label(root, text='')
question_blank_label = tk.Label(root, text='')

# Label configure
question_correct_label_result = tk.Label(root, text='') 
question_incorrect_label_result = tk.Label(root, text='')
question_blank_label_result = tk.Label(root, text='')
all_question_result = tk.Label(root, text='Puntos total de las respuestas')

# TextBox
question_correct_text = tk.Label(root, text='Respuesta correcta') 
question_incorrect_text = tk.Label(root, text='Respuesta incorrecta')
question_blank_text = tk.Label(root, text='Respuesta en blanco')

# Entry text
correct_answers = tk.Entry(root, width=20, textvariable=question_correct_text)
incorrect_answers = tk.Entry(root, width=20, textvariable=question_incorrect_text)
blank_answers = tk.Entry(root, width=20, textvariable=question_blank_text)

# Buttons
bt = tk.Button(root, text='Evaluar')

# Positions to elements
# Labels
label_title.grid(column=0, row=0)
question_correct_label.grid(column=0, row=1)
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
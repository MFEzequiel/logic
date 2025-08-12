# -*- coding: utf-8 -*-

# función
def mean_student():
    mean = float(entry_note_one.get()) + float(entry_note_two.get()) + float(entry_note_three.get()) / 3
    label_result.configure(text=f'Promedio del estudiante: {mean}')

# Crear la ventana
root = tk.Tk()

# Configuración de la ventana 
root.title('promedio simple de un estudiante')
root.minsize(350, 120)
root.geometry('+500+180')
root.resizable(True, True)

# Elements
# Labels
label_title = tk.Label(root, text='Promedio simple de un estudiante')
label_result = tk.Label(root, text='Promedio del estudiante: ')
label_one = tk.Label(root, text='Primera nota')
label_two = tk.Label(root, text='Segunda nota')
label_three = tk.Label(root, text='Tercera nota')

# Textbox
text_note__one = tk.VarString()
text_note__two = tk.VarString()
text_note__three = tk.VarString()
# Entry
entry_note_one = tk.Entry(root, width=20, textvariable=text_note__three)
entry_note_two = tk.Entry(root, width=20, textvariable=text_note__one)
entry_note_three = tk.Entry(root, width=20, textvariable=text_note__two)

# Buttons
bt = tk.Button(root, text='Evaluar')

# Positions to elements
# Labels
label_title.grid(column=0, row=0)

# Entry
entry_note_three.grid(column=1, row=3)

# Buttons
bt.grid(column=0, row=4)

# Inicializar la ventana
root.mainloop()
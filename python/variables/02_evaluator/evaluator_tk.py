# -*- coding: utf-8 -*-
try:
  from tkinter import Tk, Label, Button, Entry, StringVar
except ImportError:
  print("Please install tkinter to run this script. You can do this by running 'pip install tk'.")

def calculate_points():
    # Get values from entries
    correct = float(text_correct.get())
    incorrect = float(text_incorrect.get())
    while_responses = float(text_while.get())
    
    # Calculate points
    point_correct = correct * 3
    point_incorrect = incorrect * -1
    point_while = while_responses * 0
    
    # Total points
    total_points = point_correct + point_incorrect + point_while

    # Display result
    label_points.config(text=f"Points Total: {total_points}")

root = Tk()
# config
root.title("Evaluator")
root.geometry("300x200")

# Elements
label_correct = Label(root, text="Correct Responses:")
label_incorrect = Label(root, text="Incorrect Responses:")
label_while = Label(root, text="Responses in While:")
label_points = Label(root, text="Points Total:")

# Textbox
text_correct = StringVar()
text_incorrect = StringVar()
text_while = StringVar()

# Entry
entry_correct = Entry(root, textvariable=text_correct, width=10)
entry_incorrect = Entry(root, textvariable=text_incorrect, width=10)
entry_while = Entry(root, textvariable=text_while, width=10)

# Button
btn = Button(root, text="Calculate", command=lambda: calculate_points())

# Postitions to elements
label_correct.grid(column=0, row=1, padx=10, pady=10)
entry_correct.grid(column=1, row=1, padx=10, pady=10)
label_incorrect.grid(column=0, row=2, padx=10, pady=10)
entry_incorrect.grid(column=1, row=2, padx=10, pady=10)
label_while.grid(column=0, row=3, padx=10, pady=10)
entry_while.grid(column=1, row=3, padx=10, pady=10)
label_points.grid(column=0, row=4, columnspan=2, padx=10, pady=10)
btn.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

# Start the GUI
root.mainloop()
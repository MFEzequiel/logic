# -*- coding: utf-8 -*-
try:
  from tkinter import Tk, Label, Button, Entry, StringVar
except ImportError:
  print("tkinter is not available. Please install it to run this script.")

def calculate_mean():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        n3 = float(entry3.get())
        mean = (n1 + n2 + n3) / 3
        result_var.config(text=f"Mean: {mean:.2f}")
    except ValueError:
        result_var.config(text="Please enter valid numbers.")

# Create the main window
root = Tk()
root.title("Mean Calculator")
root.minsize(300, 200)
# Elements
result_var = Label(root, text="Mean: ", font=("Arial", 14))
label_entre1 = Label(root, text="Enter first number:")
label_entre2 = Label(root, text="Enter second number:")
label_entre3 = Label(root, text="Enter third number:")

# Create input fields
text_entry1 = StringVar()
text_entry2 = StringVar()
text_entry3 = StringVar()

entry1 = Entry(root, textvariable=text_entry1)
entry2 = Entry(root, textvariable=text_entry2)
entry3 = Entry(root, textvariable=text_entry3)

button_calculate = Button(root, text="Calculate Mean", command=calculate_mean)
# Positions to elements
result_var.grid(row=4, column=0, columnspan=2, pady=10)

label_entre1.grid(row=1, column=0, sticky="w", padx=10)
label_entre2.grid(row=2, column=0, sticky="w", padx=10)
label_entre3.grid(row=3, column=0, sticky="w", padx=10)

entry1.grid(row=1, column=1)
entry2.grid(row=2, column=1)
entry3.grid(row=3, column=1)

button_calculate.grid(row=5, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
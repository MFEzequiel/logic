# -*- coding: utf-8 -*-
try:
  from tkinter import Tk, Label, Button, StringVar, Entry
except ImportError:
  print("Tkinter is not available. Please install it to run this script.")

def calculate_points():
  # Get values from entries
  won = float(text_won.get())
  lost = float(text_lost.get())
  draw = float(text_draw.get())
  
  # Calculate points
  point_won = won * 3
  point_lost = lost * 0
  point_draw = draw * 1
  
  # Total points
  total_points = point_won + point_lost + point_draw

  # Display result
  label_points.config(text=f"Points Total: {total_points}")

root = Tk()
# Config
root.title("Won Matches")
root.geometry("300x200")

# Elements
label_won = Label(root, text="Won Matches:")
label_lost = Label(root, text="Lost Matches:")
label_draw = Label(root, text="Draw Matches:")
label_points = Label(root, text="Points Total:")

# Textbox
text_won = StringVar()
text_lost = StringVar()
text_draw = StringVar()

# Entry
entry_won = Entry(root, textvariable=text_won, width=10)
entry_lost = Entry(root, textvariable=text_lost, width=10)
entry_draw = Entry(root, textvariable=text_draw, width=10)

# Button
btn = Button(root, text="Calculate", command=calculate_points)

# Positions to elements
label_won.grid(column=0, row=1, padx=10, pady=10)
label_lost.grid(column=0, row=2, padx=10, pady=10)
label_draw.grid(column=0, row=3, padx=10, pady=10)

entry_won.grid(column=1, row=1, padx=10, pady=10)
entry_lost.grid(column=1, row=2, padx=10, pady=10)
entry_draw.grid(column=1, row=3, padx=10, pady=10)

label_points.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

btn.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

# Start the GUI
root.mainloop()
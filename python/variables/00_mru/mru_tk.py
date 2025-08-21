# -*- coding: utf-8 -*-
try:
  from tkinter import Tk, Label, Button, Entry, StringVar
except ImportError:
  print("tkinter module not found. Please ensure you have Python's tkinter installed.")

# Function to calculate distance
def calculate_distance():
    try:
        velocity = float(velocity_entry.get())
        timer = float(timer_entry.get())
        distance = velocity * timer
        result_var.config(text=f"Distance: {distance:.2f} m")
    except ValueError:
        result_var.set("Please enter valid numbers.")

root = Tk()
# config root window
root.title("MRU Calculator")
root.minsize(300, 200)

# Elements
result_var = Label(root, text="Distance: ")
label_velocity = Label(root, text="Velocity (m/s):")
label_timer = Label(root, text="Time (s):")

text_velocity = StringVar()
velocity_entry = Entry(root, textvariable=text_velocity)
text_timer = StringVar()
timer_entry = Entry(root)

btn = Button(root, text="Calculate", command=lambda: calculate_distance())

# Postitions to elements
label_velocity.grid(row=0, column=0)
label_timer.grid(row=1, column=0)
velocity_entry.grid(row=0, column=1)
timer_entry.grid(row=1, column=1)
result_var.grid(row=3, columnspan=2)
btn.grid(row=2, columnspan=2)

# Start the GUI event loop
root.mainloop()
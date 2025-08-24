# -*- coding: utf-8 -*-
try:
  from tkinter import Tk, Label, Button, Entry, StringVar
  import matplotlib.pyplot as plt
  import numpy as np
except ImportError:
  print("Tkinter is not available. Please install it to run this script.")

# Function to calculate the distance between two pointsx
def calculate_distance(point_a_x, point_a_y, point_b_x, point_b_y):
    try:
        # Convert inputs to float
        point_a_x = float(point_a_x)
        point_a_y = float(point_a_y)
        point_b_x = float(point_b_x)
        point_b_y = float(point_b_y)

        # Calculate the distance using the distance formula
        distance = ((point_b_x - point_a_x) ** 2 + (point_b_y - point_a_y) ** 2) ** 0.5

        # Display the result
        label_result.config(text=f"Distance: {distance:.2f}")
        create_grafy(point_a_x, point_a_y, point_b_x, point_b_y)

    except ValueError:
        label_result.config(text="Invalid input. Please enter numeric values.")

def create_grafy(ax, ay, bx, by):
    # create the plot
    plt.figure()
    # red line with  circle
    plt.plot([ax, ay], [bx, by], 'ro-')
    plt.text(ax, ay, f"A: {ax}, {ay}", fontsize=9, verticalalignment='bottom')
    plt.text(bx, by, f"A: {bx}, {by}", fontsize=9, verticalalignment='bottom')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    # Equal scaling for both axes
    plt.axis('equal')
    plt.show()
   

root = Tk()
# config
root.title("Distance Between Points")
root.geometry("400x300")

# Elements
label_point_a_x = Label(root, text="Point A X:")
label_point_a_y = Label(root, text="Point A Y:")
label_point_b_x = Label(root, text="Point B X:")
label_point_b_y = Label(root, text="Point B Y:")
label_result = Label(root, text="Distance: ")

# Text variables for entries
text_point_a_x = StringVar()
text_point_a_y = StringVar()
text_point_b_x = StringVar()
text_point_b_y = StringVar()

# Entry fields for coordinates
entry_point_a_x = Entry(root, textvariable=text_point_a_x, width=10)
entry_point_a_y = Entry(root, textvariable=text_point_a_y, width=10)
entry_point_b_x = Entry(root, textvariable=text_point_b_x, width=10)
entry_point_b_y = Entry(root, textvariable=text_point_b_y, width=10)

# Button
btn_calculate = Button(root, text="Calculate Distance", command=lambda: calculate_distance(
    text_point_a_x.get(), text_point_a_y.get(), text_point_b_x.get(), text_point_b_y.get()))

# Positions to elements
label_point_a_x.grid(row=0, column=0, padx=10, pady=5)
label_point_a_y.grid(row=1, column=0, padx=10, pady=5)
label_point_b_x.grid(row=2, column=0, padx=10, pady=5)
label_point_b_y.grid(row=3, column=0, padx=10, pady=5)
label_result.grid(row=5, column=0, columnspan=3, pady=10)

entry_point_a_x.grid(row=0, column=1, padx=10, pady=5)
entry_point_a_y.grid(row=1, column=1, padx=10, pady=5)
entry_point_b_x.grid(row=2, column=1, padx=10, pady=5)
entry_point_b_y.grid(row=3, column=1, padx=10, pady=5)

btn_calculate.grid(row=4, column=0, columnspan=3, pady=10)

# Start the Tkinter event loop
root.mainloop()
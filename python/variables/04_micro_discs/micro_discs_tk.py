# -*- coding: utf-8 -*-
try:
  from tkinter import Tk, Label, Button, StringVar, Entry
except ImportError:
  print("Tkinter is not available. Please install it to run this script.")

# Function to calculate the number of micro discs needed
def calculate_micro_discs(micro_disc_capacity, hard_disk_capacity):
    try:
        # Convert inputs to float
        micro_disc_capacity = float(micro_disc_capacity)
        hard_disk_capacity = float(hard_disk_capacity) * 1024  # Convert GB to MB
        
        # Calculate the number of micro discs needed
        micro_discs_needed = hard_disk_capacity / micro_disc_capacity
        
        # Display the result
        label_result.config(text=f"Micro Discs Needed: {micro_discs_needed:.2f}")
    except ValueError:
        label_result.config(text="Invalid input. Please enter numeric values.")

root = Tk()
# config
root.title("Micro Discs")
root.geometry("300x200")

# elements
label_capacity = Label(root, text="Micro Disc Capacity (MB):")
label_capacity_value = Label(root, text="1.44")
label_hard_disk = Label(root, text="Hard Disk Capacity (GB):")
label_hard_disk_value = Label(root, text="21")
# result label
label_result = Label(root, text="Micro Discs Needed: ")

# textbox
text_capacity = StringVar()
text_hard_disk = StringVar()
# entry
entry_capacity = Entry(root, textvariable=text_capacity, width=10)
entry_hard_disk = Entry(root, textvariable=text_hard_disk, width=10)

# button
btn = Button(root, text="Calculate", command=lambda: calculate_micro_discs(text_capacity.get(), text_hard_disk.get()))


# layout
label_capacity.grid(row=0, column=0, padx=10, pady=5)
label_capacity_value.grid(row=0, column=1, padx=10, pady=5)
label_hard_disk.grid(row=1, column=0, padx=10, pady=5)
label_hard_disk_value.grid(row=1, column=1, padx=10, pady=5)
label_result.grid(row=2, column=0, columnspan=3, pady=10)

entry_capacity.grid(row=0, column=2, padx=10, pady=5)
entry_hard_disk.grid(row=1, column=2, padx=10, pady=5)

btn.grid(row=3, column=0, columnspan=3, pady=10)

# Start the Tkinter event loop
root.mainloop()
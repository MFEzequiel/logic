# -*- coding: utf-8 -*-
# Get the hard disk capacity from user input
# in megabytes
micro_discs_capacity = 1.44
# in gigabytes
hard_disk_capacity = float(input("Enter the hard disk capacity in gigabytes: "))

# Convert gigabytes to megabytes
hard_disk_capacity_mb = hard_disk_capacity * 1024

# Calculate the number of micro discs needed
micro_discs_needed = hard_disk_capacity_mb / micro_discs_capacity

# Display the result
print(f"Number of micro discs needed: {micro_discs_needed:.2f}")
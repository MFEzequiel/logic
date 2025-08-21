# -*- coding: utf-8 -*-
# point A and point B coordinates
# point A coordinates
point_a_x = float(input("Enter the x-coordinate of point A: "))
point_a_y = float(input("Enter the y-coordinate of point A: "))
# point B coordinates
point_b_x = float(input("Enter the x-coordinate of point B: "))
point_b_y = float(input("Enter the y-coordinate of point B: "))

# calculate the distance between point A and point B
distance = ((point_b_x - point_a_x) ** 2 + (point_b_y - point_a_y) ** 2) ** 0.5

# show the result
print(f"La distancia entre los puntos A({point_a_x}, {point_a_y}) y B({point_b_x}, {point_b_y}) es: {distance:.2f}")
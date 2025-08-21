# -*- coding: utf-8 -*-
# response won
response_won = float(input("Enter the number of won matches: "))
# response lost
response_lost = float(input("Enter the number of lost matches: "))
# response draw
response_draw = float(input("Enter the number of drawn matches: "))

# point won
point_won = response_won * 3
# point lost
point_lost = response_lost * 0
# point draw
point_draw = response_draw * 1

# point total
point_total = point_won + point_lost + point_draw
print("Points total: ", point_total)
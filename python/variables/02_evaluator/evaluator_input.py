# -*- coding: utf-8 -*-
# response correct
response_correct = float(input("Enter the number of correct responses: "))
# response incorrect 
response_incorrect = float(input("Enter the number of incorrect responses: "))
# response in while
response_while = float(input("Enter the number of responses in while: "))

# point correct
point_correct = response_correct * 3
# point incorrect
point_incorrect = response_incorrect * -1
# point in while
point_while = response_while * 0

# point total
point_total = point_correct + point_incorrect + point_while
print("Points total: ", point_total)
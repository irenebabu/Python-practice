"""
Write a Python function color_difference(color1, color2) that 
calculates the difference between two colors in RGB format.
Each color is represented as a tuple of three integers (R, G, B), where:

R = Red value (0-255)
G = Green value (0-255)
B = Blue value (0-255)

Compute the Euclidean distance between the two colors using the formula:
 d  = ((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)^1/2

Return the result rounded to 2 decimal places
"""

import math
def color_difference(color1, color2):
    x1, y1, z1 = color1
    x2, y2, z2 = color2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return round(distance,2)

print(color_difference((240,215,155),(140,60,136)))
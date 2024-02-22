import math
num_sides = int(input("Input number of sides: "))
side_length = int(input("Input the length of a side: "))
area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides)) #tan() function in the math module calculates the tangent of an angle in radians. The tangent of an angle is the ratio of the length of the opposite side to the length of the adjacent side in a right triangle.
print("The area of the polygon is:", round(area,1))
import math

# 1. EX
side = float(input("Enter the side of the square: "))
perimeter_square = 4 * side
area_square = side ** 2
print(f"Square - Perimeter: {perimeter_square}, Area: {area_square}")

# 2. EX
diameter = float(input("Enter the diameter of the circle: "))
circumference = math.pi * diameter
print(f"Circle - Circumference (Length): {circumference}")

# 3. EX
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
mean = (a + b) / 2
print(f"Mean of a and b: {mean}")

# 4. EX
sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2
print(f"Sum: {sum_ab}, Product: {product_ab}, Square of a: {square_a}, Square of b: {square_b}")

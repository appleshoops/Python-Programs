import math

diameter = float(input("Enter the diameter of the circle: "))
while diameter != 999:
    radius = diameter / 2
    print(f'The area of the circle is {(math.pow(radius, 2)) * math.pi}')
    print(f'The circumference of the circle is {math.pi * diameter}')
    diameter = float(input("Enter the diameter of the circle: "))
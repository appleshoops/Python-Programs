import math

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
pi = math.pi

volume = pi * radius * radius * height

print(f'The volume of the cylinder is {volume:.1f} units')
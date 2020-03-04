from math import tan, pi

from Basic_Functions import get_float, get_integer

print("""
This code calculates the area of a given regular polygon. Please enter the no of sides and length of each side.
""")
while True:
    no_of_sides = get_integer("Sides: ")
    side_length = get_float("Length: ")
    area = no_of_sides * (side_length ** 2) / (4 * tan(pi / no_of_sides))
    print(f"Area =  {area} square units")
    print('')

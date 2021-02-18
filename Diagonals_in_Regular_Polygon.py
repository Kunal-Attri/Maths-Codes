from Basic_Functions import get_integer

print("""
This code finds out the no of diagonals in a regular polygon. Please enter the no mof sides.
""")

while True:
    no_of_sides = get_integer("Sides: ", wrong_message="No of sides can only be an integer like 3, 4, 5, etc")
    if no_of_sides > 2:
        no_of_diagonals = no_of_sides * (no_of_sides - 3) // 2
        print(f"No of Diagonals = {no_of_diagonals}")
    else:
        print("A polygon cannot be formed with no of sides less than 3")
    print('')

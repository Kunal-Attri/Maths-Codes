print('''
This code is used to calculate the area of a triangle given it's sides.
You have to enter the sides of the triangle in any unit! Make sure all the sides are in same units.

Eg. Q. Side 1 = 120 cm; Side 2 = 1 m; Side 3 = 11000 mm
    Ten enter the data only in one of the above units like:
    Side 1 = 120 cm; Side 2 = 100 cm; Side 3 = 110 cm.

NOTE:- DO NOT WRITE THE UNITS. ONLY WRITE THE NUMERICAL VALUE OF THE SIDE LENGTH.''')

while True:
    try:
        a = int(input('First side: '))
        b = int(input('Second Side: '))
        c = int(input('Third Side: '))
    except ValueError:
        print('Invalid Input')
    else:
        if a + b <= c or a + c <= b or b + c <= a:
            print('Triangle with these given sides is not possible. Try making one yourself!')
        else:
            s = (a + b + c) / 2
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
            print(f'Area =  {area} square units')
        print()

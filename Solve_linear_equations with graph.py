import matplotlib.pyplot as plt

def lnr_cnsts(a):
    consts = []
    x1 = -1
    y1 = -1
    if 'x' in a:
        x1 = a.index('x')
    if x1 >= 1:
        l = a[:x1]
    elif x1 == 0:
        l = 1
    else:
        l = 0
    if l == '+':
        l = 1
    elif l == '-':
        l = -1
    l = float(l)
    consts.append(l)
    if 'y' in a:
        y1 = a.index('y')
    if y1 >= 1:
        m = a[x1 + 1:y1]
    elif y1 == 0:
        m = 1
    else:
        m = 0
    if m == '+':
        m = 1
    elif m == '-':
        m = -1
    m = float(m)
    consts.append(m)
    if y1 != -1:
        if len(a) - 1 != y1:
            n = a[y1 + 1:]
        else:
            n = 0
    else:
        if len(a) - 1 != x1:
            n = a[x1 + 1:]
        else:
            n = 0
    n = float(n)
    consts.append(n)
    return consts


print('''
You can get solution of any two pair of linear equations using this program.
Please enter equations in the form "ax + by + c"''')
while True:
    en1 = input('Equation 1: ')
    en2 = input('Equation 2: ')
    eqn1 = ''
    eqn2 = ''
    e1 = en1.split()
    e2 = en2.split()
    for i in e1:
        eqn1 += i
    for i in e2:
        eqn2 += i

    constants1 = lnr_cnsts(eqn1)
    constants2 = lnr_cnsts(eqn2)
    a1, b1, c1 = constants1[0], constants1[1], constants1[2]
    a2, b2, c2 = constants2[0], constants2[1], constants2[2]

    # print(a1, a2, b1, b2, c1, c2)

    if a1 / a2 == b1 / b2 and b1 / b2 == c1 / c2:
        print('The given system of equations have infinitely many solutions.')
    elif (a1 / a2 == b1 / b2 and b1 / b2 != c1 / c2) or (a2 / a1 == b2 / b1 and b2 / b1 != c2 / c1):
        print('The given system of linear equations have no solution throughout the range!')
    elif a1 / a2 != b1 / b2:
        y = ((a2 * c1) - (a1 * c2)) / ((a1 * b2) - (a2 * b1))
        x = ((b2 * c1) - (b1 * c2)) / ((a2 * b1) - (a1 * b2))
        print(f'''Solutions:-  
x = {x}  y = {y}''')
        for i in range(2):
            xval = []
            yval = []
            l = 10
            start = x - l
            end = x + l
            resolution = 0.01
            temp = start
            while temp <= end:
                xval.append(temp)
                if i == 0:
                    yval.append(((-c1) - (a1 * temp)) / b1)
                else:
                    yval.append(((-c2) - (a2 * temp)) / b2)
                temp += resolution
            plt.plot(xval, yval)
        plt.legend([eqn1, eqn2])
        plt.grid(True)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
    print('')

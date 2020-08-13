import math

trigo_functions = ["cosec", "sin", "cos", "tan", "cot", "sec"]
unn = [" ", "(", ")", "cosec", "sin", "cos", "tan", "cot", "sec"]

func = ""
theta = 0.0

print("""
This code can easily be used to find the trigonometric ratios
of angles in degrees.
You can try it just by typing thetrigonometric ratio name and
the angle in degrees.
Eg. sin(30) or cos40 or cot 98

You can also find values of many trigonometric ratios by
separating them with a comma.
Eg. cos30, sin30, tan45, cot87, cosec25
""")


def function(string):
    global trigo_functions
    for i in trigo_functions:
        if i in string:
            return i


def angle(string):
    global unn
    for i in unn:
        if i in string:
            string = string.replace(i, "")
    if "." in string:
        return float(string)
    else:
        return int(string)
    

def measure(string):
    global func, theta
    func = function(string)
    theta = angle(string)
    if func == "cosec":
        val = 1 / math.sin(math.radians(theta))
    elif func == "sin":
        val = math.sin(math.radians(theta))
    elif func == "cos":
        val = math.cos(math.radians(theta))
    elif func == "tan":
        val = math.tan(math.radians(theta))
    elif func == "cot":
        val = 1 / math.tan(math.radians(theta))
    elif func == "sec":
        val = 1 / math.cos(math.radians(theta))
    return round(val, 3)


while True:
    ques = input("Question: ")
    lis = ques.split(",")
    for i in lis:
        value = measure(i)
        print(f"{func}({theta}) = {value}")
    print("")

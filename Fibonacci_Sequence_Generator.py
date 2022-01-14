# Fibonacci Sequence generator

def get_integer(msg="Number: ", wrng_msg="Invalid Input"):
    try:
        i = int(input(msg))
    except ValueError:
        print(wrng_msg)
        return get_integer(msg, wrng_msg)
    else:
        return i


terms = get_integer('No of terms: ')
prev_first = 0
prev_second = 1

print(prev_first)
print(prev_second)

while 2 < terms:
    new = prev_second + prev_first
    prev_first = prev_second
    prev_second = new
    print(new)
    terms -= 1

input("Press enter to exit...")

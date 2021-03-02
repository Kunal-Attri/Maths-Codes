from Basic_Functions import get_integer

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

from Basic_Functions import into_integer, isprime

while True:
    ini_no = input("No. to be checked for prime: ")
    if ini_no == "exit":
        break
    else:
        ini_no = into_integer(ini_no, 'Invalid Input')
        if type(ini_no) == int:
            if isprime(ini_no):
                print(f"{ini_no} is a prime no.")
                print('')
            else:
                print(f"{ini_no} is not a prime no.")
                print('')
        else:
            print('')

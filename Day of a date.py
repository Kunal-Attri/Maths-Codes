# F=(yrCode+monthCode+centuryCode+dateNo-leapYrCode)%7

while True:
    inp = input("Date: ")
    if "." in inp:
        inp = inp.split(".")
    elif "-" in inp:
        inp = inp.split("-")
    elif "/" in inp:
        inp = inp.split("/")
    else:
        inp = inp.split()
    
    # Yr code = (YY + (YY // 4)) mod 7
    yy = int(inp[-1][-2:])
    yrCode = (yy + (yy // 4)) % 7
    
    # Month code by dataset
    monthDataset = "033614625035"
    monthCode = int(monthDataset[int(inp[1]) - 1])

    # Century code by dataset
    centuryDataset = "4206420"
    if int(inp[-1][:-2]) < 17:
        centuryCode = (18 - int(inp[-1][:-2])) % 7
    else:
        centuryCode = int(centuryDataset[int(inp[-1][:-2]) - 17])

    # Leap yr code
    yr = int(inp[-1])
    if yr % 400 == 0:
        leapYrCode = 1
    elif yr % 4 == 0 and yr % 100 != 0:
        leapYrCode = 1
    else:
        leapYrCode = 0

    # Date number
    dateNo = int(inp[0])

    resultDataset = {0: "Sunday",
                     1: "Monday",
                     2: "Tuesday",
                     3: "Wednesday",
                     4: "Thursday",
                     5: "Friday",
                     6: "Saturday"}

    result = (yrCode + monthCode + centuryCode + dateNo - leapYrCode) % 7
    print(f"Its a {resultDataset[result]}")
    print()

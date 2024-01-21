def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                return True
    return leap


year = int(input("Year: "))

if is_leap(year):
    print("Leap")
else:
    print("Not Leap")

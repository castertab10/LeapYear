#Check whether a year is a leap year or not

year = int(input("This is a leap year checker. Input a year you wish to check whether it is a leap year or not: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Year ", year, "is a leap year!")
        else:
             print("Year ", year, "is not a leap year!")
    else:
        print("Year ", year, "is a leap year!")
else:
    print("Year ", year, "is not a leap year!")
    
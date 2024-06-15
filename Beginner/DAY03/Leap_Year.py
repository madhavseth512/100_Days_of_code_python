# Here we have to take input as year number and print weather it is a leap year or not
# A leap year is one that is divisible by 4, but not divisible by 100, but in all those years which are
# divisible by 4 and not by 100, those which are divisible by 400 are considered as leap year

year = int(input("Enter the year number you want to check as Leap Year"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a Leap Year")
else:
    print("It is not Leap Year")


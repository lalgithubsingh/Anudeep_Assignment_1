#input year through keyboard
year = (int)(input("Enter a year: "))

# Check if the year is a leap year
# Check if divisible by 4
if(year % 4 == 0):
    # Check if divisible by 100
    if(year % 100 == 0):
        print(year,"is divisible by 100")
        # Check if divisible by 400
        if year % 400 == 0:  
            print(year,"is divisible by 400")
        else:
            print(year,"is not a leap year.")
    else:
        print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")

#input number through keyboard
number = (int)(input("Enter a number: "))

# Check if the number is positive
if(number > 0):
    # Check if the number is a two-digit or three-digit number
    if(number >= 10 and number < 100):
        print("The number is a positive two-digit number.")
    elif(number >= 100 and number < 1000):
        print("The number is a positive three-digit number.")
    else:
        print("The number is positive, but not a two-digit or three-digit number.")
else:
    print("The number is not positive.")

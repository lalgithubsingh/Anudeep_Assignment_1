#input number through keyboard
number = (int)(input("Enter a number: "))

# Check the number of digits
if(number >= 0 and number < 10):
    print("The number is a one-digit number.")
elif(number >= 10 and number < 100):
    print("The number is a two-digit number.")
else:
    print("The number has more than two digits.")

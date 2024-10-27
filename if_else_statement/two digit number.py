#input number through keyboard
number = int(input("Enter a number: "))

# Check if the number is a two-digit number
if 10 <= number <= 99 or -99 <= number <= -10:
    print("The number is a two-digit number.")
else:
    print("The number is not a two-digit number.")

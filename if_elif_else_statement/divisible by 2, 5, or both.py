#input number through keyboard
number = int(input("Enter a number: "))

# Check divisibility by 2, 5, or both.
if(number % 2 == 0 and number % 5 == 0):
    print("The number is divisible by both 2 and 5.")
elif(number % 2 == 0):
    print("The number is divisible by 2.")
elif(number % 5 == 0):
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 2 or 5.")

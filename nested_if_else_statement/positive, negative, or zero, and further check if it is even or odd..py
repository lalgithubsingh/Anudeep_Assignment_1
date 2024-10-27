#input number through keyboard
number = float(input("Enter a number: "))

#Check if the number is positive, negative, or zero
if(number > 0):
    print("The number is positive.")
    # Check if the number is even or odd
    if(number % 2 == 0):
        print("It is an even number.")
    else:
        print("It is an odd number.")
elif(number < 0):
    print("The number is negative.")
    # Check if the number is even or odd
    if(number % 2 == 0):
        print("It is an even number.")
    else:
        print("It is an odd number.")
else:
    print("The number is zero.")


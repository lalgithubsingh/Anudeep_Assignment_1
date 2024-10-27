#input number through keyboard
number = (float)(input("Enter a number: "))

# Check if the number is positive
if(number > 0):
    print("The number is positive.")
    
    # Check if the number is a multiple of 5
    if(number % 5 == 0):
        print("The number is a multiple of 5.")
    else:
        print("The number is not a multiple of 5.")
else:
    print("The number is not positive.")

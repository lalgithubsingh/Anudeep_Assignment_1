#input number through keyboard
number = int(input("Enter a number: "))

#Check if a number is divisible by 4, 6, both, or neither
if(number % 4 == 0 and number % 6 == 0):
    print("The number is divisible by both 4 and 6.")
elif(number % 4 == 0):
    print("The number is divisible by 4.")
elif(number % 6 == 0):
    print("The number is divisible by 6.")
else:
    print("The number is divisible by neither 4 nor 6.")

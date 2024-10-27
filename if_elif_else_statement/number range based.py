#input number through keyboard
number = float(input("Enter a number: "))

#Check if the number is small, medium, or large
if(number > 10000):
    print("The number is large.")
elif(number >=100 and number <= 10000):
    print("The number is medium.")
else:
    print("The number is small.")

#input the three numbers through keyboard
num1 = (float)(input("Enter the first number: "))
num2 = (float)(input("Enter the second number: "))
num3 = (float)(input("Enter the third number: "))

# Determine the largest number 
if(num1 >= num2 and num1 >= num3):
    print("The largest number is:", num1)
elif(num2 >= num1 and num2 >= num3):
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)


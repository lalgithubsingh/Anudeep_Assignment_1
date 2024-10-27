#input number through keyboard
number = (int)(input("Enter the number:"))

#check if number is divisible by 2
if(number % 2 == 0):
    print("Yes,",number," is divisible by 2")
    #check if number is divisible by 4
    if(number % 4 == 0):
        print("Yes,",number," is divisible by 4")
    else:
        print("Yes,",number," is not divisible by 4")
    
else:
    print("Oops!",number," is not divisible by 2")

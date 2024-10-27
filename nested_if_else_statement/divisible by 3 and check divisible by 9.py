#input number through keyboard
number = (int)(input("Enter the number:"))

#check if number is divisible by 2
if(number % 3 == 0):
    print("Yes,",number," is divisible by 3")
    #check if number is divisible by 4
    if(number % 9 == 0):
        print("Yes,",number," is divisible by 9")
    else:
        print("Yes,",number," is not divisible by 9")
    
else:
    print("Oops!",number," is not divisible by 3")

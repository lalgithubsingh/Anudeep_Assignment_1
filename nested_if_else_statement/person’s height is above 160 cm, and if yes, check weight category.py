#input height and weight through keyboard
height = (float)(input("Enter your height in cm: "))
weight = (float)(input("Enter your weight in kg: "))

#Check if the height is above 160 cm
if(height > 160):
    #check weight category
    if(weight < 50):
        print("You are underweight.")
    elif(weight >= 50 and weight <= 70):
        print("You have a normal weight.")
    else:
        print("You are overweight.")
else:
    print("Your height is not above 160 cm.")

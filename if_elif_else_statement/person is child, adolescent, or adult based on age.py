#input age through keyboard
age =(int)(input("Enter your age: "))

# Determine the category based on age
if(age < 0):
    print("Age cannot be negative.")
elif(age <= 12):
    print("You are a child.")
elif(age <= 17):
    print("You are an adolescent.")
else:
    print("You are an adult.")

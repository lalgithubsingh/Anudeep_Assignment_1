#input age through keyboard
age = int(input("Enter your age: "))

# Determine life stage(child, teen, adult, senior)based on age
if(age < 0):
    print("Invalid age.")
elif(age <= 12):
    print("You are a child.")
elif(age <= 19):
    print("You are a teen.")
elif(age <= 64):
    print("You are an adult.")
else:
    print("You are a senior.")

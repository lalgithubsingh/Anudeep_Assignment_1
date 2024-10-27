#input weight and height through keyboard
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)
print("Your BMI is:",bmi)

# Determine weight category
if(bmi < 18.5):
    print("Person’s weight category is Underweight.")
elif(18.5 <= bmi < 24.9):
    print("Person’s weight category is Normal weight")
elif(25 <= bmi < 29.9):
    print("Person’s weight category is Overweight")
else:
    print("Person’s weight category is Obese")


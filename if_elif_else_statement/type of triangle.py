#input three sides of triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check the type of triangle (equilateral, isosceles, or scalene)
if(side1 == side2 == side3):
    print("The triangle is equilateral.")
elif(side1 == side2 or side2 == side3 or side1 == side3):
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")

#input employment type through keyboard
employment_type = input("Enter employment type (full-time/part-time): ").strip().lower()

# Check if the employee is full-time or part-time
if(employment_type == "full-time"):
    # If full-time, check if they are eligible for a bonus
    bonus_eligible = input("Is the employee eligible for a bonus? (yes/no): ").strip().lower()
    if(bonus_eligible == "yes"):
        print("The employee is a full-time employee and is eligible for a bonus.")
    else:
        print("The employee is a full-time employee but is not eligible for a bonus.")
elif(employment_type == "part-time"):
    print("The employee is a part-time employee.")
else:
    print("Invalid input. Please enter 'full-time' or 'part-time'.")

#input from user through keyboard
employed = (input)("Are you employed? (yes/no): ")

# Check if the person is employed
if(employed == "yes"):
    #input salary from user
    salary = (float)(input("Enter your salary: "))

    # Determine salary range
    if(salary < 30000):
        print("Your salary range is low.")
    else:
        if(salary <= 70000):
            print("Your salary range is medium.")
        else:
            print("Your salary range is high.")
else:
    print("You are not employed.")

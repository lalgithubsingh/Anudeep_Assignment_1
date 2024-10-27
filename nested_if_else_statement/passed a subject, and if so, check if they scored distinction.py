#input score through keyboard
score = (float)(input("Enter the student's score: "))

# Check if the student has passed
if(score >= 40):  # Assuming passing mark is 40
    print("The student has passed.")
    
    # Check if the student scored distinction
    if(score >= 75):
        print("The student has scored distinction.")
    else:
        print("The student has not scored distinction.")
else:
    print("The student has not passed.")

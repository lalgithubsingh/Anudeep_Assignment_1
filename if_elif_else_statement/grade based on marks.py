#input marks through keyboard
marks = (int)(input("Enter your marks:"))

#check the grade of student's based on their marks.
if(marks>=75):
    print("Congratulations! You got A grade. Keep it up!")
elif(marks>=65 and marks<75):
    print("Yeah!You got B grade.")
elif(marks>=55 and marks<65):
    print("You got C grade.")
elif(marks>50 and marks<55):
    print("You got D grade.")
else:
    print("Oops!You got F grade. You need more practice.")
        

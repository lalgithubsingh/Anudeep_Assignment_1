#input the percentage through keyboard
percentage =(float)(input("Enter the percentage: "))

# Assign performance rating based on the percentage(excellent, good, average, poor)
if(percentage >= 90):
    print("Performance Rating is Excellent.")
elif(percentage >= 75):
    print("Performance Rating is Good.")
elif(percentage >= 50):
    print("Performance Rating is Average.")
else:
    print("Performance Rating is Poor.")


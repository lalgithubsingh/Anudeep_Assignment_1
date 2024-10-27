# Take input from the user
day = input("Enter the day of the week: ")

# Check if the day is a weekday or weekend
if(day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday"):
    print("It is a weekday.")
elif(day == "saturday" or day == "sunday"):
    print("It is a weekend.")
else:
    print("Invalid day entered.")

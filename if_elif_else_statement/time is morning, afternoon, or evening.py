#input time through keyboard
time = input("Enter the time in HH:MM format (24-hour): ")

#Convert the hours to an integer
hours = int(time.split(':')[0])

# Determine if the time is morning, afternoon, or evening
if(hours >= 0 and hours < 12):
    print("It's morning.")
elif(hours >= 12 and hours < 18):
    print("It's afternoon.")
elif(hours >= 18 and hours < 24):
    print("It's evening.")
else:
    print("Invalid time. Please enter a valid time in HH:MM format.")

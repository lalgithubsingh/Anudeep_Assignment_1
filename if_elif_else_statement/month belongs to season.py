#input month through keyboard
month =(input("Enter the name of a month: "))

# Check the season based on the month
if(month == "december" or month == "january" or month == "february"):
    print("This month belongs to winter.")
elif(month == "march" or month == "april" or month == "may"):
    print("This month belongs to spring.")
elif(month == "june" or month == "july" or month == "august"):
    print("This month belongs to summer.")
elif(month == "september" or month == "october" or month == "november"):
    print("This month belongs to fall.")
else:
    print("Invalid month entered. Please enter a valid month name.")

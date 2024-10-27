#input year through keyboard
year = int(input("Enter a year: "))

# Determine the century of the given year
if(year >= 1801 and year <= 1900):
    print("The year is in the 19th century.")
elif(year >= 1901 and year <= 2000):
    print("The year is in the 20th century.")
elif(year >= 2001 and year <= 2100):
    print("The year is in the 21st century.")
else:
    print("The year is not in the 19th, 20th, or 21st century.")

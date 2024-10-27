#input the year through keyboard
year = int(input("Enter a year: "))

# Check if the year is a leap year
if year % 4 == 0:
    print(f"{year} is a leap year.")

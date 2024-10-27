# Define the legal speed limit
legal_speed_limit = 60  

#input car's speed through keyboard
car_speed = (float)(input("Enter the car's speed in km/h: "))

# Check if the car is speeding
if(car_speed > legal_speed_limit):
    print("The car is speeding.")
    
    # Check if the speed exceeds the legal limit by more than 10 km/h
    if(car_speed > legal_speed_limit + 10):
        print("The car is exceeding the legal limit by more than 10 km/h.")
    else:
        print("The car is within 10 km/h of the legal limit.")
else:
    print("The car is not speeding.")

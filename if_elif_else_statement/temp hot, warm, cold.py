#input temperature through keyboard
temperature = (float)(input("Enter the temperature:"))

#Check if a temperature is hot, warm, or cold.
if(temperature > 35):
    print("The temperature is hot.")
elif(temperature >= 10 and temperature <= 35):
    print("The temperature is warm.")
else:
    print("The temperature is cold.")

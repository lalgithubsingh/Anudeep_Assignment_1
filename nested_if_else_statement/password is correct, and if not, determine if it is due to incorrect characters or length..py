#Define the stored password
stored_password = "mypassword@123"

#Input password through keyboard
entered_password = (input("Please enter your password: "))

#Check if the entered password matches the stored password
if(entered_password == stored_password):
    print("Access Granted: Your password is correct!")
else:
    # Check for length
    if(len(entered_password) < len(stored_password)):
        print("Access Denied: Incorrect password. The password is too short.")
    elif(len(entered_password) > len(stored_password)):
        print("Access Denied: Incorrect password. The password is too long.")
    else:
        print("Access Denied: Incorrect password. Please check for incorrect characters.")

#Define the stored password
stored_password = "mypassword@123"

#input password through keyboard
entered_password = input("Please enter your password: ")

#Check if the entered password matches the stored password
if entered_password == stored_password:
    print("Access Granted: Your password is correct!")
else:
    print("Access Denied: Incorrect password.")

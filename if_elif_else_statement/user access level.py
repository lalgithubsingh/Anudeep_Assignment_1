#input access level from user through keyboard 
access_level = input("Enter your access level (admin, user, guest): ")

# Check the access level
if(access_level == "admin"):
    print("Access granted: Welcome, Admin!")
elif(access_level == "user"):
    print("Access granted: Welcome, User!")
elif(access_level == "guest"):
    print("Access granted: Welcome, Guest!")
else:
    print("Access denied: Invalid access level.")

#input age through keyboard
age = int(input("Enter your age: "))

# Determine if the person can vote
if(age >= 18):
    print("You are eligible to vote.")
    # Check if the person is eligible for senior voting
    if(age >= 65):
        print("You are also eligible for senior voting.")
    else:
        print("You are not eligible for senior voting.")
else:
    print("You are not eligible to vote.")

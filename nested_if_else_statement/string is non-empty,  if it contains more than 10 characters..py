# input of text through keyboard
text = input("Enter a string: ")

# Check if the string is non-empty
if text:
    print("The string is non-empty.")
    
    #Now check if the string has more than 10 characters
    if(len(text)>10):
        print("The string contains more than 10 characters.")
    else:
        print("The string contains 10 or fewer characters.")
        
else:
    print("The string is empty.")

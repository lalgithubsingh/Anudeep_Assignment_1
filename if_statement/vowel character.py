# input the character through keyboard
character = input("Enter a character: ")  
  
# Creating a list of vowels  
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
  
# Check if the character is a vowel
if character in vowels:  
    print(f"The character '{character}' is a vowel!")  

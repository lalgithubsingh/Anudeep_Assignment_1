# Input number through keyboard
number = int(input("Enter a number: "))

# Check if the number is in the range of 1 to 100
if(number >= 1 and number <= 100):
    print("The number is in the range of 1 to 100.")
    
    # Check if the number is prime
    if(number <= 1):
     print("The number is not a prime number.")
    else:
     is_prime = True  # Assume the number is prime

    # Check for factors starting from 2
    if(number == 2):
        is_prime = True  # 2 is prime
    elif(number % 2 == 0):
        is_prime = False  # Even number greater than 2 is not prime
    else:
        # Check odd numbers starting from 3
        i = 3
        while i < number:  # Continue until i is less than the number
            if number % i == 0:  # If number is divisible by i
                is_prime = False  # Not prime
                break
            i += 2  # Check only odd numbers

    if is_prime:
        print("The number is a prime number.")
    else:
        print("The number is not a prime number.")
        
else:
    print("The number is outside the range of 1 to 100.")

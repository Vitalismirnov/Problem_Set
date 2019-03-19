# This is a work by
# Vitalijs Smirnovs
# Stydent ID # g00317774

# Problem 5: Write a program that asks the user to input a positive integer and tells the user 
# whether or not the number is a prime.

# Ask for a user input
num = int(input("Please, enter positive integer: "))

# Code adapted from https://docs.python.org

# Check for divisorsstarting from 2 to the number itself
for x in range (2, num):
    # If an input number is divided by a number in range without a remiander, them break the loop
    if num % x == 0:
        break
 # Otherwise (if all divisors in range produce an output with a remaider), print the message:       
else:
    print("That is a prime.")        
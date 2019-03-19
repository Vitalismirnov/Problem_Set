# This is a work by
# Vitalijs Smirnovs
# Stydent ID # g00317774

# Problem 7: Write a program that takes a positive floating point number as input and outputs
#an approximation of it's square root

# Asks a user for an input in float format
i = float(input("Please enter a positive number: " ))
# Calculate a square root of i and round to 1 decimal point 
sqr=round((i**0.5), 1)
# Print the result 
print("The square root of" " " + str(i) + " " " is approx" + " " + str(sqr))
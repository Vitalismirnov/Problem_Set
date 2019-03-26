# This is a work by
# Vitalijs Smirnovs
# Stydent ID # g00317774

# Problem 1 :
# Solution

# Ask user for input
# Use int() as integer is needed
# This is a work by
# Vitalijs Smirnovs
# Stydent ID # g00317774

# Problem 1: Write a proram that asks the user to input any positive integer 
# Solution:
# ask a user to inpit a number 
num = int(input("Please, enter a positive integer: ")) 

# create a list of numbers between 1 and inputed number
# range function does not include the last number specified
i=list(range(1,num+1))

# function sum adds up all the numbers in the list 
Sum = sum(i)
# print the result on the screen
print(Sum)  
     
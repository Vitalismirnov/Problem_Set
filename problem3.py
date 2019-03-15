# This is a work by
# Vitalijs Smirnovs
# Stydent ID # g00317774

# Problem 3: Write a program that prints all numbers between 1000 and 10000 
# that are divisible by 6 but not 12

# Solution

# Python has built in list in for loops which is handy.
# Using range function I wrote for loop to check numbers 
# in specified range for qualifying conditions
for i in range(1000,10001):

    # there are two conditions to check: 
    # 1.  if a number in range divides without remainder into 6 
    # 2. if a number does not divide  into 12 without remainder  
    # both conditions are to satisfy simulteniously
    if (i%6)==0 and (i%12)!=0:

       # print each number that satisfies the conditions
       print(i)

# This is a work by
# Vitalijs Smirnovs
# Stydent ID # g00317774

# Problem 2 : Write a program that outputs wether or not today is a day that begins with the letter T
# An example of running thisprogram on a Tuesdayis as follow

# Solution
# download a daytime library
import datetime

# The output is an Integer which is within the range of 0 - 6 indicating Monday as 0
if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3:

# print message if one of the conditions above is satisfied
  print("Yes - today begins with a T.")

# otherwise, print the message below
else:
  print("No - today does not begin with a T.")
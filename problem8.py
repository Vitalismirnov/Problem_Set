# This is a work by
# Vitalijs Smirnovs
# Stydent ID # g00317774

# Problem 8: Write a program that outputs today's date and time in the 
# format "Monday, January 10th 2019 at 1:15pm"


import datetime

t = datetime.datetime.now()
# strftime format used to set todays date,month, year and tim 
print(t.strftime("%A, %B %dth %Y at %I:%M%p"))
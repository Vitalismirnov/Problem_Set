# This is a work by
# Vitalijs Smirnovs
# Stydent ID # g00317774

# Problem 6: Write a programme that takes a user input string and outputs every secod word
# Chater 3: Introducing Lists; book "Python Crash Course" by Eric Matthes

# Aks a user to input a sentense, safe in a variable user_sentense
user_sentense = input("Please, enter a sentense: ")
#create a list of separate strings from a provided sentense
new = user_sentense.split(' ')
# Print every second word on the list without square brackets and commas
# here indexing a list is very useful ([1::2]) as it allows to print starting from a 2nd element(word) 
# to the end of the list by skipping one
print(*new[1::2], sep=" " )


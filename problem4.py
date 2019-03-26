# This is a work by
# Vitalijs Smirnovs
# Stydent ID # g00317774

# Problem 4:
# Solution: write a program that asks the user o input any positive
num = int(input("Please enter a positive integer: " ))
mylist=[num]
i=num
while i!=1:
    if (num%2==0):
        num = num//2
        mylist.append(num)
      
    else:
        num = num * 3 + 1
        mylist.append(num)
    i=num
print(mylist)   
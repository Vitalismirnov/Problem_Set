
# import matplotlib.pyplot module, give a name of plt for shorter commands
import matplotlib.pyplot as plt

# define a range of x as a list of numvers
x = list(range(0,5))
# Python has a built in calculations for lists
y1 = [x for x in x]
y2 = [x**2 for x in x]
y3 = [2**x for x in x]

# splot functions
plt.plot(x, y1, c="red")
plt.plot(x, y2, c="blue")
plt.plot(x, y3, c="green")
# display 
plt.show()
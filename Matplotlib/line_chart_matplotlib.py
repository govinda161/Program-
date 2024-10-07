import matplotlib.pyplot as plt 
# data to display on plots 
x = [2, 1.25, 1.25, 2, 2, 1.75] 
y = [3, 3, 1.50, 1.50, 2, 2] 

# This will plot a simple line chart
# with elements of x as x axis and y
# as y axis
plt.plot(x, y)
plt.title("Line Chart")

# Adding the legends
plt.legend(["Line"])
plt.show()

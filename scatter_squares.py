import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c =y_values, cmap=plt.cm.Blues, edgecolor = 'none', s=10)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels and range for axis.
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])

plt.show()
# Saving your plots automatically, (filename, trims extra whitespace from the plot)
# plt.savefig('square_plot.png', bbox_inches='tight')

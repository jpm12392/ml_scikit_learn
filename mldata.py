import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5,6,7,8,9,10]
y = [2, 4, 6, 8, 10,12,14,16,18,20]

# Line plot
plt.plot(x, y, label='Line Plot')

# Scatter plot
plt.scatter(x, y, color='red', label='Scatter Plot')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Matplotlib Demo Ex.')

# Add legend
plt.legend()

# Show the plot
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
tips = sns.load_dataset('tips')

# Bar plot
sns.barplot(x='day', y='total_bill', data=tips)

# Add labels and title
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.title('Seaborn Example')

# Show the plot
plt.show()
import matplotlib.pyplot as plt
# Market share data
manufactures = ['Samsung', 'Apple', 'Realme', 'Vivo', 'Others']
market_share = [20, 30, 25, 18, 15]
# Create a pie chart
colors = ['blue', 'yellow', 'green', 'pink', 'grey']
# Create a pie chart
plt.pie(market_share, labels=manufactures, colors=colors, autopct ='%.2f')
# Title
plt.title('Smartphone Market Share')
# Show the pie chart
plt.show()


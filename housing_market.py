# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("housing_data.csv")

# Show first rows
print("Dataset Preview:")
print(data.head())

# Show basic info
print("\nDataset Info:")
print(data.info())

# Average house price
print("\nAverage House Price:", data["Price"].mean())

# Maximum and minimum price
print("Highest Price:", data["Price"].max())
print("Lowest Price:", data["Price"].min())

# Scatter plot
plt.figure(figsize=(8,5))
plt.scatter(data["Income"], data["Price"])

plt.xlabel("Income")
plt.ylabel("House Price")
plt.title("Housing Market Trends")

plt.show()
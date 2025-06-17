#Homework 1: Working with Basic DataFrame
import pandas as pd
import numpy as np

# Data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Rename columns
df.rename(columns={'Name': 'first_name', 'Age': 'age'}, inplace=True)

# Print first 3 rows
print("First 3 rows:\n", df.head(3))

# Average age
print("\nAverage age:", df['age'].mean())

# Print only first_name and City
print("\nFirst Name and City:\n", df[['first_name', 'City']])

# Add random salary column
df['Salary'] = np.random.randint(40000, 90000, size=len(df))

# Summary statistics
print("\nSummary statistics:\n", df.describe(include='all'))

#Homework 2: Sales and Expenses DataFrame
# Sales and Expenses data
sales_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_df = pd.DataFrame(sales_data)

# Max values
print("Max Sales:", sales_df['Sales'].max())
print("Max Expenses:", sales_df['Expenses'].max())

# Min values
print("Min Sales:", sales_df['Sales'].min())
print("Min Expenses:", sales_df['Expenses'].min())

# Average values
print("Average Sales:", sales_df['Sales'].mean())
print("Average Expenses:", sales_df['Expenses'].mean())

#Homework 3: Monthly Costs by Category
# Monthly costs data
costs_data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

costs = pd.DataFrame(costs_data)

# Set 'Category' as index
costs.set_index('Category', inplace=True)

# Max per category
print("Max per category:\n", costs.max(axis=1))

# Min per category
print("\nMin per category:\n", costs.min(axis=1))

# Average per category
print("\nAverage per category:\n", costs.mean(axis=1))

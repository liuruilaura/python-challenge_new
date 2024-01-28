#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
from pathlib import Path  

# Create a Path object for the CSV file
path_csv = Path(r'C:\Users\liuru\Documents\laura-example-folder\my_homework\Assignment_3\python-challenge\PyBank\Resources\budget_data.csv')

# Read CSV File
df = pd.read_csv(path_csv)  
df.head()


# In[ ]:


# Total Number of Months
total_months = len(df)

# The net total amount of "Profit/Losses" over the entire period
net_total = df['Profit/Losses'].sum()

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
df['Profit/Losses Change'] = df['Profit/Losses'].diff()
average_change = df['Profit/Losses Change'].mean()

# The greatest increase in profits (date and amount) over the entire period
greatest_increase = df['Profit/Losses Change'].max()
greatest_increase_date = df.loc[df['Profit/Losses Change'] == greatest_increase, 'Date'].iloc[0]

# The greatest increase in profits (date and amount) over the entire period
greatest_decrease = df['Profit/Losses Change'].min()
greatest_decrease_date = df.loc[df['Profit/Losses Change'] == greatest_decrease, 'Date'].iloc[0]


# In[32]:


# Print the analysis
separator = '-' * 30
print("Financial Analysis")
print(separator)
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${int(greatest_increase)})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${int(greatest_decrease)})")

# Prepare the result string
results = [
    "Financial Analysis",
    '-' * 30,
    f"Total Months: {total_months}",
    f"Total: ${net_total}",
    f"Average Change: ${average_change:.2f}",
    f"Greatest Increase in Profits: {greatest_increase_date} (${int(greatest_increase)})",
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${int(greatest_decrease)})"
]

# Join the result strings with newline characters
formatted_results = "\n".join(results)

# Write the results to a text file
with open('financial_analysis_results.txt', 'w') as file:
    file.write(formatted_results)


# In[ ]:





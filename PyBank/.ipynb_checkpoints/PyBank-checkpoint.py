#!/usr/bin/env python
# coding: utf-8

# In[42]:


import os
import csv

file_path = 'PyBank/Resources/budget_data.csv'

# Lists to store data
total_months = 0
net_total = 0
previous_value = None
monthly_changes = []
greatest_increase = ["", 0] 
greatest_decrease = ["", 0]  

# Open and read the CSV file
with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)  

    # Loop through each row in the CSV file
    for row in csv_reader:
        # Count the total number of months
        total_months += 1

        # Sum up the total "Profit/Losses"
        current_value = int(row[1])
        net_total += current_value

        # Calculate the monthly change and update the greatest increase/decrease
        if previous_value is not None:
            change = current_value - previous_value
            monthly_changes.append(change)

            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]

            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]

        previous_value = current_value

# Calculate the average change in "Profit/Losses"
average_change = sum(monthly_changes) / len(monthly_changes) if monthly_changes else 0

# Prepare the analysis output
output = (
    "Financial Analysis\n"
    "-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
)

# Print the analysis to the terminal
print(output)

# Define the output file path
output_file_path = 'PyBank/Resources/financial_analysis.txt'  

# Write the results to a text file
with open(output_file_path, 'w', encoding='utf-8') as textfile:
    textfile.write(output)



# In[ ]:





# In[ ]:





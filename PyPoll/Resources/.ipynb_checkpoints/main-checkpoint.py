#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from pathlib import Path  

# Create a Path object for the CSV file
path_csv = Path(r'C:\Users\liuru\Documents\laura-example-folder\my_homework\Assignment_3\python-challenge\PyPoll\Resources\election_data.csv')

# Read CSV File
df = pd.read_csv(path_csv)  
df.head()


# In[18]:


# Calculate total votes
total_votes = df.shape[0]

# Vote counts for each candidate
vote_counts = df['Candidate'].value_counts()

# Calculate percentages
percentages = (vote_counts / total_votes) * 100

# Determine the winner
winner = vote_counts.idxmax()

# Prepare the result string with the desired format
results = []
results.append("Election Results")
results.append("-------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("-------------------------")
for candidate in sorted(vote_counts.index):
    results.append(f"{candidate}: {percentages[candidate]:.3f}% ({vote_counts[candidate]})")
results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")

# Join the result strings with newline characters
formatted_results = "\n".join(results)

# Print the results to the console
print(formatted_results)

# Write the results to a text file
with open('election_results.txt', 'w') as file:
    file.write(formatted_results)




# In[ ]:





# In[ ]:





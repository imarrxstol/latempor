# Define column names (optional but recommended)
column_names = ['Name', 'Age', 'Occupation']

# Convert nested list to dataframe
df = pd.DataFrame(nested_list, columns=column_names)

# Display the dataframe
print(df)

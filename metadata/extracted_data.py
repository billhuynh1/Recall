import csv
import json
import pandas as pd

csv_file = "C:/Users/PC/Desktop/Recall/Recall/metadata/Sample_Dataset.csv"
json_file = "out.json"
data = pd.read_csv(csv_file, encoding='utf-8')

# Convert the data to a list of dictionaries
data_dict = data.to_dict(orient='records')

# Write the data to a JSON file
with open(json_file, 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

print(f"CSV data has been successfully converted to JSON and saved in {json_file}.")
print (json_file)
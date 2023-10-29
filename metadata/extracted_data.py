import csv
import json

csv_file = "out.csv"
json_file = "out.json"

data = []

# Read the CSV file and convert it to a list of dictionaries
with open(csv_file, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

# Write the data to a JSON file
with open(json_file, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"CSV data has been successfully converted to JSON and saved in {json_file}.")
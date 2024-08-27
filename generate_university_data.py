import json
import os

# Define the output files
states_university_file = 'states_university.json'
federal_university_file = 'federal_university.json'

# Initialize the output dictionaries
states_university_data = {}
federal_university_data = {}

# Iterate over the files
for file in [r'university_datas\federal', r'university_datas\states']:
    for filename in os.listdir(file):
        if filename.endswith('.json'):
            with open(os.path.join(file, filename), 'r') as f:
                data = json.load(f)
                # Extract the university name from the file name
                university_name = os.path.splitext(filename)[0]
                # Add the data to the corresponding output dictionary
                if file == r'university_datas\federal':
                    federal_university_data[university_name] = data
                else:
                    states_university_data[university_name] = data

# Write the output dictionaries to files
with open(states_university_file, 'w') as f:
    json.dump(states_university_data, f, indent=4)

with open(federal_university_file, 'w') as f:
    json.dump(federal_university_data, f, indent=4)
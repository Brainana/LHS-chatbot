import json
import csv
import argparse # Used to parse arguments

# Get all the arguments
argparser = argparse.ArgumentParser()
argparser.add_argument("--inputFile", type=str, required=True)
argparser.add_argument("--outputFile", type=str, required=True)
args = argparser.parse_args()

# Open the JSON file and load its contents into a Python dictionary
queriesJson = None
with open(args.inputFile, 'r', encoding='utf-8') as json_file:
    queriesJson = json.load(json_file)

data = []
for query in queriesJson:
    metadata = query['metadata'].replace("'", '"')
    # print(metadata)
    metadata = json.loads(metadata)

    fields = {
        "prompt": query['prompt'],
        "generation": query['generation'],
        "query_time": metadata['query_time'][:-4], # Remove " sec" (the last 4 characters)
        "user_agent": metadata['user_agent'],
        "user_ip": metadata['user_ip']
    }
    data.append(fields)

# print("data length is " + str(len(data)))

# Specify the path to your CSV file
csv_file_path = args.outputFile

# Specify the field names for the CSV file
field_names = ['prompt', 'generation', 'query_time', 'user_agent', 'user_ip']

# Open the CSV file and write data to it
with open(csv_file_path, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)

    # Write the header
    writer.writeheader()

    # Write the data
    for row in data:
        writer.writerow(row)

print(f'Data has been written to {csv_file_path}')

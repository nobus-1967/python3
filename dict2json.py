#!/usr/bin/env python3
"""Serialization of dict using JSON."""
import json

# Create Python dict for serialization
my_dict = dict(Jane=19, Jack=20, John=21)

# Print Python dict
print('Python dict:')
print(my_dict)
print()

# Serialize dict to JSON file
with open('my_dict.json', 'w') as file:
    # 1. Convert Python dict to JSON string
    dict_2_json = json.dumps(my_dict, indent=4)
    
    # 2. Print type of data and JSON string
    print('Serializing Python dict to JSON:')
    print(type(dict_2_json))
    print(dict_2_json)
    
    # 3. Write JSON string to file
    file.write(dict_2_json)
    print('\nJSON data were written to file.\n')

print('-------------------------------')

# Deserialize Python dict from JSON file 
with open('my_dict.json', 'r') as file:
    # 1. Read JSON str from file
    print('\nDeserializing JSON to Python dict:')
    json_str = file.read()    
    print('JSON data were read from file.\n')
    
    # 2. Convert JSON string to Python dict
    json_2_dict = json.loads(json_str)
    
    # 3. Print type of data and Python dict    
    print(type(json_2_dict))
    print(json_2_dict)

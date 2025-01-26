import json
# Convert Python dictionary to JSON
data={"Name":"Alice","Age":"19","City":"Jhelum"}
print("Original Data: ",data)
json_var=json.dumps(data)
print("JSON Data: ",json_var)

# Convert JSON to Python dictionary
python_var= json.loads(json_var)
print("Python Dictionary: ",python_var)


import json

# JSON object representing a person
person_json = '''
{
  "name": "John Doe",
  "age": 30,
  "email": "john.doe@example.com"
}
'''

# Parse the JSON object
person = json.loads(person_json)

# Print the person's name
print(person['name'])

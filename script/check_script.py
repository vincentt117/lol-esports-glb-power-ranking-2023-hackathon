# TESTING ONLY
import json

fileName = "games/ESPORTSTMNT03:3195064.json"
with open(fileName) as file:
        file_contents = file.read()
contents = json.loads(file_contents)

print(contents[0])
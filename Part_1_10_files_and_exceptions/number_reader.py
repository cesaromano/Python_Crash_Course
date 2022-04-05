#	Storing Data
#*Using json.dump() and json.load()

import json

filename = 'numbers.json'
with open(filename) as f:
	numbers = json.load(f)

print(numbers)
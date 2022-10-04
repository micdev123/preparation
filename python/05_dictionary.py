# Dictionary
    # Key-Value pair
    # Associative array, like java HashMap
    # Unordered | Can't be sorted

# Creating dictionary
    # curly braces :: x = {'fname' : 'John', 'lname': 'Doe'}

from turtle import clear


x = dict(fname = 'John', lname = 'Doe')
x2 = {"fname": "John", "lname": "Doe"}
x3 = dict([("fname", "John"), ("lname", "Doe")])

# Add or Update item
x['mname'] = 'J'

# Delete an item 
del(x['mname'])

# Delete all items in dictionary
x.clear()

# Delete the dictionary
del(x)


# Accessing || keys, values, items
x = dict(fname = 'John', lname = 'Doe')
getKeys = x.keys() # generate a list of dictionary keys
getValues = x.values() # generate a list of dictionary values
getItems = x.items() # generate a list of dictionary items

# Iterating a dictionary
for key in x:
    print(key, x[key])

for k, v in x.values():
    print(k, v)
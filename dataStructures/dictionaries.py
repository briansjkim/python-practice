# Dictionaries are mutable data types that stores mappings of unique keys to values

# You can look up values, change values, or insert new values in the dictionary using square brackets that enclose the key
elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
print(elements['helium'])
elements['lithium'] = 3
elements['hydrogen'] = 4
print(elements)

# Dictionaries can have keys of any immutable type, not just strings
numbers = {1: 0, 2: 1, 3: 2, 4:3, 5: 4}
print(numbers[1])
numbers[6] = 5
numbers[1] = 1
print(numbers)

# Membership Operators
print('hydrogen' in elements) #True
print(10 in numbers) #False
print(9 not in elements) #True

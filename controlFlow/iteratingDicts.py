# Practice w/ iterating through dictionaries with a for loop

# To access the keys, you iterate through a dict with a regular for loop
cast = {
    'Jerry Seinfeld': 'Jerry Seinfeld',
    'Julia Louis-Dreyfus': 'Elaine Benes',
    'Jason Alexander': 'George Costanza',
    'Michael Richards': 'Cosmo Kramer'
}

for key in cast:
    print(key)

# To access both the keys and values, you use the built-in method items()
for key, val in cast.items():
    print('This actor {} played in {}'.format(key, val))

# Task 1
# Count the number of fruits in your basket. Given a dictionary and list of fruits. If the key is in the list of fruits, add the value (number of fruits) to result
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for item, count in basket_items.items():
    if item in fruits:
        result += count

print(result)

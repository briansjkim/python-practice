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

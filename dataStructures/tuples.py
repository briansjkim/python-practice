# Tuples are another useful container
# A data type for immutable ordered sequences of elements that are often used to store related pieces of info

location = (13.4125, 103.86667)
print("Latitude:", location[0])
print("longitude:", location[1])

person = ('Brian', 23, 'Male')
print('Name:', person[0])
print('Age:', person[1])
print('Gender:', person[2])

# Tuples are similar to lists in that they store an ordered collection of objects which can be accessed by their indices.
# However, tuples are immutable so you can't add and remove items from tuples or sort them in place
# Can also be used to assign multiple variables in a compact way

dimensions = 52, 40, 100
length, width, height = dimensions
print('The dimensions are {} x {} x {}'.format(length, width, height))

year, month, date = 1996, 11, 9
print('My birthdate is {}/{}/{}'.format(month, date, year))
# the parentheses are optional when defining tuples
# Tuple unpacking is used (as shown in line 13) to assign the info from a tuple into multiple variables w/o having to access them one by one and make multiple assignment statements

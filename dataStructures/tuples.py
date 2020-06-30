# Tuples are another useful container
# A data type for immutable ordered sequences of elements that are often used to store related pieces of info

location = (13.4125, 103.86667)
print("Latitude: ", location[0])
print("longitude: ", location[1])

# Tuples are similar to lists in that they store an ordered collection of objects which can be accessed by their indices.
# However, tuples are immutable so you can't add and remove items from tuples or sort them in place
# Can also be used to assign multiple variables in a compact way

dimensions = 52, 40, 100
length, width, height = dimensions
print('The dimensions are {} x {} x {}'.format(length, width, height))

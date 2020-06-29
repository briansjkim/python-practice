# lists are containers that organize and group data types together
    # A list is a data structure that is a mutable ordered sequence of elements
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
randoms = ['hello', 1, 4, 5.8, False]

print(days[0]) # Monday
# print(days[10]) # IndexError: list index out of range
print(randoms[3]) # 5.8

# we can access a subsequence of a list using Python's slicing notation
weekdays = days[:5] # this just means slicing from index 0 (INCLUSIVE) to index 5 (EXCLUSIVE)
print(weekdays)

weekends = days[5:] # this means slicing from index 5 (INCLUSIVE) to the end of the list
print(weekends)

# len() also works with lists
print(len(days))

# Membership Operators
# membership operators are operators which are used to check whether a value/variable exists in the sequence
# In evaluates if the object on the left side is included in the object on the right side
# Not in evaluates if the object on the left side is NOT included in the object on the right side

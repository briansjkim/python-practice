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

print('Monday' in days) # True
print('Monday' in weekends) # False
print('January' not in days) # True
print(weekends not in randoms) # True

# Slicing Quiz
# Select the three most recent dates from this list
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003', 'March 29, 2006', 'August 1, 2008', 'July 22, 2009', 'July 11, 2010', 'November 13, 2012', 'March 20, 2015','March 9, 2016']
print(eclipse_dates[-3: ])

# List Methods
names = ['Harry', 'Christine', 'John', 'Joshua', 'Beth']
numbers = [1, 4, 8, 14, 57, 2, 10, 86]
# len() is a method that returns how many elements are in a list
print(len(names)) # 5

# max() is a method that returns the greatest element of the list
# if it's a list of strings, the maximum element would be the element that would occur last if the list were SORTED ALPHABETICALLY
print(max(names)) # Joshua because s is appears after h
print(max(numbers)) # 86

# min() is a method that returns the smallest element in a list
# opposite of max() with a list of strings
print(min(names)) # Beth
print(min(numbers)) # 1

# sorted() is a method that returns a copy of a list in order from smallest to largest, leaving the list unchanged
sorted_nums = sorted(numbers)
print(sorted_nums) # [1, 2, 4, 8, 10, 14, 57, 86]

# join() is a string method that takes a list of strings as an argument, and returns a string consisting of the list element joined by a separator string
print(' & '.join(names)) # 'Harry & Christine & John & Joshua & Beth'

# append() is a method that adds an element to the end of a list
names.append('Brian')
print(names) # ['Harry', 'Christine', 'John', 'Joshua', 'Beth', 'Brian']

print(names[len(names) - 1]) # Brian

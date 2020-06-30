# A set is a data type for mutable unordered collections of unique elements
# One application of a set is to quickly remove duplicates from a list

nums = [1, 4, 5, 1, 5, 7, 2, 7, 10, 48, 934, 923, 832, 954, 94, 923]
unique_nums = set(nums)
print(unique_nums);

fruit = {'apple', 'banana', 'orange', 'grapefruit'}
print(fruit)
print('watermelon' in fruit)
print('apple' in fruit)

# You add elements to sets using the add method
fruit.add('watermelon')

# You remove elements using the pop method
fruit.pop()

print(fruit)

# union() method returns a set that contains all items from the original set and all items from the specified sets
# You can specify as many sets you want, separated by commas
# if an item is present in more than one set, the result will contain only one appearance of the item

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.union(y)
print(z)


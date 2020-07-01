# Python List Exercises

# Given a Python list you should be able to display Python list in the following order:
#  [100, 200, 300, 400, 500] => [500, 400, 300, 200, 100]

aList = [100, 200, 300, 400, 500]

# this is a slicing technique used to produce a reversed copy
newList = aList[::-1]
print(newList)

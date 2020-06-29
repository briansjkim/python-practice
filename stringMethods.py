# casefold() returns a string where all the characters are lower case
# it's similar to the lower() method, but casefold() will convert more characters into lower case
print('Brian KIM'.casefold())

# lower() is very similar to casefold() where it returns a string with all the characters being lower case
print('BrIAN KIM'.lower())

# format() method formats the specified value(s) and insert them inside the string's placeholder
print('Mohammed has {} balloons'.format(27))
print('Does your {} {}?'.format('dog', 'bite'))

animal = 'bat'
verb = 'bite'

print('Does your {} {}?'.format(animal, verb))

# title() method returns a string in title case meaning the first letter of each word is capitalized
print('the man in the woods said hi'.title())

# split() method returns a container called a list that contains the words from the input string
# has two additional arguments (sep and maxsplit)
    # the sep argument stands for separator which can be used to identify how the string should be split (splice, tab, return, new line, comma, etc.).
        # if the sep argument isn't provided, the default separator is whitespace
        # the sep argument CANNOT be empty if used with the maxsplit argument. You can use None as the separator if using the maxsplit argument
    # the maxsplit argument provides the number of maximum splits. the argument gives maxsplit + 1 number of elements in the new list with the remaining string being returned as the last element in the list

my_string = 'The cow goes moo over the moon'
print(my_string.split(' ', 3)) # ['The', 'cow', 'goes', 'moo over the moon']
print(my_string.split(None, 2)) # ['The', 'cow', 'goes moo over the moon']
print(my_string.split(' ', 4)) # ['The', 'cow', 'goes', 'moo', 'over the moon']

# len() method returns the length of the string variable
print(len(my_string))

# find() method will return the lowest index of the substring if it's found in given string. If it's not found, then it returns -1
    # it basically returns the first occurrence of the substring if it's found
print(my_string.find('moo')) # 13
print(my_string.find('l')) # -1

# rfind() method will return the highest index of the substring if it's found in the given string. If it's not found, then it returns -1
print(my_string.rfind('o')) # 28
print(my_string.rfind('l')) # -1

# rindex() method is very similar to rfind() where it will return the highest index of the substring if it's found in the given string.
    # the difference between the two is that rindex() will NOT return -1 if the substring isn't found. Instead, it'll throw an exception
print(my_string.rindex('m')) #26
# print(my_string.rindex('l')) # ValueError: substring not found

# count() method will return the number of occurences of the substring in the given string
print(my_string.count('m')) # 2

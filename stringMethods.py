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

# find() method will return the lowest index of the substring if its found in given string. If it's not found, then it returns -1
    # it basically returns the first occurrence of the substring if it's found
print(my_string.find('moo'))

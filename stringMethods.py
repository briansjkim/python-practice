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

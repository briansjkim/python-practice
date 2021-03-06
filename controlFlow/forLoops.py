cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)

print('Completed')

# Using range() function
# range(start = 0, stop, step = 1)

# only one argument => stop
for i in range(3):
    print(i) #0, 1, 2

# using two arguments => start and stop
for i in range(2, 6):
    print(i) #2, 3, 4, 5

# using three arguments => start, stop, and step
for i in range(1, 10, 2):
    print(i) # 1, 3, 5, 7, 9

# creating and modifying lists
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())

print(capitalized_cities)

# modifying a list is a bit more involved and requires the use of the range() function
for idx in range(len(cities)):
    cities[idx] = cities[idx].title()

print(cities)

# Extra practice
sentence = ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']

for word in sentence:
    print(word)

# Multiples of 5
# print out every whole number that is a multiple of 5 and less than or equal to 30 
for i in range(5, 35, 5):
    print(i)

# Write a for loop that iterates over the names list to create a usernames list
# To create a username for each name, make everything lowercase and replace spaces with underscores

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(' ', '_'))

print(usernames)

# To modify the list in place using range() function
for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(' ', '_')

print(usernames)

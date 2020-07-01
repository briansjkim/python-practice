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

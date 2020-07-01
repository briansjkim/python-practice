# Practice Questions for data structure comprehension

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"

# 1. Split verse into a list of words
# 2. Convert the list into a data structure that would keep only the unique elements from the list
# 3. Print the length of the container

# split verse into a list of words
verse_list = verse.split(' ')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list)

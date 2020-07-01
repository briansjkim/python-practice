# Practice Questions for data structure comprehension

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"

# 1. Split verse into a list of words
# 2. Convert the list into a data structure that would keep only the unique elements from the list
# 3. Print the length of the container

# split verse into a list of words
verse_list = verse.split(' ')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list)

# print the number of unique words
# Subtract one from the length because an empty space will be inside the set
num_unique = len(verse_set) - 1


verse_dict = {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}

# 1. How many unique words are in verse_dict?
# 2. Is the key "breathe" in verse_dict?
# 3. What is the first element in the list created when verse_dict is sorted by keys?
    # Use the appropriate dictionary method to get a list of its keys, and then sort that list
# 4. Which key (word) has the highest value in verse_dict?

# find the unique words in verse_dict
unique_words = len(verse_dict)

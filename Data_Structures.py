# Using the PRINT module for print more readable Output
from pprint import pprint

# Find the most repeated charactor in this text
sentence = "This is a common interview question"

# We can use a Dictionary as a Data structure
# First we need to know how many times each Charactor is repeated
# Once we have this infomation, we need to find the most repeated Charactor
# Here we can use the Charactor as the keys and the repetition as the Value

# First, Define an Empty Dictionary
char_frequency = {}

# Then
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

print("There are:-", char_frequency_sorted[0])

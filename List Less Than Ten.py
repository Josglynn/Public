# Take a list, say for example this one:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Write a program that prints out all the elements of the list that are less than 13.

list_num = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

filtered_1 = [item for item in list_num if item < 13]  # Comprehensions style
print(filtered_1)

filtered_2 = list(filter(lambda item: item < 13, list_num))  # Lambda style
print(filtered_2)

# Other type to solve this:-
for i in list_num:
    if i < 13:
        print(i)

# A list comprehension behaves like this: [output] for [item] in [list] if [filter]

# As you can see there are 4 components in its syntax:
# output, item, list and filter.

# In the code [aa for aa in a if aa < 5]:

#output = aa
#item = aa
#list = a
#filter = aa < 5

# What this means is that I'm outputting the variable 'aa' which refers to each item in the list (a).

# Since 'aa' is set to refer to each item in list (a), the output will print the items in list (a). However, I also have a filter specified at the end of the code "if aa < 5".

# This means that only the items in the list (referred to as aa) that are below 5 are printed out.

# It does help if you use labels that are more intuitive in your code. For example instead of naming the list a, I can name the list "number_list":

#number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# My list comprehension will go like this:

#[number for number in number_list if number < 5]

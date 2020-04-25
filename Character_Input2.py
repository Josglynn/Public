# Missing Exceptions Handling

import datetime
now = datetime.datetime.now()
current_year = now.year

name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((current_year - age)+100)
print(name + " will be 100 years old in the year " + year)

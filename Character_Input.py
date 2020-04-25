# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

try:
    Name = str(input("Your Name: "))
    Age = int(input("Age: "))
    print("Dear", Name, "you'll be 100 years in", (100 - Age), "years!!")
except ValueError:
    print("Please enter a valid age")

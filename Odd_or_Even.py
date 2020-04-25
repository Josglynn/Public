# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

num = int(input("Enter a number: "))
answer = num % 2

if answer > 0:
    print("You picked an ODD number.")
else:
    print("You picked an Even number.")

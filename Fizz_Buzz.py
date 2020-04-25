# If 3 result displayed is Fizz
# If 5 result displayed Buzz
# IF 15 result displayed is FizzBuzz
# Else it will return/display "Not Good Input"


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    if input != (3, 5, 15):
        return "Not Good Input"


print(fizz_buzz(8))

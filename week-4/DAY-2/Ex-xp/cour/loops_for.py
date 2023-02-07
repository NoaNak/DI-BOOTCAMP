# For loop is based on a specific known range

numbers = [1,2,3,4,5]

# The range function produces a sequence of numbers atr specific range
# Example, range(3) -> 0, 1, 2
# Example, range(0, 11, 2) -> 0, 2, 4, 6, 8, 10

for i in range(len(numbers)):
    # i = 0
    # i = 1
    # i = 2
    # i = 3...
    numbers[i] *= 2

print(numbers)

# Accept a number from the user and print its multiplication table

number: int = int(input("Your number: "))

for multiplier in range(1, 10):

    result = number * multiplier

    print(f"{number} X {multiplier} = {result}")

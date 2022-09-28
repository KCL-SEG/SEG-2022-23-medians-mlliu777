"""Median calculator."""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

length = len(numbers)
half = length/2
numbers.sort()
if length%2 == 0:
    median = (numbers[int(half - 1)] + numbers[int(half)])/2
else:
    median = numbers[int(half -0.5)]
print(median)

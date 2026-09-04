# 08_second_largest.py

numbers = [10, 45, 23, 67, 67, 34, 56]

largest = None
second_largest = None

for number in numbers:

    if largest is None or number > largest:

        if number != largest:
            second_largest = largest

        largest = number

    elif number != largest and (
        second_largest is None or number > second_largest
    ):
        second_largest = number

if second_largest is None:
    print("Second-largest value does not exist.")
else:
    print("Largest:", largest)
    print("Second Largest:", second_largest)
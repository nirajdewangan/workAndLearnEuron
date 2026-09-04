# 06_accept_10_numbers.py

numbers = []

for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print("Numbers entered:", numbers)
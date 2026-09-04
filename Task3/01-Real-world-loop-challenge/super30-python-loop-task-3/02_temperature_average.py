# 02_temperature_average.py

temperatures = [32, 35, 28, 40, 38, 31, 42]

total = 0

for temperature in temperatures:
    total += temperature

average = total / len(temperatures)

print("Average Temperature:", average)
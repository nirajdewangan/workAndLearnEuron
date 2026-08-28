# Remove Duplicate Data Using Sets

# Create a list containing duplicate numbers
numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60]

# Print the original list
print("Original List:", numbers)

# Convert the list into a set
unique_numbers = set(numbers)
print("Set:", unique_numbers)

# Duplicates 10, 20 and 30 are removed
print("After Removing Duplicates:", unique_numbers)

# Convert the set back into a list
unique_numbers_list = list(unique_numbers)
print("Unique Numbers List:", unique_numbers_list)

# Print number of original elements
print("Number of Original Elements:", len(numbers))

# Print number of unique elements
print("Number of Unique Elements:", len(unique_numbers))


# Another example using duplicate student names

student_names = [
    "Rahul",
    "Priya",
    "Aman",
    "Rahul",
    "Priya",
    "Sneha",
    "Aman"
]

print("\nOriginal Student Names:", student_names)

# Convert student names into a set
unique_students = set(student_names)
print("Unique Student Names:", unique_students)

# Convert set back into a list
unique_students_list = list(unique_students)
print("Unique Student Names List:", unique_students_list)

# Print original and unique counts
print("Original Student Count:", len(student_names))
print("Unique Student Count:", len(unique_students))


# Explanation
print("\nWhy are sets useful?")

print("Sets store only unique values.")
print("Duplicate values are automatically removed.")
print("Sets are useful for cleaning duplicate data.")
# Tuple Challenge

technologies = (
    "Python",
    "Java",
    "Python",
    "C++",
    "JavaScript",
    "Python"
)

# Print the complete tuple
print("Technologies:", technologies)

# Print its data type
print("Type:", type(technologies))

# Print the first item
print("First Item:", technologies[0])

# Print the last item
print("Last Item:", technologies[-1])

# Slice the tuple
print("Sliced Tuple:", technologies[1:5])

# Count how many times Python appears
python_count = technologies.count("Python")
print("Count of Python:", python_count)

# Find the index of C++
cpp_index = technologies.index("C++")
print("Index of C++:", cpp_index)

# Find the length of the tuple
tuple_length = len(technologies)
print("Tuple Length:", tuple_length)

# Convert tuple into a list
technology_list = list(technologies)
print("Converted to List:", technology_list)

# Add Go to the list
technology_list.append("Go")
print("After Adding Go:", technology_list)

# Convert the list back into a tuple
updated_technologies = tuple(technology_list)
print("Converted Back to Tuple:", updated_technologies)

# Explanation
print("\nTuple Immutability Explanation:")
print("Tuples are immutable because their items cannot be changed after creation.")
print("We cannot directly add, remove, or modify items in a tuple.")
print("To modify this data, we converted the tuple into a list.")
print("After adding Go, we converted the list back into a tuple.")
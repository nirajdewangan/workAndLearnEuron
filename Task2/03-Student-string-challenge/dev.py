student = "python programming for data science"

# Perform operations to

# Print the complete string
print("Complete String:", student)

# Print the first character
print("First Character:", student[0])

# Print the last character
print("Last Character:", student[-1])
# Print the first 6 characters
print("First 6 Characters:", student[0:6])

# Print the last 7 characters
print("Last 7 Characters:", student[-7:])

# Reverse the string using slicing
print("Reversed String:", student[::-1])
# Convert it to uppercase
print("Uppercase:", student.upper())
# Convert it to lowercase
print("Lowercase:", student.lower())
# Convert it to title case
print("Title Case:", student.title())
# Count how many times "a" appears
print("Count of 'a':", student.count("a"))
# Find the position of "programming"
print("Position of 'programming':", student.find("programming"))
# Replace "data science" with "artificial intelligence"
print("After replace():", student.replace("data science", "artificial intelligence"))
# Split the string into individual words
print("Split into words:", student.split())
# Set Operations Challenge

python_students = {"Rahul", "Aman", "Priya", "Karan", "Neha"}
java_students = {"Priya", "Karan", "Rohit", "Simran"}

# Print both sets
print("Python Students:", python_students)
print("Java Students:", java_students)

# Students learning either Python or Java
either_language = python_students.union(java_students)
print("Students learning Python or Java:", either_language)

# Students learning both Python and Java
both_languages = python_students.intersection(java_students)
print("Students learning both:", both_languages)

# Students learning only Python
only_python = python_students.difference(java_students)
print("Students learning only Python:", only_python)

# Students learning only Java
only_java = java_students.difference(python_students)
print("Students learning only Java:", only_java)

# Students belonging to exactly one group
exactly_one_group = python_students.symmetric_difference(java_students)
print("Students in exactly one group:", exactly_one_group)

# Add a new student
python_students.add("Vivek")
print("After adding Vivek:", python_students)

# Remove a student
python_students.remove("Neha")
print("After removing Neha:", python_students)

# Demonstrate discard()
python_students.discard("Vivek")
print("After discarding Vivek:", python_students)

# discard() does not give an error if the value is not present
python_students.discard("Zoya")
print("After discarding Zoya:", python_students)


# Method Explanations
print("\nSet Method Explanations:")

print("union(): Returns all unique elements from both sets.")
print("intersection(): Returns elements common to both sets.")
print("difference(): Returns elements present in one set but not the other.")
print("symmetric_difference(): Returns elements present in exactly one set.")
print("add(): Adds one new element to a set.")
print("remove(): Removes an element, but gives an error if it is not found.")
print("discard(): Removes an element, but does not give an error if it is not found.")
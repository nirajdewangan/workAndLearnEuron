# Nested List Challenge

students = [
    ["Rahul", 21, "Python"],
    ["Priya", 22, "Data Science"],
    ["Aman", 20, "Machine Learning"]
]

# Print the complete nested list
print("Complete List:", students)

# Print Rahul's name
print("Rahul's Name:", students[0][0])

# Print Priya's age
print("Priya's Age:", students[1][1])

# Print Aman's course
print("Aman's Course:", students[2][2])

# Print Priya's complete record
print("Priya's Complete Record:", students[1])

# Change Rahul's course from Python to AI
students[0][2] = "AI"
print("Rahul's Updated Record:", students[0])

# Add another student record manually
students.append(["Sneha", 23, "Deep Learning"])

# Print the updated nested list
print("Updated Nested List:", students)


# Explanation of nested list indexing
print("\nNested List Indexing Explanation:")

print("students[0] gives Rahul's complete record.")
print("students[0][0] gives Rahul's name.")
print("students[1][1] gives Priya's age.")
print("students[2][2] gives Aman's course.")
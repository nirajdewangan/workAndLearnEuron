# Create a Student Marks List

marks = [78, 85, 90, 67, 88, 92, 76]

# Print the complete list
print("Complete List:", marks)

# Print the first element
print("First Element:", marks[0])

# Print the last element
print("Last Element:", marks[-1])

# Print elements from index 2 to 5
print("Elements from Index 2 to 5:", marks[2:6])

# Find the number of elements
print("Number of Elements:", len(marks))

# Find maximum marks
print("Maximum Marks:", max(marks))

# Find minimum marks
print("Minimum Marks:", min(marks))

# Find total marks
print("Total Marks:", sum(marks))

# Sort marks in ascending order
marks.sort()
print("Ascending Order:", marks)

# Sort marks in descending order
marks.sort(reverse=True)
print("Descending Order:", marks)

# Add 95
marks.append(95)
print("After Adding 95:", marks)

# Add [81, 84]
marks.extend([81, 84])
print("After Adding 81 and 84:", marks)

# Remove 67
marks.remove(67)
print("After Removing 67:", marks)

# Count how many times 90 occurs
print("Count of 90:", marks.count(90))

# Find the index of 88
print("Index of 88:", marks.index(88))

# Print final list
print("Final Marks List:", marks)